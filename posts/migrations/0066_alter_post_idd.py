# Generated by Django 4.0.8 on 2022-12-01 10:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0065_alter_post_idd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='idd',
            field=models.CharField(default=uuid.UUID('1aeea3d0-7165-11ed-8982-bce92f897dea'), max_length=50),
        ),
    ]
