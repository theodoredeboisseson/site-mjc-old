from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Workshop_Animation_Type, Workshop_Animation, Workshop_Animation_Slot
from activities.models import Host


def get_list_of_animation_types(request):
    return render(request, "workshops/list_of_animation_types.html")


def get_list_of_animations(request, animation_type):
    animations_type = get_object_or_404(Workshop_Animation_Type, animation_type=animation_type)
    animations = Workshop_Animation.objects.filter(animation_type=animations_type.id).order_by('name')
    return render(request, "workshops/list_of_animations.html", {'animations_type': animations_type,
                                                                 'animations': animations})


def get_animation_details(request, animation_type, animation, animation_id):

    animation = get_object_or_404(Workshop_Animation, id=animation_id)
    slots = Workshop_Animation_Slot.objects.filter(workshop_animation=animation).order_by('date_of_the_first_day',
                                                                                          'age_group__age_min',
                                                                                          'age_group__age_max')
    
    hosts = []
    [[hosts.append(h) for h in Host.objects.filter(Workshop = slot.id)] for slot in slots]
    hosts = list(set(hosts))
    
    return render(request, "workshops/animation_details.html", {'animation': animation,
                                                                'slots': slots,
                                                                'hosts': hosts})
