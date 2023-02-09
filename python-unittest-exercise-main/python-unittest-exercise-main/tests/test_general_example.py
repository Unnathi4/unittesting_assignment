import unittest

from src import general_example
from src.general_example import GeneralExample
from unittest import mock
from unittest.mock import Mock
from unittest.mock import patch


general_example_instance = GeneralExample()

def test_flatten_dictionary():

    dict1 = {'key1': [3, 2, 1], 'key2': [42, 55, 10], 'key3': [0, 22]}
    expected = [0, 1, 2, 3, 10, 22, 42, 55]

    actual = general_example_instance.flatten_dictionary(dict1)
    assert expected == actual

def test_load_employee_rec_from_database():
    expected = ['emp001', 'Sam', '100000']
    actual = general_example_instance.load_employee_rec_from_database()
    assert expected == actual

def test_general_example(mocker):
    mocker.patch('src.general_example.GeneralExample.load_employee_rec_from_database', return_value = ['emp001', 'Sam', '100000'])
    expected = { 'empId':'emp001' ,'empName': 'Sam','empSalary': '100000'}
    actual = general_example_instance.fetch_emp_details()
    assert expected == actual




