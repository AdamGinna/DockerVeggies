# Generated by Django 2.2.7 on 2020-02-27 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('veggies', '0007_auto_20200227_1310'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='rating_recipe',
            unique_together={('id_user', 'id_recipe')},
        ),
    ]
