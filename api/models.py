from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    third_name = models.CharField(max_length=50)

    def __str__(self):
        """
        Определим данный метод и такие же методы в других классых для нормального отображения объектов в админке
        """
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
    user = models.CharField(max_length=50)
    user_phone_number = models.CharField(max_length=30)
    comment = models.CharField(max_length=200, blank=True, null=True)
    order_date = models.DateField(auto_now_add=True)
