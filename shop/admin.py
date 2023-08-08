from django.contrib import admin
from shop.models import Product

# Register your models here.
admin.site.register(Product)
class product(admin.ModelAdmin):
    list_display =['id', 'title', 'discount_price', 'category','product_image']