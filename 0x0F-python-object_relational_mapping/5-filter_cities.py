#!/usr/bin/python3
''' script that lists all states from the database '''

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
    cities = []
    for state in result:
        if (state[1] == argv[4]):
            if (state[0] == state[3]):
                if not (state[4] in cities):
                    cities.append(state[4])
    if (len(cities) == 0):
        print("")
    for city in range(len(cities)):
        if (city == len(cities) - 1):
            print("{}".format(cities[city]))
        else:
            print("{}, ".format(cities[city]), end='')
    mycrusor.close()
    my_database.close()
