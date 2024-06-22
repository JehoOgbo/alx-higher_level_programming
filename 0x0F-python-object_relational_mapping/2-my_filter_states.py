#!/usr/bin/python3
""" display all entries where name is passed as arg """
import sys
import MySQLdb
if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    query1 = ("SELECT * FROM states WHERE name LIKE '{}' ORDER BY id ASC").format(sys.argv[4])
    cur.execute(query1)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
