from django.db import models


class RealtorsModel(models.Model):
    name= models.CharField(
        max_length=200,
        verbose_name="Name"
    )
    photo = models.ImageField(
        upload_to='media/',
        verbose_name="Photo"
    )
    description = models.TextField(
        blank=True,
        verbose_name="Description"
    )
    email = models.EmailField(
        verbose_name="Email"
    )
    phone = models.CharField(
        max_length=20,
        verbose_name="Phone"
    )
    is_mvp = models.BooleanField(
        default=False,
        verbose_name="Is MVP"
    )
    hire_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Hire Date"
    )

    def __str__(self):
        return self.name

