from django.contrib import admin
from .models import Board, Task, Label, Comment, List

@admin.register(Board)
class BoradAdmin(admin.ModelAdmin):
    
    list_display = (
        'owner',
        'title',
        'description',
    )
    search_fields = (
        'title',
    )
    list_filter = (
        'created_at',
    )
    raw_id_fields = (
        'owner',
    )
