# Generated by Django 4.2.4 on 2023-11-25 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('happytailsapp', '0004_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]