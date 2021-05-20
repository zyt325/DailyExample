from django.db import models


# Create your models here.
class Workday(models.Model):
    CATEGORY_FIELD=models.TextChoices('CATEGORY_FIELD','render workstation')
    workday = models.DateField(blank=True, null=True)
    category = models.CharField(max_length=11, choices=CATEGORY_FIELD.choices,blank=True, null=True)

    def __str__(self):
        return "%s | %s" % (self.workday,self.category)

    class Meta:
        managed = False
        db_table = 'workday'
        unique_together = (('workday', 'category'),)
        app_label = 'workday'
