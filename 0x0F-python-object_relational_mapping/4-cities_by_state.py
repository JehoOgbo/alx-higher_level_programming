#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa """
import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
                FROM cities JOIN states ON\
                cities.state_id = states.id ORDER BY cities.id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
