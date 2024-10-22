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