from django.shortcuts import render, redirect, get_object_or_404
from .models import Social_Family, Social


def get_list_of_all_socials(request):
    socials = Social.objects.all()
    return render(request, "social/list_of_all_socials.html", {'socials': socials})

    
def get_social_details(request, social_id):
    social = get_object_or_404(Social, id=social_id)
    return render(request, "social/social_details.html", {'social': social})
