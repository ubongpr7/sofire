from django.contrib import admin

from mainapps.common.helpers import register_models
from .models import Post,PostComment,PostLike,Reaction
# Register your models here.
register_models([Post,PostLike,PostComment,Reaction])