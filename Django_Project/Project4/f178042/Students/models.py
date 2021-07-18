from django.db import models

# Create your models here.
class Student(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    RegistrationDate = models.DateField()
    image = models.ImageField(upload_to='pics', blank=True, null=True)

