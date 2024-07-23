# Generated by Django 4.2.7 on 2024-07-21 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spot_album', '0013_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='pub',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='spot_album.publication'),
            preserve_default=False,
        ),
    ]