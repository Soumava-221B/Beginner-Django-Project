from django.contrib import admin

from . import models

class NotesAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(models.Note, NotesAdmin)
admin.site.register(models.Like)