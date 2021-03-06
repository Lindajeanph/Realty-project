# Generated by Django 2.2.5 on 2020-09-22 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestaurantApp', '0005_auto_20200920_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='user_comments',
            field=models.TextField(blank=True, default='', max_length=500),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='user_rating',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='MyRating'),
        ),
    ]
