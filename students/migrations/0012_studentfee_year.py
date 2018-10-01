# Generated by Django 2.1 on 2018-08-24 18:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('students', '0011_auto_20180824_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentfee',
            name='year',
            field=models.IntegerField(default='2018', validators=[django.core.validators.MinValueValidator(2017),
                                                                  django.core.validators.MaxValueValidator(2018)]),
        ),
    ]