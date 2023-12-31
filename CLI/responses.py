import requests
import json
from datetime import datetime
from colorama import Fore
TOKEN = ''
USERNAME = ''
HEADERS = {
    'Authorization': ""}
HOST = '127.0.0.1'
PORT = 8000
URL = f'http://{HOST}:{PORT}'


def register_user(name: str, lastname: str, username: str, password: str, bornDate: str = None) -> dict:
    global URL, HEADERS
    if bornDate:
        bornDate = str(datetime.strptime(bornDate, '%d-%m-%Y').date())
    data = {
        'name': name,
        'lastName': lastname,
        'bornDate': bornDate,
        'username': username,
        'password': password
    }
    r = requests.post(URL+'/register-user', data=json.dumps(data))
    if r.status_code == 200:
        print(Fore.GREEN + r.json()['message']+Fore.RESET)
        return True
    return False


def login_user(username: str, password: str) -> dict:
    global TOKEN, HEADERS, URL, USERNAME
    USERNAME = username
    data = {
        'username': username,
        'password': password
    }
    r = requests.post(URL+'/login', data=json.dumps(data))
    if r.status_code == 200:
        print(Fore.GREEN+ r.json()['message']+Fore.RESET)
        TOKEN = r.json()['access_token']
        HEADERS['Authorization'] = f'Bearer {TOKEN}'
        return True
    elif r.status_code == 401:
        print(Fore.RED+r.json()['detail']+Fore.RESET)
        return False

def add_task(tittle: str, description: str = '', state: str = 'Pendient'):
    global URL, USERNAME, HEADERS
    data = {
        'tittle': tittle,
        'description': description,
        'state': state,
        'author': USERNAME
    }
    r = requests.post(url=URL+'/task', data=json.dumps(data), headers=HEADERS)
    if r.status_code == 200:
        print(Fore.GREEN+r.json()['message']+Fore.RESET)
    elif r.status_code == 401:
        print(Fore.RED+"Unauthorized must login"+Fore.RESET)

def get_tasks() -> list:
    global URL, USERNAME, HEADERS
    r = requests.get(url=URL+f'/tasks/{USERNAME}', headers=HEADERS)
    if r.status_code == 200:
        return r.json()
    elif r.status_code == 404:
        print(Fore.RED + r.json()['detail']+Fore.RESET)
    elif r.status_code == 401:
        print(Fore.RED + "Unauthorized must login"+Fore.RESET)

def get_task_by_id(id_task: int) -> dict:
    global URL, USERNAME, HEADERS
    r = requests.get(url=URL+f'/task/{id_task}/{USERNAME}', headers=HEADERS)

    if r.status_code == 200:
        return r.json()
    elif r.status_code == 404:
        print(Fore.RED+r.json()['detail']+Fore.RESET)
    elif r.status_code == 401:
        print(Fore.RED+"Unauthorized must login"+Fore.RESET)

def delete_task(id_task: int):
    global URL, USERNAME, HEADERS
    r = requests.delete(
        url=URL+f'/task_delete/{id_task}/{USERNAME}', headers=HEADERS)

    if r.status_code == 200:
        print(Fore.GREEN+r.json()['message']+Fore.RESET)
    elif r.status_code == 404:
        print(Fore.RED+r.json()['detail']+Fore.RESET)
    elif r.status_code == 401:
        print(Fore.RED+"Unauthorized must login"+Fore.RESET)

def update_state_task(id_task: int, new_state: str):
    global URL, USERNAME, HEADERS
    r = requests.put(
        url=URL+f'/task_new_state/{id_task}/{USERNAME}/{new_state}', headers=HEADERS)
    if r.status_code == 200:
        print(Fore.GREEN+r.json()['message']+Fore.RESET)
    elif r.status_code == 404:
        print(Fore.RED+r.json()['detail']+Fore.RESET)
    elif r.status_code == 401:
        print(Fore.RED+"Unauthorized must login"+Fore.RESET)
        
print(Fore.RESET)
