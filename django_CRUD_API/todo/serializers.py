from rest_framework import serializers
from .models import Todo
from django.contrib.auth.models import User


class TodoSerializer(serializers.ModelSerializer):  # create class to serializer model
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Todo
        fields = ('id', 'task', 'genre', 'no', 'owner')


class UserSerializer(serializers.ModelSerializer):  # create class to serializer user model
    todo = serializers.PrimaryKeyRelatedField(many=True, queryset=Todo.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'todo')
