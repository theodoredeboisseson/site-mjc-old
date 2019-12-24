from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="Profile")
    adherent_number = models.CharField(max_length=5, null=False)
    rate_coefficient = models.DecimalField(max_digits=4, decimal_places=3)
    
    def __str__(self):
        return self.user.username
        
    class Meta:
        verbose_name = 'Profile Adhérent'
        verbose_name_plural = 'Profiles Adhérents'
