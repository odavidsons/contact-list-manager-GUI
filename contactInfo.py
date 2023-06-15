import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as msg
import json

class App(tk.Frame):

    contactsDataJSON = [] #Imported or added Contacts are stored in a list

    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.config(width=200,height=400)
        self.pack()

    #Select and import a JSON file
    def importContactsJSON(self):
        filetypes = (('JSON files', '*.json'),('All files', '*.*'))
        filename = fd.askopenfilename(title='Open a file',initialdir='/home/dsantos/Documentos/VsCode/Python',filetypes=filetypes)
        file = open(filename)
        data = json.load(file)
        self.contactsDataJSON = data
        for contact in self.contactsDataJSON:
            contactList.insert(tk.END,contact["name"])

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

    #Create a form window
    def addContactWindow(self):
        window = tk.Toplevel(self)
        window.title("Add a contact")
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
        addBtn = tk.Button(body,text="OK",command=lambda: [self.addContact(inputName.get(),inputPhone.get(),inputEmail.get(),inputAddress.get()),window.destroy()])
        addBtn.grid(columnspan=2)

    #Execute the operation for adding a new contact
    def addContact(self,name,phone,email,address):
        self.contactsDataJSON.append({"name": name, "phone": phone, "email": email, "address": address})
        contactList.insert(tk.END,name)

    def viewContact(self):
        print(contactList.curselection())

#Run application
app = App()
menubar = tk.Menu(app)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Import contacts",command=app.importContactsJSON)
filemenu.add_command(label="Export contacts",command=app.exportContactsJSON)
menubar.add_cascade(label="File", menu=filemenu)
menubar.add_command(label="Exit", command=app.quit)

app.master.config(menu=menubar)
app.master.title("Contact Manager")
titleLabel = tk.Label(app,text="Welcome",font=("default bold",20),padx=10,pady=10)
titleLabel.pack()
optionsFrame = tk.Frame(app,padx=20,pady=10)
optionsFrame.pack(fill="x")

viewBtn = tk.Button(optionsFrame,text="View",command=app.viewContact)
viewBtn.pack(side="left",padx=5)
addBtn = tk.Button(optionsFrame,text="Add",command=app.addContactWindow)
addBtn.pack(side="left",padx=5)
removeBtn = tk.Button(optionsFrame,text="Remove")
removeBtn.pack(side="left",padx=5)

contactsFrame = tk.Frame(app,padx=20,pady=10)
contactsFrame.pack(fill="x")
contactList = tk.Listbox(contactsFrame)
contactList.pack(side="left",fill="x")
scrollbar_y = tk.Scrollbar(contactsFrame)
scrollbar_y.pack(side="left", fill="y")
contactList.config(yscrollcommand=scrollbar_y.set)
scrollbar_y.config(command = contactList.yview)

app.mainloop()