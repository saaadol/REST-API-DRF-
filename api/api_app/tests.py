from django.test import TestCase
from rest_framework.test import APIClient

from .models import Data


class AddUserTest(TestCase):
    
    def setUp(self): #setting up the test
        self.client = APIClient()
        self.userCreate =  self.client.post('/api/addUser/', {"username": "TestingUser"}, format = 'json')
        self.sameUserCreate =  self.client.post('/api/addUser/', {"username": "TestingUser"}, format = 'json')

    def test_addUser(self): # Normally it should return 201, but since we are adding the same user again it will return 400
        self.assertEqual(self.userCreate.status_code, 201)
        self.assertEqual(self.sameUserCreate.status_code, 400)


tester = AddUserTest()
tester.setUp()
tester.test_addUser()