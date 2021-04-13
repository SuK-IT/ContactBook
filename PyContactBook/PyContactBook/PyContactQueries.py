import mysql.connector
import time
import json

mydb = None
cursor = None
connection_config = None

def make_query_statement(vorname):

    return "SELECT * FROM dhe_kontakte WHERE name=\'" + vorname + "\'"

def make_insert_statement(dict):

    return "INSERT INTO dhe_kontakte (name, vorname, adresse, tel, email) VALUES ('{}', '{}', '{}', '{}', '{}')".format(dict['surname'], dict['firstname'], dict['address'], dict['tel'], dict['mail'])

def execute_statement(statement):

    while cursor is None:
        connect_to_database()

    cursor.execute(statement)
    mydb.commit()
    try:
        return cursor.fetchall()
    except:
        return None


def get_connection_config():

    with open("connection_config.json", "r") as m_File:
        m_JsonString = m_File.read()
        m_Json = json.loads(m_JsonString)
        return m_Json

def save_connection_config(object):

    m_ConfigString = json.dumps(object)
    print(m_ConfigString)
    with open("connection_config.json", "w") as m_File:
        m_File.write(m_ConfigString)

def connect_to_database():

    global mydb
    global cursor
    global connection_config

    while connection_config == None:
        connection_config = get_connection_config()

    while mydb is None:
        try:
            mydb = mysql.connector.connect(**connection_config)
        except:
            print("[INFO   ] [PyContacBook]\r\nCould not connected to remote database.\r\nretrying in 2s.")
            time.sleep(2);
            mydb = None

    cursor = mydb.cursor(buffered=True)
    print("[INFO   ] [PyContacBook]\r\nConnected to remote database " + connection_config['host'] + ":" + str(connection_config['port']) + ".")



#TABLES = {}
#TABLES['dhe_kontakte'] = (
#    "CREATE TABLE `dhe_kontakte` ("
#    "  `kont_no` int(11) NOT NULL AUTO_INCREMENT,"
#    "  `name` varchar(64) NOT NULL,"
#    "  `vorname` varchar(64) NOT NULL,"
#    "  `adresse` varchar(64) NOT NULL,"
#    "  `tel` varchar(64) NOT NULL,"
#    "  `email` varchar(64) NOT NULL,"
#    "  PRIMARY KEY (`kont_no`)"
#    ") ENGINE=InnoDB")