# Generated by Django 4.2.7 on 2024-05-02 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spot_album', '0009_alter_album_capa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='capa',
            field=models.ImageField(blank=True, default='blank.png', upload_to='upload/images'),
        ),
    ]
