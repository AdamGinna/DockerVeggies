# Generated by Django 2.2.7 on 2020-03-06 13:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('veggies', '0022_auto_20200306_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main_post',
            name='data_stamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]