from django.db import models

# Create your models here.
# your_app/models.py
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    department = models.CharField(max_length=100)
    joining_date = models.DateField(null=True, blank=True)