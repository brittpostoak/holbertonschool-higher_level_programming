#!/usr/bin/python3
""" Lists all states with a name starting with N """

import sys
import MySQLdb


def all_N_states():
    """ Lists all states with a name starting with N """

    """ Connects MySQL """
    DB = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    """ Sets cursor """
    cursor = DB.cursor()

    """ SQL Query """
    cursor.execute("SELECT * FROM states \
                    WHERE BINARY name LIKE 'N%' \
                    ORDER BY id")

    """ Fetch results """
    states = cursor.fetchall()

    for state in states:
        print(state)

    """ Closes connection """
    cursor.close()
    DB.close()


if __name__ == "__main__":
    all_N_states()
