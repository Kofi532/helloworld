# Generated by Django 4.0.8 on 2022-11-28 22:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0054_alter_post_idd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='idd',
            field=models.CharField(default=uuid.UUID('61511d1b-6f6e-11ed-951f-bce92f897dea'), max_length=50),
        ),
    ]
