# Generated by Django 4.1.1 on 2022-09-19 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_delete_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='all_logins',
            fields=[
                ('donoremail', models.CharField(max_length=200, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]