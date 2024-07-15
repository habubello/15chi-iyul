import psycopg2
conn = psycopg2.connect(database='homework',
                        user='postgres',host='localhost'
                        ,password='1234',port='5432')

cur = conn.cursor()





import hashlib
import os

def hash_password(password):
    salt = os.urandom(16)

    password_bytes = password.encode('utf-8')
    salted_password = salt + password_bytes

    hash_object = hashlib.sha256()

    hash_object.update(salted_password)

    hashed_password = hash_object.hexdigest()

    return salt, hashed_password


def match_password(stored_password, stored_salt, provided_password):
    password_bytes =provided_password.encode('utf-8')
    salted_password =stored_salt +password_bytes

    hash_object =hashlib.sha256()

    hash_object.update(salted_password)

    hashed_password= hash_object.hexdigest()

    return hashed_password ==stored_password














def register():
    print("REGISTER PAGE")


    insert_query = """Insert into users(first_name,last_name,username,password,email) values (%s,%s,%s,%s,%s)"""
    cur.execute(insert_query)


    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    username = input("Username: ")
    password = input("Password: ")
    password_2 = input("Password: ")
    email = input("Email: ")
    if password != password_2:
        print("Passwords don't match")

    else:
        print("Registration successful")
        insert_query(first_name,last_name,username,password,email)

