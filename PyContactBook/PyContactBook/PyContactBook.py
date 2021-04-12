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

TABLES = {}
TABLES['dhe_kontakte'] = (
    "CREATE TABLE `dhe_kontakte` ("
    "  `kont_no` int(11) NOT NULL AUTO_INCREMENT,"
    "  `name` varchar(64) NOT NULL,"
    "  `vorname` varchar(64) NOT NULL,"
    "  `adresse` varchar(64) NOT NULL,"
    "  `tel` varchar(64) NOT NULL,"
    "  `email` varchar(64) NOT NULL,"
    "  PRIMARY KEY (`kont_no`)"
    ") ENGINE=InnoDB")

mydb = None
cursor = None
sql_statement = None
user = None
domain = None

<<<<<<< HEAD
=======
# contact =[firstname, lastname, adress, phonenumber, mobilenumber, email]
contact = ["", "", "", "", "", ""]

>>>>>>> dc3e0bf2e66e24f95939e321e5b804133c2d33a3
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

<<<<<<< HEAD

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
def create_table():

    global mydb
    global cursor
    global TABLES

    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print("Creating table {}: ".format(table_description), end='')
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")

def make_statement():
    global sql_statement
    global email

    sql_statement = "INSERT INTO dhe_kontakte (name, vorname, adresse, tel, email) VALUES ('{}', '{}', '{}', '{}', '{}')".format(contact[1],contact[0],contact[2],contact[3],email)

def insert_statement():
    global mydb
    global cursor
    global sql_statement

    mydb = mysql.connector.connect(**connection_config)
    cursor = mydb.cursor()
    cursor.execute(sql_statement)



def main():
    global mydb
    global cursor
    global sql_statement
    global email

    isConnected()
    create_table()

    print(create_entry_dict()['surname'])

=======
    contact[0] = input ("Geben Sie den Vornamen ein: ")
    contact[1] = input ("Geben Sie den Nachnamen ein: ")
    contact[2] = input ("Geben Sie die Adresse ein: ")
    contact[3] = input ("Geben Sie die Mobilnummer ein: ")
    contact[4] = input ("Geben Sie die Emailadresse ein: ").strip()
    user = contact[4][:contact[4].index("@")]
    domain = contact[4][contact[4].index("@")+1:]
    output = "Your username is {}and your domain name is {}".format(user,domain)
    email = "{}@{}".format(user,domain)
    print(output)

    make_statement()
    print(sql_statement)

    insert_statement()

main()