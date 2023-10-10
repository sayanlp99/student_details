from django.db import models

class Student(models.Model):
    GENDER_CHOICES = [
        ("M","Male"),
        ("F","Female")
    ]
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=10)
    address = models.TextField(max_length=100)
    gender = models.CharField(choices=GENDER_CHOICES,max_length=1)
    dob = models.DateField()
    department = models.ManyToManyField('Department')

class Department(models.Model):
    department = models.CharField(max_length=30)

    def __str__(self):
        return self.department