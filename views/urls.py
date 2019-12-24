from django.conf.urls.static import static
from django.views.static import serve
from django.conf import settings
from django.urls import path
from .views import get_home_page, get_about_page, get_info_page, get_calendar_activities_page, \
                   get_youth_mauguio_page, get_youth_carnon_page, get_venue, get_venues_list, \
                   get_host, get_admin_panel, get_rate_and_registration_activities_page, \
                   get_rate_and_registration_workshop_page, edit_activity, edit_workshop


urlpatterns = [
    path('', get_home_page, name='home'),
    path('about', get_about_page, name='about'),
    path('info', get_info_page, name='info'),
    path('calendar_activities', get_calendar_activities_page, name='calendar_activities'),
    path('rate_and_registration_activities', get_rate_and_registration_activities_page,
         name='rate_and_registration_activities'),
    path('rate_and_registration_workshops', get_rate_and_registration_workshop_page,
         name='rate_and_registration_workshops'),
    path('youth_mauguio', get_youth_mauguio_page, name='youth_mauguio'),
    path('youth_carnon', get_youth_carnon_page, name='youth_carnon'),
    path('venue/<name_venue>', get_venue, name='venue'),
    path('venues', get_venues_list, name='venues_list'),
    path('host/<id>', get_host, name='host'),
    path('admin_panel', get_admin_panel, name='admin_panel'),
    path('admin/activity/<activity_slot_id>', edit_activity, name='admin_edit_activity'),
    path('admin/workshop/<workshop_slot_id>', edit_workshop, name='admin_edit_workshop'),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
]
