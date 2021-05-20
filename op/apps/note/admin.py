from django.contrib import admin

# Register your models here.
from note.models import Note

class NoteAdmin(admin.ModelAdmin):
    list_display = ['title','file_name','create_at']


admin.site.register(Note, NoteAdmin)
