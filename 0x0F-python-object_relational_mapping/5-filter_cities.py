#!/usr/bin/python3
# script that lists all states from the database
if __name__ == "__main__":

    import MySQLdb

    from sys import argv

    username = argv[1]
    password = argv[2]
    database = argv[3]
    state_name = argv[4]

    my_database = MySQLdb.connect(host="localhost", user=username,
                                  passwd=password, port=3306, db=database)
    mycrusor = my_database.cursor()
    mycrusor.execute("SELECT * FROM states,cities ORDER BY cities.id ASC")
    result = mycrusor.fetchall()
    final_result = ""
    final_final_result = ""
    for state in result:
        if state[0] == state[3]:
            if final_result == "" and state_name == state[1] and\
                    state[4] not in final_result:
                final_result = state[4]
            if final_result is not "" and state_name == state[1] and\
                    state[4] not in final_result:
                final_result += ", " + state[4]
    print(final_result)
    mycrusor.close()
    my_database.close()
