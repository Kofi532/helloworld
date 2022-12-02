# Generated by Django 4.0.8 on 2022-12-01 10:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clubm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='Paste here', max_length=10)),
                ('surname', models.CharField(default='Type here', max_length=20)),
                ('firstname', models.CharField(default='Type here', max_length=25)),
                ('level', models.TextField(default='Type here', max_length=10)),
                ('title', models.CharField(default='Type here', max_length=25)),
                ('message', models.TextField(default='Type here', max_length=50)),
                ('image', models.ImageField(default='Please upload image', upload_to='')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('approve', models.CharField(default='Pending', max_length=10)),
                ('act', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(default='..', max_length=25)),
                ('firstname', models.CharField(default='..', max_length=25)),
                ('email', models.EmailField(default='..', max_length=254)),
                ('message', models.TextField(default='..', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sportm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='Paste here', max_length=10)),
                ('surname', models.CharField(default='Type here', max_length=10)),
                ('firstname', models.CharField(default='Type here', max_length=25)),
                ('level', models.TextField(default='Type here', max_length=10)),
                ('title', models.CharField(default='Type here', max_length=25)),
                ('message', models.TextField(default='Type here', max_length=50)),
                ('image', models.ImageField(default='Please upload image', upload_to='')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('approve', models.CharField(default='Pending', max_length=10)),
                ('act', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=10)),
            ],
        ),
    ]