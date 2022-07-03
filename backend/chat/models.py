from asyncio.windows_events import NULL
from django.db import models

# Create your models here.
class Person(models.Model):

    GENDER_CHOICE = [
        ("M", "MALE"),
        ("F", "FEMALE"),
        ("O", "OTHERS")
    ]

    # profile_photo = models.ImageField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=31)
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE, default="M")
    country = models.CharField(max_length=127)
    date_birth = models.DateField()

class Chat(models.Model):
    chat_name = models.CharField(max_length=255, default=NULL, null=True)
    persons = models.ManyToManyField(Person)

class Message(models.Model):
    text = models.TextField()
    time_send = models.DateTimeField(auto_now_add=True)
    person = models.ForeignKey(Person, on_delete=models.PROTECT)
    chat = models.ForeignKey(Chat, on_delete=models.PROTECT)
