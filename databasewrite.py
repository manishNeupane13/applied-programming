import mysql.connector

def connect_to_db():
    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="@Archer#9810",
    database="taxcustomerdata"

    )
    return mydb

if __name__=="__main__":
    connect_to_db()

