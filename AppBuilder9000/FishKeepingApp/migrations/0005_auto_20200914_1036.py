# Generated by Django 2.2.5 on 2020-09-14 17:36

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('FishKeepingApp', '0004_auto_20200912_1422'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='fishkeepinguser',
            managers=[
                ('Accounts', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='fishwishlist',
            managers=[
                ('Fish', django.db.models.manager.Manager()),
            ],
        ),
    ]
