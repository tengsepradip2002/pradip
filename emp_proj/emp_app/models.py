from django.db import models

class Departments(models.Model):
    name=models.CharField(max_length=100,null=False)
    location=models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Role(models.Model):
    name=models.CharField(max_length=100,null=False)
    def __str__(self):
        return self.name

from django.core.validators import RegexValidator

# Create your models here.
class Employee(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    dept=models.ForeignKey(Departments,on_delete=models.CASCADE)
    role=models.ForeignKey(Role,on_delete=models.CASCADE)
    location=models.CharField(max_length=100)
    salary=models.IntegerField(default=0)


    phone = models.CharField(
        max_length=10,
        validators=[RegexValidator(r'^\d{10}$', 'Phone number must be exactly 10 digits')],
        default='0000000000'
    )


def __str__(self):
        return "%s %s %s %s" % (self.first_name, self.last_name, self.dept, self.role)


