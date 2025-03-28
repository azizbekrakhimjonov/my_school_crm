from django.contrib import admin
from .models import Category, Subject

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'lesson', 'category', 'file', 'created_at')
    list_filter = ('category',)