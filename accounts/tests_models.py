from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile


class TestAccountModels(TestCase):
    
    def test_profile(self):
        
        self.user = User.objects.create_user(username='testuser', password='12345')
        profile = Profile(user=self.user, adherent_number="123456", rate_coefficient="1")
    
        self.assertEqual(str(profile), "testuser")
