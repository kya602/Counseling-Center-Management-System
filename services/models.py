from django.db import models

class Service(models.Model):
    service_name = models.CharField(max_length=250)
    specification = models.CharField(max_length=100,null=True,blank=True)
