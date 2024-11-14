from django.contrib import admin

from api.models import Book, CustomUser

# Register your models here.

admin.site.register(Book)
admin.site.register(CustomUser)