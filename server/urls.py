"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.test),
    path('ketan/', views.ketan),
    path('ben/', views.ben),
    path('alfred/', views.alfred),
    path('garrett/', views.garrett),
    path('lam/', views.lam),
    path('bcrypt-test', views.bcrypt_test),
    path('db-status', views.database_status),
    path('', include('LowKey.urls'))
]
