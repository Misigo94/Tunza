from tunzapp import views
from django.urls import path
from .views import *
from . import viewsets 

urlpatterns=[
    path('',viewsets.apiOverview, name='api-overview'),
    path('api/childList/',viewsets.childList, name="child-list"),
    path('api/childDetail/<str:pk>/',viewsets.childDetail, name="child-detail"),
    path('api/childCreate/',viewsets.childCreate, name="child-create"),
    path('api/childUpdate/<str:pk>/',viewsets.childUpdate, name="child-update"),
    path('api/childDelete/<str:pk>/',viewsets.childDelete, name="child-delete"),
]