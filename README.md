# contactListManager-GUI

Basic contact list manager app that allows the user to add, edit, remove and view contact entries

Made with the tkinter GUI toolkit and python 3.10

![image](https://github.com/odavidsons/contact-list-manager-GUI/assets/122760540/68c01c9e-8fc3-4acc-85b9-e23681cf744d)
![image](https://github.com/odavidsons/contact-list-manager-GUI/assets/122760540/f6cb9186-f64d-42ff-8efd-d0c550115973)
![image](https://github.com/odavidsons/contact-list-manager-GUI/assets/122760540/36169ebe-76a1-44bd-86ad-4b185d7e3b72)

## Features

The application works both for local and database storage:

- [X] Import and export contacts via JSON files.
- [X] Connect to a MySQL database.
- [X] Import and export data from database.
- [X] Keep a configuration file with the saved connection details and other settings.
- [X] Settings menu for toggling multiple options
- [X] Auto connect to database on open
- [X] Reset saved connection details
- [X] Keep log file
- [X] Responsive GUI

**Planned stuff**
- [ ] Variant with user authentication
- [ ] More contact data fields

## Setup

**Provided in the releases is a single file executable that you can use to run the application easily. The only thing that needs setup is the database, this beeing if you plan on using it**

The currently supported database structure dump is provided in the repository (SQL/database.sql). Keep in mind this is using MySQL.

**#1** Create a database called 'contactslist'
```
mysql> CREATE DATABASE contactslist;
```
**#2** Enter the created database
```
mysql> USE contactslist;
```

**#3** Import the database dump provided in the repository code (database.sql)
```
mysql> source (your_path_to_file)/database.sql;
```
