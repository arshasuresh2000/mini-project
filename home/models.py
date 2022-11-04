from distutils.command.upload import upload
import email
from email.policy import default
from django.db import models
from django.core.validators import RegexValidator


# Create your models here.




class new_donor(models.Model):
    donorname = models.CharField(max_length=200)
    donoremail = models.CharField(max_length=200, unique=True)
    donorphone = models.CharField(max_length=200)
    donorplace = models.CharField(max_length=200)
    password = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Donor Details"


class volunteer(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique=True)
    phone = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    password = models.CharField(max_length=100)


class all_logins(models.Model):
    email = models.CharField(max_length=200, unique=True, primary_key=True)
    password = models.CharField(max_length=100)



class District(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name




class Orphanage(models.Model):
    name = models.CharField(max_length=124)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
    city = models.CharField(max_length=250)
    pin= models.CharField(max_length=12, blank=True)
    image = models.ImageField(upload_to='pics')
    phone = models.CharField(max_length=12, blank=True)
    email=models.EmailField()
    no_of_persons=models.IntegerField()
    

class donationtype(models.Model):
    name = models.CharField(max_length=200,unique=True)
    description = models.TextField(max_length=200,blank=True)
    def __str__(self):
        return self.name

class userdonate(models.Model):
    user=models.ForeignKey(all_logins,on_delete=models.CASCADE)    
    item=models.ForeignKey(donationtype,on_delete=models.CASCADE,default=5)   
    firstname= models.CharField(max_length=250)
    lastname=models.CharField(max_length=250)
    email=models.EmailField(max_length=250)
    phone=models.CharField(max_length=12, blank=True)
    district=models.ForeignKey(District,on_delete=models.CASCADE,default=1) 
    city= models.CharField(max_length=250)
    hname= models.CharField(max_length=250,default=0)
    pin= models.CharField(max_length=250)
    


class Donorprofile(models.Model):
    user=models.ForeignKey(all_logins,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200,null=True)
    hname = models.CharField(max_length=200)
    district=models.ForeignKey(District,on_delete=models.CASCADE,default=1) 
    city=models.CharField(max_length=200)
    zipcode = models.IntegerField()
    

    # def __str__(self):
    #     return self.name