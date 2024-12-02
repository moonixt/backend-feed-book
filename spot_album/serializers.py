from rest_framework import routers, serializers, viewsets
from .models import Publication
from .models import Comments
from .models import User
from .models import Friends

class PublicationSerializer(serializers.ModelSerializer):
    poster = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    poster_email = serializers.CharField(source='poster.email', read_only=True)  # Para exibição do e-mail

    

    class Meta:
        model = Publication
        fields = ('id','title','text','artwork','publication_date','poster','poster_email')
        
class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('id','comment_text','comments_date','comment_artwork','pub')
        
class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(write_only=False)
    email = serializers.EmailField(write_only=True) #EMAIL SER EXIBIDO PUBLICAMENTE
    password = serializers.CharField(write_only=True)  # Apenas para escrita, não será incluído na resposta

    class Meta:
        model = User
        fields = ('id','profile_pic','name','email','password','bio')
        
    
    def validate_name(self, value):
        """Verifica se o nome já existe e verifica se o nome contém espaços."""
        if ' ' in value:
            raise serializers.ValidationError("O nome não pode conter espaços.")
        if User.objects.filter(name=value).exists():
            raise serializers.ValidationError("Este nome já está em uso.")
        return value
        
        
    def validate_email(self, value):
        """Verifica se o e-mail já está em uso."""
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Este e-mail já está em uso.")
        return value
        
        
        
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            name=validated_data['name'],
        )
        user.set_password(validated_data['password'])  # Criptografa a senha
        user.save()
        return user
    

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('id','comment_text','comments_date','comment_artwork','pub')
        
class FriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friends
        fields = ('user_id','user_id_2')
  
