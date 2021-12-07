#!/usr/bin/env python3
""" Unit tests for client.py """
from parameterized import parameterized
from unittest import TestCase, mock


class TestGithubOrgClient(TestCase):
    """ Tests for GithubOrgClient methods """

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @mock.patch('client.get_json',
                mock.MagicMock(return_value={'key': 'value'}))
    def test_org(self, org_name):
        """ Test for GithubOrgClient.org and .get_json methods """
        from client import GithubOrgClient
        test = GithubOrgClient(org_name)
        self.assertEqual(test.org, {'key': 'value'})
