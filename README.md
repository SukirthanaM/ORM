# Ex02 Django ORM Web Application
## Date: 22/10/24

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM
![alt text](<ER diagram.png>)
## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
models.py
from django.db import models
from django.contrib import admin
class User(models.Model):
 uname=models.CharField(max_length=100)
 phone=models.IntegerField()
 email=models.EmailField()
 accountnum=models.IntegerField(primary_key=True)
 loan=models.IntegerField()


class UserAdmin(admin.ModelAdmin):
 list_display=('uname','phone','email','accountnum','loan')
 admin.py
 from django.contrib import admin
from.models import User,UserAdmin
admin.site.register(User,UserAdmin)
```
## OUTPUT
![alt text](<Screenshot (2).png>)
Include the screenshot of your admin page.


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
