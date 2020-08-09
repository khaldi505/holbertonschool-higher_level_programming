#!/usr/bin/python3
# script that lists all states from the database
if __name__ == "__main__":

    import MySQLdb

    from sys import argv

    username = argv[1]
    password = argv[2]
    database = argv[3]

    my_database = MySQLdb.connect(host="localhost", user=username,
                                  passwd=password, port=3306, db=database)
    mycrusor = my_database.cursor()
    mycrusor.execute("SELECT * FROM states,cities ORDER BY cities.id ASC")
    result = mycrusor.fetchall()
    for state in result:
        if state[0] == state[3]:
                print("({}, '{}', '{}')".format(state[2], state[4], state[1]))
    mycrusor.close()
    my_database.close()
