# Generated by Django 4.0.8 on 2022-11-28 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('approve', '0005_cals'),
    ]

    operations = [
        migrations.AddField(
            model_name='cals',
            name='eventtime',
            field=models.CharField(default='HH:MM', max_length=10),
        ),
    ]