from django.http.response import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from django.templatetags.static import static
from .models import Montsum2020_01, Montsum2020_01
import numpy as np
import folium
import folium.plugins as plugins
from matplotlib import cm as colormaps
from .utils import  print_rows, cmap_nan

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'base.html'

def montsum2020_01_dataset(request):
    head = ('ncols 145 \nnrows 195 \nxllcorner 119.3899917602535\nyllcorner 21.8099994659424 \ndx 0.019862102641 \ndy 0.019897441374 \nNODATA_value  0\n')
    january = Montsum2020_01.objects.all().values('Irradiance', 'id').order_by('id')
    matrix = np.zeros((195,145))
    iy = 0
    ix = 0
    counter = 0
    for data in january:
        value = float(data['Irradiance'])
        counter = counter + 1
        matrix [iy, ix] = value
        ix = ix + 1
        if ix == 145:
            ix = 0
            if iy == 195:
                iy = iy
            else:
               iy = iy + 1
    test2 = head +   print_rows(matrix)
    return HttpResponse(test2, content_type="asc")

def base_map(request):
    january = Montsum2020_01.objects.all().values('Irradiance', 'id').order_by('id')
    matrix = np.zeros((195,145))
    iy = 0
    ix = 0
    counter = 0
    for data in january:
        value = float(data['Irradiance'])
        counter = counter + 1
        matrix [iy, ix] = value
        ix = ix + 1
        if ix == 145:
            ix = 0
            if iy == 195:
                iy = iy
            else:
               iy = iy + 1

    #corners for raster layer
    maxlat = 25.700000762939453
    maxlon = 122.27999877929688
    minlat = 21.81999969482422
    minlon = 119.39999389648438

    #normalize data to fit max on color bar  
    norm_data = matrix/150000

    #Custom colorbar base on turbo, low value are placed as transparent
    turbo = cmap_nan(colormaps.turbo)

    #Folium map 
    m = folium.Map(width = 700, height= 700, location=[23.6, 120.839], zoom_start=7.5)
    #Folium raster 
    folium.raster_layers.ImageOverlay(norm_data,
                                    [[minlat, minlon], [maxlat, maxlon]], opacity = 0.8,
                                    colormap = turbo,
                                    zindex=0).add_to(m)

    #adding pop-up with lat + lon
    #m.add_child(folium.LatLngPopup())
    
    #adding colorbar to folium view
    cm_png = static('img/color_bar.png')
    cmbar_img = plugins.FloatImage(cm_png, bottom=11, left=1)
    m.add_child(cmbar_img)
    #folium.LayerControl().add_to(m)

    m = m._repr_html_()
    context = {'map': m,}
    return render(request, 'main.html', context)