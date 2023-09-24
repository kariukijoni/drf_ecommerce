from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# vendors models

# vendor


class Vendor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField(null=True)

    def __str__(self):
        return self.user.username

# category


class ProductCategory(models.Model):
    title = models.CharField(max_length=200)
    detail = models.TextField(null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Product Categories'

# product


class Product(models.Model):
    category = models.ForeignKey(
        ProductCategory, on_delete=models.SET_NULL, null=True, related_name='category_product')
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    detail = models.TextField(null=True)
    price = models.FloatField()

    def __str__(self):
        return self.title

# customer


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile = models.PositiveIntegerField()

    def __str__(self):
        return self.user.username

# ordermodel


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name='customer_orders')
    order_time = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.customer

    def __unicode__(self):
        return '%s' % (self.order_time)


# orderitems


class OrderItems(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name_plural = 'Order Items'
