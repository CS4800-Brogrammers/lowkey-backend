from django.urls import include, path

urlpatterns = [
    #list of api endpoints for dj-rest-auth and registration
        #https://dj-rest-auth.readthedocs.io/en/latest/api_endpoints.html
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/register/', include('dj_rest_auth.registration.urls'))
]


'''
/dj-rest-auth/login/ (POST)

        username
        email
        password
    returns JWT access token + refresh token + user details

/dj-rest-auth/logout/ (POST)

/dj-rest-auth/token/verify/ (POST)

        token

/dj-rest-auth/register/ (POST)

        username
        password1
        password2
        email

    returns JWT access token + refresh token + user details
'''