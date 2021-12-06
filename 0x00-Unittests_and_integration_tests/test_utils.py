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
        with mock.patch("requests.get") as req:
            req().json.return_value = payload
            self.assertEqual(get_json(url), payload)


class TestMemoize(TestCase):
    """ Tests for memoize function """

    def test_memoize(self):
        """ Test for asserting that memoize function sets attr """
        from utils import memoize

        class TestClass:
            """ Test class for memoize function """
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        # MagicMock to mock method/return value
        test1 = TestClass()
        test1.a_method = mock.MagicMock(return_value=42)
        self.assertEqual(test1.a_property, 42)
        self.assertEqual(test1.a_property, 42)
        test1.a_method.assert_called_once()

        # patch.object to mock method/return value
        with mock.patch.object(TestClass, "a_method", return_value=42) as mock_method:
            test2 = TestClass()
            self.assertEqual(test2.a_property, 42)
            self.assertEqual(test2.a_property, 42)
            mock_method.assert_called_once()
