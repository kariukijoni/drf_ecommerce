from rest_framework import serializers
from .models import Vendor, Product


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['id', 'user', 'address']
        depth = 1


class VendorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['id', 'user', 'address']
        depth = 1

        # def __init__(self,*args, **kwargs):
        #     super(VendorDetailSerializer,self).__init__(*args, **kwargs)
        #     request=self.context.get('request')
        #     self.Meta.depth=1


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'category', 'vendor', 'title', 'detail', 'price']
        depth = 1


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'category', 'vendor', 'title', 'detail', 'price']
        depth = 1
