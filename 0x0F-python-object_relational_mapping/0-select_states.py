#!/usr/bin/python3
"""List all states from a given db sorted in ascending order by id
Username, password, and database names are given as user args
"""

import sys
import MySQLdb

if __name__ == "__main__":
db = MySQLdb.connect (
        host='local host'
        port=3306
        user='sys.argv[1]'
        passwd='sys.argv[2]'
        database='sys.argv[3]'
        )
c = db.cursor()
c.execute("SELECT id, name FROM states ORDER BY id ASC")
thestates = c.fetchall()

for state in thestates:
    print(state)

    c.close()
    db.close()

