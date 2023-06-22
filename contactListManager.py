"""
Basic python app for managing a list of contacs.
Allows the user to add new, edit and remove contacts, as well as import or export the list as a JSON file.

Made by David Santos - https://github.com/odavidsons/contact-list-manager-GUI
"""
#File imports
import dbconnection #File containing database class/functions
import filehandling #File containing config/log file handling functions
import views #File containing GUI creation for windows inside the app
#Module imports
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as msg
import json
from os import getcwdb,path
from configparser import ConfigParser

class App(tk.Frame):

    contactsDataJSON = [] #Contact data is stored in a temporary list while the app is running, which is then used to export
    db = "" #database connection variable
    databaseStatus = False
    fontLarge = ('default',14)
    fontMedium = ('default',12)

    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.master.config(width=300,height=300)
        self.views = views.views(self)
        self.views.mainAppWindow()

    #Select and import a JSON file
    def importContactsJSON(self):
        if self.databaseStatus == True:
                msg.showinfo(title="Import to database",message="This will import the contacts from the selected file to the database.")
        filetypes = (('JSON files', '*.json'),('All files', '*.*'))
        filename = fd.askopenfilename(title='Open a file',initialdir=getcwdb(),filetypes=filetypes)
        try:
            file = open(filename)
            data = json.load(file)
            for contact in data:
                #If database connection is set
                if self.databaseStatus == True:
                    self.db.insertContact(contact["name"],contact["phone_number"],contact["email"],contact["address"],contact["gender"])
                    self.contactList.insert(tk.END,contact["name"])
                #Import to local data
                else:
                    self.contactList.insert(tk.END,contact["name"])
                    self.contactsDataJSON.append(contact)
            if self.filehandling.logger != '': self.filehandling.logger.info(f'Imported contacts list from ({filename})')
        except: pass

    #Export the current dictionary as a JSON file
    def exportContactsJSON(self):
        try:
            #If database connecton is set
            if self.databaseStatus == True:
                contacts = self.db.getContacts()
            else: contacts = self.contactsDataJSON
            if len(contacts) > 0:
                json_object = json.dumps(contacts, indent=4)
                filetypes = (('JSON files', '*.json'),('All files', '*.*'))
                filename = fd.asksaveasfilename(title="Save file",initialdir=getcwdb(),filetypes=filetypes)
                with open(filename, "w") as outfile:
                    outfile.write(json_object)
                msg.showinfo(title="Success",message="Your contacts were exported. ("+filename+")")
                if self.filehandling.logger != '': self.filehandling.logger.info(f'Exported contacts list to ({filename})')
            else: msg.showerror(title="Failed",message="You have no data to export!")
        except: msg.showerror(title="Error",message="There was an error while exporting your contacts")

    #Execute the operations for adding a new contact
    def addContact(self,window,name,phone,email,address,gender):
        if name != "":
            #If database connection is set
            if self.databaseStatus == True:
                self.db.insertContact(name,phone,email,address,gender)
                self.contactList.insert(tk.END,name)
            else:
                #Add a local data entry
                self.contactsDataJSON.append({"name": name, "phone_number": phone, "email": email, "address": address, "gender": gender})
                self.contactList.insert(tk.END,name)
            window.destroy()
        else: msg.showwarning(title="Missing field",message="Please enter at least the contact name")

    #Execute the operations for editing a contact
    def editContact(self,window,selected_index,name,phone,email,address,gender):
        try:
            old_name = self.contactList.get(selected_index)
            if self.databaseStatus == True:
                self.db.editContact(old_name,name,phone,email,address,gender)
                #Update the listbox entry with the new name
                self.contactList.delete(selected_index,selected_index)
                self.contactList.insert(selected_index,name)
            else:
                for contact in self.contactsDataJSON:
                    if contact["name"] == old_name:
                        contact["name"] = name
                        contact["phone_number"] = phone
                        contact["email"] = email
                        contact["address"] = address
                        contact["gender"] = gender
            msg.showinfo(title="Success",message="Contact updated")
            window.destroy()
        except: msg.showerror(title="Failed",message="There was en error updating your contact.")

    #Execute the operations for removing a contact
    def removeContact(self):
        try: 
            selected_index = self.contactList.curselection()
            selected = self.contactList.get(self.contactList.curselection())
            confirm = msg.askyesno(title="Remove contact",message="Do you want to remove this contact? ("+selected+")")
            if confirm == True:
                #If database connection is set
                if self.databaseStatus == True:
                    self.db.removeContact(selected)
                    self.contactList.delete(selected_index,selected_index)
                else:
                    #Delete the local list entry
                    for contact in self.contactsDataJSON:
                        if contact["name"] == selected:
                            self.contactsDataJSON.pop(self.contactsDataJSON.index(contact))
                    self.contactList.delete(selected_index,selected_index)
        except: pass

    #Update the contact list counter
    def contactCounter(self):
        n_contacts = self.contactList.size()
        self.counterLabel.config(text=f"Total contacts: {n_contacts}")
        self.after(1000,self.contactCounter)

    """ *---------------------------------------------------------------*
        |         Functions for config and logs file handling           |
        *---------------------------------------------------------------* """

    #Create the filehandling constructor
    def initializeFiles(self):
        self.configFile = ConfigParser()
        self.filehandling = filehandling.filehandling(self.configFile)
        if not path.exists('config.ini'):
            self.configFile['DATABASE_DETAILS'] = {'dbhost': '', 'dbuser': '', 'dbpwd': '', 'dbname': ''}
            self.configFile['GLOBAL_SETTINGS'] = {'auto_connect': 0, 'keep_logs': 0}
            with open('config.ini', 'w') as configfile:
                self.configFile.write(configfile)
        else: 
            self.configFile.read('config.ini')
            #Check if the auto connect setting is on
            auto_connect = self.configFile.get('GLOBAL_SETTINGS','auto_connect')
            if auto_connect == '1':
                database_details = self.filehandling.loadDatabaseConfig()
                #If the connection details are missing, throw a warning saying that this settings is not working properly
                if database_details[0] != '':
                    self.connectDB(tk.Frame(),database_details[0],database_details[1],database_details[2],database_details[3])
                else: msg.showwarning(title="Auto connect error",message="You have turned on 'Auto connect' in the settings, but you don't have a saved database connection!")
            #Check if the keep logs setting is on
            keep_logs = self.configFile.get('GLOBAL_SETTINGS','keep_logs')
            if keep_logs == '1':
                self.filehandling.configLog()
                #If auto_connect was on, pass the newly created logger object
                if self.db:
                    self.db.logger = self.filehandling.logger

    """ *---------------------------------------------------------------*
        |                Functions for database handling                |
        *---------------------------------------------------------------* """

    #Call dbconnection constructor and set variables
    def connectDB(self,window,dbhost,dbuser,dbpassword,dbname):
        try:
            self.db = dbconnection.dbconnection(dbhost,dbuser,dbpassword,dbname)
            self.db.logger = self.filehandling.logger #Pass the logger object to the dbconnection object
            self.filehandling.saveDatabaseConfig(dbhost,dbuser,dbpassword,dbname)
            self.databaseStatus = True
            self.setDatabaseStatus()
            msg.showinfo(title="Connected",message="Connected to database")
            window.destroy()
            self.importContactsDB()
            self.databaseMenu.entryconfig("Connect",state="disabled")
            self.databaseMenu.entryconfig("Disconnect",state="normal")
        except: msg.showerror(title="Connection failed",message="There was an error connecting to the database")

    def disconnectDB(self):
        try:
            self.db.cursor.close()
            self.db.conn.close()
            self.databaseStatus = False
            self.contactList.delete(0,tk.END)
            self.setDatabaseStatus()
            self.databaseMenu.entryconfig("Connect",state="normal")
            self.databaseMenu.entryconfig("Disconnect",state="disabled")
        except: msg.showerror(title="Disconnection failed",message="There was an error disconnecting the database")

    #Set the displayed stats of the database connection
    def setDatabaseStatus(self):
        if self.databaseStatus == True:
            self.statusLabel.config(text="Database Connected",fg="white")
        else: self.statusLabel.config(text="Database Disconnected",fg="black")

    def importContactsDB(self):
        dbContacts = self.db.getContacts()
        self.contactList.delete(0,tk.END)
        for contact in dbContacts:
            self.contactList.insert(tk.END,contact["name"])

#---------------------------- Run application ----------------------------
if __name__ == '__main__':
    app = App()
    app.contactCounter()
    app.initializeFiles() #Check for the existance of a config file
    app.mainloop()
