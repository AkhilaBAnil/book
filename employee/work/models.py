from django.db import models

class Employee(models.Model):
    uname=models.CharField(max_length=30)
    age = models.PositiveIntegerField()
    place=models.CharField(max_length=30)
# Create your models here.

class Emp(models.Model):
    name=models.CharField(max_length=30)
    place=models.CharField(max_length=30)
    salary=models.PositiveIntegerField(null=True)
    contact=models.CharField(max_length=30)

class Book(models.Model):
    title=models.CharField(max_length=30)
    author=models.CharField(max_length=30)
    publication_year=models.CharField(max_length=30)
    genre=models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Person(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(unique=True,null=True)
    course=models.CharField(max_length=50)

class Student(models.Model):
    name=models.CharField(max_length=30)
    age=models.PositiveIntegerField()
    place=models.CharField(max_length=30)
    course=models.CharField(max_length=30)
    gender=models.CharField(max_length=30)