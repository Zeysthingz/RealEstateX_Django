# Generated by Django 4.2.9 on 2024-02-08 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0003_propertieslistingmodel_hire_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertieslistingmodel',
            name='hire_date',
            field=models.DateTimeField(blank=True, verbose_name='Hire Date'),
        ),
    ]
