# Generated by Django 3.2.25 on 2024-05-04 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0011_auto_20240430_2025'),
    ]

    operations = [
        migrations.RenameField(
            model_name='achievement',
            old_name='achievement',
            new_name='text',
        ),
    ]
