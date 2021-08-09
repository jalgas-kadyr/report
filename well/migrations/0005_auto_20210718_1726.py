# Generated by Django 3.2.5 on 2021-07-18 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('well', '0004_consumptions'),
    ]

    operations = [
        migrations.AddField(
            model_name='well',
            name='begin_date',
            field=models.DateField(default='2021-07-18'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='well',
            name='planned_end',
            field=models.DateField(default='2021-07-18'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='well',
            name='preparation_begin',
            field=models.DateField(default='2021-07-18'),
            preserve_default=False,
        ),
    ]
