from django.urls import path, include
from .views import *

urlpatterns = [
    path('', apiOverview),
    path('product/', ProductList.as_view()),
    path('product/<int:pk>/', ProductDetail.as_view()),
    path('test/', test),
    path('ketan/', ketan),
    path('ben/', ben, name = 'ben'),
    path('alfred/', alfred),
    path('garrett/', garrett),
    path('lam/', lam),
    path('bcrypt-test/', bcrypt_test),
    path('db-status/', database_status),
    path('register/', RegisterView.as_view()),
    path('login/',LoginView.as_view())
    # path('connect/', ReactView.as_view(), name = "something")
]