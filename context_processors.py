from activities.models import Activity_Animation_Type, Elements_Type
from workshops.models import Workshop_Animation_Type


def get_list_of_animation_types_activities(request):
    animations_types_activities = Activity_Animation_Type.objects.all().order_by('animation_type')
    return {'animations_types_activities':animations_types_activities}


def get_list_of_animation_types_workshops(request):
    animations_types_workshops = Workshop_Animation_Type.objects.all().order_by('animation_type')
    return {'animations_types_workshops':animations_types_workshops}
   

def get_elements_types(request):

    try:
        activity = Elements_Type.objects.get(element_type__exact="ACTIVITY")
        workshop = Elements_Type.objects.get(element_type__exact="WORKSHOP")
        event = Elements_Type.objects.get(element_type__exact="EVENT")
    except:
        activity = "Your admin need to fix that! =)"
        workshop = "Your admin need to fix that! =)"
        event = "Your admin need to fix that! =)"
    
    return {'activity': activity,
            'workshop': workshop,
            'event': event}
    

def get_documents(request):
    documents = Files_Pseudostatic.objects.all()
    return {'documents': documents}
