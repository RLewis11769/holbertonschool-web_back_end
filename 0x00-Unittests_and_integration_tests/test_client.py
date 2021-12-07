#!/usr/bin/env python3
""" Unit tests for client.py """
from client import GithubOrgClient
from parameterized import parameterized
from unittest import TestCase
from unittest.mock import patch, MagicMock, PropertyMock


class TestGithubOrgClient(TestCase):
    """ Tests for GithubOrgClient methods """

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    # MagicMock creates attributes and methods
    # org returns jsonized dict - so specify return_value dict
    @patch('client.get_json',
           MagicMock(return_value={'key': 'value'}))
    def test_org(self, org_name):
        """ Test for GithubOrgClient.org method """
        cls = GithubOrgClient(org_name)
        self.assertEqual(cls.org, {'key': 'value'})

    def test_public_repos_url(self):
        """ Test for GithubOrgClient._public_repos_url method """
        # PropertyMock provides getter/setter methods and calls with no args
        # _public_repos_url returns value for key repos_url
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock,
                   return_value={'repos_url': 'url'}):
            # Method doesn't take args but need to mock with org_name for org
            cls = GithubOrgClient('org_name')
            self.assertEqual(cls._public_repos_url, 'url')

    @patch('client.get_json')
    def test_public_repos(self, license):
        """ Test for GithubOrgClient.public_repos method """
        # PropertyMock provides getter/setter methods and calls with no args
        # public_repos returns value from license using _public_repos_url
        with patch('client.GithubOrgClient.public_repos',
                   new_callable=PropertyMock) as mock_repo:
            cls = GithubOrgClient('org_name')
            # Mock license dict
            license.return_value = {'repos_url': 'url'}
            # Pass org_name to org to retrieve license dict
            mock_repo.return_value = cls.org.get('repos_url')
            self.assertEqual(cls.public_repos, 'url')
            license.assert_called_once()
            mock_repo.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """ Test for GithubOrgClient.has_license if repo has license """
        cls = GithubOrgClient('org_name')
        self.assertEqual(cls.has_license(repo, license_key), expected)
