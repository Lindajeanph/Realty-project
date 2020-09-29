# Generated by Django 2.2.5 on 2020-09-19 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestaurantApp', '0002_auto_20200910_1030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='city',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='cuisine',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='delivery',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='outdoor_seating',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='price',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='state_province',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='take_out',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='zip_code',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='avgfortwo',
            field=models.IntegerField(blank=True, null=True, verbose_name='Average for two'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='cuisines',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='establishment',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Type'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='highlights',
            field=models.TextField(blank=True, max_length=500, verbose_name="Highlights, ie 'Delivery', 'Casual Attire', or 'Vegan Options'"),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='hours',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='img',
            field=models.URLField(blank=True, null=True, verbose_name='Image link'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='latitude',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='Latitude'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='longitude',
            field=models.FloatField(blank=True, max_length=10, null=True, verbose_name='Longitude'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='menu',
            field=models.URLField(blank=True, null=True, verbose_name='Link to menu'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='Phone number(s)'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='pricerange',
            field=models.IntegerField(blank=True, null=True, verbose_name='Price range'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='rating_text',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='Described as'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='url',
            field=models.URLField(blank=True, null=True, verbose_name='Link to Zomato page'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='votes',
            field=models.IntegerField(blank=True, null=True, verbose_name='Number of votes'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='zomatoID',
            field=models.IntegerField(blank=True, null=True, verbose_name='Zomato ID'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='name',
            field=models.CharField(default='', max_length=255, verbose_name='Restaurant Name'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='Community rating'),
        ),
    ]
