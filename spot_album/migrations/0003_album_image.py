# Generated by Django 4.2.7 on 2024-05-02 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spot_album', '0002_album_artista'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='image',
            field=models.ImageField(blank=True, default='blank.jpg', upload_to='upload/images'),
        ),
    ]
