#!/usr/bin/python3
# script that takes in an argument and displays all values
if __name__ == "__main__":

    import MySQLdb

    from sys import argv

    username = argv[1]
    password = argv[2]
    database = argv[3]
    state_name = argv[4]

    if ";" in state_name:
        exit()

    my_database = MySQLdb.connect(host="localhost", user=username,
                                  passwd=password, port=3306, db=database)
    mycursor = my_database.cursor()

    mycursor.execute("SELECT * FROM states WHERE name LIKE '{}'\
         ORDER BY id ASC".format(state_name))
    for state in mycursor:
        if (state[1] == state_name):
            print(state)
    mycursor.close()
    my_database.close()
