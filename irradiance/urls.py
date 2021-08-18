from django.urls import path
from .views import HomePageView, montsum2020_01_dataset, base_map

app_name = 'irradiance'

urlpatterns = [
    path('',  HomePageView.as_view(), name="home"),
    path('montsum2020_01/',  montsum2020_01_dataset, name="montsum2020_01"),
    path('base_map/',  base_map, name="base_map"),
]