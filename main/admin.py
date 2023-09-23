from django.contrib import admin
from main.models import Vendor, Product, ProductCategory, Customer
# Register your models here.

admin.site.register(Vendor)
admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Customer)
