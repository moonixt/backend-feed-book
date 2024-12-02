from django.shortcuts import render
from rest_framework import viewsets, status
from .models import Publication
from .serializers import PublicationSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Comments
from .models import User
from .serializers import CommentsSerializer
from .serializers import UserSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import User
from .serializers import FriendsSerializer
from .models import Friends






class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    # permission_classes = (IsAuthenticated,)
    
class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer

class FriendsViewSet(viewsets.ModelViewSet):
    queryset = Friends.objects.all()
    serializer_class = FriendsSerializer
    
################ Usuario personalizado

@classmethod
def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['name'] = user.name  # colocar username dentro do colchetes e após o ponto colocar username
        # ...
        return token
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (IsAuthenticated,)
    
@api_view(['POST'])
def create_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
####################

@api_view(['GET','Post'])
def get_items_post(request, id_post):
    
    publication = Publication.objects.filter(id = id_post)

    publication_s = PublicationSerializer(instance=publication ,many=True)

    return Response(publication_s.data, status=status.HTTP_200_OK)    

@api_view(['GET'])
def get_user(request, id_user):
    
    user = User.objects.filter(id = id_user)

    user_s = UserSerializer(instance=user ,many=True)

    return Response(user_s.data, status=status.HTTP_200_OK)  


@api_view(['GET'])
def get_all_users(request,):
    
    users = User.objects.all() # Usa `all()` para obter todos os usuários

    user_serializer = UserSerializer(users, many=True)  # Passa `users` diretamente

    return Response(user_serializer.data, status=status.HTTP_200_OK)

@api_view(['GET','POST']) #ADICIONADO POST NA LISTA PARA PERMITIR POSTAGENS
def get_items_post_comments(request, id_comment):
    if request.method == 'POST':
        # Valide os dados usando um serializer (se você estiver usando um)
        serializer = CommentsSerializer(data=request.data)
        if serializer.is_valid():
            # Crie uma nova instância do modelo Comments com os dados válidos
            comment_instance = serializer.save()

            # Retorne uma resposta adequada, como um status 201 (criado) ou 200 (OK)
            return Response({"message": "Dados adicionados com sucesso!"}, status=status.HTTP_201_CREATED)
        else:
            # Se os dados não forem válidos, retorne os erros de validação
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        # Lógica para o método GET (se necessário)
        comment = Comments.objects.filter(pub=id_comment)
        comment_s = CommentsSerializer(instance=comment, many=True)
        return Response(comment_s.data, status=status.HTTP_200_OK)