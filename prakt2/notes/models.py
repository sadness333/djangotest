from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    username=models.CharField(max_length=200,unique=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    

    def create_user(self, username, first_name,last_name, email, password):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.set_password(password)
        self.save()


class Notes(models.Model):
    content=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)