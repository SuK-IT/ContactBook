#author Kevin Kowalski
#SUK IT

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)


def main():
    print("Hello World")

main()