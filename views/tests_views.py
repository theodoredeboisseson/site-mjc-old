from django.test import TestCase
from django.urls import reverse
from activities.models import Venue, City, Host
from django.contrib.auth.models import User
# from django.test import Client


class TestViewsViews(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_superuser(username='myuser', email="test@example.com", password='password')
        
        self.city = City.objects.create(city="mauguio")
        self.venue = Venue.objects.create(name="venue01", street_nb="101", street_name="rue",
                                          city=self.city, postcode="34130")
        self.host = Host.objects.create()
    
    def test_index_page(self):
        page = self.client.get(reverse("home"))
        self.assertEqual(page.status_code, 200)
        
    def test_about_page(self):
        page = self.client.get(reverse("about"))
        self.assertEqual(page.status_code, 200)
        
    def test_info_page(self):
        page = self.client.get(reverse("info"))
        self.assertEqual(page.status_code, 200)

    def test_calendar_activities_page(self):
        page = self.client.get(reverse("calendar_activities"))
        self.assertEqual(page.status_code, 200)
        
    def test_rate_and_registration_activities_page(self):
        page = self.client.get(reverse("rate_and_registration_activities"))
        self.assertEqual(page.status_code, 200)
        
    def test_rate_and_registration_workshops_page(self):
        page = self.client.get(reverse("rate_and_registration_workshops"))
        self.assertEqual(page.status_code, 200)

    def test_youth_mauguio_page(self):
        page = self.client.get(reverse("youth_mauguio"))
        self.assertEqual(page.status_code, 200)
        
    def test_youth_carnon_page(self):
        page = self.client.get(reverse("youth_carnon"))
        self.assertEqual(page.status_code, 200)
    
    def test_venues_list_page(self):
        page = self.client.get(reverse("venues_list"))
        self.assertEqual(page.status_code, 200)
    
    def test_venu_page(self):
        page = self.client.get(reverse("venue", args=[self.venue.name]))
        self.assertEqual(page.status_code, 200)
    
    def test_host_page(self):
        page = self.client.get(reverse("host", args=[self.host.id]))
        self.assertEqual(page.status_code, 200)

    def test_admin_panel_page(self):
        # Doesn't log in. Make another test with code 200.
        # login = self.client.login(username='myuser', password='password')
        # c = Client()
        # login = c.login(username='myuser', password='password')
        # login = self.client.login(username='myuser', password='password')
        # self.client.force_login(self.user)
        page = self.client.get(reverse("admin_panel"))
        self.assertEqual(page.status_code, 302)

    def test_admin_edit_activity_page(self):
        # Doesn't log in. Make another test with code 200.
        page = self.client.get(reverse("admin_edit_activity", args=[1]))
        self.assertEqual(page.status_code, 302)
    
    def test_admin_edit_workshop_page(self):
        # Doesn't log in. Make another test with code 200.
        page = self.client.get(reverse("admin_edit_workshop", args=[1]))
        self.assertEqual(page.status_code, 302)