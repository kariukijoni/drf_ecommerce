from django.shortcuts import render
from main.serializers import VendorSerializer,VendorDetailSerializer
from main.models import Vendor
from rest_framework import generics,permissions
# Create your views here.

class VendorList(generics.ListCreateAPIView):
    queryset=Vendor.objects.all()
    serializer_class=VendorSerializer
    # permission_classes=[permissions.IsAuthenticated]

class VendorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Vendor.objects.all()
    serializer_class=VendorSerializer