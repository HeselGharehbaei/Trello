from django.contrib import admin
from .models import Board, Task, Label, Comment, List


class ListInline(admin.TabularInline):
    model = List


class CommentInline(admin.TabularInline):
    model = Comment


class TaskInline(admin.TabularInline):
    model = Task


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
    inlines = [
        ListInline,
    ]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'deadline',
        'start_date',
        'finished_date',
        'time_spent',
        'order',
    )
    search_fields = (
        'title',
    )
    list_filter = (
        'created_at',
    )
    inlines = [
        CommentInline,
    ]


@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'color',
    )
    search_fields = (
        'title',
    )
    list_filter = (
        'created_at',
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'text',
    )
    list_filter = (
        'created_at',
    )


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'order',
    )
    search_fields = (
        'title',
    )
    list_filter = (
        'created_at',
    )
    inlines = [
        TaskInline,
    ]
