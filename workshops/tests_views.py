from django.test import TestCase
from django.urls import reverse
from activities.models import Elements_Type
from .models import Workshop_Animation_Type, Workshop_Animation, Workshop_Animation_Slot
import datetime


class TestWorkshopViews(TestCase):
    
    def setUp(self):
        self.element_type = Elements_Type.objects.create(element_type='ACTIVITY')
        self.workshop_animation_type = Workshop_Animation_Type.objects.create(animation_type="sport")
        self.workshop_animation = Workshop_Animation.objects.create(name="judo", available_in_both_cities=True,
                                                                    disabled_friendly=True, new=True, description="")
        self.slot = Workshop_Animation_Slot.objects.create(new=False, date_of_the_last_day=datetime.datetime.now())
    
    def test_w_list_of_animations_types_page(self):
        page = self.client.get(reverse("w_list_of_animations_types", args=[]))
        self.assertEqual(page.status_code, 200)
    
    def test_list_of_animation_type_page(self):
        page = self.client.get(reverse("w_list_of_animations", args=[self.workshop_animation_type.animation_type]))
        self.assertEqual(page.status_code, 200)
    
    def test_w_animation_details_page(self):
        page = self.client.get(reverse("w_animation_details",
                                       args=[self.workshop_animation_type.animation_type, self.workshop_animation.name,
                                             self.slot.id]))
        self.assertEqual(page.status_code, 200)
