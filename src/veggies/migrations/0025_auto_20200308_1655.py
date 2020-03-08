# Generated by Django 2.2.7 on 2020-03-08 16:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('veggies', '0024_auto_20200306_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient_list',
            name='id_recipes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='veggies.Recipe'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='id_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]