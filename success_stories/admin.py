from django.contrib import admin
from .models import Success_Stories


@admin.register(Success_Stories)
class Success_StoriesAdmin(admin.ModelAdmin):

    list_display = (
        'class_attended',
        'title',
        'weight_loss',
        'start_weight',
        'weight_now',
        'image_before',
        'image_after',
        'name',
    )
