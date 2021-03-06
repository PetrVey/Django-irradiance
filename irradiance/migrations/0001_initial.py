# Generated by Django 3.2.6 on 2021-08-06 07:48

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Montsum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('y2020_01', models.FloatField(blank=True, null=True)),
                ('y2020_02', models.FloatField(blank=True, null=True)),
                ('y2020_03', models.FloatField(blank=True, null=True)),
                ('y2020_04', models.FloatField(blank=True, null=True)),
                ('y2020_05', models.FloatField(blank=True, null=True)),
                ('y2020_06', models.FloatField(blank=True, null=True)),
                ('y2020_07', models.FloatField(blank=True, null=True)),
                ('y2020_08', models.FloatField(blank=True, null=True)),
                ('y2020_09', models.FloatField(blank=True, null=True)),
                ('y2020_10', models.FloatField(blank=True, null=True)),
                ('y2020_11', models.FloatField(blank=True, null=True)),
                ('y2020_12', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'montsum',
                'managed': False,
            },
        ),
    ]
