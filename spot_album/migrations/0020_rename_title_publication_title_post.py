# Generated by Django 4.2.7 on 2024-07-27 00:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spot_album', '0019_alter_publication_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publication',
            old_name='title',
            new_name='title_post',
        ),
    ]
