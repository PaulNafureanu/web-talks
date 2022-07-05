from rest_framework import serializers
from .models import *

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ["first_name", "last_name", "email", "username", "password", "phone", "gender", "country", "date_birth"]

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ["chat_name", "persons"]

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ["text", "time_send", "person", "chat"]

class ChatHeaderSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    chat_name = serializers.CharField()
    # persons = serializers.PrimaryKeyRelatedField(queryset = Person.objects.all())