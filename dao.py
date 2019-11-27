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

def breed_insert(inst:str):
    my_db = open_conn()
    insert_stmt = "INSERT INTO BREED (name, temperament, coat) VALUES" + inst
    mycursor = my_db.cursor()
    mycursor.execute(insert_stmt)
    my_db.commit()
    return mycursor.rowcount

def pupper_adopt(delt:str):
    my_db = open_conn()
    delete_stmt = "DELETE FROM PUPPER WHERE ID = " + delt
    mycursor = my_db.cursor()
    mycursor.execute(delete_stmt)
    my_db.commit()
    return mycursor.rowcount
