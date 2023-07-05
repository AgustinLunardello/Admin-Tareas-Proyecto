import sqlite3 as sql
from datetime import datetime
from hashlib import sha256
from uuid import uuid4
from models.userModel import *
from models.tasksModel import *

class AdminDB:
    def __init__(self):
        self.path = '.\DB\DataBase.db'
        
        with sql.connect(self.path) as conn:
            cursor = conn.cursor()
            
            query = '''CREATE TABLE IF NOT EXISTS Users (
                id TEXT PRIMARY KEY,
                name TEXT,
                lastName TEXT,
                bornDate DATE,
                username TEXT,
                password TEXT)'''   
            
            cursor.execute(query)
            conn.commit()
            
            query = '''CREATE TABLE IF NOT EXISTS Tasks (
                id INTEGER PRIMARY KEY,
                tittle TEXT,
                description TEXT,
                state TEXT,
                created DATE,
                updated DATE,
                author TEXT)'''
            
            cursor.execute(query)
            conn.commit()
    
    def registerUser(self, user: UserModelRegister):
        with sql.connect(self.path) as conn:
            cursor = conn.cursor()
            
            data = (str(uuid4()),user.name, user.lastName, user.bornDate, user.username, sha256(user.password.encode()).hexdigest() )
            query = '''INSERT INTO Users (id, name, lastName, bornDate, username, password) VALUES (?,?,?,?,?,?)'''
            
            cursor.execute(query, data)
            conn.commit()
    
    def loginUser(self, user: UserModelLogin):
        with sql.connect(self.path) as conn:
            passwEncrypt = sha256(user.password.encode()).hexdigest()
            data = (user.username, passwEncrypt)
            
            cursor = conn.cursor()
            query = '''SELECT * FROM Users WHERE username = ? AND password = ?'''
            cursor.execute(query, data)
            
            user = cursor.fetchone()
           
            if user:
                return True
            return False
    
    def __get_id(self):
        with sql.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute('''SELECT id FROM Tasks ORDER BY id DESC''')
            
            id = cursor.fetchone()
            if id :
                return id[0] + 1
            return 0 
    
    def addTask(self, task: taskModel):
        new_id = self.__get_id()
        with sql.connect(self.path) as conn:   
            cursor = conn.cursor()
            query = '''INSERT INTO Tasks (id, tittle, description, state, created, updated, author) VALUES (?,?,?,?,?,?,?)'''
            data = (new_id, task.tittle, task.description, task.state, str(datetime.now().strftime('%d-%m-%Y')), str(datetime.now().strftime('%d-%m-%Y')), task.author )
            
            cursor.execute(query, data)
            conn.commit()
            return new_id
