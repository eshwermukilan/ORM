# Ex02 Django ORM Web Application
## Date: 09.04.2025
## Name: Eshwer M
## Reg No: 212224040086
## AIM
To develop a Django application to store and retrieve data from Movies Database using Object Relational Mapping(ORM).

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
admin.py

from django.contrib import admin
from .models import Movies,MoviesAdmin
admin.site.register(Movies,MoviesAdmin)

models.py

from django.db import models
from django.contrib import admin
class Movies(models.Model):
    Movie_id=models.CharField(max_length=20,help_text="Like 'm101.m102..'")
    Title=models.CharField(max_length=100)
    Release_year=models.IntegerField()
    Genre=models.CharField(max_length=30)
    Rating=models.FloatField(help_text="From '0.0' to '5.0'")

class MoviesAdmin(admin.ModelAdmin):
    list_display=('Movie_id','Title','Release_year','Genre','Rating')
    
```


## OUTPUT

![alt text](<Movies Database.png>)

## RESULT
Thus the program for creating a database using ORM hass been executed successfully
