# Generated by Django 3.2.25 on 2024-05-12 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_portfolio_git_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portfolio',
            old_name='git_address',
            new_name='github',
        ),
    ]