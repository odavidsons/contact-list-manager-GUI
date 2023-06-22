"""
Class file containing all of the GUI creation/operation functions for various windows inside the main app.
Imported by the main program (contactListManager.py)

Made by David Santos - https://github.com/odavidsons/contact-list-manager-GUI
"""
import tkinter as tk
from tkinter import messagebox as msg

class views():

    def __init__(self,app):
        self.app = app
        
    #Create a window with a contact form
    def addContactWindow(self):
        window = tk.Toplevel(self.app)
        window.title("Add a contact")
        window.geometry(f'+{self.app.master.winfo_rootx()}+{self.app.master.winfo_rooty()}')
        body = tk.Frame(window)
        body.grid()
        name = tk.Label(body,text="Name:",font=self.app.fontMedium)
        name.grid(row=0,column=0)
        inputName = tk.Entry(body,font=self.app.fontMedium)
        inputName.grid(row=0,column=1,pady=5,padx=15)
        phone = tk.Label(body,text="Phone number:",font=self.app.fontMedium)
        phone.grid(row=1,column=0)
        inputPhone = tk.Entry(body,font=self.app.fontMedium)
        inputPhone.grid(row=1,column=1,pady=5,padx=15)
        email = tk.Label(body,text="Email:",font=self.app.fontMedium)
        email.grid(row=2,column=0)
        inputEmail = tk.Entry(body,font=self.app.fontMedium)
        inputEmail.grid(row=2,column=1,pady=5,padx=15)
        address = tk.Label(body,text="Address:",font=self.app.fontMedium)
        address.grid(row=3,column=0)
        inputAddress = tk.Entry(body,font=self.app.fontMedium)
        inputAddress.grid(row=3,column=1,pady=5,padx=15)
        gender = tk.Label(body,text="Gender:",font=self.app.fontMedium)
        gender.grid(row=4,column=0)
        gender_value = tk.StringVar(body,"Select a gender")
        inputGender = tk.OptionMenu(body,gender_value,"Male","Female","Other")
        inputGender.grid(row=4,column=1,pady=5,padx=15)
        addBtn = tk.Button(body,text="OK",command=lambda: [self.app.addContact(window,inputName.get(),inputPhone.get(),inputEmail.get(),inputAddress.get(),gender_value.get())])
        addBtn.grid(columnspan=2,pady=5,padx=15)
        self.make_dynamic(window)

    #Create a window with the contact details
    def viewContact(self):
        try:
            selected = self.app.contactList.get(self.app.contactList.curselection())
            #If database connection is set
            if self.app.databaseStatus == True:
                contact = self.app.db.getContactByName(selected)
                view_name = contact[0]["name"]
                view_phone = contact[0]["phone_number"]
                view_email = contact[0]["email"]
                view_address = contact[0]["address"]
                view_gender = contact[0]["gender"]
            else:
                #For local data
                for contact in self.app.contactsDataJSON:
                    if contact["name"] == selected:
                        view_name = contact["name"]
                        view_phone = contact["phone_number"]
                        view_email = contact["email"]
                        view_address = contact["address"]
                        view_gender = contact["gender"]
            #Open view window
            window = tk.Toplevel(self.app)
            window.title("View contact")
            window.geometry(f'+{self.app.master.winfo_rootx()}+{self.app.master.winfo_rooty()}')
            body = tk.Frame(window)
            body.grid()
            name = tk.Label(body,text="Name:",font=self.app.fontMedium)
            name.grid(row=0,column=0,pady=5,padx=15)
            inputName = tk.Label(body,text=view_name,font=self.app.fontMedium)
            inputName.grid(row=0,column=1)
            phone = tk.Label(body,text="Phone number:",font=self.app.fontMedium)
            phone.grid(row=1,column=0,pady=5,padx=15)
            inputPhone = tk.Label(body,text=view_phone,font=self.app.fontMedium)
            inputPhone.grid(row=1,column=1)
            email = tk.Label(body,text="Email:",font=self.app.fontMedium)
            email.grid(row=2,column=0,pady=5,padx=15)
            inputEmail = tk.Label(body,text=view_email,font=self.app.fontMedium)
            inputEmail.grid(row=2,column=1)
            address = tk.Label(body,text="Address:",font=self.app.fontMedium)
            address.grid(row=3,column=0,pady=5,padx=15)
            inputAddress = tk.Label(body,text=view_address,font=self.app.fontMedium)
            inputAddress.grid(row=3,column=1)
            gender = tk.Label(body,text="Gender:",font=self.app.fontMedium)
            gender.grid(row=4,column=0,pady=5,padx=15)
            inputGender = tk.Label(body,text=view_gender,font=self.app.fontMedium)
            inputGender.grid(row=4,column=1)
            addBtn = tk.Button(body,text="Close",font=self.app.fontMedium,command=window.destroy)
            addBtn.grid(columnspan=2,pady=5,padx=15)
            self.make_dynamic(window)
        except: pass
    
    #Create a window with the contact edit form
    def editContactWindow(self):
        try:
            selected = self.app.contactList.get(self.app.contactList.curselection())
            selected_index = self.app.contactList.curselection()
            #If database connection is set
            if self.app.databaseStatus == True:
                contact = self.app.db.getContactByName(selected)
                edit_name = contact[0]["name"]
                edit_phone = contact[0]["phone_number"]
                edit_email = contact[0]["email"]
                edit_address = contact[0]["address"]
                edit_gender = contact[0]["gender"]
            else:
                #For local data
                for contact in self.app.contactsDataJSON:
                    if contact["name"] == selected:
                        edit_name = contact["name"]
                        edit_phone = contact["phone_number"]
                        edit_email = contact["email"]
                        edit_address = contact["address"]
                        edit_gender = contact["gender"]
            #Open edit window
            window = tk.Toplevel(self.app)
            window.title("Edit contact")
            window.geometry(f'+{self.app.master.winfo_rootx()}+{self.app.master.winfo_rooty()}')
            body = tk.Frame(window)
            body.grid()
            name = tk.Label(body,text="Name:",font=self.app.fontMedium)
            name.grid(row=0,column=0)
            inputName = tk.Entry(body,text=edit_name,font=self.app.fontMedium)
            inputName.grid(row=0,column=1,pady=5,padx=15)
            inputName.delete(0,tk.END)
            inputName.insert(tk.END,edit_name)
            phone = tk.Label(body,text="Phone number:",font=self.app.fontMedium)
            phone.grid(row=1,column=0)
            inputPhone = tk.Entry(body,text=edit_phone,font=self.app.fontMedium)
            inputPhone.grid(row=1,column=1,pady=5,padx=15)
            inputPhone.delete(0,tk.END)
            inputPhone.insert(tk.END,edit_phone)
            email = tk.Label(body,text="Email:",font=self.app.fontMedium)
            email.grid(row=2,column=0)
            inputEmail = tk.Entry(body,text=edit_email,font=self.app.fontMedium)
            inputEmail.grid(row=2,column=1,pady=5,padx=15)
            inputEmail.delete(0,tk.END)
            inputEmail.insert(tk.END,edit_email)
            address = tk.Label(body,text="Address:",font=self.app.fontMedium)
            address.grid(row=3,column=0)
            inputAddress = tk.Entry(body,text=edit_address,font=self.app.fontMedium)
            inputAddress.grid(row=3,column=1,pady=5,padx=15)
            inputAddress.delete(0,tk.END)
            inputAddress.insert(tk.END,edit_address)
            gender = tk.Label(body,text="Gender:",font=self.app.fontMedium)
            gender.grid(row=4,column=0)
            gender_value = tk.StringVar(body,edit_gender)
            inputGender = tk.OptionMenu(body,gender_value,"Male","Female","Other")
            inputGender.grid(row=4,column=1,pady=5,padx=15)
            addBtn = tk.Button(body,text="OK",command=lambda: [self.app.editContact(window,selected_index,inputName.get(),inputPhone.get(),inputEmail.get(),inputAddress.get(),gender_value.get())])
            addBtn.grid(columnspan=2,pady=5,padx=15)
            self.make_dynamic(window)
        except: pass

    #Create a Window for inputing the database details
    def connectDBWindow(self):
        database_details = self.app.filehandling.loadDatabaseConfig() #Load the server details from the configuration file
        window = tk.Toplevel(self.app)
        window.title("Database details")
        window.geometry(f'+{self.app.master.winfo_rootx()}+{self.app.master.winfo_rooty()}')
        body = tk.Frame(window,padx=20,pady=20)
        body.grid()
        DBhost = tk.Label(body,text="Host:",font=self.app.fontMedium)
        DBhost.grid(row=0,column=0)
        inputDBhost = tk.Entry(body,font=self.app.fontMedium)
        inputDBhost.grid(row=0,column=1,pady=5,padx=15)
        inputDBhost.insert(0,database_details[0])
        DBuser = tk.Label(body,text="User:",font=self.app.fontMedium)
        DBuser.grid(row=1,column=0)
        inputDBuser = tk.Entry(body,font=self.app.fontMedium)
        inputDBuser.grid(row=1,column=1,pady=5,padx=15)
        inputDBuser.insert(0,database_details[1])
        DBpassword = tk.Label(body,text="Password:",font=self.app.fontMedium)
        DBpassword.grid(row=2,column=0)
        inputDBpassword = tk.Entry(body,font=self.app.fontMedium)
        inputDBpassword.grid(row=2,column=1,pady=5,padx=15)
        inputDBpassword.insert(0,database_details[2])
        DBname = tk.Label(body,text="Database name:",font=self.app.fontMedium)
        DBname.grid(row=3,column=0)
        inputDBname = tk.Entry(body,font=self.app.fontMedium)
        inputDBname.grid(row=3,column=1,pady=5,padx=15)
        inputDBname.insert(0,database_details[3])
        addBtn = tk.Button(body,text="OK",font=self.app.fontMedium,command=lambda: [self.app.connectDB(window,inputDBhost.get(),inputDBuser.get(),inputDBpassword.get(),inputDBname.get())])
        addBtn.grid(columnspan=2,pady=5,padx=15)
        self.make_dynamic(window)

    #Create a window for changing the application settings
    def settingsWindow(self):
        global_settings = self.app.filehandling.loadGlobalConfig()
        autoConnect = tk.StringVar()
        autoConnect.set(global_settings[0])
        keepLogs = tk.StringVar()
        keepLogs.set(global_settings[1])
        
        window = tk.Toplevel(self.app)
        window.title("Settings")
        window.geometry(f'+{self.app.master.winfo_rootx()}+{self.app.master.winfo_rooty()}')
        body = tk.Frame(window, padx=20,pady=20)
        body.grid()
        label1 = tk.Label(window,text="Auto connect on open:",pady=15,padx=15,font=self.app.fontMedium)
        label1.grid(row=0,column=0)
        chk_autoConn = tk.Checkbutton(window,variable=autoConnect,onvalue=1,offvalue=0)
        chk_autoConn.grid(row=0,column=1)
        label2 = tk.Label(window, text="Keep logs:",pady=15,padx=15,font=self.app.fontMedium)
        label2.grid(row=1,column=0)
        chk_keepLogs = tk.Checkbutton(window,variable=keepLogs,onvalue=1,offvalue=0)
        chk_keepLogs.grid(row=1,column=1)
        label3 = tk.Label(window,text="Delete saved connection details",font=self.app.fontMedium)
        label3.grid(row=2,column=0)
        delDBBtn = tk.Button(window,text="Delete",font=self.app.fontMedium, command=self.app.filehandling.resetDatabaseConfig)
        delDBBtn.grid(row=2,column=1,pady=15,padx=15)
        database_details = self.app.filehandling.loadDatabaseConfig()
        if database_details[0] == '': delDBBtn.config(state="disabled")
        saveBtn = tk.Button(window, text="Save",font=self.app.fontMedium, command=lambda: self.app.filehandling.saveGlobalConfig(window,autoConnect.get(),keepLogs.get()))
        saveBtn.grid(row=3,column=0,columnspan=2,pady=15,padx=15)
        self.make_dynamic(window)

    #Make a window's widgets dynamic when resizing
    def make_dynamic(self,window):
        col_count,row_count = window.grid_size()
        
        for i in range(row_count):
            window.grid_rowconfigure(i, weight=1)

        for i in range(col_count):
            window.grid_columnconfigure(i, weight=1)

        for child in window.children.values():
            try:
                child.grid_configure(sticky="nsew")
                self.make_dynamic(child)
            except: pass