from django.urls import path 
from .views import WatchList_api, WatchList_detail_api

urlpatterns = [
    path('',WatchList_api.as_view(), name='watchlsit'),
    path('<int:pk>/', WatchList_detail_api.as_view(),),
]
