# Generated by Django 4.1.7 on 2023-04-09 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_destination_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='image',
            field=models.ImageField(null=True, upload_to='static/'),
        ),
    ]