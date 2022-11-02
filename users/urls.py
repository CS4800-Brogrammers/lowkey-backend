from django.urls import include, path

urlpatterns = [
    #list of api endpoints for dj-rest-auth and registration
        #https://dj-rest-auth.readthedocs.io/en/latest/api_endpoints.html
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/register/', include('dj_rest_auth.registration.urls'))
]
