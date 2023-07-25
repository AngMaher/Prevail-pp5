from django.contrib import admin
from .models import Classes


@admin.register(Classes)
class ClassesAdmin(admin.ModelAdmin):

    list_display = ('leader_name', 'class_address', 'class_day', 'class_time')
    list_filter = ('leader_name', 'class_day')
