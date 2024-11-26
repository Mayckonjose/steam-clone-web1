# Generated by Django 4.2.4 on 2023-08-21 12:15

from django.db import migrations, models
import games.models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0009_games_img_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='reviews',
            field=models.JSONField(blank=True, default=games.models.defaultDict, null=True, verbose_name='reviews'),
        ),
    ]
