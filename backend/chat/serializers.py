from rest_framework import serializers
from .models import *

class ProfileSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()
    class Meta:
        model = Profile
        fields = ["id", "user_id", "phone", "gender", "country", "date_birth"]

# class ChatSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Chat
#         fields = ["chat_name", "persons"]

# class MessageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Message
#         fields = ["text", "time_send", "person", "chat"]

# class ChatHeaderSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     chat_name = serializers.CharField()
    # persons = serializers.PrimaryKeyRelatedField(queryset = Person.objects.all())