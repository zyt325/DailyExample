from django.contrib import admin

# Register your models here.
from ignoreUser.models import SyncIgnoreUsers


class SyncIgnoreUsersAdmin(admin.ModelAdmin):
    list_display = ['username','service','reason']
    list_filter = ['service']


admin.site.register(SyncIgnoreUsers, SyncIgnoreUsersAdmin)
