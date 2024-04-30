from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import GenericAPIView
from .models import *
from .serializers import *
from rest_framework import viewsets

# Create your views here.

# class VendorListCreateView(generics.ListCreateAPIView):
#     queryset = Vendor.objects.all()
#     serializer_class = VendorSerializer
    
# class VendorRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Vendor.objects.all()
#     serializer_class = VendorSerializer
    
# class PurchaseListCreateView(generics.ListCreateAPIView):
#     queryset = Purchase.objects.all()
#     serializer_class = PurchaseSerializer
    
# class PurchaseRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Purchase.objects.all()
#     serializer_class = PurchaseSerializer

class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
