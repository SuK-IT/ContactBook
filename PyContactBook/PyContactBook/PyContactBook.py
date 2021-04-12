#author Kevin Kowalski
#SUK IT

import mysql.connector


contact =[firstname, lastname, adress, phonenumber, mobilenumber, email]

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