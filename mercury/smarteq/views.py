from django.shortcuts import render
from rest_framework import generics
from .models import EmploymentAuthorization, Address, Employee
from .serializers import EmploymentAuthorizationSerializer, AddressSerializer, EmployeeSerializer


class AddressView(generics.RetrieveAPIView):
    queryset = Address
    serialzer_class = AddressSerializer


class EmployeeAuthorizationView(generics.RetrieveAPIView):
    queryset = EmploymentAuthorization.objects.all()
    serializer_class = EmploymentAuthorizationSerializer


class EmployeeView(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
