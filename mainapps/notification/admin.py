from django.contrib import admin

from mainapps.common.helpers import register_models
from .models import *
# Register your models here.

register_models([Notification,])
