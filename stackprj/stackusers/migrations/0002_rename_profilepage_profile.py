# Generated by Django 4.2.1 on 2023-05-22 17:50

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stackusers', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProfilePage',
            new_name='Profile',
        ),
    ]
