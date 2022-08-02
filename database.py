import sqlite3 as db
from tabulate import tabulate
from contacts import Contacts

connection = db.connect("database.db")
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS contacts (
    name text,
    phone_number integer,
    email text
)""")


def insert_contact(contact):
    with connection:
        cursor.execute("INSERT INTO contacts VALUES (:name, :phone_number, :email)", {
            "name": contact.name, "phone_number": contact.phone_number, "email": contact.email
        })


def get_contact_by_name(name):
    cursor.execute("SELECT * FROM contacts WHERE name =:name", {"name": name})
    return cursor.fetchall()


def get_all_contacts():
    cursor.execute("SELECT * FROM contacts")
    return cursor.fetchall()


def edit_contact(name, email, phone_number):
    with connection:
        cursor.execute("UPDATE contacts SET phone_number =:phone_number, email=:email WHERE name=:name", {
            "name": name, "email": email, "phone_number": phone_number
        })


def delete_contact(contact):
    with connection:
        cursor.execute("DELETE FROM contacts WHERE name=:name", {
            "name": contact.name
        })


contact_1 = Contacts("Python", 897854988, "python@gmail.com")
contact_2 = Contacts("Django", 455888999, "django@gmail.com")
contact_3 = Contacts("Flutter", 333555777222, "flutter@gmail.com")
contact_4 = Contacts("Java", 9845455544, "java@gmail.com")

allContacts = get_all_contacts()
print(tabulate(allContacts))

connection.close()
