from django.contrib import admin

# Register your models here.
from ipmiRender.models import IpmiRender
class IpmiRenderAdmin(admin.ModelAdmin):
    list_display = ['ip','fqdn','status','intf']
    list_filter = ['status']


admin.site.register(IpmiRender, IpmiRenderAdmin)
