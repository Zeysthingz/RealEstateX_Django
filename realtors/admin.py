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
    ]
    search_fields = [
        'name',
        'email',
        'phone',
        'created_at',
    ]
    list_editable = [
        'name',
        'email',
        'description',
        'phone',
        'is_mvp',
    ]

    class Meta:
        model = RealtorsModel
