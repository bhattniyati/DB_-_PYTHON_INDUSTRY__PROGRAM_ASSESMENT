from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    email= models.EmailField()
    password= models.CharField(max_length=20)
    role= models.CharField(max_length=20)

    def __str__(self):
        return self.email + " | " + self.role
    
class Principle(models.Model):
    userid= models.ForeignKey(User,on_delete=models.CASCADE)
    firstname= models.CharField(max_length=30)
    lastname= models.CharField(max_length=30)
    mobile= models.BigIntegerField()
    picture= models.ImageField(default="default.jpg", upload_to="media/P_Picture")

    def __str__(self):  
        return f"{self.firstname}_{self.lastname}"

class Student(models.Model):
    userid= models.ForeignKey(User,on_delete=models.CASCADE)
    firstname= models.CharField(max_length=30)
    lastname= models.CharField(max_length=30)
    mobile= models.BigIntegerField()
    birth_date=models.DateField()
    date_of_joining=models.DateTimeField(default=timezone.now)
    address=models.TextField()
    roll_no=models.IntegerField()
    fees= models.FloatField()
    picture= models.ImageField(default="default.jpg",upload_to="media/P_Picture")

    def __str__(self):  
        return f"{self.firstname}_{self.lastname}"
    
class Teacher(models.Model):
    userid= models.ForeignKey(User,on_delete=models.CASCADE)
    firstname= models.CharField(max_length=30)
    lastname= models.CharField(max_length=30)
    mobile= models.BigIntegerField()
    birth_date=models.DateField()
    date_of_joining=models.DateTimeField(default=timezone.now)
    address=models.TextField()
    salary= models.FloatField()
    picture= models.ImageField(default="default.jpg",upload_to="media/P_Picture")

    def __str__(self):  
        return f"{self.firstname}_{self.lastname}"