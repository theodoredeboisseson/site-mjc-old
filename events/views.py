from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.http import FileResponse, Http404
from .models import Event_Family, Event
from datetime import datetime, timedelta


def get_list_of_all_events(request):
    events_coming = Event.objects.filter(date_last_day__gte=datetime.now()).order_by('date_first_day')
    events_past = Event.objects.filter(date_last_day__lt=datetime.now()).order_by('-date_first_day')
    return render(request, "events/list_of_all_events.html", {'events_coming': events_coming,
                                                              'events_past': events_past})

    
def get_event_details(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, "events/event_details.html", {'event': event})
