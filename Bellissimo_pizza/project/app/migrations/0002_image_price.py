# Generated by Django 5.0.4 on 2024-04-18 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='price',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
