# Generated by Django 4.0.8 on 2022-11-28 22:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0051_alter_post_idd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='idd',
            field=models.CharField(default=uuid.UUID('72038d38-6f6d-11ed-a588-bce92f897dea'), max_length=50),
        ),
    ]
