"""
Assertions for test_json_ph
"""

import pytest


# pylint: disable=missing-function-docstring
@pytest.fixture()
def base_url():
    return "https://jsonplaceholder.typicode.com/users"


@pytest.fixture()
def new_user_load():
    return {"name": "Json Tester", "username": "Tester", "email": "json@test.org"}


@pytest.fixture()
def existing_user_load_id_1():
    return {"id": "1", "name": "Leanne Graham", "username": "Bret", "email": "Sincere@april.biz"}
