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
    h = 'localhost'
    search_n = sys.argv[4]
    db = MySQLdb.connect(host=h, port=3306, user=u_name, passwd=p, db=db_name)
    cur = db.cursor()
    sql = "SELECT * FROM states WHERE name= %s"
    numrows = cur.execute(sql, (search_n, ))
    rows = cur.fetchall()
    for row in rows:
        print(row)
