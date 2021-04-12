<<<<<<< HEAD
=======
# author Kevin Kowalski
# SUK IT
from errno import errorcode

>>>>>>> 91325b84a8e7ffa0986dc1b5558560e89484e9b8
import mysql.connector
import time

connection_config = {
<<<<<<< HEAD
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

contact =[firstname, lastname, adress, phonenumber, mobilenumber, email]


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

def main():

    isConnected()

    contact[0] = input ("Geben Sie den Vornamen ein: ")
    contact[1] = input ("Geben Sie den Nachnamen ein: ")
    contact[2] = input ("Geben Sie die Adresse ein: ")
    contact[3] = input ("Geben Sie die Mobilnummer ein: ")
    contact[4] = input ("Geben Sie die Mobilnummer ein: ")
    contact[5] = input ("Geben Sie die Emailadresse ein: ").strip()
    user = contact[5][:contact[5].index("@")]
    domain = contact[5][contact[5].index("@")+1:]

=======
    'user': 'sukit',
    'password': '10erWennDu!',
    'host': 'griefed.de',
    'port': '3306',
    'database': 'contact',
    'raise_on_warnings': True
}

cnx = mysql.connector.connect(**connection_config)
cursor = cnx.cursor()

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf-8'".format(connection_config['database']))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)
    try:
        cursor.execute("USE {}".format(connection_config['database']))
    except mysql.connector.Error as err:
        print("Database {} does not exist.".format(connection_config['database']))
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database(cursor)
            print("Database {} created successfully.".format(connection_config['database']))
            cnx.database = connection_config['database']
        else:
            print(err)
            exit(1)

answer = "N"

while answer != "Y":
    name = input("Bitte geben Sie den Nachnamen des neuen Kontakts ein: ")
    vorname = input("Bitte geben Sie den Vornamen des neuen Kontakts ein: ")
    tel = input("Bitte geben Sie die Telefonnummer des neuen Kontakts ein: ")
    strasse = input("Bitte geben Sie den Strassennamen des neuen Kontakts ein: ")
    hausnr = input("Bitte geben Sie die Hausnummer des neuen Kontakts ein: ")
    print("Der neue Kontakt lautet: ", vorname, name, tel, strasse, hausnr, " Sind sie damit einverstanden?")
    answer = input("Bitte mit Y/N bestätigen: ")

print("Hurra", vorname, name, tel, strasse, hausnr)

def main():
    print("Hello World")

>>>>>>> 91325b84a8e7ffa0986dc1b5558560e89484e9b8
main()