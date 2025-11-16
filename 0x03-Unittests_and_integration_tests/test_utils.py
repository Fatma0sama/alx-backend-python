#!/usr/bin/env python3
"""Unit tests for utils.py"""
from typing import Any, Dict, Tuple
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
import utils


class TestAccessNestedMap(unittest.TestCase):
    """Tests for access_nested_map"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
        self, nested_map: Dict, path: Tuple[str, ...], expected: Any
    ) -> None:
        """access_nested_map returns the value for a given path"""
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b"),
    ])
    def test_access_nested_map_exception(
        self, nested_map: Dict, path: Tuple[str, ...], missing_key: str
    ) -> None:
        """access_nested_map raises KeyError with the missing key as message"""
        with self.assertRaises(KeyError) as ctx:
            utils.access_nested_map(nested_map, path)
        self.assertEqual(
            str(ctx.exception),
            "'{}'".format(missing_key)
        )


class TestGetJson(unittest.TestCase):
    """Tests for get_json"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url: str, test_payload: Dict) -> None:
        """get_json should call requests.get and return json payload"""
        mock_resp = Mock()
        mock_resp.json.return_value = test_payload
        with patch(
            "utils.requests.get",
            return_value=mock_resp
        ) as mock_get:
            result = utils.get_json(test_url)
            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """Tests for memoize decorator"""

def test_memoize(self) -> None:
        """memoize caches the result of a method call"""
    class TestClass:
        def a_method(self) -> int:
            return 42

            @utils.memoize
        def a_property(self) -> int:
            return self.a_method()

obj = TestClass()
with patch.object(TestClass, "a_method", return_value=42) as mock_a_method:
    # call twice; a_method should be called only once due to memoization
    self.assertEqual(obj.a_property, 42)
    self.assertEqual(obj.a_property, 42)
    mock_a_method.assert_called_once()
