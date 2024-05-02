
from django.contrib import admin
from django.urls import path, include
from spot_album.views import AlbumViewSet, get_items_post #xxxx nome da pasta app
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'albums',AlbumViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('albums-post/<int:id_post>/', get_items_post, name='albums-post'),
 ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

