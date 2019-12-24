from django.conf.urls.static import static
from django.views.static import serve
from django.conf import settings
from django.urls import path
from .views import get_list_of_all_socials, get_social_details


urlpatterns = [
    path('list-of-all-events', get_list_of_all_socials, name='list-of-all-socials'),
    path('<social_id>', get_social_details, name='social_details'),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT})
]
