# -*- coding: utf-8 -*-
"""
Example of tests of user resource for https://jsonplaceholder.typicode.com/users

JSONPlaceholder fakes POST and PUT writing, so GET should always return the same thing.
Response does not have nested dict, only http_headers_keys values are present, this affects tests
for resources modification.
"""

import pytest
import requests

# pylint: disable=unused-import
from json_ph.assertions.assertions import BaseUserAsserts
from json_ph.fixtures.user_fixtures import base_url, existing_user_load_id_1, new_user_load


# pylint: disable=missing-function-docstring, redefined-outer-name, no-member, unused-import, unused-argument
def test_get_users(base_url):
    response = requests.get(base_url)
    BaseUserAsserts.assert_response_code(response.status_code, requests.codes.ok)
    BaseUserAsserts.assert_headers(response.headers)


@pytest.mark.parametrize("prop", ["id", "name", "username", "email"])
def test_get_user_by_property(base_url, existing_user_load_id_1, prop):
    response = requests.get(base_url, {prop: existing_user_load_id_1[prop]})
    BaseUserAsserts.assert_response_code(response.status_code, requests.codes.ok)
    BaseUserAsserts.assert_result_count(response, expected_result_count=1)
    BaseUserAsserts.assert_user_id_1(response.json()[0])
    BaseUserAsserts.assert_headers(response.headers)


@pytest.mark.parametrize("id_value", ["999", "0"])
def test_get_user_by_incorrect_id(base_url, existing_user_load_id_1, id_value):
    response = requests.get(base_url, {"id": id_value})
    BaseUserAsserts.assert_response_code(response.status_code, requests.codes.ok)
    BaseUserAsserts.assert_result_count(response, expected_result_count=0)


def test_post_user(base_url, new_user_load):
    response = requests.post(base_url, data=new_user_load)
    BaseUserAsserts.assert_response_code(response.status_code, requests.codes.created)
    BaseUserAsserts.assert_user_load_keys(new_user_load.keys(), response.json().keys())
    BaseUserAsserts.assert_headers(response.headers)


@pytest.mark.parametrize("user_id", ["1"])
def test_put_user(base_url, user_id):
    response = requests.get(''.join([base_url, "/", user_id]))
    user = response.json()
    user["name"] = "New user name"
    response = requests.put((''.join([base_url, "/", user_id])), user)
    BaseUserAsserts.assert_response_code(response.status_code, requests.codes.ok)
    BaseUserAsserts.assert_user_details(response.json(), user)


@pytest.mark.parametrize("user_id", ["1", "5", "9"])
def test_delete_user(base_url, user_id):
    response = requests.delete(''.join([base_url, "/", user_id]))
    BaseUserAsserts.assert_response_code(response.status_code, requests.codes.ok)
    BaseUserAsserts.assert_headers(response.headers)


@pytest.mark.parametrize("user_id", ["1", "5", "9"])
def test_get_nested_posts_by_user_id(base_url, user_id):
    resource_name = "posts"
    response = requests.get(''.join([base_url, "/", user_id, "/", resource_name]))
    BaseUserAsserts.assert_response_code(response.status_code, requests.codes.ok)
    BaseUserAsserts.assert_headers(response.headers)
    BaseUserAsserts.assert_result_count(response, expected_result_count=10)
