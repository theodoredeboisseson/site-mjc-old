from django.test import TestCase
from django.urls import reverse
from .models import Elements_Type, Period, Activity_Animation, Weekday
# from .models import Activity_Animation_Type, Activity_Animation, Activity_Animation_Slot, Elements_Type, Host, City, Weekday, Venue, Room


class TestActivitiesModels(TestCase):
    
    def setUp(self):
        
        # self.user = User.objects.create_user(username='testuser', password='12345')
        
        self.element_type = Elements_Type.objects.create(element_type='ACTIVITY')
        self.period = Period.objects.create(period="period01")
        # self.activity_animation_type = Activity_Animation_Type.objects.create(animation_type="sport")
        self.activity_animation = Activity_Animation.objects.create(name="judo", available_in_both_cities=True, disabled_friendly=True, new=True)
        self.weekday = Weekday.objects.create(day='Lundi')
        # self.host = Host.objects.create()
        # self.city = City.objects.create(city="mauguio")
        # self.venue = Venue.objects.create(name="venue01", street_nb="101", street_name="rue", city = self.city, postcode="34130")
        # self.room = Room.objects.create(venue=self.venue, room_nb="202", room_name="arts")
        # self.activity_animation_slot = Activity_Animation_Slot.objects.create(room= self.room, new=False)

    def test_str(self):
        
        self.assertEqual(str(self.element_type), "ACTIVITY")
        self.assertEqual(str(self.period), "period01")
        self.assertEqual(str(self.activity_animation), "judo")
        self.assertEqual(str(self.weekday), "Lundi")
