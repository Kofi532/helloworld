# Generated by Django 4.0.8 on 2022-11-28 09:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0024_alter_post_approve_alter_post_idd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='approve',
            field=models.CharField(default='Pending', max_length=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='idd',
            field=models.CharField(default=uuid.UUID('a9cd2bcd-6eff-11ed-bed8-bce92f897dea'), max_length=50),
        ),
    ]
