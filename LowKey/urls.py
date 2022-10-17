from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.apiOverview),
    path('product/', views.ProductList.as_view()),
    path('product/<int:pk>/', views.ProductDetail.as_view()),
    path('test/', views.test),
    path('ketan/', views.ketan),
    path('ben/', views.ben),
    path('alfred/', views.alfred),
    path('garrett/', views.garrett),
    path('lam/', views.lam),
    path('bcrypt-test/', views.bcrypt_test),
    path('db-status/', views.database_status)
    # path('connect/', ReactView.as_view(), name = "something")
]