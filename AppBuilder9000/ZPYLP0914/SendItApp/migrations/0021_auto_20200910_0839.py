# Generated by Django 2.2.5 on 2020-09-10 14:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SendItApp', '0020_auto_20200910_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attempt',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='attempt',
            name='light',
            field=models.CharField(blank=True, choices=[('Shade', 'Shade'), ('Sun', 'Sun'), ('Night', 'Night')], default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='attempt',
            name='status',
            field=models.CharField(blank=True, choices=[('Onsight', 'Onsight'), ('Redpoint', 'Redpoint'), ('Pinkpoint', 'Pinkpoint'), ('To Do', 'To Do'), ('Flash', 'Flash'), ('Flail', 'Flail'), ('Sent', 'Sent')], default='', max_length=40),
        ),
    ]
