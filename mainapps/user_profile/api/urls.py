# urls.py
from django.urls import path
from .views import UserProfileListCreateAPIView, UserProfileRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', UserProfileListCreateAPIView.as_view(), name='profile-list-create'),
    path('<int:pk>/', UserProfileRetrieveUpdateDestroyAPIView.as_view(), name='profile-detail'),
]
