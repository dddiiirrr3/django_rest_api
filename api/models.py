from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import get_user_model


class Author(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Фамилия')
    last_name = models.CharField(max_length=50)
    third_name = models.CharField(max_length=50)

    def __str__(self):
        full_name = self.first_name + ' ' + self.last_name
        return full_name


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING)
    #user = models.CharField(max_length=50)  auth_token, date_joined, email, first_name, groups, id, is_active,
    # is_staff, is_superuser, last_login, last_name, logentry, order, password, user_permissions, username
    user = models.CharField(max_length=50)
    user_phone_number = models.CharField(max_length=30)
    comment = models.CharField(max_length=200, blank=True, null=True)
    order_date = models.DateField(auto_now_add=True)



