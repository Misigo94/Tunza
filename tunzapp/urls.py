from tunzapp import views
from django.urls import path
from .views import *

urlpatterns=[
    path('',views.apiOverview, name='api-overview'),
    path('api/childList/',views.postList, name="child-list"),
    path('api/childDetail/<str:pk>/',views.postDetail, name="child-detail"),
    path('api/childCreate/',views.postCreate, name="child-create"),
    path('api/childUpdate/<str:pk>/',views.postUpdate, name="child-update"),
    path('api/childDelete/<str:pk>/',views.postDelete, name="child-delete"),
]