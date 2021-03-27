#!/usr/bin/python3
"""
    list
"""
import sys
import MySQLdb
if __name__ == "__main__":
    u_name = sys.argv[1]
    p = sys.argv[2]
    db_name = sys.argv[3]
    state_s = sys.argv[4]
    h = 'localhost'
    db = MySQLdb.connect(host=h, port=3306, user=u_name, passwd=p, db=db_name)
    cur = db.cursor()
    sql = "SELECT cities.name FROM cities JOIN \
          states ON cities.state_id=states.id WHERE states.name=%s"
    numrows = cur.execute(sql, (state_s, ))
    rows = cur.fetchall()
    for i, row in enumerate(rows):
        for x in row:
            if i + 1 < len(rows):
                print(x, end=", ")
            else:
                print(x, end="")
    print()
