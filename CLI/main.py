import requests
import json
from datetime import datetime
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
    print(r.json()['message'])


def login_user(username: str, password: str) -> dict:
    global TOKEN, HEADERS, URL, USERNAME
    USERNAME = username
    data = {
        'username': username,
        'password': password
    }
    r = requests.post(URL+'/login', data=json.dumps(data))
    if r.status_code == 200:
        print(r.json()['message'])

        TOKEN = r.json()['access_token']
        HEADERS['Authorization'] = f'Bearer {TOKEN}'
    elif r.status_code == 401:
        print(r.json()['detail'])


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
        print(r.json()['message'])
    elif r.status_code == 401:
        print("Unauthorized must login")


def get_tasks() -> list:
    global URL, USERNAME, HEADERS
    r = requests.get(url=URL+f'/tasks/{USERNAME}', headers=HEADERS)
    if r.status_code == 200:
        return r.json()
    elif r.status_code == 404:
        print(r.json()['detail'])
    elif r.status_code == 401:
        print("Unauthorized must login")


def get_task_by_id(id_task: int) -> dict:
    global URL, USERNAME, HEADERS
    r = requests.get(url=URL+f'/task/{id_task}/{USERNAME}', headers=HEADERS)

    if r.status_code == 200:
        return r.json()
    elif r.status_code == 404:
        print(r.json()['detail'])
    elif r.status_code == 401:
        print("Unauthorized must login")


def delete_task(id_task: int):
    global URL, USERNAME, HEADERS
    r = requests.delete(
        url=URL+f'/task_delete/{id_task}/{USERNAME}', headers=HEADERS)

    if r.status_code == 200:
        print(r.json()['message'])
    elif r.status_code == 404:
        print(r.json()['detail'])
    elif r.status_code == 401:
        print("Unauthorized must login")


def update_state_task(id_task: int, new_state: str):
    global URL, USERNAME, HEADERS
    r = requests.put(
        url=URL+f'/task_new_state/{id_task}/{USERNAME}/{new_state}', headers=HEADERS)
    if r.status_code == 200:
        print(r.json()['message'])
    elif r.status_code == 404:
        print(r.json()['detail'])
    elif r.status_code == 401:
        print("Unauthorized must login")


# register_user('Agustin', 'Lunardello', 'AgusLuna', '12345', '03-05-2004')
# login_user('AgusLuna', '12345')
# add_task('google')
# tasks = get_tasks()
# print('ID   |   Tittle  |   Desc    |   state   |   created    |    updated')
# for task in tasks:
#     print(task['id'], end='      ')
#     print(task['tittle'], end='        ')
#     print(task['description'], end='         ')
#     print(task['state'], end='         ')
#     print(task['created'], end='       ')
#     print(task['updated'], end='       ')
# get_task_by_id(3)
# update_state_task(3,'new state')
# get_task_by_id(3)
# delete_task(3)
