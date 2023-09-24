from rest_framework import serializers
from .models import Vendor, Product, Customer, Order, OrderItems


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['id', 'user', 'address']
        # depth = 1


class VendorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['id', 'user', 'address']
        # depth = 1

        # def __init__(self,*args, **kwargs):
        #     super(VendorDetailSerializer,self).__init__(*args, **kwargs)
        #     request=self.context.get('request')
        #     self.Meta.depth=1


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'category', 'vendor', 'title', 'detail', 'price']
        # depth = 1


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'category', 'vendor', 'title', 'detail', 'price']
        # depth = 1


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'user', 'mobile']
        # depth = 1


class CustomerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'user', 'address']
        # depth = 1


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'customer']
        depth = 1


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItems
        fields = ['id', 'order', 'product']
        depth = 1
