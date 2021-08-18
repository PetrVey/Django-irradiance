from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Montsum2020_01
#from .models import Incidences


# Register your models here.
class Montsum2020_01Admin(LeafletGeoAdmin):
    list_display = ('geom', 'id', 'Irradiance', 'Year', 'Month')

admin.site.register(Montsum2020_01, Montsum2020_01Admin)