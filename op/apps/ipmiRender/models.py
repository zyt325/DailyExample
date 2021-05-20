from django.db import models

# Create your models here.
class IpmiRender(models.Model):
    ip = models.CharField(max_length=60, blank=True, null=True)
    fqdn = models.CharField(max_length=120, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    intf = models.CharField(max_length=7, blank=True, null=True)
    username = models.CharField(max_length=12, blank=True, null=True)
    password = models.CharField(max_length=12, blank=True, null=True)
    mdate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ipmi_render'
        unique_together = (('ip', 'fqdn'),)
