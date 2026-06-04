import pytest
import json
import requests

base_url = "https://yougile.com/"

auth_param = {
         'login' : 'dozen-993@mail.ru',
         'password' : 'ST!2iPJ!dJPZAwZ'
     }
def test_delete_key():
    resp = requests.post(base_url + "api-v2/auth/keys/get", json=auth_param)
    data = resp.json()
    token = data[0]['key']
    print(token)
    resp = requests.delete(base_url +'api-v2/auth/keys/'+token)
    assert resp.status_code == 200