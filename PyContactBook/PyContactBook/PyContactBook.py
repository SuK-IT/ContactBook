from errno import errorcode
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

mydb = None
cursor = None

# contact =[firstname, lastname, adress, phonenumber, mobilenumber, email]
contact = ["", "", "", "", "", ""]

def isConnected():

    global mydb
    global cursor

    while mydb is None:
        print("Could not connected to remote database.\r\nretrying in 2s.")
        time.sleep(2);
        try:
            mydb = mysql.connector.connect(**connection_config)
        except:
            mydb = None

    cursor = mydb.cursor()

    print("Connected to remote database" + connection_config['host'] + ":" + str(connection_config['port']) + ".")

def create_entry():

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
    
    return None

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

main()