from rest_framework import generics, permissions,viewsets

from .serializers import *
from mainapps.event.models import BellEvent
from mainapps.common.models import *
from mainapps.common.mixins import *
from mainapps.post.models import GeneralPost

from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404



class GeneralPostCreateView(ContentTypeViewMixinForUser,):
    queryset = GeneralPost.objects.all()
    serializer_class = GeneralPostSerializer

class GeneralPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GeneralPost.objects.all()
    serializer_class = GeneralPostSerializer