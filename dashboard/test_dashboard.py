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


class TestDashboard(unittest.TestCase):

    def test_1_get_dashboard_by_id(self):
        id_companies = get_id_companies()
        header = {'Authorization': get_authorization_token()}
        response = requests.get(f'{URL}/dashboard/{id_companies}', headers=header)
        assert_equal(response.status_code, 200)

        json_data = json.loads(response.content)
        journeys = json_data['journeys']

        jor_company = journeys[0]
        assert_in('id', jor_company)
        assert_equal(type(jor_company['id']), int)
        assert_equal(jor_company['id'], 10590)

        assert_in('sort_order', jor_company)
        assert_equal(type(jor_company['sort_order']), int)
        assert_equal(jor_company['sort_order'], 1)

        assert_in('current', jor_company)
        assert_equal(type(jor_company['current']), bool)

        assert_in('open', jor_company)
        assert_equal(type(jor_company['open']), bool)

        jor_company = journeys[1]
        assert_in('id', jor_company)
        assert_equal(type(jor_company['id']), int)
        assert_equal(jor_company['id'], 10591)

        assert_in('sort_order', jor_company)
        assert_equal(type(jor_company['sort_order']), int)
        assert_equal(jor_company['sort_order'], 2)

        assert_in('current', jor_company)
        assert_equal(type(jor_company['current']), bool)

        assert_in('open', jor_company)
        assert_equal(type(jor_company['open']), bool)

        jor_company = journeys[2]
        assert_in('id', jor_company)
        assert_equal(type(jor_company['id']), int)
        assert_equal(jor_company['id'], 10592)

        assert_in('sort_order', jor_company)
        assert_equal(type(jor_company['sort_order']), int)
        assert_equal(jor_company['sort_order'], 3)

        assert_in('current', jor_company)
        assert_equal(type(jor_company['current']), bool)

        assert_in('open', jor_company)
        assert_equal(type(jor_company['open']), bool)

        jor_company = journeys[3]
        assert_in('id', jor_company)
        assert_equal(type(jor_company['id']), int)
        assert_equal(jor_company['id'], 10593)

        assert_in('sort_order', jor_company)
        assert_equal(type(jor_company['sort_order']), int)
        assert_equal(jor_company['sort_order'], 4)

        assert_in('current', jor_company)
        assert_equal(type(jor_company['current']), bool)

        assert_in('open', jor_company)
        assert_equal(type(jor_company['open']), bool)

        jor_company = journeys[4]
        assert_in('id', jor_company)
        assert_equal(type(jor_company['id']), int)
        assert_equal(jor_company['id'], 10594)

        assert_in('sort_order', jor_company)
        assert_equal(type(jor_company['sort_order']), int)
        assert_equal(jor_company['sort_order'], 5)

        assert_in('current', jor_company)
        assert_equal(type(jor_company['current']), bool)

        assert_in('open', jor_company)
        assert_equal(type(jor_company['open']), bool)

        jor_company = journeys[5]
        assert_in('id', jor_company)
        assert_equal(type(jor_company['id']), int)
        assert_equal(jor_company['id'], 10595)

        assert_in('sort_order', jor_company)
        assert_equal(type(jor_company['sort_order']), int)
        assert_equal(jor_company['sort_order'], 6)

        assert_in('current', jor_company)
        assert_equal(type(jor_company['current']), bool)

        assert_in('open', jor_company)
        assert_equal(type(jor_company['open']), bool)

        jor_company = journeys[6]
        assert_in('id', jor_company)
        assert_equal(type(jor_company['id']), int)
        assert_equal(jor_company['id'], 10596)

        assert_in('sort_order', jor_company)
        assert_equal(type(jor_company['sort_order']), int)
        assert_equal(jor_company['sort_order'], 7)

        assert_in('current', jor_company)
        assert_equal(type(jor_company['current']), bool)

        assert_in('open', jor_company)
        assert_equal(type(jor_company['open']), bool)

        jor_company = journeys[7]
        assert_in('id', jor_company)
        assert_equal(type(jor_company['id']), int)
        assert_equal(jor_company['id'], 10597)

        assert_in('sort_order', jor_company)
        assert_equal(type(jor_company['sort_order']), int)
        assert_equal(jor_company['sort_order'], 8)

        assert_in('current', jor_company)
        assert_equal(type(jor_company['current']), bool)

        assert_in('open', jor_company)
        assert_equal(type(jor_company['open']), bool)

        jor_company = journeys[8]
        assert_in('id', jor_company)
        assert_equal(type(jor_company['id']), int)
        assert_equal(jor_company['id'], 10598)

        assert_in('sort_order', jor_company)
        assert_equal(type(jor_company['sort_order']), int)
        assert_equal(jor_company['sort_order'], 9)

        assert_in('current', jor_company)
        assert_equal(type(jor_company['current']), bool)

        assert_in('open', jor_company)
        assert_equal(type(jor_company['open']), bool)

        jor_company = journeys[9]
        assert_in('id', jor_company)
        assert_equal(type(jor_company['id']), int)
        assert_equal(jor_company['id'], 10599)

        assert_in('sort_order', jor_company)
        assert_equal(type(jor_company['sort_order']), int)
        assert_equal(jor_company['sort_order'], 10)

        assert_in('current', jor_company)
        assert_equal(type(jor_company['current']), bool)

        assert_in('open', jor_company)
        assert_equal(type(jor_company['open']), bool)

    def test_2_get_dashboard_goals_by_id(self):

        id_companies = get_id_companies()
        header = {'Authorization': get_authorization_token()}
        response = requests.get(f'{URL}/dashboard/goals/1563', headers=header)
        assert_equal(response.status_code, 200)

        print(response.text)

