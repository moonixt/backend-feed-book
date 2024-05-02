from django.shortcuts import render
from rest_framework import viewsets, status
from .models import Album
from .serializers import AlbumSerializer
from rest_framework.permissions import IsAuthenticated

from rest_framework.decorators import api_view
from rest_framework.response import Response




class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


@api_view(['GET'])
def get_items_post(request, id_post):
    
    albums = Album.objects.filter(id = id_post)

    album_s = AlbumSerializer(instance=albums ,many=True)

    return Response(album_s.data, status=status.HTTP_200_OK)    