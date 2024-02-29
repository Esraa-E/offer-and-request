from django.db import models

# Create your models here.
class offer(models.Model):
    images = models.ImageField(upload_to='images/', blank=True, null=True)
    username = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    rent_start_time = models.DateField() 
    rent_finish_time = models.DateField()
    price = models.FloatField()
    
    favorit=models.BooleanField(default=False)
    location=models.TextField(default='Beni-Seuf')
    discount=models.FloatField(default=0.0)
    level=models.IntegerField(default=0)
    bedrooms=models.IntegerField(default=0)
    bathrooms=models.IntegerField(default=0)
    area=models.FloatField(default=0.0)
    description=models.CharField(max_length=50,default='null')
    conditions=models.TextField (default='null')
    ava=models.CharField(max_length=100,default='null')
    rev=models.BooleanField(default=False)
    furnished=models.BooleanField(default=False)
    viewer=models.FloatField(default=0.0)
    video=models.FileField(upload_to='vedios_house',default='null',null=True)

    def __str__(self):
        return self.username
    

class AddOffer(models.Model):
    price = models.FloatField()
    rent_start_time = models.DateField() 
    rent_finish_time = models.DateField()


class request(models.Model):
    username = models.CharField(max_length=255)
    images = models.ImageField(upload_to='imageee/', blank=True, null=True)
    date=models.DateField()
    text=models.TextField()



class comment(models.Model):
     username = models.CharField(max_length=255)
     images = models.ImageField(upload_to='imagggeee/', blank=True, null=True)
     date=models.DateField()
     text=models.TextField()