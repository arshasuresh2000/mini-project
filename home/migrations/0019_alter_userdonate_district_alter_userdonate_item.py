# Generated by Django 4.1.1 on 2022-10-28 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_userdonate_hname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdonate',
            name='district',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='home.district'),
        ),
        migrations.AlterField(
            model_name='userdonate',
            name='item',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='home.donationtype'),
        ),
    ]
