# Generated by Django 4.0.8 on 2022-11-28 21:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0032_alter_post_idd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='idd',
            field=models.CharField(default=uuid.UUID('a19fcdbb-6f61-11ed-a7e8-bce92f897dea'), max_length=50),
        ),
    ]
