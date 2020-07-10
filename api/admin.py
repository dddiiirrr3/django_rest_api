from django.contrib import admin

from .models import Author, Book, Order

# чтобы модели появились в админке
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Order)
