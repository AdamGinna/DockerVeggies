# Generated by Django 2.2.7 on 2020-03-08 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veggies', '0030_reply_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply_post',
            name='title',
            field=models.TextField(blank=True),
        ),
    ]