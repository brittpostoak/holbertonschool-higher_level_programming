#!/usr/bin/python3
# Displays all values in the states table of hbtn_0e_0_usa
import MySQLdb
import sys

if __name__ == '__main__':
    db_host = 'localhost'
    usuario = sys.argv[1]
    clave = sys.argv[2]
    base_de_datos = sys.argv[3]

    db = MySQLdb.connect(host=db_host, user=usuario,
                         password=clave, database=base_de_datos, port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{:s}'\
ORDER BY id ASC".format(sys.argv[4]))
    rows = cur.fetchall()

    for data in rows:
        print(data)
    cur.close()
    db.close()
