# Generated by Django 4.0.8 on 2022-11-28 21:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0037_alter_post_idd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='idd',
            field=models.CharField(default=uuid.UUID('98d093eb-6f62-11ed-b549-bce92f897dea'), max_length=50),
        ),
    ]