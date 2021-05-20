from django.db import models
from django.utils import timezone

# Create your models here.
class Note(models.Model):
    title = models.CharField(default="", unique=True, max_length=50, verbose_name="标题", help_text="标题")
    body = models.TextField(default="", blank=True, null=True, verbose_name="内容", help_text="内容")
    file_name = models.CharField(default="", unique=True, max_length=25, verbose_name="文件名", help_text="文件名")
    create_at = models.DateTimeField(default=timezone.now, verbose_name="创建时间")

    class Meta:
        managed = False  # don't create table
        db_table = 'note'
        app_label = 'note'
