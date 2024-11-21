from django.contrib import admin
from .models import *


for model in [UserInterest,OptionType,AnswerType,CustomForm,FormQuestion,Option,ShortAnswer,EssayAnswer,Attachment,File,Reaction,Tag,Comment,Share,Like,PlatformSettings,Subscription,CustomCategory,SocialMediaHandles]:
    admin.site.register(model)