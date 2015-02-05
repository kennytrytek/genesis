from mock import patch
from unittest import TestCase
from webtest import TestApp

from ....app import public_app


class BaseTestCase(TestCase):
    def setUp(self):
        self.addCleanup(patch.stopall)
        self.app = TestApp(public_app)


class MainHandlerTestCase(BaseTestCase):
    def test_get(self):
        resp = self.app.get('/')
        self.assertEqual(resp.body, 'Hi, Maggie!')
