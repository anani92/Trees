# Generated by Django 2.2.4 on 2022-10-06 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arbortary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tree',
            name='date_planted',
            field=models.DateField(auto_now=True),
        ),
    ]
