# Generated by Django 3.2.25 on 2024-04-29 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('description', models.TextField(max_length=500)),
                ('technologies', models.TextField(max_length=250)),
                ('web_address', models.TextField(max_length=500)),
            ],
        ),
    ]