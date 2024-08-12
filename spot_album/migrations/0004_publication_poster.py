# Generated by Django 4.2.7 on 2024-08-12 18:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spot_album', '0003_user_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='poster',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
