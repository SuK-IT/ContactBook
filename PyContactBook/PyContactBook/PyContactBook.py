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

def isConnected():

    global mydb
    global cursor

    while mydb is None:
        try:
            mydb = mysql.connector.connect(**connection_config)
        except:
            print("Could not connected to remote database.\r\nretrying in 2s.")
            time.sleep(2);
            mydb = None

    cursor = mydb.cursor()

    print("Connected to remote database " + connection_config['host'] + ":" + str(connection_config['port']) + ".")


def create_entry_dict():

    m_Answer = "N"
    m_Surname = ""
    m_Firstname = ""

    while m_Answer != "Y":

        while m_Surname == "":
            m_Surname = input("Bitte geben Sie den Nachnamen ein: ")

            if m_Surname == "":
                print("Der Nachname darf nicht leer sein!")
                continue
        
        while m_Firstname == "":
            m_Firstname = input("Bitte geben Sie den Vorname ein: ")

            if m_Firstname == "":
                print("Der Vorname darf nicht leer sein!")
                continue

        m_Telephone = input("Bitte geben Sie eine Telefonnummer ein (Optional): ")
        m_Mail = input("Bitte geben Sie eine E-Mail-Adresse ein (Optional): ")
        m_Street = input("Bitte geben Sie eine Strasse und Hausnummer ein (Optional): ")

        print("Soll der Kontakt", m_Surname, m_Firstname, "erstellt werden?")
        m_Answer = input("Bitte mit \'Y\' bestaetigen: ")

        if m_Answer != "Y":
            m_Surname = ""
            m_Firstname = ""

    return { 'surname': m_Surname,
             'firstname': m_Firstname,
             'phone': m_Telephone,
             'street': m_Street,
             'mail': m_Mail,
            }

def main():

    isConnected()

    print(create_entry_dict()['surname'])


main()