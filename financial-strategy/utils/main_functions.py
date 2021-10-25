import requests
import json
from nose.tools import *

URL = "https://test.jasgme.com/sgme/api"


def get_authorization_token():
    data = {
        "login": "mirla.santos@dellead.com",
        "password": "abcd1234"
    }

    response = requests.post(f'{URL}/authenticate/login', json=data)
    assert_equal(response.status_code, 200)

    json_data = json.loads(response.content)
    token = json_data['token']

    return f'Bearer {token}'


def get_id_companies():
    header = {'Authorization': get_authorization_token()}

    response = requests.get(f'{URL}/companies', headers=header)
    assert_equal(response.status_code, 200)

    json_data = json.loads(response.content)
    id_companies = json_data[0]['id']

    return id_companies
