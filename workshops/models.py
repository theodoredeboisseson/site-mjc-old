from django.db import models
from activities.models import Host, Age_Group, Room


class Workshop_Animation_Type(models.Model):
    
    animation_type = models.CharField("Type d'animation (PAS DE SLASH DANS LE NOM !)", max_length=100, null=False)
    description = models.TextField("Description", null=True)
    image = models.ImageField("Image", upload_to="images/workshop/animation_type", blank=True, null=True)
    
    def __str__(self):
        return self.animation_type
    
    class Meta:
        verbose_name = "Atelier - Type d'animation"
        verbose_name_plural = "1. Ateliers - Types d'animations"
    
    
class Workshop_Animation(models.Model):
    
    name = models.CharField("Nom", max_length=100)
    animation_type = models.ForeignKey(Workshop_Animation_Type, related_name="Animation", on_delete=models.SET_NULL, null=True)
    disabled_friendly = models.BooleanField("Accessible handicap", default=None)
    new = models.BooleanField("Nouveau", default=None)
    available_in_both_cities = models.BooleanField("Existe à Mauguio ET à Carnon", default=None)
    image = models.ImageField("Image", upload_to="images/workshop/animation/", default="noimage.jpg")
    description = models.TextField("Présentation générale", blank=True)
    notes = models.TextField("Notes spécifiques", null=True, blank=True)
    
    def __str__(self):
        return '%s - %s' % (self.animation_type, self.name)
    
    class Meta:
        verbose_name = 'Atelier - Animation'
        verbose_name_plural = '2. Ateliers - Animation'


class Workshop_Animation_Slot(models.Model):
    
    workshop_animation = models.ForeignKey(Workshop_Animation, related_name="Workshop", on_delete=models.SET_NULL, null=True)
    host = models.ManyToManyField(Host, related_name="Workshop", blank=True)
    name = models.CharField("Nom", max_length=50, null=True)
    new = models.BooleanField("Nouveau", default=None)
    age_group = models.ForeignKey(Age_Group, related_name="Workshop", on_delete=models.SET_NULL, null=True)
    level = models.CharField("Niveau", max_length=50, null=True, blank=True)
    dates = models.TextField("Dates & Horaires", null=True, blank=True)
    date_of_the_first_day = models.DateField("Date du premier jour", null=True)
    date_of_the_last_day = models.DateField("Date du dernier jour")
    description = models.TextField("Présentation générale", null=True, blank=True)
    notes = models.TextField("Notes particulières", null=True, blank=True)
    rate = models.TextField("Tarifs", null=True, blank=True)
    room = models.ForeignKey(Room, related_name="Workshop", on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return '%s - %s - %s' % (self.workshop_animation, self.name, self.age_group)
    
    class Meta:
        verbose_name = 'Atelier - Créneau'
        verbose_name_plural = '3. Ateliers - Créneaux'