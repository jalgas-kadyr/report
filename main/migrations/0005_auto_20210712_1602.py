# Generated by Django 3.2.5 on 2021-07-12 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_dispatcher_supervisor_well'),
    ]

    operations = [
        migrations.AddField(
            model_name='dispatcher',
            name='name',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dispatcher',
            name='surname',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='master',
            name='name',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='master',
            name='surname',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='supervisor',
            name='name',
            field=models.CharField(default='sdsd', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='supervisor',
            name='surname',
            field=models.CharField(default='sd', max_length=30),
            preserve_default=False,
        ),
    ]
