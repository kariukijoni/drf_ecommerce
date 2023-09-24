from django.urls import path
from . import views
# from rest_framework import generics

urlpatterns = [
    path('vendors/', views.VendorList.as_view()),
    path('vendors/<int:pk>', views.VendorDetail.as_view()),
    path('products/', views.ProductList.as_view()),
    path('products/<int:pk>', views.ProductDetail.as_view()),
    # customers
    path('customers/', views.CustomerList.as_view()),
    path('customers/<int:pk>', views.CustomerDetail.as_view()),
    # orders
    path('orders/', views.OrderList.as_view()),
    path('orders/<int:pk>', views.OrderDetail.as_view()),

]
