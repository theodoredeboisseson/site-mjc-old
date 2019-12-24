from django.test import TestCase  # Client
from django.urls import reverse
from django.contrib.auth.models import User
from activities.models import Venue, City, Host
from .models import Profile
from .forms import UserRegistrationForm, ProfileRegistrationForm


class TestAccountsViews(TestCase):
    
    def setUp(self):
        self.userform = UserRegistrationForm({'username': 'testuser2568',
                                              'email': 'test@gmail.com',
                                              'password1': 'password1234_*/',
                                              'password2': 'password1234_*/'
                                              })
        self.profileform = ProfileRegistrationForm({'adherent_number': '1234',
                                                    'rate_coefficient': '1'})
        self.user = User.objects.create_user(username='testuser2', password='password1234_*/')
        
    def test_register_page(self):
        page = self.client.get(reverse("Register"))
        self.assertEqual(page.status_code, 200)
        page = self.client.post(reverse("Register"), {'username': 'testuser2568',
                                                      'email': 'test@gmail.com',
                                                      'password1': 'password1234_*/',
                                                      'password2': 'password1234_*/',
                                                      'adherent_number': '1234',
                                                      'rate_coefficient': '1'
                                                      })
        self.assertEqual(page.status_code, 302)
    
    def test_login_page(self):
        page = self.client.get(reverse("Login"))
        self.assertEqual(page.status_code, 200)
        page = self.client.post(reverse("Login"), {'username': 'testuser2', 'password': 'password1234_*/'})
        self.assertEqual(page.status_code, 302)
        page = self.client.post(reverse("Login"), {'username': 'fakeuser', 'password': '2'})
        self.assertEqual(page.status_code, 200)
    
    def test_logout_page(self):
        login = self.client.login(username='testuser2', password='password1234_*/')
        page = self.client.get(reverse("Logout"))
        self.assertEqual(page.status_code, 302)