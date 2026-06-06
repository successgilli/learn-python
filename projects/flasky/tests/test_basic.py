import unittest
from app import create_app
from flask import current_app

class BasicTestCase(unittest.TestCase):
    def setUp(self):
        super().setUp()

        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
    
    def tearDown(self):
        super().tearDown()

        self.app_context.pop()
    
    def test_app_exist(self):
        self.assertTrue(current_app)
    
    def test_app_is_test(self):
        self.assertTrue(current_app.config['TESTING'])
