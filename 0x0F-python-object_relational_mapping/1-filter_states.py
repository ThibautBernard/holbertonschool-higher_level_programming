#!/usr/bin/python3
"""
    lists
"""
import sys
import MySQLdb
if __name__ == "__main__":
    u_name = sys.argv[1]
    p = sys.argv[2]
    db_name = sys.argv[3]
    h = 'localhost'
    db = MySQLdb.connect(host=h, port=3306, user=u_name, passwd=p, db=db_name)
    cur = db.cursor()
    numrows = cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
