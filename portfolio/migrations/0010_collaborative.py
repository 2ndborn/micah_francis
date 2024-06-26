# Generated by Django 3.2.25 on 2024-05-30 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_portfolio_image_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collaborative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('description', models.TextField(max_length=500)),
                ('technologies', models.TextField(max_length=250)),
                ('web_address', models.URLField(max_length=500)),
                ('github', models.URLField(max_length=500, null=True)),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('image_description', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
