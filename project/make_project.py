""" Args parse Implemented and View """
import os
import json
import re
import sqlite3


def make_project(local_path="./"):
    course = input("Course Name (i.e. CSE220): ")
    semester = input("Semester (f for fall, s for spring, i.e. f20, s19): ")
    assignment = input("FULL ASSIGNMENT NAME from Autograder: ")
    assignment = assignment.lower()
    assignment = re.sub('[^A-Za-z0-9]+', '', assignment)

    duedate = input("Due Date (MM/DD/YY): ")
    retdict = {"course": course, "semester": semester, "assignment": assignment, "duedate": duedate}

    curr_path = os.getcwd()
    separator = "/"  # path separator (change for linux)

    # turn current directory into project
    if local_path == "./":
        conn = sqlite3.connect('projects.db')
        c = conn.cursor()

        # Insert a row of data
        c.execute("INSERT INTO projects VALUES (?,?,?,?,?,?)", (local_path, duedate, course, semester, assignment, curr_path))

        # Save (commit) the changes
        conn.commit()
        conn.close()

        with open('./metadata.json', 'w') as outfile:
            jval = json.dumps(retdict)
            outfile.write(jval)

    # make new project directory
    else:
        new_path = curr_path + separator + local_path

        try:
            os.mkdir(local_path)

            conn = sqlite3.connect('projects.db')
            c = conn.cursor()

            # Insert a row of data
            c.execute("INSERT INTO projects VALUES (?,?,?,?,?)", (local_path, duedate, course, semester, new_path))

            # Save (commit) the changes
            conn.commit()
            conn.close()

            with open('./metadata.json', 'w') as outfile:
                jval = json.dumps(retdict)
                outfile.write(jval)

        except FileExistsError:
            print("file already exists")
