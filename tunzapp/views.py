from django.shortcuts import render
from .models import Child
from .serializers import ChildSerializer
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .serializers import ChildSerializer

# Create your views here.


class ChildList(generics.ListCreateAPIView):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer

class ChildDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer


