# Generated by Django 4.2.9 on 2024-02-08 20:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='realtorsmodel',
            name='hire_date',
        ),
        migrations.AddField(
            model_name='realtorsmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='realtorsmodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated'),
        ),
    ]
