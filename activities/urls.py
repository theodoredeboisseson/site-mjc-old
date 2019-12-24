from django.conf.urls.static import static
from django.views.static import serve
from django.conf import settings
from django.urls import path
from .views import get_list_of_animation_types, research, get_list_of_animations, \
                   get_animation_details, register_to_animation_slot


urlpatterns = [
    path('list-of-animation-types', get_list_of_animation_types, name="a_list_of_animations_types"),
    path('research', research, name="a_research"),
    path('<animation_type>', get_list_of_animations, name="a_list_of_animations"),
    path('<animation_type>/<animation>/<animation_id>', get_animation_details, name="a_animation_details"),
    path('<animation_type>/<animation>/<animation_id>/<slot_id>/registration', register_to_animation_slot,
         name="a_animation_slot_registration"),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
    # path('<event_type>/<event_subtype>/<event_id>/registration', register_to_event, name='register_to_event'),
]