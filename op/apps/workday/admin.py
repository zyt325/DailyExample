from django.contrib import admin

# Register your models here.
from workday.models import Workday


class WorkdayAdmin(admin.ModelAdmin):
    list_display = ['workday','category']


admin.site.register(Workday, WorkdayAdmin)
