from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('mainapps.accounts.urls',namespace='accounts'),),
    path('auth/',include('mainapps.accounts.api.urls'),),
]
