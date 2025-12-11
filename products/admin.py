from django.contrib import admin
from .models import Category, ColorVariant, SizeVariant, Product, ProductImage

admin.site.register(Category)

class ProductImageAdmin(admin.StackedInline):
    model = ProductImage

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'category']   # FIXED: product_name → title
    inlines = [ProductImageAdmin]

@admin.register(ColorVariant)
class ColorVariantAdmin(admin.ModelAdmin):
    list_display = ['color_name', 'price']

@admin.register(SizeVariant)
class SizeVariantAdmin(admin.ModelAdmin):
    list_display = ['size_name', 'price']

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
