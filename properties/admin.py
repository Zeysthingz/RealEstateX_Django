from django.contrib import admin
from .models import PropertiesListingModel


@admin.register(PropertiesListingModel)
class PropertiesModelAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'realtor',
        'title',
        'address',
        'city',
        'state',
        'zipcode',
        'price',
        'bedrooms',
        'bathrooms',
        'description',
        'garage',
        'square_size',
        'lot_size',
        'images',
        'is_published',
        'created_at',
        'list_date',

    ]
    search_fields = [
        'title',
        'city',
        'price',
        'bedrooms',
        'bathrooms',
        'garage',
        'is_published',
        'created_at',
        'list_date',

    ]
    list_editable = [
        'title',
        'address',
        'city',
        'state',
        'zipcode',
        'price',
        'bedrooms',
        'bathrooms',
        'description',
        'garage',
        'square_size',
        'lot_size',
        'images',
        'is_published',
        'list_date',

    ]

    class Meta:
        model = PropertiesListingModel
