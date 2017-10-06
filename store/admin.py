from django.contrib import admin

from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'stock') ##what is displayed on the django backend view

admin.site.register(Book, BookAdmin)
