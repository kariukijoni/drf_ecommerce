from django.shortcuts import render
from main.serializers import (VendorSerializer, VendorDetailSerializer,
                              ProductSerializer, ProductDetailSerializer,
                              CustomerSerializer, CustomerDetailSerializer,
                              OrderSerializer, OrderDetailSerializer,
                              CustomerAddressSerializer)
from main.models import Vendor, Product, Customer, Order, OrderItems, CustomerAddress
from rest_framework import generics, permissions, viewsets
# Create your views here.


class VendorList(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    # permission_classes=[permissions.IsAuthenticated]


class VendorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    # permission_classes=[permissions.IsAuthenticated]


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerDetailSerializer


class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # permission_classes=[permissions.IsAuthenticated]


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    # queryset = OrderItems.objects.all()
    serializer_class = OrderDetailSerializer

    def get_queryset(self):
        order_id = self.kwargs['pk']
        order = Order.objects.get(id=order_id)
        order_items = OrderItems.objects.filter(order=order)

        return order_items


class CustomerAddressViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerAddressSerializer
    queryset = CustomerAddress.objects.all()
