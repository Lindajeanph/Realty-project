# Generated by Django 2.2.5 on 2020-09-03 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SendItApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='type',
            field=models.CharField(choices=[('Sport', 'Sport'), ('Trad', 'Trad'), ('Ice', 'Ice'), ('Boulder', 'Boulder'), ('Alpine', 'Alpine')], max_length=40),
        ),
    ]