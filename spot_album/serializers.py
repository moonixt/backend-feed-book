from rest_framework import routers, serializers, viewsets
from .models import Publication
from .models import Comments

class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ('id','title','text','artwork','publication_date',)
        
class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('id','comment_text','comments_date','comment_artwork','pub')