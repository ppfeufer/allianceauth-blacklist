from django.contrib import admin

from .models import EveNote


@admin.register(EveNote)
class EveNoteAdmin(admin.ModelAdmin):
    search_fields = ['eve_name', ]
    list_display = ('eve_name', 'blacklisted','restricted', 'added_by')