# Generated by Django 2.2.5 on 2020-09-09 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApproachApp', '0004_auto_20200909_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guidebook',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
