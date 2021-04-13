import mysql.connector
import time
import json


# GLOBALS

connection_config = { }

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

# FUNCTION DEFINITIONS

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

def make_insert_statement(dict):

    return "INSERT INTO dhe_kontakte (name, vorname, adresse, tel, email) VALUES ('{}', '{}', '{}', '{}', '{}')".format(dict['firstname'], dict['surname'], dict['address'], dict['tel'], dict['mail'])

def execute_statement(statement):

    cursor.execute(statement)
    mydb.commit()


def getConnectionConfig():

    with open("connection_config.json", "r") as m_File:
        m_JsonString = m_File.read()
        m_Json = json.loads(m_JsonString)
        return m_Json

def saveConnectionConfig(object):

    m_ConfigString = json.dumps(object)
    print(m_ConfigString)
    with open("connectiong_config.json", "w") as m_File:
        m_File.write(m_ConfigString)

def main():
    global connection_config

    connection_config = getConnectionConfig()

    isConnected()

    #statement = make_insert_statement({ 
        
    #    'firstname': 'fsfd',
    #    'surname': 'NTessdfgsggt1304',
    #    'address': 'dgdgdfg',
    #    'tel': 'fdgdfg',
    #    'mail': 'ghfjmfhfd'

    #    })

    #execute_statement(statement)

# EXECUTE APP
