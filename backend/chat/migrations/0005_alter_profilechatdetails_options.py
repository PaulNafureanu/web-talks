# Generated by Django 4.0.6 on 2022-07-06 03:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_remove_chat_profile_chat_details_list_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profilechatdetails',
            options={'verbose_name_plural': 'Profile Chat Details'},
        ),
    ]
