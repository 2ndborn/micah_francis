# Generated by Django 3.2.25 on 2024-04-27 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0005_auto_20240427_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='from_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='education',
            name='to_date',
            field=models.DateField(),
        ),
    ]