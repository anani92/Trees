# Generated by Django 2.2.4 on 2022-10-06 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arbortary', '0003_auto_20221006_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tree',
            name='date_planted',
            field=models.DateField(),
        ),
    ]