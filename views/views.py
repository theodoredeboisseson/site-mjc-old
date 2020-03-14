from django.shortcuts import render, redirect, get_object_or_404
from django.http import FileResponse, Http404
from activities.models import Venue, Host
from news.models import News
from .models import Slides, LandingPageMessage, PagePseudoStatic, PageFile


def pseudostaticpage(page_id):
    """ page_id: int - id of the PageFile record """
    page = get_object_or_404(PagePseudoStatic, id=page_id)
    documents = PageFile.objects.filter(page=page.id).order_by('file_name')
    return {'page': page, 'documents': documents}


def get_home_page(request):
    carousel = Slides.objects.all()
    messages = LandingPageMessage.objects.all().order_by('order')
    last_news = News.objects.order_by('-published_date')[:3]
    return render(request, "views/index.html", {'carousel':carousel, 'messages': messages,'last_news': last_news})


def get_about_page(request):
    return render(request, "views/pagepseudostatic.html", pseudostaticpage(1))


def get_info_page(request):
    return render(request, "views/pagepseudostatic.html", pseudostaticpage(2))


def get_youth_carnon_page(request):
    return render(request, "views/pagepseudostatic.html", pseudostaticpage(3))


def get_youth_mauguio_page(request):
    return render(request, "views/pagepseudostatic.html", pseudostaticpage(4))


def get_rate_and_registration_activities_page(request):
    return render(request, "views/pagepseudostatic.html", pseudostaticpage(5))


def get_calendar_activities_page(request):
    return render(request, "views/pagepseudostatic.html", pseudostaticpage(6))


def get_rate_and_registration_workshop_page(request):
    return render(request, "views/pagepseudostatic.html", pseudostaticpage(7))


def get_social_page(request):
    return render(request, "views/pagepseudostatic.html", pseudostaticpage(8))


def get_venue(request, name_venue):
    venue = get_object_or_404(Venue, name=name_venue)
    return render(request, "views/venue.html", {'venue': venue} )


def get_venues_list(request):
    venues = Venue.objects.all().order_by('name')
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
