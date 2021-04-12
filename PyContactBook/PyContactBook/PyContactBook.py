# author Kevin Kowalski
# SUK IT

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


def main():
    print("Hello World")


main()

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

