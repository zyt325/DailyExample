from django.db import models

# Create your models here.
app_label = 'bfx'
class SyncIgnoreUsers(models.Model):
    username = models.CharField(max_length=70)
    service = models.CharField(max_length=13)
    reason = models.CharField(max_length=255)

    class Meta:
        app_label = app_label
        managed = True
        db_table = 'sync_ignore_users'
        unique_together = (('username', 'service'),)
