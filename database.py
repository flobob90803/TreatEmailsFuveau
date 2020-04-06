import sqlite3
import os.path
from os import path

class Database:

    createtablequery = """
                        CREATE TABLE IF NOT EXISTS users(
                            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                            name TEXT,
                            email TEXT,
                            adresse TEXT,
                            tel TEXT,
                            quartier TEXT,
                            course BOOLEAN,
                            bricolage BOOLEAN,
                            isolees BOOLEAN,
                            scolaire BOOLEAN,
                            autre TEXT
                        )
                        """
    databasename = "users.db"
    databaselocation = "data"



    def __init__(self, listofuser):
        if not path.exists(self.databaselocation):
            try:
                os.mkdir(self.databaselocation)
            except OSError:
                print("Creation of the directory %s failed" % path)
                exit(1)
            else:
                print("Successfully created the directory %s " % path)
        self.conn = self.create_connection(self.databaselocation + '\\' + self.databasename)
        self.cursor = self.conn.cursor()
        self.listOfUser = listofuser
        if self.conn is not None:
            self.createusertable()
            self.createusers()

    def createusers(self):
        for eachuser in self.listOfUser:
            self.createuserifneeded(eachuser)

    def createuserifneeded(self, user):
        if self.checkifuserexist(user):
            print("User :" + user.name + "- Already exists")
        else:
            try:
                usertoadd = (user.name, user.email, user.adresse, user.tel, user.quartier, user.course, user.brico, user.periso, user.scolaire, user.autre)
                sqlinsertquery = """INSERT INTO users (name, email, adresse, tel, quartier, course, bricolage, 
                isolees, scolaire, autre)  VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?) """
                self.cursor.execute(sqlinsertquery, usertoadd)
                self.conn.commit()
                print("User created: " + user.name)
            except sqlite3.OperationalError as e:
                print(e)
                exit(1)

    def checkifuserexist(self, user):
        try:
            self.cursor.execute("SELECT count(*) FROM users WHERE name = \"" + user.name + "\"")
            data = self.cursor.fetchone()[0]
            if data == 0:
                return False
            else:
                return True
        except sqlite3.OperationalError as e:
            print(e)
            exit(1)

    def create_connection(self, db):
        conn = None
        try:
            conn = sqlite3.connect(db)
            return conn
        except sqlite3.OperationalError as e:
            print(e)
            exit(1)
        return conn

    def createusertable(self):
        try:
            self.cursor.execute(self.createtablequery)
        except sqlite3.OperationalError as e:
            print(e)
            exit(1)

    def closedb(self):
        self.conn.close()
