# Generated by Django 5.0.4 on 2024-04-18 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_pizza_delete_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='price',
            field=models.DecimalField(decimal_places=1, max_digits=10),
        ),
    ]
