# Generated by Django 4.1.1 on 2022-09-19 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_donationtype_orphan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_donor',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]
