from django.db import models

# Create your models here.
class contactUs(models.Model):
    name = models.TextField(max_length=50, default="non")
    email = models.EmailField(max_length=100, default="non")
    phone = models.BigIntegerField()
    textarea = models.TextField(max_length=500, default="non")


class BookOnline(models.Model):
    name = models.TextField(max_length=50, default="non") 
    email = models.EmailField(max_length=100, default="null")
    phone = models.BigIntegerField()
    city = models.TextField(max_length=50, default="null")
    service_name = models.TextField(max_length=1000, default="null")
    textarea = models.TextField(max_length=500, default="null")  