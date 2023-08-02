from django.db import models

# Create your models here.
class contactUs(models.Model):
    name = models.TextField(max_length=50, default="non")
    email = models.EmailField(max_length=100, default="non")
    phone = models.IntegerField(max_length=12, default="0")
    textarea = models.TextField(max_length=500, default="non")