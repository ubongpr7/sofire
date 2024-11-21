from django.contrib import admin
from .models import *
from mainapps.common.helpers import register_models

# Register your models here.



register_models([GroupAnnouncements,GroupSettings,GroupRule,SofireGroup,SofireGroupPermission])
