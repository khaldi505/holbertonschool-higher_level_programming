#!/usr/bin/python3

"""script that takes in an argument and displays all values in the states"""

if __name__ == "__main__":
    import MySQLdb
    import sys
    db = MySQLdb.connect(host="localhost", user=sys.argv[
                         1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        if (row[1] == sys.argv[4]):
            print("{}".format(row))
    cur.close()
    db.close()
