from django.contrib import admin
from .models import RealtorsModel


@admin.register(RealtorsModel)
class RealtorsModelAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'email',
        'description',
        'phone',
        'is_mvp',
        'created_at',
        'updated_at',
        'photo',
        'hire_date'
    ]
    search_fields = [
        'name',
        'email',
        'phone',
        'created_at',
        'hire_date'
    ]
    list_editable = [
        'name',
        'email',
        'description',
        'phone',
        'is_mvp',
        'hire_date'
    ]

    class Meta:
        model = RealtorsModel
