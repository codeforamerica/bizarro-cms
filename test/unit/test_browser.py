import sys
from os.path import abspath, join, dirname
from acceptance.browser import Browser

repo_root = abspath(join(dirname(__file__), '..'))
sys.path.insert(0, repo_root)

import unittest
from unittest import TestCase


class TestBrowser(TestCase):
    def test_creation(self):
        browser = Browser('Windows', '7', "IE", '8.0')
        self.assertEqual('Windows', browser.os)
        self.assertEqual('7', browser.os_version)
        self.assertEqual('IE', browser.browser)
        self.assertEqual('8.0', browser.browser_version)

    def test_as_selenium_capabilities(self):
        browser = Browser('Windows', '7', "IE", '8.0')
        self.assertEqual(
            {'os': 'Windows', 'os_version': '7',
             'browser': 'IE', 'browser_version': '8.0'},
            browser.as_selenium_capabilities())

    def test_as_selenium_capabilities_with_extra_info(self):
        browser = Browser('Windows', '7', "IE", '8.0')
        self.assertEqual(
            {'os': 'Windows', 'os_version': '7',
             'browser': 'IE', 'browser_version': '8.0', 'foo': 'bar'},
            browser.as_selenium_capabilities({'foo': 'bar'}))

    def test_doesnt_mutate_extra_info(self):
        browser = Browser('Windows', '7', "IE", '8.0')
        other_info = {'foo': 'bar'}
        self.assertEqual(
            {'os': 'Windows', 'os_version': '7',
             'browser': 'IE', 'browser_version': '8.0', 'foo': 'bar'},
            browser.as_selenium_capabilities(other_info))
        self.assertEqual(1, len(other_info.keys()))

    def test_from_string(self):
        browsers = Browser.from_string("all")
        self.assertEqual(9, len(browsers))

        browsers = Browser.from_string("ie8")
        self.assertEqual([Browser('Windows', '7', "IE", '8.0')], browsers)

    def test_safe_name(self):
        browser = Browser('Windows', '7', "IE", '8.0')
        self.assertEqual("windows_7_ie_8_0", browser.safe_name())

    def test_as_string(self):
        browser = Browser('Windows', '7', 'IE', '8.0')
        self.assertEqual('Windows 7 IE 8.0', str(browser))




if __name__ == '__main__':
    unittest.main()
