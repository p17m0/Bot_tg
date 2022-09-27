from symbol import pass_stmt
import mysql.connector
import os

from dotenv import load_dotenv

load_dotenv()
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
db = os.getenv('DB_NAME')


cnx = mysql.connector.connect(user=user,
                              password=password,
                              database=db,
                              host=host)
cursor = cnx.cursor()

def add_user(data):
    email = data['email'] 
    fio = data['fio']
    obrazovanie = data['fio']
    samozan = data['samozan']
    city = data['city']
    opit = data['opit']
    phone = data['phone']
    date = data['date']
    resume = data['resume']
    photo = data['photo']
    telegramid = data['telegramid']
    add_employee = ("INSERT INTO agents "
                    "(email, fio, obrazovanie, samozan, city, opit, phone, date, resume, photo, telegramid) "
                   f"VALUES ({email}, {fio}, {obrazovanie}, {samozan}, {city}, {opit}, {phone}, {date}, {resume}, LOAD_FILE({photo}), {telegramid})")
    cursor.execute(add_employee)

    # Make sure data is committed to the database
    cnx.commit()

def add_client(data):
    inn = data['inn']
    contact_name = data['contact_name']
    contacts = data['contacts']
    comments = data['comment']
    agent_id = data['telegramid']
    add_cliento = ("INSERT INTO agents "
                   "(inn, contatc_name, contacts, comments, agent_id) "
                  f"VALUES ({inn}, {contact_name}, {contacts}, {comments}, {agent_id})")
    cursor.execute(add_cliento)
    # Make sure data is committed to the database
    cnx.commit()

def take_login_password(user_id):
    query = ("SELECT email, password FROM agents "
            f"WHERE telegramid = {user_id}")
    cursor.execute(query)
    return cursor

def check_user(user_id):
    query = ("SELECT telegramid FROM agents "
            f"WHERE telegramid = {user_id}")

    cursor.execute(query)
    if user_id in cursor:
        return True
    return False 

def check_activation(user_id):
    query = ("SELECT activation FROM agents "
            f"WHERE telegramid = {user_id}")
    cursor.execute(query)
    if 1 in cursor:
        # обязательно ли переключение на 2?
        return True
    return False

def take_deals_history(user_id):
    query = ("SELECT message from deals_history "
             "WHERE id = (SELECT deals_id FROM deals "
            f"WHERE agent_id = {user_id})")
    cursor.execute(query)
    return cursor


cursor.close()
cnx.close()