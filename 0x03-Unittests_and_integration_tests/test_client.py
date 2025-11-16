#!/usr/bin/env python3
"""Unit and Integration tests for client.GithubOrgClient"""
import unittest
import fixtures
from client import GithubOrgClient
from unittest.mock import Mock, patch
from parameterized import parameterized, parameterized_class

import client  # make sure test_client.py is in the same folder as client.py


class TestGithubOrgClient(unittest.TestCase):
    """Unit tests for GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name: str, mock_get_json: Mock) -> None:
        """GithubOrgClient.org returns the org payload from get_json"""
        expected = {"org": org_name}
        mock_get_json.return_value = expected
        g = client.GithubOrgClient(org_name)
        self.assertEqual(g.org, expected)
        mock_get_json.assert_called_once_with(
            client.GithubOrgClient.ORG_URL.format(org=org_name)
        )

    def test_public_repos_url(self) -> None:
        """Unit test for _public_repos_url property (Task 5)"""
        g = client.GithubOrgClient("google")
        fake_org = {"repos_url": "https://api.github.com/orgs/google/repos"}
        with patch.object(
            client.GithubOrgClient,
            "org",
            new_callable=property,
            return_value=fake_org
        ):
            self.assertEqual(g._public_repos_url, fake_org["repos_url"])

    @patch("client.get_json")
def test_public_repos(self, mock_get_json: Mock) -> None:
    """Test GithubOrgClient.public_repos returns list of repo names"""
    test_repos_payload = [
        {"name": "repo1", "license": {"key": "apache-2.0"}},
        {"name": "repo2", "license": {"key": "bsd-3-clause"}},
        {"name": "repo3", "license": None},
    ]
    mock_get_json.return_value = test_repos_payload

    g = client.GithubOrgClient("google")

    # Patch the property _public_repos_url to a fake URL
    with patch.object(
        client.GithubOrgClient,
        "_public_repos_url",
        new_callable=property,
        return_value="https://fake.url"
    ):
        repos = g.public_repos()
        self.assertListEqual(repos, ["repo1", "repo2", "repo3"])

        apache_repos = g.public_repos(license="apache-2.0")
        self.assertListEqual(apache_repos, ["repo1"])

    # Check that get_json was called exactly once per public_repos call
    self.assertEqual(mock_get_json.call_count, 2)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key: str, expected: bool) -> None:
        """has_license returns True if repo has the given license key"""
        self.assertEqual(client.GithubOrgClient.has_license(repo, license_key),
                         expected)


# Integration tests


param = {
    "org_payload": fixtures.TEST_PAYLOAD[0][0],
    "repos_payload": fixtures.TEST_PAYLOAD[0][1],
    "expected_repos": fixtures.TEST_PAYLOAD[0][2],
    "apache2_repos": fixtures.TEST_PAYLOAD[0][3],
}


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    [param]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient.public_repos using fixtures"""

    @classmethod
    def setUpClass(cls) -> None:
        """Patch requests.get to return fixture data"""
        cls.get_patcher = patch("client.requests.get")
        mock_get = cls.get_patcher.start()

        def side_effect(url: str, *args, **kwargs):
            """Return a Mock whose json() returns fixture"""
            if url == cls.org_payload.get("repos_url", ""):
                return Mock(json=Mock(return_value=cls.repos_payload))
            return Mock(json=Mock(return_value=cls.org_payload))

        mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls) -> None:
        """Stop patcher"""
        cls.get_patcher.stop()

    def test_public_repos(self) -> None:
        """public_repos returns expected list from fixtures"""
        g = client.GithubOrgClient("google")
        self.assertEqual(sorted(g.public_repos()), sorted(self.expected_repos))

    def test_public_repos_with_license(self) -> None:
        """public_repos filters by license (apache-2.0)"""
        g = client.GithubOrgClient("google")
        self.assertEqual(
            sorted(g.public_repos("apache-2.0")),
            sorted(self.apache2_repos)
        )
