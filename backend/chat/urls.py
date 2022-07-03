from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register("persons", PersonViewSet)
router.register("chats", ChatViewSet)
router.register("messages", MessageViewSet)

urlpatterns = router.urls