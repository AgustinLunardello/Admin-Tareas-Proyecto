from responses import *
from getpass import getpass
import os
from colorama import Fore

def register_user_cli():
    name = input('Enter your name: ')
    lastName = input('Enter your lastname: ')
    bornDate = input('Enter your birthday (dd-mm-YYYY): ')
    username = input('Enter any username: ')
    password = input('Enter any password: ')
    register_user(name, lastName, username, password, bornDate) 

def login_cli():
    while True:
        print('0. Login user')
        print('1. Register user')
        print('2. Exit')
        _ = int(input(''))
        if _ == 0:
            username = input('Username: ')
            password = getpass('Password: ')
            os.system('cls')
            __ = login_user(username, password)
            if __ :
                break
        elif _ == 1:
            register_user_cli()
        elif _ == 2:
            break
        else:
            print(Fore.RED+'Option not exists'+Fore.RESET)
        

def add_task_cli():
    while True:
        title = input('Enter the title of the task: ')
        if title != '':
            description = input('Enter the description of the task: ')
            state = input('Enter the state of the task: ')
            if state:
                state = 'Pendiente'
                
            add_task(title, description, state)
            break
        print(Fore.RED +'The task must have a title'+Fore.RESET)

def get_all_tasks_cli():
    tasks = get_tasks()
    if tasks:
        print('<------- task list ------>')
        for task in tasks:
            print(Fore.RED+'ID:'+Fore.RESET, task['id'])
            print(Fore.RED+'Title:'+Fore.RESET, task['tittle'])
            print(Fore.RED+'Description:'+Fore.RESET, task['description'])
            print(Fore.RED+'State:'+Fore.RESET, task['state'])
            print(Fore.RED+'Created:'+Fore.RESET, task['created'])
            print(Fore.RED+'Updated:'+Fore.RESET, task['updated'])
            print('<-------------------------------->')

def get_task_by_id_cli():
    id_task = int(input('Enter the id task: '))
    task = get_task_by_id(id_task)
    if task :
        print('<----- task ----->')
        print(Fore.RED+'ID:'+Fore.RESET, task['id'])
        print(Fore.RED+'Title:'+Fore.RESET, task['tittle'])
        print(Fore.RED+'Description:'+Fore.RESET, task['description'])
        print(Fore.RED+'State:'+Fore.RESET, task['state'])
        print(Fore.RED+'Created:'+Fore.RESET, task['created'])
        print(Fore.RED+'Updated:'+Fore.RESET, task['updated'])
        print('<-------------------------------->')

def update_state_task_cli():
    id_task = int(input('Enter the id task: '))
    new_state = input('Enter the new state: ')
    update_state_task(id_task, new_state)

def delete_task_cli():
    id_task = int(input('Enter the id task: '))
    delete_task(id_task)

def main():
    login_cli()
    while True:
        print('<------ Options -------->')
        print('1. Add tasks')
        print('2. Get all tasks')
        print('3. Get task by id')
        print('4. Updated state task')
        print('5. delete task')
        print('6. Login')
        print('7. Exit')
        print('<-------------------------->')
        
        opt = int(input(''))
        
        #add task
        if opt == 1:
            os.system('cls')
            add_task_cli()
        #get all task
        elif opt == 2:
            os.system('cls')
            get_all_tasks_cli()
        #get task by id
        elif opt == 3:
            os.system('cls')
            get_task_by_id_cli()
        #update state task
        elif opt == 4:
            os.system('cls')
            update_state_task_cli()
        #delete task
        elif opt == 5:
            os.system('cls')
            delete_task_cli()
        #login
        elif opt == 6:
            os.system('cls')
            login_cli()
        #exit
        elif opt == 7:
            os.system('cls')
            break
        #option not exists
        else:
            os.system('cls')
            print(Fore.RED +'Option not exists'+Fore.RESET)

if __name__ == '__main__':
    main()