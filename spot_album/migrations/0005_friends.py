# Generated by Django 5.0.4 on 2024-08-12 23:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spot_album', '0004_publication_poster'),
    ]

    operations = [
        migrations.CreateModel(
            name='friends',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_id_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_f', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
