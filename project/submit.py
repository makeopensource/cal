import webbrowser
import json
import os.path
import sqlite3
def submit(filename):
    conn = sqlite3.connect('projects.db')
    c = conn.cursor()
    for row in c.execute('SELECT * FROM projects'):
        dat = row
    if dat:
        webbrowser.open("https://autograder.cse.buffalo.edu/courses/" + dat[2] + "-" + dat[3] + "/assessments/" + dat[4],0)
    else:
        print("missing metadata, redirecting to autograder main page")
        webbrowser.open("https://autograder.cse.buffalo.edu/", 0)
