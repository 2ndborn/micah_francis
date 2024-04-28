# Generated by Django 3.2.25 on 2024-04-26 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About_me',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=500)),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'verbose_name': 'About',
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateTimeField()),
                ('to_date', models.DateTimeField()),
                ('institution', models.CharField(max_length=100)),
                ('qualifation', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest1', models.TextField(max_length=100)),
                ('interest2', models.TextField(max_length=100)),
                ('interest3', models.TextField(max_length=100)),
                ('interest4', models.TextField(blank=True, max_length=100)),
                ('interest5', models.TextField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Work_experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateTimeField()),
                ('to_date', models.DateTimeField(blank=True)),
                ('job_title', models.CharField(max_length=25)),
                ('company', models.CharField(max_length=25)),
                ('location', models.CharField(max_length=25)),
                ('achievement1', models.TextField(max_length=25)),
                ('achievement2', models.TextField(max_length=25)),
                ('achievement3', models.TextField(max_length=25)),
                ('achievement4', models.TextField(max_length=25)),
                ('achievement5', models.TextField(max_length=25)),
            ],
        ),
    ]