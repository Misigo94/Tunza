from tunzapp import views
from django.urls import path
from .views import *

urlpatterns=[
    path('', views.home, name='home'),
    path('login/', views.login_page, name='login'),
    path('register/', views.signup, name='register'),
    path('logout/',  views.logout_user, name='logout'),
    path('about/', views.about, name='about'),
    path('details/', views.details, name='details'),
    path('list/', views.list, name='list'),
]
