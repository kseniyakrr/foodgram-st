from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    birth_date = models.DateField(blank = True),
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.username
    
    