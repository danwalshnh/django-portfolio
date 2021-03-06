# Generated by Django 3.1 on 2020-08-22 15:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20200822_1020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='technology',
        ),
        migrations.AddField(
            model_name='project',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='project',
            name='organization',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='project',
            name='position',
            field=models.CharField(default='', max_length=100),
        ),
    ]
