from django.contrib import admin
from .models import Product, Category
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'rating',
        'image',
    )
    summernote_fields = ['description']
    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name'
    )


admin.site.register(Category, CategoryAdmin)
