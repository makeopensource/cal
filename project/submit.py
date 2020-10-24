import webbrowser
import json
import os.path

def submit(filename):
    if os.path.isfile("./metadata.json"):
        with open("./metadata.json", "r") as f:
            meta = json.loads(f.read())
    else:
        meta = {}
    course = meta.get("course", "")
    semester = meta.get("semester", "")
    assignment = meta.get("assignment", "")
    if course != "" and assignment != "" and semester != "":
        webbrowser.open("https://autograder.cse.buffalo.edu/courses/" + course + "-" + semester + "/assessments/" + assignment)
    else:
        print("missing metadata, redirecting to autograder main page")
        webbrowser.open("https://autograder.cse.buffalo.edu/", 0)
