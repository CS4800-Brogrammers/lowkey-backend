from django.urls import include, path

urlpatterns = [
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    #path('auth/register/', include('rest_auth.registration.urls'))
]
