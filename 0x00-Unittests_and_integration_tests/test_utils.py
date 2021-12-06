#!/usr/bin/env python3
""" Unit tests for utils.py """
from parameterized import parameterized
from unittest import TestCase, mock


class TestAccessNestedMap(TestCase):
    """ Tests for access_nested_map function """

    @parameterized.expand([
        ({"a": 1}, ("a"), 1),
        ({"a": {"b": 2}}, ("a"), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Test for access_nested_map function """
        from utils import access_nested_map
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a")),
        ({"a": 1}, ("a", "b")),
        ({"a": {"b": 2}}, ("b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ Test for key error failures of access_nested_map function """
        from utils import access_nested_map
        self.assertRaises(KeyError, access_nested_map, nested_map, path)

class TestGetJson(TestCase):
    """ Tests for get_json function """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, payload):
        """ Test for get_json returning payload """
        from utils import get_json
        import requests
        with mock.patch("requests.get") as req:
            req().json.return_value = payload
            self.assertEqual(get_json(url), payload)
