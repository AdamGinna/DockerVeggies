# Generated by Django 2.2.7 on 2020-03-06 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('veggies', '0017_main_post_reply_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reply_post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='reply_post',
            name='id_post',
        ),
        migrations.DeleteModel(
            name='Main_Post',
        ),
        migrations.DeleteModel(
            name='Reply_Post',
        ),
    ]