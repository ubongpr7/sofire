from django.contrib import admin
from django.urls import path,include
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.views.decorators.csrf import csrf_exempt

schema_view = get_schema_view(
   openapi.Info(
      title="Sofire API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
   path('admin/', admin.site.urls),
   path('account/',include('mainapps.accounts.urls',namespace='accounts'),),
   path('acccount-api/',include('mainapps.accounts.api.urls'),),
   
   path('group/',include('mainapps.bell_group.api.urls'),),
   path('',include('mainapps.common.api.urls'),),
   path('event/',include('mainapps.event.api.urls'),),
   path('notification/',include('mainapps.notification.api.urls'),),
   path('post/',include('mainapps.post.api.urls'),),
   path('user_profile/',include('mainapps.user_profile.api.urls'),),

    # third party
   path('auth-api/', include('djoser.urls')),
   # path('auth-token/', include('djoser.urls.jwt')),
   path('social_auth/', include('djoser.social.urls')),
   path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   # path('ses/event-webhook/', SESEventWebhookView.as_view(), name='handle-event-webhook'),

]
