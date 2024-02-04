# Generated by Django 4.2.6 on 2023-12-09 16:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('happytailsapp', '0013_process_pet_process_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adoptionapplication',
            name='name',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='process',
            name='pet',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='happytailsapp.adoptionapplication'),
        ),
    ]
