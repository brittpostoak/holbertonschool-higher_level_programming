#!/usr/bin/python3
""" Lists all cities of that state """

import sys
import MySQLdb


def all_cities():
    """ Lists all cities of that state """

    """ Connects MySQL """
    DB = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    """ Sets cursor """
    cursor = DB.cursor()

    """ SQL Query """
    cursor.execute("SELECT cities.name \
                    FROM cities \
                    INNER JOIN states ON cities.state_id = states.id \
                    WHERE states.name = %s \
                    ORDER BY cities.id ASC", (sys.argv[4],))

    """ Fetch results """
    cities = cursor.fetchall()

    print(", ".join([record[0] for record in cities]))

    """ Closes connection """
    cursor.close()
    DB.close()


if __name__ == "__main__":
    all_cities()
