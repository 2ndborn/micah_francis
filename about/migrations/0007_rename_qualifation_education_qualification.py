# Generated by Django 3.2.25 on 2024-04-27 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0006_auto_20240427_1222'),
    ]

    operations = [
        migrations.RenameField(
            model_name='education',
            old_name='qualifation',
            new_name='qualification',
        ),
    ]
