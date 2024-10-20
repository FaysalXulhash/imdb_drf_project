from rest_framework import serializers 
from .models import StreamPlatform, WatchList

class StreamPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamPlatform
        fields = ['id', 'name', 'about', 'website']


class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = ['id', 'title', 'storyline', 'platform', 'active', 'created']