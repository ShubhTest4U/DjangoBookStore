from django.contrib import admin

# Register your models here.

from .models import Book, Contact, Orders

admin.site.register(Book)
admin.site.register(Contact)
admin.site.register(Orders)