from django.contrib.auth import authenticate

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from .models import Author, Book, Order
from .serializers import OrderSerializer, UserSerializer


class OrderCreate(generics.CreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer






class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer




class AuthorsView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        #authors = Author.objects.all()
        authors =  [user.last_name + ' ' + user.first_name + ' ' + user.third_name for user in Author.objects.all()]
        authors_id = [user.id for user in Author.objects.all()]
        books = [book.author.id for book in Book.objects.all()]
        books_names = [[book.author.id, book.name] for book in Book.objects.all()]

        response = {"authors": [{'fio': author} for author in authors]}
        count_books = [0 for i in range(len(authors))]

        for i in range(len(response['authors'])):
            response['authors'][i]['books'] = []

        for i in range(len(authors)):
            for k in books_names:
                if k[0] == authors_id[i]:
                    response['authors'][i]['books'].append(k[1])

        for i in range(len(authors_id)):
            count_books[i] = books.count(authors_id[i])


        for i in range(len(response['authors'])):
            response['authors'][i]['books_count'] = count_books[i]


        return Response(
            response
        )


class BooksView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        books = [book.name for book in Book.objects.all()]

        return Response({"books": books})


class LoginView(APIView):
    permission_classes = ()

    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)
