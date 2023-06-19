# contactListManager-GUI

Basic contact list manager app that allows the user to add, edit, remove and view contact entries

Made with the tkinter GUI toolkit and python 3.10

![image](https://github.com/odavidsons/contactListManager-GUI/assets/122760540/57f9ad6e-c131-4b8f-b4da-82de61a3a257)
![image](https://github.com/odavidsons/contactListManager-GUI/assets/122760540/ea9b674b-6adf-44b3-83ea-71bfab76140d)
![image](https://github.com/odavidsons/contactListManager-GUI/assets/122760540/550f144f-1979-4a72-b1cc-0f581e716976)

## Features

The application works both for local and database storage:

- Local storage: All contact entries are stored within the application's memory temporarily. They can be imported and exported via a JSON file with the correct format. An example is provided in the repository files (contacts.json)
- Database storage: It's possible to connect to a MySQL database by inputting the connection details. All the data is imported automatically and the operations then happen directly to the database. The connection details are also saved in a configuration file and automatically loaded when you open the 'Connect' menu.

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
