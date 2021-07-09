from django.contrib import admin

# Register your models here.
from product.models import Category, SubCategory, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug",)


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug",)


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "price")


admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Product, ProductAdmin)
