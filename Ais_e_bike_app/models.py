from django.db import models


class Register_form(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    mobile = models.BigIntegerField()
    age = models.IntegerField()
    passewrd = models.CharField( max_length=16)
    passewrd1 = models.CharField(max_length=16)


class Provider_register(models.Model):
    name = models.CharField(max_length=50)
    email=models.EmailField(max_length=30)
    Username=models.FileField(max_length=30)
    phone_number =models.BigIntegerField()
    password= models.CharField(max_length=18)
    passwordR = models.CharField(max_length=18)
    date_of_birth =models.DateField()
    gender =models.CharField(max_length=10)
    vekele_number = models.CharField(max_length=20)
    image = models.ImageField()

    
    
    
class cntact_us(models.Model):
    emai_id=models.EmailField(max_length=30)
    messages = models.CharField(max_length=200)
    
    
    
class Addvaickal(models.Model):
    
    Vai_name  = models.CharField(max_length=50)
    RC = models.FileField()
    cost = models.IntegerField()
    vai_number = models.CharField(max_length=50)
    cost_per_hr = models.IntegerField()
    image = models.ImageField()
    
class vaik_taking_user(models.Model):
    name = models.CharField(max_length=50)
    Phone_valid = models.BigIntegerField()
    licence = models.FileField()
    taker_img =  models.ImageField()
    time_to_take_days =  models.IntegerField()
    time_in_hr = models.IntegerField()
    
    
    
    
    
    