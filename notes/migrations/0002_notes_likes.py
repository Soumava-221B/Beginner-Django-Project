# Generated by Django 5.1.7 on 2025-03-23 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='likes',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
