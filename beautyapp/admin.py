from django.contrib import admin
from beautyapp.models import Product,Cart,Order


# Register your models here.
# admin.site.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['id','name','price','pdetails','is_active']
    list_filter=['cat','is_active']
    ordering = ['id'] 


# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name',)

# class SubcategoryAdmin(admin.ModelAdmin):
#     list_display = ('name', 'category')
admin.site.register(Product,ProductAdmin)
admin.site.register(Cart)
admin.site.register(Order)
# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Subcategory, SubcategoryAdmin)