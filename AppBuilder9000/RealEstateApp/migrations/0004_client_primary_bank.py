# Generated by Django 2.2.5 on 2020-09-25 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RealEstateApp', '0003_remove_client_primary_bank'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='primary_bank',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='RealEstateApp.PrimaryBank'),
            preserve_default=False,
        ),
    ]
