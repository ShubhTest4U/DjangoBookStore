from django.contrib import admin

# Register your models here.

from .models import Book, Contact

admin.site.register(Book)
admin.site.register(Contact)