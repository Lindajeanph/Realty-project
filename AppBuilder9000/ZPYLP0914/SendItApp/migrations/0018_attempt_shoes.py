# Generated by Django 2.2.5 on 2020-09-10 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SendItApp', '0017_auto_20200910_0235'),
    ]

    operations = [
        migrations.AddField(
            model_name='attempt',
            name='shoes',
            field=models.CharField(default='', max_length=40),
        ),
    ]