# Generated by Django 4.2.9 on 2024-02-08 21:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0002_propertieslistingmodel_delete_listingmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertieslistingmodel',
            name='hire_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Hire Date'),
            preserve_default=False,
        ),
    ]