# Generated by Django 4.2.7 on 2023-12-07 13:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('happytailsapp', '0012_process'),
    ]

    operations = [
        migrations.AddField(
            model_name='process',
            name='pet',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='happytailsapp.animal'),
        ),
        migrations.AddField(
            model_name='process',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]