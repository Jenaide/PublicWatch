from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class MostWanted(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    aliases = models.CharField(max_length=100)
    discription = models.TextField()
    reward = models.TextField()
    remarks = models.TextField()
    caution = models.TextField()
    picture = models.ImageField()
    

    def __str__(self):
        return self.name

class MissingPerson(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    discription = models.TextField()
    last_seen = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
