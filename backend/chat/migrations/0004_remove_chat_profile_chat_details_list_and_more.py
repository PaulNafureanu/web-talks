# Generated by Django 4.0.6 on 2022-07-06 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_remove_profilechatdetails_profile_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='profile_chat_details_list',
        ),
        migrations.AddField(
            model_name='chat',
            name='profile_chat_details_list',
            field=models.ManyToManyField(to='chat.profilechatdetails'),
        ),
    ]
