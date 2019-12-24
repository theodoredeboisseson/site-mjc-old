from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Activity_Animation_Type, Activity_Animation, Activity_Animation_Slot, Elements_Type, \
                    Host, City, Weekday, Venue, Room


class TestActivitiesViews(TestCase):

    def setUp(self):
        
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.element_type = Elements_Type.objects.create(element_type='ACTIVITY')
        self.activity_animation_type = Activity_Animation_Type.objects.create(animation_type="sport")
        self.activity_animation = Activity_Animation.objects.create(name="judo", available_in_both_cities=True,
                                                                    disabled_friendly=True, new=True)
        self.host = Host.objects.create()
        self.city = City.objects.create(city="mauguio")
        self.venue = Venue.objects.create(name="venue01", street_nb="101", street_name="rue",
                                          city=self.city, postcode="34130")
        self.room = Room.objects.create(venue=self.venue, room_nb="202", room_name="arts")
        self.activity_animation_slot = Activity_Animation_Slot.objects.create(room=self.room, new=False)
        
        # self.weekday = Weekday.objects.create()
        # self.host = Host.objects.create()
        # self.city = City.objects.create()
    
    def test_list_of_animation_types_page(self):
        page = self.client.get(reverse("a_list_of_animations_types"))
        self.assertEqual(page.status_code, 200)
    
    def test_research_page(self):
        page = self.client.get(reverse("a_research"))
        self.assertEqual(page.status_code, 200)
    
    def test_list_of_animation_page(self):
        page = self.client.get(reverse("a_list_of_animations", args=[self.activity_animation_type.animation_type]))
        self.assertEqual(page.status_code, 200)
        
    def test_animation_details_page(self):
        page = self.client.get(reverse("a_animation_details", args=[self.activity_animation_type.animation_type,
                                                                    self.activity_animation.name,
                                                                    self.activity_animation.id ]))
        self.assertEqual(page.status_code, 200)
    
    def test_activity_registration_page(self):
        login = self.client.login(username='testuser', password='12345')
        page = self.client.get(reverse("a_animation_slot_registration", args=[self.activity_animation_type.animation_type,
                                                                              self.activity_animation.name,
                                                                              self.activity_animation.id,
                                                                              self.activity_animation_slot.id ]))
        self.assertEqual(page.status_code, 200)
