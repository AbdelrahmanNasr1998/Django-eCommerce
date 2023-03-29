from django.contrib import admin
from products.models import Category, Product, Product_Images
# Register your models here.

class CategoryAdminConfig(admin.ModelAdmin):
    model = Category
    list_display = ('name',)
    fieldsets = (
        ('Category Information', {'fields': ('name', 'image')}),
    )

class Product_ImagesInline(admin.StackedInline):
    model = Product_Images
    extra = 0

class ProductAdminConfig(admin.ModelAdmin):
    model = Product
    list_display = ('name', 'category', 'price', 'items')
    fieldsets = (
        ('Product Information', {'fields': ('name', 'category', 'description', 'price', 'items')}),
    )
    inlines = [
        Product_ImagesInline,
    ]

class Product_ImagesAdminConfig(admin.ModelAdmin):
    model = Product_Images
    list_display = ('product',)
    fieldsets = (
        ('Product Information', {'fields': ('product', 'image')}),
    )


admin.site.register(Category, CategoryAdminConfig)
admin.site.register(Product, ProductAdminConfig)
admin.site.register(Product_Images, Product_ImagesAdminConfig)