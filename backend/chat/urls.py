from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register("profiles", ProfileViewSet)
# router.register("chats", ChatViewSet)
# router.register("messages", MessageViewSet)

urlpatterns = [
    path("", include(router.urls)),
    # path("chat-header", chat_header_list),
    # path("chat-header/<int:id_account>", chat_header_details)
    # path("specific-messages")
]