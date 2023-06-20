# contactListManager-GUI

Basic contact list manager app that allows the user to add, edit, remove and view contact entries

Made with the tkinter GUI toolkit and python 3.10

![image](https://github.com/odavidsons/contactListManager-GUI/assets/122760540/57f9ad6e-c131-4b8f-b4da-82de61a3a257)
![image](https://github.com/odavidsons/contactListManager-GUI/assets/122760540/ea9b674b-6adf-44b3-83ea-71bfab76140d)
![image](https://github.com/odavidsons/contactListManager-GUI/assets/122760540/550f144f-1979-4a72-b1cc-0f581e716976)

## Features

The application works both for local and database storage:

- [X] Import and export contacts via JSON files.
- [X] Connect to a MySQL database.
- [X] Import and export data from database.
- [X] Keep a configuration file with the saved connection details and other settings.
- [X] Settings menu for toggling multiple options
- [X] Auto connect to database on open
- [X] Reset saved connection details

**Planned features**
- [ ] Keep log file
- [ ] Variant with user authentication
- [ ] More contact data fields

## Setup

**Provided in the releases is a single file executable that you can use to run the application easily. The only thing that needs setup is the database, this beeing if you plan on using it**

The currently supported database structure dump is provided in the repository (database.sql). Keep in mind this is using MySQL.

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
