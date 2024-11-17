from django.db import models

# Create your models here.
class Student(models.Model):
    fullname = models.CharField(max_length=200)
    username=models.CharField(max_length=200)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    age = models.IntegerField()
    yob = models.DateField()

    def __str__(self):
        return self.fullname

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=50)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

# Create a model named Patient. The values saved are
# firstname,lastname,dateofbirth,gender,email,phonenumber,address.
# Save at least 5 patient records
class Patient(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    dateofbirth = models.DateField()
    gender = models.CharField(max_length=50)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=50)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.firstname
class Appointment(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.DateTimeField()
    department = models.CharField(max_length=200)
    doctor = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name

