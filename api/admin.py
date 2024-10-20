from django.contrib import admin

# Register your models here.
from .models import StreamPlatform, WatchList

@admin.register(WatchList)
class WatchiListAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'platform', 'active']


@admin.register(StreamPlatform)
class StreamPlatformAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'website']
    

    
