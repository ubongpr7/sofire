# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'location-types', LocationTypeViewSet)
router.register(r'event-locations', EventLocationViewSet)
router.register(r'', BellEventViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create-event/', EventCreateAPIView.as_view(), name='create-form'),
]
