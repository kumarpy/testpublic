import model
import mysql.connector

def open_conn():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="pupperpals"
    )
    return mydb

def pupper_select(slct:str):
    my_db = open_conn()
    select_stmt = "SELECT * FROM PUPPER p join BREED b ON p.breed_id=b.id Where p." + slct
    mycursor = my_db.cursor()
    mycursor.execute(select_stmt)
    mypups = mycursor.fetchall()
    return mypups

def breed_insert(slct:str):
    select_stmt = "SELECT * FROM BREED Where " + slct
    mycursor = mydb.cursor()
    mycursor.execute(select_stmt)
    mybreeds = mycursor.fetchall()
    return mybreeds

