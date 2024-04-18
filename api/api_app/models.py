from django.db import models
from django.contrib.auth.hashers import check_password , make_password

# Create your models here.

# class Data(models.Model):
#     username = models.CharField(max_length = 15)
#     email = models.CharField(max_length = 15) 
#     password = models.CharField(max_length = 128)
#     def save(self, *args, **kwargs):
#         self.password = make_password(self.password)
#         super().save(*args, **kwargs)

#     def check_pass(self, raw_pass):
#         return(check_password(raw_pass, self.password))
    
class Data(models.Model):
    username = models.CharField(max_length = 100, unique=True) 

    def __str__(self) -> str:
        return self.username

class Todo(models.Model):
    todoName = models.CharField(max_length = 100, primary_key=True)
    description = models.CharField(max_length = 100)
    isCompleted = models.BooleanField()
    userid = models.ForeignKey(Data, related_name='todos', on_delete=models.CASCADE)
    def __str__(self) -> str:
        return str(self.todoName)