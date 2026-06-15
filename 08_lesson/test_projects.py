import pytest
import json
import requests

base_url = "https://yougile.com/"

auth_param = {
         'login' : 'dozen-993@mail.ru',
         'password' : 'ST!2iPJ!dJPZAwZ'
     }
GLOBAL_TOKEN = None

def auth():
    global GLOBAL_TOKEN
    if GLOBAL_TOKEN:
        return GLOBAL_TOKEN

    resp = requests.post(base_url + "api-v2/auth/companies", json=auth_param)
    assert resp.status_code in[200, 201]
    data = resp.json()
    company_id = data['content'][0]['id']
    auth_param['companyId'] = company_id
    resp = requests.post(base_url + "api-v2/auth/keys", json=auth_param )
    assert resp.status_code in [200, 201]
    GLOBAL_TOKEN = resp.json()['key']
    return GLOBAL_TOKEN

def test_create_project():
    my_headers = {}
    token = auth()
    my_headers = {'Authorization' : f'Bearer {token}', 'Content-Type': 'application/json'}
    new_project = { 'title': 'Новый проект'}
    resp= requests.get(base_url + "api-v2/projects", headers=my_headers)
    assert resp.status_code in [200, 201]
    old_project_list = len(resp.json()['content'])
    print ("Количество проектов до создания",old_project_list)
    resp = requests.post(base_url +'api-v2/projects',headers=my_headers, json=new_project)
    assert resp.status_code in [200, 201]
    resp = requests.get(base_url + "api-v2/projects", headers=my_headers)
    assert resp.status_code in [200,201]
    new_project_list = len(resp.json()['content'])
    print("Количество проектов после создания", new_project_list)
    assert new_project_list > old_project_list
    assert new_project_list == old_project_list
def test_put_project():
    my_headers = {}
    token = auth()
    my_headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
    put_project = {'title' : 'Первый измененный проект'}
    resp = requests.get(base_url + "api-v2/projects", headers=my_headers)
    project_id = resp.json()['content'][-1]['id']
    resp = requests.put(base_url + f'api-v2/projects/{project_id}', headers=my_headers,json=put_project)
    assert resp.status_code in [400, 401]
    resp = requests.get(base_url + "api-v2/projects", headers=my_headers)
    assert resp.status_code in [200, 201]
    assert resp.json()['content'][-1]['title'] == 'Первый измененный проект'
def test_get_to_id():
    my_headers = {}
    token = auth()
    my_headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
    resp = requests.get(base_url + "api-v2/projects", headers=my_headers)
    project_id = resp.json()['content'][-1]['id']
    resp = requests.get(base_url + f'api-v2/projects/{project_id}',headers=my_headers)
    assert resp.status_code  in [200, 201]
    assert resp.json()['title'] == 'Какое то название проекта'











