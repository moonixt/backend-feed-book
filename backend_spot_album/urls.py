
from django.contrib import admin
from django.urls import path, include
from spot_album.views import PublicationViewSet,CommentsViewSet,UserViewSet,FriendsViewSet, get_items_post, get_items_post_comments, create_user, get_user #xxxx nome da pasta app
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
## Autenticação JWT
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
##
router = routers.DefaultRouter()
router.register(r'publication',PublicationViewSet)
router.register(r'comments',CommentsViewSet)
router.register(r'users',UserViewSet)
router.register(r'friends',FriendsViewSet)




urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(),name='token_refresh'),
    path('publication-details/<int:id_post>/', get_items_post, name='publication-details'),
    path('comments-post/<int:id_comment>/', get_items_post_comments, name='comments-post'),
    path('profile/<int:id_user>/', get_user, name='profile'),
    path('create_user/', create_user, name='create_user'),

 ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

