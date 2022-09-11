#!/usr/bin/python3
"""list all states where "name' matches the argument
But this time, one safe from MYSQL injection.
Username, password, database name and state name given as user args
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)
    c = db.cursor()
    cmd = """SELECT id, name
         FROM states
         WHERE name=%s
         ORDER BY id ASC"""
    c.execute(cmd, (sys.argv[4],))
    nStates = c.fetchall()

    for state in nStates:
        print(state)

    c.close()
    db.close()
