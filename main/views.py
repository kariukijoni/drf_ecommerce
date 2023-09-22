from django.shortcuts import render
from main.serializers import VendorSerializer
from main.models import Vendor
from rest_framework import generics
# Create your views here.

class VendorList(generics.ListAPIView):
    queryset=Vendor.objects.all()
    serializer_class=VendorSerializer

