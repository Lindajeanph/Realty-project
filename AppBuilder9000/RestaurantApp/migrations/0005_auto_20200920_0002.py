# Generated by Django 2.2.5 on 2020-09-20 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestaurantApp', '0004_auto_20200919_0455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='cuisines',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
