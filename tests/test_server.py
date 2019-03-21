import requests
import unittest

class Test(unittest.TestCase):
    def test_a(self):
        resp = requests.get("http://server")
        self.assertEqual(resp.status_code, 200)