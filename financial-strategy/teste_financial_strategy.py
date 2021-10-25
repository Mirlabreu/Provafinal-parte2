import json
import os
import requests
from nose.tools import *
import sys
import unittest

from dashboard.utils.main_functions import URL

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
path_dir = os.path.join(ROOT_DIR, 'utils')
sys.path.append(path_dir)

from main_functions import *


class TestFinancial_strategy(unittest.TestCase):

    def test_1_get_dashboard_by_id(self):
        id_companies = get_id_companies()
        header = {'Authorization': get_authorization_token()}
        response = requests.get(f'{URL}/financial-strategy/1563', headers=header)
        assert_equal(response.status_code, 200)

        print(response.content)

