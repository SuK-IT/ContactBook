# author Kevin Kowalski
# SUK IT
from errno import errorcode

import mysql.connector

connection_config = {
    'user': 'sukit',
    'password': '10erWennDu!',
    'host': 'griefed.de',
    'port': '3306',
    'database': 'contact',
    'raise_on_warnings': True
}

mydb = mysql.connector.connect(**connection_config)
cnx = mysql.connector.connect(user=connection_config['user'])
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

main()