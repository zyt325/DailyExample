from django.contrib import admin


# Register your models here.
# class MultiDBModelAdmin(admin.ModelAdmin):
#     using = 'notes'
#
#     def save_model(self, request, obj, form, change):
#         # Tell Django to save objects to the 'other' database.
#         obj.save(using=self.using)
#
#     def delete_model(self, request, obj):
#         # Tell Django to delete objects from the 'other' database
#         obj.delete(using=self.using)
#
#     def get_queryset(self, request):
#         # Tell Django to look for objects on the 'other' database.
#         return super().get_queryset(request).using(self.using)
#
#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         # Tell Django to populate ForeignKey widgets using a query
#         # on the 'other' database.
#         return super().formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)
#
#     def formfield_for_manytomany(self, db_field, request, **kwargs):
#         # Tell Django to populate ManyToMany widgets using a query
#         # on the 'other' database.
#         return super().formfield_for_manytomany(db_field, request, using=self.using, **kwargs)

class HostAdmin(admin.ModelAdmin):
    list_display = ['name', 'hostname', 'username', 'virtual']
    list_filter = ['virtual']
    search_fields = ['name', 'hostname']
    list_per_page = 20


class BasicInfoAdmin(admin.ModelAdmin):
    list_display = ['type', 'value', 'comment']
    list_filter = ['type']
    list_per_page = 20
    search_fields = ['type', 'value']


class HostMapBasicInfoAdmin(admin.ModelAdmin):
    list_display = ['host', 'basic_info_type','basic_info_value']
    list_filter = ['basic_info__type']
    list_per_page = 20
    search_fields = ['host__hostname','basic_info__type']
    def basic_info_type(self, obj):
        return obj.basic_info.type

    def basic_info_value(self, obj):
        return obj.basic_info.value

class LabelAdmin(admin.ModelAdmin):
    list_display = ['name', 'value']
    list_filter = ['name']
    list_per_page = 20


class HostMapLabelAdmin(admin.ModelAdmin):
    list_display = ('host', 'label_name', 'label_value')
    list_filter = ('label__name',)
    search_fields = ['host__hostname', 'label__value']
    list_per_page = 20

    def label_name(self, obj):
        return obj.label.name

    def label_value(self, obj):
        return obj.label.value


from .models import Host, BasicInfo, HostMapBasicInfo, Label, HostMapLabel

admin.site.register(Host, HostAdmin)
admin.site.register(BasicInfo, BasicInfoAdmin)
admin.site.register(HostMapBasicInfo, HostMapBasicInfoAdmin)
admin.site.register(Label, LabelAdmin)
admin.site.register(HostMapLabel, HostMapLabelAdmin)
