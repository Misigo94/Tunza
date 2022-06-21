from tunzapp import views
from django.urls import path
from .views import *
from . import views 

urlpatterns=[
    path('api/child-detail/<int:pk>/', views.ChildDetail.as_view()),
    path('api/child-list', views.ChildList.as_view()),
]
