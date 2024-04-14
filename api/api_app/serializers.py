from rest_framework import serializers
from .models import Data, Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"

class DataSerializer(serializers.ModelSerializer):
    todos = TodoSerializer(many=True, read_only=True)
    class Meta:
        model = Data
        fields = "__all__"

        