
from django.contrib import admin
from django.urls import path, include
from spot_album.views import PublicationViewSet,CommentsViewSet, get_items_post, get_items_post_comments #xxxx nome da pasta app
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'publication',PublicationViewSet)
router.register(r'comments',CommentsViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('publication-details/<int:id_post>/', get_items_post, name='publication-details'),
    path('comments-post/<int:id_comment>/', get_items_post_comments, name='comments-post'),
 ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

