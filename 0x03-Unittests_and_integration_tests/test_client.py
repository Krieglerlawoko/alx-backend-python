#!/usr/bin/env python3
"""Test client module"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test GithubOrgClient class"""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns correct value"""
        mock_get_json.return_value = {"payload": True}
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, {"payload": True})
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

    @patch('client.GithubOrgClient.org', new_callable=Mock)
    def test_public_repos_url(self, mock_org):
        """Test GithubOrgClient._public_repos_url returns correct value"""
        mock_org.return_value = {"repos_url": "http://example.com/repos"}
        client = GithubOrgClient("test_org")
        self.assertEqual(client._public_repos_url, "http://example.com/repos")

    @patch('client.get_json')
    @patch('client.GithubOrgClient._public_repos_url', new_callable=Mock)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """Test GithubOrgClient.public_repos returns correct value"""
        mock_public_repos_url.return_value = "http://example.com/repos"
        mock_get_json.return_value = [{"name": "repo1"}, {"name": "repo2"}]
        client = GithubOrgClient("test_org")
        self.assertEqual(client.public_repos(), [
                         {"name": "repo1"}, {"name": "repo2"}])
        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with("http://example.com/repos")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test GithubOrgClient.has_license returns correct value"""
        self.assertEqual(
            GithubOrgClient.has_license(repo, license_key),
            expected)


@parameterized_class([
    {
        "org_payload": {"repos_url": "http://example.com/repos"},
        "repos_payload": [{"name": "repo1"}, {"name": "repo2"}],
        "expected_repos": [{"name": "repo1"}, {"name": "repo2"}],
        "apache2_repos": []
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test for GithubOrgClient"""

    @classmethod
    def setUpClass(cls):
        """Set up class method"""
        cls.get_patcher = patch('client.requests.get')
        cls.mock_get = cls.get_patcher.start()
        cls.mock_get.return_value.json.side_effect = [
            cls.org_payload, cls.repos_payload]

    @classmethod
    def tearDownClass(cls):
        """Tear down class method"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test GithubOrgClient.public_repos integration"""
        client = GithubOrgClient("test_org")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test GithubOrgClient.public_repos with license integration"""
        client = GithubOrgClient("test_org")
        self.assertEqual(client.public_repos("apache-2.0"),
                         self.apache2_repos)
