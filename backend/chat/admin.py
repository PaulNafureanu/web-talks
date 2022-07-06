from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    autocomplete_fields = ["user"]
    list_display = ["username", "first_name", "last_name", "email", "id"]
    list_select_related = ["user"]
    ordering = ["user__first_name", "user__last_name"]
    search_fields = ["email"]

@admin.register(ProfileChatDetails)
class ProfileChatDetailsAdmin(admin.ModelAdmin):
    autocomplete_fields = ["profile"]
    list_display = ["id", "profile", "last_time_active_on_chat", "chat_name"]
    search_fields = ["id"]

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    autocomplete_fields = ["profile_chat_details_list"]
    list_display = ["id"]
    search_fields = ["id"]

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    autocomplete_fields = ["profile", "chat"]
    list_display = ["id", "profile", "chat", "time_send"]
    search_fields = ["id"]