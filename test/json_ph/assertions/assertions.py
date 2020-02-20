# -*- coding: utf-8 -*-
"""
Assertions for test_json_ph
"""

from json_ph.model.messages import AssertionMessages
from json_ph.model.http_headers.http_keys import HeadersKeys
from json_ph.model.http_headers.http_values import HeaderValues


# pylint: disable=missing-class-docstring, missing-function-docstring
class BaseUserAsserts:

    @staticmethod
    def assert_user_id_1(single_search_result):
        assert single_search_result["id"] == 1
        assert single_search_result.get("name") == "Leanne Graham"
        assert single_search_result["username"] == "Bret"
        assert single_search_result["email"] == "Sincere@april.biz"

    @staticmethod
    def assert_headers(headers):
        assert headers.get(HeadersKeys.CONTENT_TYPE) == HeaderValues.APPLICATION_JSON, \
            AssertionMessages.HEADER_NAME_VALUE_EQ.format(header_name=HeadersKeys.CONTENT_TYPE,
                                                          header_value=HeaderValues.APPLICATION_JSON)

        assert headers.get(HeadersKeys.CONNECTION) == HeaderValues.KEEP_ALIVE, \
            AssertionMessages.HEADER_NAME_VALUE_EQ.format(header_name=HeadersKeys.CONNECTION,
                                                          header_value=HeaderValues.KEEP_ALIVE)

        assert headers.get(HeadersKeys.EXPIRES) == "-1", \
            AssertionMessages.HEADER_NAME_VALUE_EQ.format(header_name=HeadersKeys.EXPIRES,
                                                          header_value="-1")

        assert headers.get(HeadersKeys.ACAC) == "true", \
            AssertionMessages.HEADER_NAME_VALUE_EQ.format(header_name=HeadersKeys.ACAC,
                                                          header_value="true")

    @staticmethod
    def assert_user_load_keys(user_load_keys, response_json):
        for user_load_key in user_load_keys:
            assert user_load_key in response_json, AssertionMessages.USER_LOAD_RESPONSE_KEY.format(key=user_load_key)

    @staticmethod
    def assert_response_code(response_code, expected_code):
        assert response_code == expected_code, AssertionMessages.STATUS_CODE.format(status_code=expected_code)

    @staticmethod
    def assert_result_count(response, expected_result_count):
        response_length = len(response.json())
        assert response_length == expected_result_count, \
            AssertionMessages.RESULT_COUNT.format(current_count=response_length, expected_count=expected_result_count)

    @classmethod
    def assert_user_details(cls, response_user_details, expected_user_details):
        nested_keys = ["address", "company"]
        cls.__clear_nested_values_in_dict(expected_user_details, nested_keys)
        assert response_user_details == expected_user_details

    @staticmethod
    def __clear_nested_values_in_dict(dictionary, keys):
        for key in keys:
            dictionary[key] = list(dictionary[key])
