from django.urls import path, include

from .views import AuthorsView, BooksView, UserCreate, OrderCreate


urlpatterns = [
    path('authors/', AuthorsView.as_view()),
    path('books/', BooksView.as_view()),
    path("register/", UserCreate.as_view(), name="user_create"),
    path('api-auth/', include('rest_framework.urls')),
    path('order/', OrderCreate.as_view(), name="order_create"),
]
