# Generated by Django 4.2.6 on 2023-12-11 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('happytailsapp', '0015_alter_adoptionapplication_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='adoptionapplication',
            name='adopted_animal',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='happytailsapp.animal'),
        ),
    ]