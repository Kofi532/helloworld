# Generated by Django 4.0.8 on 2022-11-30 22:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0060_alter_post_idd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='idd',
            field=models.CharField(default=uuid.UUID('140059ac-70fd-11ed-a54e-bce92f897dea'), max_length=50),
        ),
    ]