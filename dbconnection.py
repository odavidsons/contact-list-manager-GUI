"""
Class file containing all of the database operation functions. Imported by the main program (contactListManager.py)

Made by David Santos - https://github.com/odavidsons/contactListManager-GUI
"""

import mysql.connector

class dbconnection():

    conn = ""
    cursor = ""

    def __init__(self,dbhost,dbuser,dbpassword,dbname):
        self.conn = mysql.connector.connect(host=dbhost,user=dbuser,password=dbpassword,database=dbname)
        self.cursor = self.conn.cursor()

    def getContacts(self):
        self.cursor.execute("select * from contacts")
        contacts = []
        for row in self.cursor:
            contacts.append({"name": row[1], "phone_number": row[2], "email": row[3], "address": row[4]})
        return contacts

    def getContactByName(self,name):
        query = f"SELECT * FROM contacts WHERE name = '{name}'"
        try:
            self.cursor.execute(query)
            contact = []
            for row in self.cursor:
                contact.append({"name": row[1], "phone_number": row[2], "email": row[3], "address": row[4]})
            return contact
        except:
            print("Error in getContactByName()")

    def insertContact(self,name,phone_number,email,address):
        query = "INSERT INTO contacts (name,phone_number,email,address) VALUES (%s, %s, %s, %s)"
        values = (name,phone_number,email,address)
        try:
            self.cursor.execute(query,values)
            self.conn.commit()
        except: 
            self.conn.rollback()
            print("Error in insertContact()")

    def editContact(self,old_name,name,phone_number,email,address):
        query = f"UPDATE contacts SET name = '{name}',phone_number = '{phone_number}',email = '{email}',address = '{address}' WHERE name = '{old_name}'"
        try:
            self.cursor.execute(query)
            self.conn.commit()
        except:
            self.conn.rollback()
            print("Error in editContact()")

    def removeContact(self,name):
        query = f"DELETE FROM contacts WHERE name = '{name}'"
        try:
            self.cursor.execute(query)
            self.conn.commit()
        except:
            self.conn.rollback()
            print("Error in removeContact()")
