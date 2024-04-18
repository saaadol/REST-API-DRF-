from django.test import TestCase
from rest_framework.test import APIClient

from .models import Data, Todo

class AddUserTest(TestCase): 
    def setUp(self): #setting up the test
        self.client = APIClient() # Creating a client
        self.objectTestId = Data.objects.create(username="TestingGetUser").id # Creating a user for testing
        
    def test_addUser(self): # Testing /api/addUser/ router
        self.userCreate =  self.client.post('/api/addUser/', {"username": "TestingUser"}, format = 'json') # Creating a user
        self.sameUserCreate =  self.client.post('/api/addUser/', {"username": "TestingUser"}, format = 'json') # Creating the same user again
        self.assertEqual(self.userCreate.status_code, 201) # Checking if the user was created
        self.assertEqual(self.sameUserCreate.status_code, 400)  # Checking if the user was created (should return 400 since the user already exists)

    def test_getUser(self): #Testing /api/users/<int:pk>/ router
        self.getUser = self.client.get(f'/api/users/{self.objectTestId}/', format = 'json')
        self.noUser = self.client.get('/api/users/2/', format = 'json') # Should return 404 (since the user does not exist)
        self.assertEqual(self.getUser.status_code, 200)
        self.assertEqual(self.noUser.status_code, 404)
        
    def test_getAllUsers(self): #Testing /api/users/ router:
        self.objects =  ["User1","User2","User3"] 
        for element in self.objects:
            Data.objects.create(username=element)
        self.getAllUsers = self.client.get('/api/users/', format = 'json')
        self.assertEqual(self.getAllUsers.status_code, 200)
        self.assertEqual(len(self.getAllUsers.data), 4) # 4 since we have 4 users in the database (including the one we created in the setUp method)
        for i in range(0,4):
            if i == 0:
                self.assertEqual(self.getAllUsers.data[0]["username"], "TestingGetUser") # Checking if the username is correct
            else:
                self.assertEqual(self.getAllUsers.data[i]["username"], f"User{i}") # Checking if the username is correct
    
    def test_deleteUser(self):
        
        self.deleteUser = self.client.delete(f'/api/delete/{self.objectTestId}/', format = 'json')
        self.noUser = self.client.delete('/api/delete/2/', format = 'json')
        self.assertEqual(self.deleteUser.status_code, 200)
        self.assertEqual(self.noUser.status_code, 400)
    

    # def test_deleteAllUsers(self):
    #     self.deleteAll = self.client.delete('/api/delete/all', format = 'json')
    #     self.assertEqual(self.deleteAll.status_code, 201)
    #     self.assertEqual(len(Data.objects.all()), 0)

    def test_updateUser(self):
        if Data.objects.filter(username="TestingUser").count() == 0:
            Data.objects.create(username="TestingUser")
        self.updateUser = self.client.put(f'/api/updateUser/{self.objectTestId}/', {"username": "lol"}, format = 'json')
        
        self.noUser = self.client.put('/api/updateUser/3/', {"username": "TestingUser"}, format = 'json')
        self.assertEqual(self.updateUser.status_code, 201)
        self.assertEqual(self.noUser.status_code, 400)