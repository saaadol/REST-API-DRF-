# REST API
This is a REST API project in django for TodoList project developed in django 

# Instalation
For Unix-based systems: <br>
```source myenv/bin/activate``` <br>
For Windows system: <br>
```./myenv/Scripts/activate``` <br>
# Usage
``` cd api/ ``` <br>
``` py manage.py runserver ```<br>
Feel free to navigate the the endpoints : <br>
For admin section : ``` 127.0.0.1/admin/ ```  (username = saadol / password : 123456) <br>
To get all User data : ``` 127.0.0.1/api/all/ ``` <br>
To get specific User data : ``` 127.0.0.1/api/all/1/ ``` (You can change the id of user, for now there is only one)<br> 
To signin : ``` 127.0.0.1/signin/``` <br>
To login : ``` 127.0.0.1/login/ ``` <br>
To Home : ``` 127.0.0.1/home/ ``` <br>
To insert new user : ``` 127.0.0.1/insert/ ``` <br>
To insert new user Todo : ``` 127.0.0.1/insert/todo/ ``` <br>
To update user  : ``` 127.0.0.1/insert/1/ ``` <br> (You can change the id of user)
To delete user : ``` 127.0.0.1/delete/1/ ``` <br> (You can change the id of user)
To delete all :  ``` 127.0.0.1/delete/all/ ``` <br>
### API Endpoints
API Token Endpoint : ``` 127.0.0.1/api/token/ ``` <br>
API refresh Endpoint : ``` 127.0.0.1/api/refresh/ ``` <br>
API verify Endpoint : ``` 127.0.0.1/api/verify/ ``` <br>

# FrontEnd 
Front End is developed in React, Still working on linking the API to it <br>
# Contributing
Pull Requests are welcome, for major changes open an issue first to discuss what you would like to change. <br>
