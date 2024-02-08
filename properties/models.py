from datetime import datetime
from django.db import models
from realtors.models import (
    AbstractModel,
    RealtorsModel
)


class PropertiesListingModel(AbstractModel):
    realtor = models.ForeignKey(
        RealtorsModel,
        on_delete=models.DO_NOTHING,
        verbose_name="Realtor"
    )

    title = models.CharField(
        max_length=200,
        verbose_name="Title"
    )
    address = models.CharField(
        max_length=200,
        verbose_name="Address"
    )
    city = models.CharField(
        max_length=100,
        verbose_name="City"
    )
    state = models.CharField(
        max_length=100,
        verbose_name="State"
    )
    zipcode = models.CharField(
        max_length=20,
        verbose_name="Zipcode"
    )
    description = models.TextField(
        blank=True,
        verbose_name="Description"
    )
    price = models.IntegerField(
        verbose_name="Price"
    )
    bedrooms = models.IntegerField(
        verbose_name="Bedrooms"
    )
    bathrooms = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        verbose_name="Bathrooms"
    )
    garage = models.IntegerField(
        default=0,
        verbose_name="Garage"
    )
    square_size = models.IntegerField(
        verbose_name="Square Feet"
    )
    lot_size = models.DecimalField(
        max_digits=5,
        decimal_places=1,
        verbose_name="Lot Size"
    )
    images = models.ImageField(
        upload_to='media/',
        blank=True,
        verbose_name="Photos"
    )
    photo_in_one = models.ImageField(
        upload_to='media/',
        blank=True,
        verbose_name="Inside Photos"
    )
    photo_in_two = models.ImageField(
        upload_to='media/',
        blank=True,
        verbose_name="Inside Photos"
    )
    photo_in_three = models.ImageField(
        upload_to='media/',
        blank=True,
        verbose_name="Inside Photos"
    )
    photo_in_four = models.ImageField(
        upload_to='media/',
        blank=True,
        verbose_name="Inside Photos"
    )
    photo_in_five = models.ImageField(
        upload_to='media/',
        blank=True,
        verbose_name="Inside Photos"
    )
    photo_in_six = models.ImageField(
        upload_to='media/',
        blank=True,
        verbose_name="Inside Photos"
    )

    is_published = models.BooleanField(
        default=True,
        verbose_name="Is Published"
    )
    list_date = models.DateTimeField(
        default=datetime.now,
        blank=True,
        verbose_name="List Date"
    )

    def __str__(self):
        return self.title
