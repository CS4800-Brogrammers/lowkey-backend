from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.apiOverview),
    path('shops/<int:shop_id>/product/', views.ShopProductList.as_view()),
    path('shops/<int:shop_id>/product/<int:product_id>/', views.ShopProductDetail.as_view()),
    path('user/shops/', views.ShopUser.as_view()),
    path("product/", views.ProductList.as_view()),
    path("product/<int:product_id>/", views.ProductDetail.as_view()),
    path('shops/', views.ShopList.as_view()),
    path('shops/<int:pk>/',views.ShopDetail.as_view()),
    path('test/', views.test),
    path('ketan/', views.ketan),
    path('ben/', views.ben, name = 'ben'),
    path('alfred/', views.alfred),
    path('garrett/', views.garrett),
    path('lam/', views.lam),
    path('bcrypt-test/', views.bcrypt_test),
    path('db-status/', views.database_status)
    # path('connect/', ReactView.as_view(), name = "something")
]