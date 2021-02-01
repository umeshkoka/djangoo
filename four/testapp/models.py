from django.db import models
from django.core import validators
class student(models.Model):
    name=models.CharField(max_length=15)
    age=models.IntegerField()
    email=models.EmailField()
    dob=models.DateField()
    gender=models.CharField(max_length=2)
    feedback=models.TextField(validators=[validators.MaxLengthValidator(40),validators.MinLengthValidator(10)])
