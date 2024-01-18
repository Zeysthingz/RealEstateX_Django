from django.urls import path
from .views import (
    list_all_properties,
    property_detail,
    search_properties,
)

urlpatterns = [
    path('', list_all_properties, name='list_all_properties'),
    path('<int:property_id>', property_detail, name='property_detail'),
    path('search/', search_properties, name='search_properties'),

]
