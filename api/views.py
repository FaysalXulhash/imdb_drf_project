from django.shortcuts import render
from .models import StreamPlatform, WatchList
from .serializers import StreamPlatformSerializer, WatchListSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 


class WatchList_api(APIView):
    def get(self, request, format = None):
        lists = WatchList.objects.all()
        serializer = WatchListSerializer(lists, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = WatchListSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WatchList_detail_api(APIView):
    def get(self, request, pk, format=None):
        list = WatchList.objects.get(id=pk)
        serializer = WatchListSerializer(list)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        list = WatchList.objects.get(id=pk)
        serializer = WatchListSerializer(list, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk, format=None):
        list = WatchList.objects.get(id=pk)
        serializer = WatchListSerializer(list, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        list = WatchList.objects.get(id=pk)
        list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)