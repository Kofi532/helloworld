# Generated by Django 4.0.8 on 2022-11-30 22:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0061_alter_post_idd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='idd',
            field=models.CharField(default=uuid.UUID('2436208e-70fe-11ed-95d8-bce92f897dea'), max_length=50),
        ),
    ]
