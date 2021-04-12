#author Kevin Kowalski
#SUK IT

import mysql.connector

connection_config = {
        'user': 'sukit',
        'password': '10erWennDu!',
        'host': 'griefed.de',
        'database': 'contact',
        'raise_on_warnings': True,
        'port': 3306
    }

mydb = mysql.connector.connect(**connection_config)


def main():
    print("Hello World") 

    ret = mydb.cmd_ping()
main()