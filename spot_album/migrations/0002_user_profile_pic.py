# Generated by Django 4.2.7 on 2024-08-11 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spot_album', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, default='nuser.png', null=True, upload_to='upload/profile'),
        ),
    ]
