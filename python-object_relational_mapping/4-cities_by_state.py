#!/usr/bin/python3
""" Lists all cities from the database hbtn_0e_4_usa """

import sys
import MySQLdb


def all_cities():
    """ Lists all cities from the database hbtn_0e_4_usa """

    """ Connects MySQL """
    DB = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    """ Sets cursor """
    cursor = DB.cursor()

    """ SQL Query """
    cursor.execute("SELECT cities.id, cities.name, states.name \
                    FROM cities \
                    INNER JOIN states ON cities.state_id = states.id \
                    ORDER BY cities.id ASC")

    """ Fetch results """
    cities = cursor.fetchall()

    for city in cities:
        print(city)

    """ Closes connection """
    cursor.close()
    DB.close()


if __name__ == "__main__":
    all_cities()
