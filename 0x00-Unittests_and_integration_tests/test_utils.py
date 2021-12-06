#!/usr/bin/env python3
""" Unit tests for utils.py """
from parameterized import parameterized
from unittest import TestCase


class TestAccessNestedMap(TestCase):
    """ Test for nested map methods """

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
        """ Test for failures of access_nested_map function """
        from utils import access_nested_map
        self.assertRaises(KeyError, access_nested_map, nested_map, path)
