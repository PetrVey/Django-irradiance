# Generated by Django 3.2.6 on 2021-08-06 08:06

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('irradiance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Montsum2020_01',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('y2020_01', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'montsum',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Montsum2020_02',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('y2020_02', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'montsum',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Montsum',
        ),
    ]