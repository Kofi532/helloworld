# Generated by Django 4.0.8 on 2022-12-01 11:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0069_alter_post_idd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='idd',
            field=models.CharField(default=uuid.UUID('7b61aaa7-7167-11ed-9d8e-bce92f897dea'), max_length=50),
        ),
    ]
