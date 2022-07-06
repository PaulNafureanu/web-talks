from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.
class ProfileViewSet(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

# class ChatViewSet(ModelViewSet):
#     queryset = Chat.objects.all()
#     serializer_class = ChatSerializer

# class MessageViewSet(ModelViewSet):
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer

# @api_view()
# def chat_header_list(request):
#     return Response("ok")

# @api_view()
# def chat_header_details(request, id_account):
#     numberOfChats = Person.objects.only("id").get(pk = id_account).chat_set.count() #Returns a specific number like 3
#     chatNames = Person.objects.only("id").get(pk = id_account).chat_set.values("chat_name") #Returns a query set, specifically a list of chat name

    # serializer = ChatHeaderSerializer(chats, many = True)
    # return render(request, "test.html", {"data":list(chats)})
    # return render(request, "test.html", {"chat_no":numberOfChats, "data": list(chatNames)})
    # return Response(serializer.data)
