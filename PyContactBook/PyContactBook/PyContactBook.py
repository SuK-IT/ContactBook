import PyContactQueries


def GetContactByName(surname):
    statement = PyContactQueries.make_query_statement(surname)
    result = PyContactQueries.execute_statement(statement)[0]
    return {    'surname': result[1],
                'firstname': result[2],
                'address': result[3],
                'tel': result[4],
                'mail': result[5] }

def GetAllContactsByName(surname):
    statement = PyContactQueries.make_query_statement(surname)
    result = PyContactQueries.execute_statement(statement)
    return result

def CreateContact(dict):
    statement = PyContactQueries.make_insert_statement(dict)
    PyContactQueries.execute_statement(statement)

