# Generated by Django 4.0.8 on 2022-11-13 15:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_alter_post_a_approve'),
    ]

    operations = [
        migrations.AddField(
            model_name='post_a',
            name='Comments',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='.', max_length=50),
        ),
        migrations.AddField(
            model_name='post_a',
            name='Date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='post_a',
            name='Approve',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='.', max_length=6),
        ),
    ]
