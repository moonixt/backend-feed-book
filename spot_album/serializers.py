from rest_framework import routers, serializers, viewsets
from .models import Publication

class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ('id','artwork','title','subtitle','publication_date','category')
