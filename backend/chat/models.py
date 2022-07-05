from django.db import models
from django.conf import settings

# Create your models here.
class Profile(models.Model):

    GENDER_CHOICE = [
        ("M", "MALE"),
        ("F", "FEMALE"),
        ("O", "OTHERS")
    ]

    # profile_photo = models.ImageField()
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE, default="M")
    country = models.CharField(max_length=127)
    date_birth = models.DateField()
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.email

    def username(self):
        return self.user.username

    def first_name(self):
        return self.user.first_name

    def last_name(self):
        return self.user.last_name

    def email(self):
        return self.user.email
    class Meta:
        ordering = ["user__first_name", "user__last_name"]

class ProfileChatDetails(models.Model):
    profile = models.ManyToManyField(Profile)
    last_time_active_on_chat = models.DateTimeField(auto_now=True)
    chat_name = models.CharField(max_length=255, default="", null=True, blank=True)

class Chat(models.Model):
    profile_chat_details_list = models.ForeignKey(ProfileChatDetails, on_delete=models.CASCADE)

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.TextField()
    time_send = models.DateTimeField(auto_now_add=True)
