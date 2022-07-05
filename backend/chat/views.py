from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.
class PersonViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class ChatViewSet(ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

@api_view()
def chat_header_list(request):
    # chats = Chat.objects.all()
    # # serializer = ChatSerializer(chats)
    # serializer = ChatHeaderSerializer(chats)
    return Response("ok")

@api_view()
def chat_header_details(request, id_account):
    # chats = Chat.objects.values("id", "chat_name")
    # serializer = ChatHeaderSerializer(chats)
    # # serializer = ChatSerializer(chats)
    return Response("ok")
