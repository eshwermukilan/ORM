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
    