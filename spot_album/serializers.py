from rest_framework import routers, serializers, viewsets
from .models import Album

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('id','nome','ano','tipo','artista','capa')
