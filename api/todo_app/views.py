from django.shortcuts import render, redirect,  HttpResponse
from .TodoForms import TodoForm
from api_app.models import Data
from django.contrib.auth.models import User
import requests
import json
from django.contrib import messages


def isAuthenticated(request): #isAuthenticated
    if  request.COOKIES.get("refresh") == None: 
        return False
    tokenEndpoint = request.META["HTTP_HOST"]
    token = {
        "token" : request.COOKIES.get("refresh")
    }
    isValid =  requests.post(f"http://{tokenEndpoint}/api/verify/", json=token)
    if isValid.status_code != 200:
        return False
    return True
def setTokens(request,tokenEndpoint,creds):
    getTokens = requests.post(f"{tokenEndpoint}/api/token/", json=creds)
    if getTokens.status_code != 200:
        messages.success(request, 'account not found')
        return render(request,  "login.html", {})
    getTokens = getTokens.json()
    httpResponse = redirect("/home")
    httpResponse.set_cookie("refresh", getTokens["refresh"])
    httpResponse.set_cookie("access", getTokens["access"])
    return httpResponse
def login(request):
    if isAuthenticated(request) == True:
        return redirect("/home")
 
    if request.method == "POST":
        submit_type = request.POST.get('button_clicked')
        if submit_type == "signin":
            return redirect("/signin")
        login_data= request.POST.dict()
        username = login_data.get("username")
        password = login_data.get("password")
        creds = {
            "username" : username,
            "password" : password, 
        }
        tokenEndpoint = request.META["HTTP_ORIGIN"]
        httpResponse = setTokens(request,tokenEndpoint, creds)
        return httpResponse
    return render(request, "login.html", {})


def homepage(request):
    if  isAuthenticated(request) == False:
        return redirect("/login")
    if request.method == "POST":
        httpResponse = redirect("/login")
        httpResponse.delete_cookie("refresh")
        httpResponse.delete_cookie("access")
        httpResponse.delete_cookie("sessionid")
        return httpResponse
        
    return render(request, "home.html")

def signin(request):
    if isAuthenticated(request) == True:
        return redirect("/home")
    if request.method == "POST":
        myform = TodoForm(request.POST)
        if  myform.is_valid():
            try:
                newuser = User.objects.create_user(
                username=myform.cleaned_data["username"],
                email=myform.cleaned_data["email"],
                password=myform.cleaned_data["password"],)
                creds = {
                    "username" : myform.cleaned_data["username"],
                    "password" : myform.cleaned_data["password"]
                }
                tokenEndpoint = request.META["HTTP_ORIGIN"]
                httpResponse = setTokens(request,tokenEndpoint,creds)
                return httpResponse
            except:
                return HttpResponse("User already exists")
        return HttpResponse("404")
    else:
        myform = TodoForm()
    return render(request, "signin.html", {"myform" : myform})