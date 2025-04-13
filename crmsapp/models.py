from django.db import models

# Create your models here.
class Administrator(models.Model):
    adminuname = models.CharField(max_length =50)
    adminpwd = models.CharField(max_length =50)
    def __str__(self):
        return self.adminuname


class caruser(models.Model):
    username = models.CharField(max_length =50)
    password = models.CharField(max_length =50)
    fname = models.CharField(max_length =100)
    useremail = models.CharField(max_length =100)
    mobno = models.CharField(max_length =10)
    def __str__(self):
        return self.username
    

class car(models.Model):
    username = models.CharField(max_length =50)
    regno = models.CharField(max_length =50)
    model = models.CharField(max_length =100)
    year = models.IntegerField()
    km = models.CharField(max_length =10)
    noacc = models.IntegerField()
    opos = models.IntegerField()
    mileage = models.IntegerField()
    noseat = models.IntegerField()
    enginetype = models.CharField(max_length =30)
    expprice = models.CharField(max_length =10)
    transmission = models.CharField(max_length =30)
    status = models.IntegerField()

    def __str__(self):
        return self.username
