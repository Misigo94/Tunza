from django.shortcuts import render
from .models import Child
from .serializers import ChildSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.

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

@api_view(['GET'])
def childList(request):
    child = Child.objects.all()
    serializer = ChildSerializer(child, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def childDetail(request,pk):
    child = Child.objects.get(id=pk)
    serializer = ChildSerializer(child, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def childCreate(request):
    serializer = ChildSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET','POST'])
def childUpdate(request, pk):
    child = Child.objects.get(id=pk)
    
    serializer = ChildSerializer(instance=child, data=request.data)
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)

@api_view(['DELETE'])
def childDelete(request, pk):
    child = Child.objects.get(id=pk)
    child.delete
    
    return Response('Item Successfully Deleted')
