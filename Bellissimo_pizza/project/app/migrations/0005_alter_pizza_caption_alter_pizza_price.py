# Generated by Django 5.0.4 on 2024-04-18 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_pizza_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='caption',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='price',
            field=models.BigIntegerField(),
        ),
    ]