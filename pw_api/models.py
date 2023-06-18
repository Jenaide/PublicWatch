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
    SEX_CHOICES = (
        ('M', 'male'),
        ('F', 'Female'),
        ('O', 'other')
    )
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    sex = models.CharField(max_length=10, choices=SEX_CHOICES, default='Male')
    aliases = models.CharField(max_length=100)
    discription = models.TextField()
    reward = models.TextField()
    remarks = models.TextField()
    caution = models.TextField()
    picture = models.ImageField(upload_to='wanted_persons/', default='')
    

    def __str__(self):
        return self.name + '_' + self.surname

class MissingPerson(models.Model):
    SEX_CHOICES = (
        ('M', 'male'),
        ('F', 'Female'),
        ('O', 'other')
    )
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.CharField(max_length=10, choices=SEX_CHOICES, default='Male')
    discription = models.TextField()
    last_seen = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to='missing_persons/', default='')

    def __str__(self):
        return self.name + '_' + self.surname
