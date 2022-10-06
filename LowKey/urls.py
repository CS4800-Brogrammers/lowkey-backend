from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('test/', views.test),
    path('ketan/', views.ketan),
    path('ben/', views.ben),
    path('alfred/', views.alfred),
    path('garrett/', views.garrett),
    path('lam/', views.lam),
    path('bcrypt-test', views.bcrypt_test)
]