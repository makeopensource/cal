""" Args parse Implemented and View """
import sys
import os
import json
import sqlite3


def check():
    conn = sqlite3.connect('projects.db')
    c = conn.cursor()

    # Insert a row of data
    for row in c.execute('SELECT * FROM projects'):
        lst = ""
        for value in row:
            lst += value + "\t"
        print(lst.strip())

    # Save (commit) the changes
    conn.commit()
    conn.close()
