# serializers.py
from rest_framework import serializers
from mainapps.event.models import LocationType, EventLocation, BellEvent

class LocationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationType
        fields = '__all__'

class EventLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventLocation
        fields = '__all__'

class BellEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = BellEvent
        fields = '__all__'

class BellEventCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BellEvent
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at','user']
