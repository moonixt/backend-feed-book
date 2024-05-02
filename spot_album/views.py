from django.shortcuts import render
from rest_framework import viewsets
from .models import Album
from .serializers import AlbumSerializer
from rest_framework.permissions import IsAuthenticated




class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
