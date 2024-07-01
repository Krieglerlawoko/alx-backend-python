#!/usr/bin/env python3
"""Unit and integration tests for client.py"""

import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from utils import get_json


class TestGithubOrgClient(unittest.TestCase):
    """Test class for GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json', return_value={"repos_url": "test_url"})
    def test_org(self, org_name, mock_get_json):
        """Test GithubOrgClient.org returns expected result"""
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, mock_get_json.return_value)
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """Test GithubOrgClient._public_repos_url returns expected result"""
        mock_org.return_value = {"repos_url": "test_url"}
        client = GithubOrgClient("test_org")
        self.assertEqual(client._public_repos_url, "test_url")

    @patch('client.get_json')
    @patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """Test GithubOrgClient.public_repos returns expected result"""
        mock_public_repos_url.return_value = "test_url"
        mock_get_json.return_value = [{"name": "repo1"}, {"name": "repo2"}]
        client = GithubOrgClient("test_org")
        self.assertEqual(client.public_repos(), ["repo1", "repo2"])
        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with("test_url")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test GithubOrgClient.has_license returns expected result"""
        self.assertEqual(GithubOrgClient.has_license(repo, license_key), expected)


@parameterized_class([
    {
        "org_payload": {"repos_url": "test_url"},
        "repos_payload": [{"name": "repo1"}, {"name": "repo2"}],
        "expected_repos": ["repo1", "repo2"],
        "apache2_repos": [{"name": "repo1"}]
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient"""

    @classmethod
    def setUpClass(cls):
        """Set up class for integration tests"""
        cls.get_patcher = patch('utils.requests.get', side_effect=cls.side_effect)
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Tear down class for integration tests"""
        cls.get_patcher.stop()

    @staticmethod
    def side_effect(url):
        """Side effect for requests.get"""
        if url == "https://api.github.com/orgs/test_org":
            return Mock(**{'json.return_value': TestIntegrationGithubOrgClient.org_payload})
        if url == "test_url":
            return Mock(**{'json.return_value': TestIntegrationGithubOrgClient.repos_payload})
        return None

    def test_public_repos(self):
        """Test GithubOrgClient.public_repos integration"""
        client = GithubOrgClient("test_org")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test GithubOrgClient.public_repos with license integration"""
        client = GithubOrgClient("test_org")
        self.assertEqual(client.public_repos(license="apache-2.0"), self.apache2_repos)


if __name__ == '__main__':
    unittest.main()

