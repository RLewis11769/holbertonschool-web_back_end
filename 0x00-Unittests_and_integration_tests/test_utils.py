#!/usr/bin/env python3
""" Unit tests for utils.py """
from parameterized import parameterized
from unittest import TestCase
from unittest.mock import patch, MagicMock
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(TestCase):
    """ Tests for access_nested_map function """

    # tuple of (nested_map, path, expected value)
    @parameterized.expand([
        ({"a": 1}, ("a"), 1),
        ({"a": {"b": 2}}, ("a"), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Test for access_nested_map function """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    # tuple of (nested_map, path) - expect KeyError
    @parameterized.expand([
        ({}, ("a")),
        ({"a": 1}, ("a", "b")),
        ({"a": {"b": 2}}, ("b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ Test for key error failures of access_nested_map function """
        self.assertRaises(KeyError, access_nested_map, nested_map, path)


class TestGetJson(TestCase):
    """ Tests for get_json function """
    # tuple of (url, payload dict)
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, payload):
        """ Test for get_json returning payload """
        with patch("requests.get") as req:
            # Set return value of requests.get to payload
            req().json.return_value = payload
            # Verify that when pass in url, recieve value of payload
            self.assertEqual(get_json(url), payload)


class TestMemoize(TestCase):
    """ Tests for memoize function """

    def test_memoize(self):
        """ Test for asserting that memoize function sets attr """

        class TestClass:
            """ Helper class to test with specific return value """
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        # MagicMock to mock method/return value
        test1 = TestClass()
        test1.a_method = MagicMock(return_value=42)
        self.assertEqual(test1.a_property, 42)
        self.assertEqual(test1.a_property, 42)
        test1.a_method.assert_called_once()

        # patch.object to mock method/return value
        with patch.object(TestClass, "a_method",
                          return_value=42) as mock_method:
            test2 = TestClass()
            self.assertEqual(test2.a_property, 42)
            self.assertEqual(test2.a_property, 42)
            mock_method.assert_called_once()
