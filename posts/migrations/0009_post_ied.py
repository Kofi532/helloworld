# Generated by Django 4.0.8 on 2022-11-15 18:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_alter_post_a_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Ied',
            field=models.CharField(default=uuid.UUID('84cf9980-6511-11ed-b373-bce92f897dea'), max_length=25),
        ),
    ]
