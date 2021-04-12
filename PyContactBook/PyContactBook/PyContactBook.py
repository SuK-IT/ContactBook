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

contact = ["", "", "", "", "", ""]


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

    #contact[0] = input ("Geben Sie den Vornamen ein: ")
    #contact[1] = input ("Geben Sie den Nachnamen ein: ")
    #contact[2] = input ("Geben Sie die Adresse ein: ")
    #contact[3] = input ("Geben Sie die Mobilnummer ein: ")
    #contact[4] = input ("Geben Sie die Mobilnummer ein: ")
    #contact[5] = input ("Geben Sie die Emailadresse ein: ").strip()
    #user = contact[5][:contact[5].index("@")]
    #domain = contact[5][contact[5].index("@")+1:]

main()