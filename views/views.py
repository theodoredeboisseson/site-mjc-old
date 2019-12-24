from django.shortcuts import render, redirect, get_object_or_404
from django.http import FileResponse, Http404
from activities.models import Venue, Host
from news.models import News
from files.models import Files_CR
from .models import Slides


def get_home_page(request):
    carousel = Slides.objects.all()
    last_news = News.objects.order_by('-published_date')[:3]
    return render(request, "views/index.html", {'carousel':carousel, 'last_news': last_news})


def get_info_page(request):
    return render(request, "views/info.html")


def get_calendar_activities_page(request):
    return render(request, "views/calendar_activities.html")


def get_about_page(request):
    documents = Files_CR.objects.all().order_by('order')
    return render(request, "views/about.html", {'documents':documents})

   
def get_rate_and_registration_activities_page(request):
    return render(request, "views/rate_and_registration_activities.html")


def get_rate_and_registration_workshop_page(request):
    return render(request, "views/rate_and_registration_workshops.html")


def get_youth_mauguio_page(request):
    return render(request, "views/youth_mauguio.html")


def get_youth_carnon_page(request):
    return render(request, "views/youth_carnon.html")


def get_venue(request, name_venue):
    venue = get_object_or_404(Venue, name=name_venue)
    return render(request, "views/venue.html", {'venue': venue} )


def get_venues_list(request):
    venues = Venue.objects.all
    return render(request, "views/venues_list.html", {'venues': venues} )


def get_host(request, id):
    host = get_object_or_404(Host, pk=id)
    return render(request, "views/host.html", {'host': host} )


def get_admin_panel(request):
    return redirect("/admin")
    

def edit_activity(request, activity_slot_id):
    return redirect("/admin/activities/activity_animation_slot/" + str(activity_slot_id) + "/change")


def edit_workshop(request, workshop_slot_id):
    return redirect("/admin/workshops/workshop_animation_slot/" + str(workshop_slot_id) + "/change")
