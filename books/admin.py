from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'genre', 'available_copies', 'total_copies']
    list_filter=['genre', 'author']
    search_fields=['title', 'author', 'isbn']

    
