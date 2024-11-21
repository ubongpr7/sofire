from django.contrib import admin
from .models import *


for model in [UserInterest,Attachment,File,Tag,Share,PlatformSettings,Subscription,CustomCategory,SocialMediaHandles]:
    admin.site.register(model)