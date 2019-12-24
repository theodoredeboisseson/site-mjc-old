from django.conf.urls.static import static
from django.views.static import serve
from django.conf import settings
from django.urls import path
from .views import get_news_list, create_news, news_details, edit_news, delete_news


urlpatterns = [
    path('', get_news_list, name='news_list'),
    path('new', create_news, name='create_news'),
    path('<pk>/', news_details, name='news_details'),
    path('<pk>/edit', edit_news, name='edit_news'),
    path('<pk>/delete', delete_news, name='delete_news'),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT})
]
