# Generated by Django 4.2.9 on 2024-02-08 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0004_alter_propertieslistingmodel_hire_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='propertieslistingmodel',
            name='hire_date',
        ),
    ]