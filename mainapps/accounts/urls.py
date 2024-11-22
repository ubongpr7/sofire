from django.urls import path
from .views import login_view,AccountTokenObtainPairView,AccountTokenRefreshView,AccountTokenVerify,LogoutAPI
app_name='accounts'
urlpatterns=[
    path('', login_view, name='login'),
    path('token/refresh/', AccountTokenRefreshView.as_view(),name='refresh_token'),
    path('token/verify/', AccountTokenVerify.as_view(),name='verify_token'),
    path('token/create/', AccountTokenObtainPairView.as_view(),name='create_token'),
    path('token/logout/', LogoutAPI.as_view(),name='logout_token'),
]