# Generated by Django 3.2.5 on 2021-07-06 17:00

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to=users.models.media_path_organizer, verbose_name='Profile Picture'),
        ),
    ]