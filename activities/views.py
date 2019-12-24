from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
from .models import Activity_Animation_Type, Activity_Animation, Activity_Animation_Slot, \
                    Elements_Type, Host, City, Weekday  # EventRegistration


def get_list_of_animation_types(request):
    
    return render(request, "activities/list_of_animation_types.html")


@cache_page(60*60*24)
def research(request):
    
    # filters
    cities = City.objects.all().order_by('city')
    days = Weekday.objects.all().order_by('id')
    animation_types = Activity_Animation_Type.objects.all().order_by('animation_type')
    
    # activities data
    activities = Activity_Animation_Slot.objects.all().order_by('animation__animation_type__animation_type',
                                                                'animation__name', 'age_group__age_min',
                                                                'age_group__age_max', 'day_id', 'time_start')
    
    return render(request, "activities/research_activities.html", {'cities': cities,
                                                                   'days': days,
                                                                   'animation_types': animation_types,
                                                                   'activities': activities})


def get_list_of_animations(request, animation_type):
    
    animations_type = get_object_or_404(Activity_Animation_Type, animation_type=animation_type)
    animations = Activity_Animation.objects.filter(animation_type=animations_type.id).order_by('name')
    
    return render(request, "activities/list_of_animations.html", {'animations_type': animations_type,
                                                                  'animations': animations})


def get_animation_details(request, animation_type, animation, animation_id):

    animation_type = animation_type
    animation = get_object_or_404(Activity_Animation, id=animation_id)
    slots = Activity_Animation_Slot.objects.filter(animation=animation).order_by('age_group__age_min',
                                                                                 'age_group__age_max',
                                                                                 'name', 'day_id', 'time_start')
    
    hosts = []
    [[hosts.append(h) for h in Host.objects.filter(Slot=slot.id)] for slot in slots]
    hosts = list(set(hosts))
    
    unmentionned_rate_text = "Si le tarif n'est pas indiqué dans les notes, contacter la MJC."
    two_rates_no_info_on_second_rate = "Contacter la MJC pour connaitre les conditions du deuxième tarif."
    
    return render(request, "activities/animation_details.html",
                  {'animation_type': animation_type,
                   'animation': animation,
                   'slots': slots,
                   'hosts': hosts,
                   'unmentionned_rate_text': unmentionned_rate_text,
                   'two_rates_no_info_on_second_rate': two_rates_no_info_on_second_rate})


@login_required
def register_to_animation_slot(request, animation_type, animation, animation_id, slot_id):
    """todo: implement check if there is still room for more registration. Look at former code."""

    animation_type = animation_type
    animation = get_object_or_404(Activity_Animation, pk=animation_id)
    slot = get_object_or_404(Activity_Animation_Slot, pk=slot_id)
            
    return render(request, "activities/animation_registration.html", {"animation_type": animation_type,
                                                                      "animation": animation,
                                                                      "slot": slot})
