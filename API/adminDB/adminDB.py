import sqlite3 as sql
from datetime import datetime
from hashlib import sha256
from uuid import uuid4
from models.userModel import *
from models.tasksModel import *

class AdminDB:
    def __init__(self):
        self.path = 'DataBase.db'
        
        with sql.connect(self.path) as conn:
            cursor = conn.cursor()
            
            query = '''CREATE TABLE IF NOT EXISTS Users (
                id VARCHAR PRIMARY KEY,
                name TEXT,
                lastName TEXT,
                bornDate DATE,
                username VARCHAR(25) UNIQUE,
                password VARCHAR)'''   
            
            cursor.execute(query)
            conn.commit()
            
            query = '''CREATE TABLE IF NOT EXISTS Tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tittle VARCHAR(50) NOT NULL,
                description VARCHAR(50) NOT NULL,
                state VARCHAR(25) NOT NULL,
                created DATE NOT NULL,
                updated DATE NOT NULL,
                user_id VARCHAR)'''
            
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
    
    def __get_last_id(self):
        with sql.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute('''SELECT id FROM Tasks ORDER BY id DESC''')
            
            id = cursor.fetchone()
            if id :
                return id[0]
    
    def __get_user_id(self,username: str):
        with sql.connect(self.path) as conn:
            cursor = conn.cursor()
            
            query = 'SELECT id FROM Users WHERE username = ?'
            data = (username,)
            
            cursor.execute(query, data)
            user_id = cursor.fetchone()
            
            if user_id:
                return user_id[0]
    
    
    def addTask(self, task: taskModel):
        with sql.connect(self.path) as conn:   
            cursor = conn.cursor()
            query = '''INSERT INTO Tasks (tittle, description, state, created, updated, user_id) VALUES (?,?,?,?,?,?)'''
            data = (task.tittle, task.description, task.state, str(datetime.now().strftime('%d-%m-%Y')), str(datetime.now().strftime('%d-%m-%Y')), self.__get_user_id(task.author))
            
            cursor.execute(query, data)
            conn.commit()
            return self.__get_last_id()

    def get_all_tasks(self, author: str):
        with sql.connect(self.path) as conn:
            cursor = conn.cursor()
            
            query = '''SELECT * FROM Tasks WHERE user_id = ? '''
            data = (self.__get_user_id(author),)
            cursor.execute(query, data)
            
            tasksData = cursor.fetchall()
            if tasksData:
                tasksList = []
                for taskData in tasksData:
                    task = {
                        'id': taskData[0],
                        'tittle': taskData[1],
                        'description': taskData[2],
                        'state': taskData[3],
                        'created': taskData[4],
                        'updated': taskData[5],
                    }
                    tasksList.append(task)    
                return tasksList
            return None
    
    def get_task_by_id(self, id: int, author: str):
        with sql.connect(self.path) as conn:
            cursor = conn.cursor()
            
            query = '''SELECT * FROM Tasks WHERE id = ? AND user_id = ? '''
            data = (id, self.__get_user_id(author))
            
            cursor.execute(query, data)
            
            taskData = cursor.fetchone()
            if taskData:
                task = {
                    'id': taskData[0],
                    'tittle': taskData[1],
                    'description': taskData[2],
                    'state': taskData[3],
                    'created': taskData[4],
                    'updated': taskData[5],
                }
                return task
            return None

    def delete_task_by_id(self, id: int, author: str):
        with sql.connect(self.path) as conn:
            cursor = conn.cursor()
            
            query = '''DELETE FROM Tasks WHERE id = ? AND user_id = ?'''
            data = (id, self.__get_user_id(author))
            
            cursor.execute(query, data)
            conn.commit()
            return True
        return False
    
    def update_state_task(self, id: int, author: str, new_state: str):
        with sql.connect(self.path) as conn:
            cursor = conn.cursor()
            
            query = '''UPDATE Tasks SET state = ?, updated = ? WHERE id = ? AND user_id = ?'''
            data = (new_state, datetime.now().strftime('%d-%m-%Y'), id, self.__get_user_id(author))
            
            cursor.execute(query,data)
            conn.commit()
            return True
        return False