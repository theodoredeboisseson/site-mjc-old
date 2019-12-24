from django.test import TestCase
from django.contrib.auth.models import User
from .forms import UserRegistrationForm, ProfileRegistrationForm


class TestAccountsForms(TestCase):
    
    def setUp(self):
        self.userform = UserRegistrationForm({'username': 'testuser2568',
                                              'email': 'test@gmail.com',
                                              'password1': 'password1234_*/',
                                              'password2': 'password1234_*/'
                                              })
        self.user = User.objects.create_user(username='testuser9999', password='password1234_*/',
                                             email='test9999@gmail.com')
        self.profileform = ProfileRegistrationForm({'user': self.user,
                                                    'adherent_number': '1234',
                                                    'rate_coefficient': '1'})
    
    def test_registration_form(self):
        self.assertTrue(self.userform.is_valid())
   
    def test_profile_form(self):
        self.assertTrue(self.profileform.is_valid())
