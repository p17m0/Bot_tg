import mysql.connector
import os

from dotenv import load_dotenv

load_dotenv()
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
db = os.getenv('DB_NAME')


def read_image(image):
    with open(image, 'rb') as file:
        binaryData = file.read()
    return binaryData


def add_user(data):
    cnx = mysql.connector.connect(user=user,
                              password=password,
                              database=db,
                              host=host)

    cursor = cnx.cursor()
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
    photo = read_image(photo)

    telegramid = data['telegramid']
    add_employee = (f"INSERT INTO agents (email, fio, obrazovanie, samozan, city, opit, phone, date, resume, photo, telegramid) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    insert_tuple = email, fio, obrazovanie, samozan, city, opit, phone, date, resume, photo, telegramid
    try:
        cursor.execute(add_employee, insert_tuple)
        cnx.commit()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        cnx.close()

def take_user_data(user_id):
    cnx = mysql.connector.connect(user=user,
                                  password=password,
                                  database=db,
                                  host=host)

    cursor = cnx.cursor()
    try:
        cursor = cnx.cursor()
        query = (f"SELECT email, phone, fio FROM agents WHERE telegramid = '{user_id}'")
        cursor.execute(query)
        print('takeUserData', cursor)
        for i in cursor:
            return i
    finally:
        cursor.close()
        cnx.close()

def add_client(data):
    cnx = mysql.connector.connect(user=user,
                              password=password,
                              database=db,
                              host=host)

    cursor = cnx.cursor()
    inn = data['inn']
    contact_name = data['contact_name']
    contacts = data['contacts']
    comments = data['comment']
    agent_id = data['telegramid']
    add_cliento = ("INSERT INTO clients (inn, contact_name, contacts, comments, agent_id) VALUES (%s,%s,%s,%s,%s)")
    insert_clento = inn, contact_name, contacts, comments, agent_id
    try:
        cursor.execute(add_cliento, insert_clento)
        cnx.commit()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        cnx.close()

def take_login_password(user_id):
    cnx = mysql.connector.connect(user=user,
                              password=password,
                              database=db,
                              host=host)
    try:
        cursor = cnx.cursor()
        query = (f"SELECT email, password FROM agents WHERE telegramid = '{user_id}'")
        cursor.execute(query)
        print('takelogin', cursor)
        for i in cursor:
            return i
    finally:
        cursor.close()
        cnx.close()

def check_user(user_id):
    cnx = mysql.connector.connect(user=user,
                              password=password,
                              database=db,
                              host=host)

    cursor = cnx.cursor()
    print('check_user')
    query = (f"SELECT telegramid FROM agents WHERE telegramid = '{user_id}'")
    try:
        cursor.execute(query)
        for i in cursor:
            if user_id in i:
                return True
            return False
    except:
        return False 
    finally:
        cursor.close()
        cnx.close()

def check_activation(user_id):
    cnx = mysql.connector.connect(user=user,
                              password=password,
                              database=db,
                              host=host)

    cursor = cnx.cursor()
    print('check_activation')
    query = ("SELECT activation FROM agents "
            f"WHERE telegramid = '{user_id}'")
    try:
        cursor.execute(query)
        for i in cursor:
            print(i)
            if 1 in i:
                cursor.execute("UPDATE agents SET activation = 2 "
                              f"WHERE telegramid = '{user_id}'")
                cnx.commit()
                # обязательно ли переключение на 2?
                return True
            if 2 in i:
                return True
    except:
        return False
    finally:
        cursor.close()
        cnx.close()

def take_deals_history(user_id):
    cnx = mysql.connector.connect(user=user,
                              password=password,
                              database=db,
                              host=host)

    cursor = cnx.cursor()
    
    query = (f"SELECT message, sended_agent from deals_history WHERE deals_id = (SELECT deals_id FROM deals WHERE agent_id = '{user_id}')")  
    try:
        cursor.execute(query)
        print('take_deals_history', cursor)
        datum = cursor.fetchall()
        print(datum)
        if datum == []:
            return 'Сделок нет'
        for lst in datum:
            if lst[1] == True:
                continue
            if lst[1] == False:
                print(lst)
                query = ("UPDATE deals_history SET sended_agent = 1 "
                        f"WHERE deals_id = (SELECT deals_id FROM deals WHERE agent_id = '{user_id}')")
                cursor.execute(query)
                cnx.commit()
                print(cursor)
                return lst[0]
        else:
            return 'Сделок нет'
        
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        cnx.close()
# ssh root@45.84.224.26