# Generated by Django 4.1.7 on 2023-04-09 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='destination',
            old_name='author',
            new_name='date',
        ),
    ]
