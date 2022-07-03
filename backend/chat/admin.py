from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ["username", "first_name", "last_name", "email", "id"]
    search_fields = ["email"]

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    autocomplete_fields = ["persons"]
    list_display = ["id", "chat_name"]
    search_fields = ["id"]

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    autocomplete_fields = ["person", "chat"]
    list_display = ["id", "person", "chat", "time_send"]
    search_fields = ["id"]