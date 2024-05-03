from django.shortcuts import render
from rest_framework import viewsets, status
from .models import Publication
from .serializers import PublicationSerializer
from rest_framework.permissions import IsAuthenticated

from rest_framework.decorators import api_view
from rest_framework.response import Response




class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer


@api_view(['GET'])
def get_items_post(request, id_post):
    
    publication = Publication.objects.filter(id = id_post)

    publication_s = PublicationSerializer(instance=publication ,many=True)

    return Response(publication_s.data, status=status.HTTP_200_OK)    