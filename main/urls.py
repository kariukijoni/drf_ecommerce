from django.urls import path
from . import views
# from rest_framework import generics

urlpatterns = [
    path('vendors/',views.VendorList.as_view()),
    path('vendors/<int:pk>',views.VendorDetail.as_view()),
]
