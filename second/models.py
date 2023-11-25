from django.db import models
from django.db import connection

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
class Contact2(models.Model):
    name2 = models.CharField(max_length=122)
    email2 = models.CharField(max_length=122)
    phone2 = models.CharField(max_length=12)
class Meta:
    db_table='first_app_contact2'
class orderinfo(models.Model):
    uname=models.CharField(max_length=122)
    date=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    number=models.CharField(max_length=122)
    Restaurant=models.CharField(max_length=122)
    drinks=models.CharField(max_length=122)
    soups=models.CharField(max_length=122)
    dish=models.CharField(max_length=122)
    take= models.CharField(max_length=15, blank=True, null=True)
    homed= models.CharField(max_length=15, blank=True, null=True)