# Generated by Django 2.2.5 on 2020-07-15 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PupApp', '0008_auto_20200714_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='owner_phone',
            field=models.IntegerField(max_length=25, verbose_name='Phone Number'),
        ),
    ]
