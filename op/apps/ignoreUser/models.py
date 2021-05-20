from django.db import models


# Create your models here.
class SyncIgnoreUsers(models.Model):
    SERVICE_FIELD = models.TextChoices('SERVICE_FIELD', 'shotgun shotgun2 ad zknet_beijing wiki_hr')

    username = models.CharField(max_length=70)
    service = models.CharField(max_length=13,choices=SERVICE_FIELD.choices)
    reason = models.CharField(max_length=255)

    def __str__(self):
        return "%s | %s" % (self.username,self.service)

    class Meta:
        managed = False
        db_table = 'sync_ignore_users'
        unique_together = (('username', 'service'),)
        app_label = 'ignoreUser'

