# Generated by Django 4.1.1 on 2022-09-19 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_new_donor_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('donoremail', models.CharField(max_length=200, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
