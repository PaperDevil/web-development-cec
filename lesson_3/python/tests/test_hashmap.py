import pytest
import requests
import json


@pytest.fixture
def get_key_url():
    return 'http://127.0.0.1:5000/hashmap/get'


@pytest.fixture
def set_key_url():
    return 'http://127.0.0.1:5000/hashmap/set'


@pytest.fixture
def get_hash_url():
    return 'http://127.0.0.1:5000/hashmap/items'


def test_hashmap(get_key_url, set_key_url):
    requests.post(set_key_url, json={'key': 'name', 'value': 'Bob'})
    result = requests.get(get_key_url, json={'key': 'name'})
    assert result.json() == 'Bob'