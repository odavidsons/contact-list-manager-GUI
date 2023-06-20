"""
Class file containing all of the configuration and logs file handling. Imported by the main program (contactListManager.py)

Made by David Santos - https://github.com/odavidsons/contact-list-manager-GUI
"""

from tkinter import messagebox as msg
from os import path
from configparser import ConfigParser
from tkinter import Frame

class filehandling():

    configFile = ""
    app = ""

    def __init__(self,configFile):
        self.configFile = configFile

    #--------------------------------* CONFIG FILE *--------------------------------#

    #Load the parameters from the DATABASE_DETAILS of the config file to fill out the connection form
    def loadDatabaseConfig(self):
        try:
            self.configFile.read('config.ini')
            dbhost = self.configFile.get('DATABASE_DETAILS','dbhost')
            dbuser = self.configFile.get('DATABASE_DETAILS','dbuser')
            dbpwd = self.configFile.get('DATABASE_DETAILS','dbpwd')
            dbname = self.configFile.get('DATABASE_DETAILS','dbname')
        except:
            dbhost = ''
            dbuser = ''
            dbpwd = ''
            dbname = ''
        return dbhost,dbuser,dbpwd,dbname

    def loadGlobalConfig(self):
        try:
            self.configFile.read('config.ini')
            rememberConn = self.configFile.get('GLOBAL_SETTINGS','auto_connect')
            keepLogs = self.configFile.get('GLOBAL_SETTINGS','keep_logs')
        except:
            rememberConn = 0
            keepLogs = 0
        return rememberConn,keepLogs


    #Save the DATABASE_DETAILS section of the config file if a connection has been set successfully
    def saveDatabaseConfig(self,dbhost,dbuser,dbpwd,dbname):
        try:
            self.configFile.read('config.ini')
            self.configFile.set('DATABASE_DETAILS','dbhost',dbhost)
            self.configFile.set('DATABASE_DETAILS','dbuser',dbuser)
            self.configFile.set('DATABASE_DETAILS','dbpwd',dbpwd)
            self.configFile.set('DATABASE_DETAILS','dbname',dbname)
            with open('config.ini', 'w') as configFile:
                self.configFile.write(configFile)
            return True
        except:
            return False

    def saveGlobalConfig(self,window,rememberConn,keepLogs):
        try:
            self.configFile.read('config.ini')
            self.configFile.set('GLOBAL_SETTINGS','auto_connect',rememberConn)
            self.configFile.set('GLOBAL_SETTINGS','keep_logs',keepLogs)
            with open('config.ini', 'w') as configFile:
                self.configFile.write(configFile)
            window.destroy()
            return True
        except:
            return False

    def resetDatabaseConfig(self):
        try:
            self.configFile.read('config.ini')
            self.configFile.set('DATABASE_DETAILS','dbhost','')
            self.configFile.set('DATABASE_DETAILS','dbuser','')
            self.configFile.set('DATABASE_DETAILS','dbpwd','')
            self.configFile.set('DATABASE_DETAILS','dbname','')
            with open('config.ini', 'w') as configFile:
                self.configFile.write(configFile)
            msg.showinfo(title="Deleted details",message="Your connection details have been reset.")
            return True
        except:
            return False
        
        #--------------------------------* LOGS FILE *--------------------------------#