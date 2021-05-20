from django.db import models
from django.utils import timezone
from libs import ModelMixin, human_datetime
from apps.setting.utils import AppSetting
from libs.ssh import SSH

# Create your models here.
table_prefix = 'cmdb_'
app_label = 'cmdb'


class Host(models.Model, ModelMixin):
    class isVirtual(models.TextChoices):
        Yes = 'True', ('Yes')
        No = 'False', ('No')

    name = models.CharField(max_length=50)
    hostname = models.CharField(max_length=50)
    port = models.IntegerField(default=22)
    username = models.CharField(max_length=50, null=True)
    pkey = models.TextField(null=True)
    virtual = models.CharField(max_length=5, choices=isVirtual.choices, default=isVirtual.No)
    desc = models.CharField(max_length=255, null=True)

    created_at = models.CharField(max_length=20, default=human_datetime)
    created_by = models.CharField(max_length=20, null=True)
    deleted_at = models.CharField(max_length=20, null=True)
    deleted_by = models.CharField(max_length=20, null=True)

    @property
    def private_key(self):
        return self.pkey or AppSetting.get('private_key')

    def get_ssh(self, pkey=None):
        pkey = pkey or self.private_key
        return SSH(self.hostname, self.port, self.username, pkey)

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<Host %r>' % self.name

    class Meta:
        app_label = app_label
        db_table = "%shosts" % table_prefix
        ordering = ('-id',)


class BasicInfo(models.Model):
    type = models.CharField(max_length=50, verbose_name="类别")
    value = models.CharField(max_length=120,verbose_name="设备信息", null=True)
    comment = models.CharField(max_length=50, verbose_name="备注", blank=True)

    def __str__(self):
        return "%s|%s" % (self.type, self.value)

    class Meta:
        app_label = app_label
        db_table = "%sbasic_info" % table_prefix
        unique_together = [['type', 'value']]


class HostMapBasicInfo(models.Model):
    host = models.ForeignKey(Host, related_name='map_basicInfo_host',verbose_name="主机", on_delete=models.SET_NULL, blank=True, null=True)
    basic_info = models.ForeignKey(BasicInfo, related_name='map_basicInfo',verbose_name="设备信息", on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return '%s|%s' % (self.host,self.basic_info)

    class Meta:
        app_label = app_label
        db_table = "%shost_map_basicinfo" % table_prefix


class Label(models.Model):
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=100, null=True)
    comment = models.CharField(max_length=200, verbose_name="备注",null=True)

    def __str__(self):
        return self.name + '|' + self.value

    class Meta:
        app_label = app_label
        db_table = "%slabel" % table_prefix
        unique_together = [['name', 'value']]


class HostMapLabel(models.Model):
    host = models.ForeignKey(Host, related_name='map_label_host',verbose_name="主机", on_delete=models.SET_NULL, blank=True, null=True)
    label = models.ForeignKey(Label, related_name='map_label',verbose_name="标签", on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return '%s|%s' %(self.host,self.label)
    class Meta:
        app_label = app_label
        db_table = "%shost_map_label" % table_prefix
