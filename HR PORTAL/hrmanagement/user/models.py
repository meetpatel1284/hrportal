from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    age = models.PositiveIntegerField(null=True,blank=True)
    salary = models.FloatField(null=True,blank=True)
    dateofbirth = models.DateField(null=True,blank=True)
    is_hr = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)

    class Meta:
        db_table = "user" 
