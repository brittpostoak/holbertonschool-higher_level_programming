#!/usr/bin/python3
""" Lists all states from the database hbtn_0e_0_usa """

import sys
import MySQLdb


def all_states():
    """ Lists all states from the database hbtn_0e_0_usa """

    """ Connects MySQL """
    DB = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    """ Sets cursor """
    cursor = DB.cursor()

    """ SQL Query """
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    """ Fetch results """
    states = cursor.fetchall()

    for state in states:
        print(state)

    """ Close connection """
    cursor.close()
    DB.close()


if __name__ == "__main__":
    all_states()
