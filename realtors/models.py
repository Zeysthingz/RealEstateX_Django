from django.db import models


class AbstractModel(models.Model):
    updated_at = models.DateTimeField(
        auto_now=True,
        blank=True,
        verbose_name='Updated',
        help_text='',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        verbose_name='Created',
        help_text='',
    )

    class Meta:
        abstract = True


class RealtorsModel(AbstractModel):
    name = models.CharField(
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
        blank=True,
        verbose_name='Hire Date',
        help_text='',
    )

    def __str__(self):
        return self.name
