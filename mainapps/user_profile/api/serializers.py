# serializers.py
from rest_framework import serializers
from mainapps.user_profile.models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
