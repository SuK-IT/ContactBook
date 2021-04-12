#author Kevin Kowalski
#SUK IT

import mysql.connector
import time

connection_config = {
        'user': 'sukit',
        'password': '10erWennDu!',
        'host': 'griefed.de',
        'database': 'contact',
        'raise_on_warnings': True,
        'port': 3306,
        'connect_timeout': 10,
    }

try:
    mydb = mysql.connector.connect(**connection_config)
except:
    mydb = None


def main():
    isConnected()



def isConnected():

    global mydb

    while mydb is None:
        print("Could not connected to remote database.\r\nretrying in 2s.")
        time.sleep(2);
        try:
            mydb = mysql.connector.connect(**connection_config)
        except:
            mydb = None

    print("Connected to remote database" + connection_config['host'] + ":" + str(connection_config['port']) + ".")


main()