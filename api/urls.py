from django.urls import path
from . import views

urlpatterns = [
    path('stations/', views.station_list, name='station_list'),
    path('stations/create/', views.station_create, name='station_create'),
    path('stations/<str:code>/', views.station_detail, name='station_detail'),
    path('stations/<str:code>/update/', views.station_update, name='station_update'),
    path('stations/<str:code>/delete/', views.station_delete, name='station_delete'),
    path('stations/search/', views.station_search, name='station_search'),
    
    path('gas-types/', views.gas_type_list, name='gas_type_list'),
    path('stations/<str:station_code>/gas-types/', views.gas_types_for_station, name='gas_types_for_station'),
    
    path('station-images/create/', views.station_image_create, name='station_image_create'),
    path('station-images/<str:code>/update/', views.station_image_update, name='station_image_update'),
    path('station-images/<str:code>/delete/', views.station_image_delete, name='station_image_delete'),
    path('stations/<str:station_code>/images/', views.station_images_for_station, name='station_images_for_station'),
]
