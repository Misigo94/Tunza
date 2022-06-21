from tunzapp import views
from django.urls import path
from .views import *

urlpatterns=[
    path('', views.home, name='home'),
    path('login/', views.login_page, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/',  views.logout_user, name='logout'),
]
