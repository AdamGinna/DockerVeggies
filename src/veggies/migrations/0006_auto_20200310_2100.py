# Generated by Django 2.2.7 on 2020-03-10 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veggies', '0005_auto_20200310_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_foto',
            field=models.ImageField(null=True, upload_to='images/recipe_fotos', verbose_name='recipe_foto'),
        ),
    ]
