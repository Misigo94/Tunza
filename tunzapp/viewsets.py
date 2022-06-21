from rest_framework import viewsets
from . import models
from . import serializers
from .models import Child
from .serializers import ChildSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


class ChildViewset(viewsets.ModelViewSet):
    queryset = models.Child.objects.all()
    serializer_class = serializers.ChildSerializer
 
 
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/child-list/',
        'Detail View': '/child-detail/<str:pk>/',
        'Create': '/child-create/',
        'Update': '/childt-update/<str:pk>/',
        'Delete': '/child-delete/<str:pk>/',
    }
    return Response(api_urls)
