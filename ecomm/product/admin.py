from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Category)


class ProductimageAdmin(admin.StackedInline):
    list_display=['product_name','price',]
    model=product_images


class ProductAdmin(admin.ModelAdmin):
    inlines =[ProductimageAdmin]



@admin.register(ColorVariant)
class ColorVarientAdmin(admin.ModelAdmin):
    list_display=['color_varient','price']
    model=ColorVariant 


@admin.register(SizeVarient)
class SizevarientAdmin(admin.ModelAdmin):
    list_display=['size_variant','price']
    model=SizeVarient




admin.site.register(product_images)
admin.site.register(Product,ProductAdmin)