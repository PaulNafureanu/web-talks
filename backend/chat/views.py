from rest_framework.viewsets import ModelViewSet
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