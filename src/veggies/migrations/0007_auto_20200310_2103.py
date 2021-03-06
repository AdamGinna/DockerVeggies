# Generated by Django 2.2.7 on 2020-03-10 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veggies', '0006_auto_20200310_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main_post',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='images/main_posts', verbose_name='foto'),
        ),
        migrations.AlterField(
            model_name='reply_post',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='images/post_replies', verbose_name='foto'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='images/restaurants', verbose_name='foto'),
        ),
    ]
