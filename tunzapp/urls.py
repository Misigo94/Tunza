from tunzapp import views
from django.urls import path
from .views import *
from . import views 

urlpatterns=[
    path('',views.apiOverview, name='api-overview'),
    path('api/childList/',views.childList, name="child-list"),
    path('api/childDetail/<str:pk>/',views.childDetail, name="child-detail"),
    path('api/childCreate/',views.childCreate, name="child-create"),
    path('api/childUpdate/<str:pk>/',views.childUpdate, name="child-update"),
    path('api/childDelete/<str:pk>/',views.childDelete, name="child-delete"),
]
