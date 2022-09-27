import psycopg2
import sys
# Connect to your postgres DB
connection = psycopg2.connect(dbname='test_db',
                              user='postgres',
                              password='12qw',
                              host='localhost')

# Open a cursor to perform database operations
cursor = connection.cursor()

def read_image(image):
    fin = None
    print(image)
    try:
        fin = open(image, "rb")
        img = fin.read()
        return img
    except IOError as e:
        print(f'Error {e.args[0]}, {e.args[1]}')
        sys.exit(1)
    finally:
        if fin:
            fin.close()

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
    photo = read_image(photo)
    binary = psycopg2.Binary(photo)
    telegramid = data['telegramid']
    add_employee = (f"""INSERT INTO agents 
                        (email, fio, obrazovanie, samozan, city, opit, phone, date, resume, photo, telegramid)
                        VALUES ('{email}', '{fio}', '{obrazovanie}', '{samozan}', '{city}', '{opit}', '{phone}', '{date}', '{resume}', {binary}, {telegramid})""")
    try:
        cursor.execute(add_employee)
        # Make sure data is committed to the database
        connection.commit()
    except Exception as e:
        print(e)

def add_client(data):
    inn = data['inn']
    contact_name = data['contact_name']
    contacts = data['contacts']
    comments = data['comment']
    agent_id = data['telegramid']
    add_cliento = ("INSERT INTO clients "
                   "(inn, contact_name, contacts, comments, agent_id) "
                  f"VALUES ('{inn}', '{contact_name}', '{contacts}', '{comments}', '{agent_id}')")
    try:
        cursor.execute(add_cliento)
        # Make sure data is committed to the database
        connection.commit()
    except Exception as e:
        print(e)


def take_login_password(user_id):
    query = ("SELECT email, password FROM agents "
            f"WHERE telegramid = {user_id}")
    try:
        cursor.execute(query)
        datum = cursor.fetchall()
        datum = datum[0]
        return datum
    except Exception as e:
        print(e)

def check_user(user_id):
    try:
        cursor.execute("SELECT telegramid FROM agents "
                      f"WHERE telegramid = {user_id}")
        datum = cursor.fetchall()
        for i in datum:
            if user_id in i:
                return True
        return False 
    except Exception as e:
        print(e)

def check_activation(user_id):
    query = ("SELECT activation FROM agents "
            f"WHERE telegramid = {user_id}")
    try:
        cursor.execute(query)
        datum = cursor.fetchall()
        for i in datum:
            if 2 in i:
                return True
            if 1 in i:
                cursor.execute("UPDATE agents SET activation = 2 "
                              f"WHERE telegramid = {user_id}")
                connection.commit()
                # обязательно ли переключение на 2?
                return True
        return False
    except Exception as e:
        print(e)
    
    return False

def take_deals_history(user_id):
    query = ("SELECT message from deals_history "
             "WHERE id = (SELECT deals_id FROM deals "
            f"WHERE agent_id = {user_id})")
    try:
        cursor.execute(query)
        datum = cursor.fetchall()
        if datum == []:
            return 'Сделок нет'
        return datum
    except Exception as e:
        print(e)


