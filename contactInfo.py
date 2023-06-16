"""
Basic python app for managing a list of contacs.
Allows the user to add new, edit and remove contacts, as well as import or export the list as a JSON file.

Made by David Santos - https://github.com/odavidsons/contactListManager-GUI
"""

import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as msg
import json
import dbconnection #File containing database class/functions

class App(tk.Frame):

    contactsDataJSON = [] #Contact data is stored in a temporary list while the app is running, which is then used to export
    contactsDataDB = [] #Contact data imported from a database connection
    db = "" #database connection variable
    databaseStatus = False

    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.config(width=300,height=400)
        self.pack()

    #Select and import a JSON file
    def importContactsJSON(self):
        filetypes = (('JSON files', '*.json'),('All files', '*.*'))
        filename = fd.askopenfilename(title='Open a file',initialdir='/home/dsantos/Documentos/VsCode/Python',filetypes=filetypes)
        try:
            file = open(filename)
            data = json.load(file)
            for contact in data:
                contactList.insert(tk.END,contact["name"])
                self.contactsDataJSON.append(contact)
        except: pass

    #Export the current dictionary as a JSON file
    def exportContactsJSON(self):
        try:
            if len(self.contactsDataJSON) > 0:
                json_object = json.dumps(self.contactsDataJSON, indent=4)
                filetypes = (('JSON files', '*.json'),('All files', '*.*'))
                filename = fd.asksaveasfilename(title="Save file",initialdir="/home/dsantos/Documentos/VsCode/Python",filetypes=filetypes)
                with open(filename, "w") as outfile:
                    outfile.write(json_object)
                msg.showinfo(title="Success",message="Your contacts were exported. ("+filename+")")
            else: msg.showerror(title="Failed",message="You have no data to export!")
        except: msg.showerror(title="Error",message="There was an error while exporting your contacts")

    #Create a window with a contact form
    def addContactWindow(self):
        window = tk.Toplevel(self)
        window.title("Add a contact")
        window.geometry(f'+{self.winfo_rootx()}+{self.winfo_rooty()}')
        body = tk.Frame(window,padx=20,pady=20)
        body.grid()
        name = tk.Label(body,text="Name:",pady=5)
        name.grid(row=0,column=0)
        inputName = tk.Entry(body)
        inputName.grid(row=0,column=1)
        phone = tk.Label(body,text="Phone number:",pady=5)
        phone.grid(row=1,column=0)
        inputPhone = tk.Entry(body)
        inputPhone.grid(row=1,column=1)
        email = tk.Label(body,text="Email:",pady=5)
        email.grid(row=2,column=0)
        inputEmail = tk.Entry(body)
        inputEmail.grid(row=2,column=1)
        address = tk.Label(body,text="Address:",pady=5)
        address.grid(row=3,column=0)
        inputAddress = tk.Entry(body)
        inputAddress.grid(row=3,column=1)
        addBtn = tk.Button(body,text="OK",command=lambda: [self.addContact(window,inputName.get(),inputPhone.get(),inputEmail.get(),inputAddress.get())])
        addBtn.grid(columnspan=2)

    #Execute the operations for adding a new contact
    def addContact(self,window,name,phone,email,address):
        if name != "":
            #If database connection is set
            if self.databaseStatus == True:
                self.db.insertContact(name,phone,email,address)
                self.contactsDataDB.append({"name": name, "phone_number": phone, "email": email, "address": address})
                contactList.insert(tk.END,name)
            else:
                #Add a local data entry
                self.contactsDataJSON.append({"name": name, "phone_number": phone, "email": email, "address": address})
                contactList.insert(tk.END,name)
            window.destroy()
        else: msg.showwarning(title="Missing field",message="Please enter at least the contact name")

    #Create a window with the contact details
    def viewContact(self):
        try:
            selected = contactList.get(contactList.curselection())
            for contact in self.contactsDataJSON:
                if contact["name"] == selected:
                    view_name = contact["name"]
                    view_phone = contact["phone_number"]
                    view_email = contact["email"]
                    view_address = contact["address"]
            #Open view window
            window = tk.Toplevel(self)
            window.title("View contact")
            window.geometry(f'+{self.winfo_rootx()}+{self.winfo_rooty()}')
            body = tk.Frame(window,padx=20,pady=20)
            body.grid()
            name = tk.Label(body,text="Name:",pady=5)
            name.grid(row=0,column=0)
            inputName = tk.Label(body,text=view_name)
            inputName.grid(row=0,column=1)
            phone = tk.Label(body,text="Phone number:",pady=5)
            phone.grid(row=1,column=0)
            inputPhone = tk.Label(body,text=view_phone)
            inputPhone.grid(row=1,column=1)
            email = tk.Label(body,text="Email:",pady=5)
            email.grid(row=2,column=0)
            inputEmail = tk.Label(body,text=view_email)
            inputEmail.grid(row=2,column=1)
            address = tk.Label(body,text="Address:",pady=5)
            address.grid(row=3,column=0)
            inputAddress = tk.Label(body,text=view_address)
            inputAddress.grid(row=3,column=1)
            addBtn = tk.Button(body,text="Close",command=window.destroy)
            addBtn.grid(columnspan=2)
        except: pass
            
    #Create a window with the contact edit form
    def editContactWindow(self):
        try:
            selected = contactList.get(contactList.curselection())
            for contact in self.contactsDataJSON:
                if contact["name"] == selected:
                    edit_name = contact["name"]
                    edit_phone = contact["phone_number"]
                    edit_email = contact["email"]
                    edit_address = contact["address"]
            #Open edit window
            window = tk.Toplevel(self)
            window.title("Edit contact")
            window.geometry(f'+{self.winfo_rootx()}+{self.winfo_rooty()}')
            body = tk.Frame(window,padx=20,pady=20)
            body.grid()
            name = tk.Label(body,text="Name:",pady=5)
            name.grid(row=0,column=0)
            inputName = tk.Entry(body,text=edit_name)
            inputName.grid(row=0,column=1)
            inputName.insert(tk.END,edit_name)
            phone = tk.Label(body,text="Phone number:",pady=5)
            phone.grid(row=1,column=0)
            inputPhone = tk.Entry(body,text=edit_phone)
            inputPhone.grid(row=1,column=1)
            inputPhone.insert(tk.END,edit_phone)
            email = tk.Label(body,text="Email:",pady=5)
            email.grid(row=2,column=0)
            inputEmail = tk.Entry(body,text=edit_email)
            inputEmail.grid(row=2,column=1)
            inputEmail.insert(tk.END,edit_email)
            address = tk.Label(body,text="Address:",pady=5)
            address.grid(row=3,column=0)
            inputAddress = tk.Entry(body,text=edit_address)
            inputAddress.grid(row=3,column=1)
            inputAddress.insert(tk.END,edit_address)
            addBtn = tk.Button(body,text="OK",command=lambda: [self.editContact(window,selected,inputName.get(),inputPhone.get(),inputEmail.get(),inputAddress.get())])
            addBtn.grid(columnspan=2)
        except: pass

    #Execute the operations for editing a contact
    def editContact(self,window,old_name,name,phone,email,address):
        try:
            for contact in self.contactsDataJSON:
                if contact["name"] == old_name:
                    contact["name"] = name
                    contact["phone_number"] = phone
                    contact["email"] = email
                    contact["address"] = address
            msg.showinfo(title="Success",message="Contact updated")
            window.destroy()
        except: msg.showerror(title="Failed",message="There was en error updating your contact.")

    #Execute the operations for removing a contact
    def removeContact(self):
        try: 
            selected_index = contactList.curselection()
            selected = contactList.get(contactList.curselection())
            confirm = msg.askyesno(title="Remove contact",message="Do you want to remove this contact? ("+selected+")")
            if confirm == True:
                #If database connection is set
                if self.databaseStatus == True:
                    self.db.removeContact(selected)
                    for contact in self.contactsDataDB:
                        if contact["name"] == selected:
                            self.contactsDataDB.pop(self.contactsDataDB.index(contact))
                    contactList.delete(selected_index,selected_index)
                    print(self.contactsDataDB)
                else:
                    #Delete the local data entries
                    for contact in self.contactsDataJSON:
                        if contact["name"] == selected:
                            self.contactsDataJSON.pop(self.contactsDataJSON.index(contact))
                    contactList.delete(selected_index,selected_index)
        except: pass

    #Create a Window for inputing the database details
    def connectDBWindow(self):
        window = tk.Toplevel(self)
        window.title("Database details")
        window.geometry(f'+{self.winfo_rootx()}+{self.winfo_rooty()}')
        body = tk.Frame(window,padx=20,pady=20)
        body.grid()
        DBhost = tk.Label(body,text="Host:",pady=5)
        DBhost.grid(row=0,column=0)
        inputDBhost = tk.Entry(body)
        inputDBhost.grid(row=0,column=1)
        DBuser = tk.Label(body,text="User:",pady=5)
        DBuser.grid(row=1,column=0)
        inputDBuser = tk.Entry(body)
        inputDBuser.grid(row=1,column=1)
        DBpassword = tk.Label(body,text="Password:",pady=5)
        DBpassword.grid(row=2,column=0)
        inputDBpassword = tk.Entry(body)
        inputDBpassword.grid(row=2,column=1)
        DBname = tk.Label(body,text="Database name:",pady=5)
        DBname.grid(row=3,column=0)
        inputDBname = tk.Entry(body)
        inputDBname.grid(row=3,column=1)
        addBtn = tk.Button(body,text="OK",command=lambda: [self.connectDB(window,inputDBhost.get(),inputDBuser.get(),inputDBpassword.get(),inputDBname.get())])
        addBtn.grid(columnspan=2)

    """ *---------------------------------------------------------------*
        |                Functions for database handling                |
        *---------------------------------------------------------------* """

    #Call dbconnection constructor and set variables
    def connectDB(self,window,dbhost,dbuser,dbpassword,dbname):
        try:
            #self.db = dbconnection.dbconnection(dbhost,dbuser,dbpassword,dbname)
            self.db = dbconnection.dbconnection("localhost","dsantos","123456","contactslist")
            self.databaseStatus = True
            self.setDatabaseStatus()
            msg.showinfo(title="Connected",message="Connected to database")
            window.destroy()
            self.importContactsDB()
        except: msg.showerror(title="Connection failed",message="There was an error connecting to the database")

    #Set the displayed stats of the database connection
    def setDatabaseStatus(self):
        if self.databaseStatus == True:
            statusLabel.config(text="Database Connected")
        else: statusLabel.config(text="Database Disconnected")

    def importContactsDB(self):
        self.contactsDataDB = self.db.getContacts()
        contactList.delete(0,tk.END)
        for contact in self.contactsDataDB:
            contactList.insert(tk.END,contact["name"])

#---------------------------- Run application ----------------------------
app = App()
menubar = tk.Menu(app)
menubar = tk.Menu(app)
contactsMenu = tk.Menu(menubar, tearoff=0)
contactsMenu.add_command(label="Import contacts",command=app.importContactsJSON)
contactsMenu.add_command(label="Export contacts",command=app.exportContactsJSON)
databaseMenu = tk.Menu(menubar, tearoff=0)
databaseMenu.add_command(label="Connect",command=app.connectDBWindow)
databaseMenu.add_command(label="Disconnect",command=app)
menubar.add_cascade(label="Contacts", menu=contactsMenu)
menubar.add_cascade(label="Database", menu=databaseMenu)
menubar.add_command(label="Exit", command=app.quit)

app.master.config(menu=menubar)
app.master.title("Contact Manager")
app.master.resizable(True, True)
optionsFrame = tk.Frame(app,padx=20,pady=10,bg="#2b7287")
optionsFrame.pack()

viewBtn = tk.Button(optionsFrame,text="View",bg="teal",fg="white",highlightthickness=0,command=app.viewContact)
viewBtn.pack(side="left",padx=5)
addBtn = tk.Button(optionsFrame,text="Add",bg="teal",fg="white",highlightthickness=0,command=app.addContactWindow)
addBtn.pack(side="left",padx=5)
editBtn = tk.Button(optionsFrame,text="Edit",bg="teal",fg="white",highlightthickness=0,command=app.editContactWindow)
editBtn.pack(side="left",padx=5)
removeBtn = tk.Button(optionsFrame,text="Remove",bg="teal",fg="white",highlightthickness=0,command=app.removeContact)
removeBtn.pack(side="left",padx=5)

contactsFrame = tk.Frame(app,pady=10,bg="#b0b0b0")
contactsFrame.pack(fill="x")
contactList = tk.Listbox(contactsFrame,width=30)
contactList.pack(side="left",padx=10)
scrollbar_y = tk.Scrollbar(contactsFrame)
scrollbar_y.pack(side="left", fill="y")
contactList.config(yscrollcommand=scrollbar_y.set)
scrollbar_y.config(command = contactList.yview)

statusFrame = tk.Frame(app)
statusFrame.pack(fill="x")
statusLabel = tk.Label(statusFrame,text="Database Disconnected",fg="white",bg="#2b7287")
statusLabel.pack(fill="x")

app.mainloop()