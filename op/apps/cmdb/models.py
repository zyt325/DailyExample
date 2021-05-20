from django.db import models
from libs.utils import human_datetime

# Create your models here.

class Host(models.Model):
    class isVirtual(models.TextChoices):
        Yes = 'True', ('Yes')
        No = 'False', ('No')

    name = models.CharField(max_length=50)
    hostname = models.CharField(max_length=50)
    port = models.IntegerField(default=22)
    virtual = models.CharField(max_length=5, choices=isVirtual.choices, default=isVirtual.No)
    desc = models.CharField(max_length=255, null=True)

    created_at = models.CharField(max_length=20, default=human_datetime)
    created_by = models.CharField(max_length=20, null=True)
    deleted_at = models.CharField(max_length=20, default=human_datetime)
    deleted_by = models.CharField(max_length=20, null=True)

class Nic(models.Model):
    name = models.CharField(max_length=50)
    mac = models.CharField(max_length=20)
    ip = models.GenericIPAddressField()
    host_id = models.IntegerField()

