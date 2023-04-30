from django.db import models

# Create your models here.

class Company(models.Model):
    stringId = models.TextField(max_length=100)
    company = models.TextField(max_length=100)
    postedBy = models.TextField(max_length=100)
    postTime = models.DateTimeField()
    deadLine = models.DateField()
    package = models.TextField(max_length=29)
    info = models.TextField(max_length=500)
    link = models.URLField(max_length=1000)
    image = models.ImageField(upload_to='images/')


class Internships(models.Model):
    stringId = models.TextField(max_length=100)
    company = models.TextField(max_length=100)
    postedBy = models.TextField(max_length=100)
    postTime = models.DateTimeField()
    deadLine = models.DateField()
    package = models.TextField(max_length=29)
    info = models.TextField(max_length=500)
    link = models.URLField(max_length=1000)
    image = models.ImageField(upload_to='images/')


class Eligibilities(models.Model):
    stringId = models.TextField(max_length=100)
    no = models.IntegerField()
    heading = models.TextField(max_length=500)
    info = models.TextField(max_length=10000)


class Database(models.Model):
    stringId = models.TextField(max_length=100)
    no = models.IntegerField()
    heading = models.TextField(max_length=500)
    info = models.TextField(max_length=10000)

class Contest(models.Model):
    stringId = models.TextField(max_length=100)
    name = models.TextField(max_length=100)
    startDateTime = models.DateTimeField()
    EndDateTime = models.DateTimeField()
    link = models.URLField()

class ContestDatabase(models.Model):
    stringId = models.TextField(max_length=100)
    no = models.IntegerField()
    language = models.CharField(max_length=100)
    solution = models.ImageField(upload_to='solutions/')


class User(models.Model):
    username = models.CharField(max_length=300)
    email = models.CharField(max_length=100)
    year = models.CharField(max_length=30)
    password = models.CharField(max_length=100)

