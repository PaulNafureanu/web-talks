from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["username", "first_name", "last_name", "email", "id"]
    list_select_related = ["user"]
    ordering = ["user__first_name", "user__last_name"]
    search_fields = ["email"]

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    # autocomplete_fields = ["persons"]
    list_select_related = ["profile_chat_details_list"]
    list_display = ["id"]
    search_fields = ["id"]

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    # autocomplete_fields = ["person", "chat"]
    list_display = ["id", "profile", "chat", "time_send"]
    search_fields = ["id"]