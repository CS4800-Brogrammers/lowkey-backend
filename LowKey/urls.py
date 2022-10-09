from django.urls import path, include
from django.conf.urls import url
from . import views
from views import *

urlpatterns = [
    path('', views.home),
    path('test/', views.test),
    path('ketan/', views.ketan),
    path('ben/', views.ben),
    path('alfred/', views.alfred),
    path('garrett/', views.garrett),
    path('lam/', views.lam),
    path('bcrypt-test', views.bcrypt_test),
    # path('connect/', ReactView.as_view(), name = "something")
]