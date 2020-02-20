# -*- coding: utf-8 -*-
"""
Assertion messages test_json_ph
"""


# pylint: disable=missing-class-docstring, too-few-public-methods
class AssertionMessages:
    HEADER_NAME_VALUE_EQ = "Header {header_name} should be {header_value}"
    HEADER_NAME_VALUE_CONTAINS = "Header {header_name} should contains {header_value}"
    RESULT_COUNT = "Expected result count should be {expected_count} is {current_count}"
    STATUS_CODE = "Status code should be {status_code}"
    USER_LOAD_RESPONSE_KEY = "Response should contain key {key}"
