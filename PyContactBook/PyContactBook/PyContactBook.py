#author Kevin Kowalski
#SUK IT

import mysql.connector
import time

<<<<<<< HEAD
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
=======
>>>>>>> 9cc9edf9a6f01b6bde42afd97c701c352fe9131f

contact =[firstname, lastname, adress, phonenumber, mobilenumber, email]

<<<<<<< HEAD
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

=======
connection_config = {
        'user': 'sukit',
        'password': '10erWennDu!',
        'host': 'griefed.de',
        'database': 'contact',
        'raise_on_warnings': True,
        'port': 3306
    }

mydb = mysql.connector.connect(**connection_config)
>>>>>>> 9cc9edf9a6f01b6bde42afd97c701c352fe9131f


def main():
 
  contact[0] = input ("Geben Sie den Vornamen ein: ")
  contact[1] = input ("Geben Sie den Nachnamen ein: ")
  contact[2] = input ("Geben Sie die Adresse ein: ")
  contact[3] = input ("Geben Sie die Mobilnummer ein: ")
  contact[4] = input ("Geben Sie die Mobilnummer ein: ")
  contact[5] = input ("Geben Sie die Emailadresse ein: ").strip()
  user = contact[5][:contact[5].index("@")]
  domain = contact[5][contact[5].index("@")+1:]
  ret = mydb.cmd_ping()
main()