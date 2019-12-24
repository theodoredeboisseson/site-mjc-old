from django.db import models
from django.contrib.auth.models import User
from activities.models import Activity_Animation_Slot


class RegistrationOrder(models.Model):
    
    user = models.ForeignKey(User,  on_delete=models.SET_NULL, null=True, related_name="RegistrationOrder")
    slot = models.ForeignKey(Activity_Animation_Slot, on_delete=models.SET_NULL, null=True, related_name="RegistrationOrder")
    date = models.DateField(auto_now_add=True)
    paid_fare = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.activity_slot, self.user)
    
    class Meta:
        verbose_name = 'Paiement'
        verbose_name_plural = 'Paiements'
