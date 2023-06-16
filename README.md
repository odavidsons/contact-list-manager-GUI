# contactListManager-GUI

Basic contact list manager app that allows the user to add, edit, remove and view contact entries

Made with the tkinter GUI toolkit and python 3.10

![image](https://github.com/odavidsons/contactListManager-GUI/assets/122760540/40cf428a-671b-4eae-a8e4-6d203cba28a6)
![image](https://github.com/odavidsons/contactListManager-GUI/assets/122760540/55e19dfb-0d39-4ef0-a895-36a625282e99)

The application works both for local and database storage:

- Local storage: All contact entries can be imported and exported via JSON files.
- Database storage: It's possible to create a connection to a databse by inputting it's credentials, and all the data is handled in the remote database.

The currently supported database structure dump is provided in the repository (database.sql).

You should create a database called 'contactslist' and import the dump to it.
```
mysql> CREATE DATABASE contactslist;
mysql> USE contactslist;
mysql> source (path_to_file)/database.sql;
```
