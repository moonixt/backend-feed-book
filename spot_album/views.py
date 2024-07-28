from django.shortcuts import render
from rest_framework import viewsets, status
from .models import Publication
from .serializers import PublicationSerializer
from rest_framework.permissions import IsAuthenticated

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Comments
from .serializers import CommentsSerializer




class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    
class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer



@api_view(['GET'])
def get_items_post(request, id_post):
    
    publication = Publication.objects.filter(id = id_post)

    publication_s = PublicationSerializer(instance=publication ,many=True)

    return Response(publication_s.data, status=status.HTTP_200_OK)    

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