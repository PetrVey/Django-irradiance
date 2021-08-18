from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager

class Montsum2020_01(models.Model):
    # GeoDjango-specific: a geometry field (MultiPolygonField)
    geom = models.PointField()
    #table columns
    Irradiance = models.FloatField(blank=True, db_column='y2020_01')
    id = models.FloatField(blank=True, db_column='id', primary_key=True)
    Year = '2020'
    Month = 'January'
    class Meta:
        managed = False
        db_table = 'montsum'



class Montsum2020_02(models.Model):
    # GeoDjango-specific: a geometry field (MultiPolygonField)
    geom = models.PointField()
    #table columns
    Irradiance = models.FloatField(blank=True, db_column='y2020_02')
    id = models.FloatField(blank=True, db_column='id', primary_key=True)
    Year = '2020'
    Month = 'February'
    class Meta:
        managed = False
        db_table = 'montsum'


