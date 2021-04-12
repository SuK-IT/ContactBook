#author Kevin Kowalski
#SUK IT

import mysql.connector

connection_config = {
        'user': 'sukit',
        'password': '10erWennDu!',
        'host': 'griefed.de:3306',
        'database': 'contact',
        'raise_on_warnings': True
    }

mydb = mysql.connector.connect(**connection_config)


def main():
    print("Hello World")
main()