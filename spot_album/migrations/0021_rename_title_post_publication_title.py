# Generated by Django 4.2.7 on 2024-07-27 00:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spot_album', '0020_rename_title_publication_title_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publication',
            old_name='title_post',
            new_name='title',
        ),
    ]
