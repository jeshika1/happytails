# Generated by Django 4.2.6 on 2023-12-09 16:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('happytailsapp', '0014_alter_adoptionapplication_name_alter_process_pet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adoptionapplication',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]