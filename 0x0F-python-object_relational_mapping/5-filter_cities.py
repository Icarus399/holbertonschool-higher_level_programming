#!/usr/bin/python3
''' Write a script that takes in the name of a state as an arg
and lists all cities of that state '''

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cur = db.cursor()
    state_search = argv[4]
    cur.execute('''
                SELECT name FROM cities
                WHERE state_id = (
                    SELECT id FROM states
                    WHERE name = %(state_search)s )
                ORDER BY id
                ''', {'state_search': state_search})
    rows = cur.fetchall()
    print(", ".join(row[0] for row in rows))
    cur.close()
    db.close()
