#!/usr/bin/python3
import sys
import MySQLdb
""" Lists all states from the database """
if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost",user=sys.argv[1],
                         passwd=sys.argv[2],db=sys.argv[3],port=3306)
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
