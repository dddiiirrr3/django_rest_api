from django.core.mail import mail_admins
from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import Order


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('book', 'user', 'user_phone_number', 'comment')

    def create(self, validated_data):
        order = Order(
            book=validated_data['book'],
            user=validated_data['user'],
            user_phone_number=validated_data['user_phone_number'],
            comment=validated_data['comment'],
        )
        order.save()
        mail_admins('ha', 'hahaha')
        return order



