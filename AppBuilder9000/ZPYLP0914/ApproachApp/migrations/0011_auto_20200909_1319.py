# Generated by Django 2.2.5 on 2020-09-09 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApproachApp', '0010_auto_20200909_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guidebook',
            name='image',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='images/ApproachApp/'),
        ),
    ]
