# Generated by Django 4.0.1 on 2022-02-21 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_appdb_tid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appdb',
            name='intervall',
            field=models.CharField(default='', max_length=75),
        ),
        migrations.AlterField(
            model_name='appdb',
            name='tid_siden_siste',
            field=models.CharField(default='', max_length=75),
        ),
        migrations.AlterField(
            model_name='appdb',
            name='tidspunkt',
            field=models.CharField(default='', max_length=75),
        ),
    ]
