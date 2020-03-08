from django.db import models
from django.contrib.auth.models import User
from utils import upload_path_handler
# from accounts.models import Profile


class Elements_Type(models.Model):
    
    ACTIVITY = 'ACTIVITY'
    WORKSHOP = 'WORKSHOP'
    EVENT = 'EVENT'
    
    TYPE = (
        (ACTIVITY, 'ACTIVITY'),
        (WORKSHOP, 'WORKSHOP'),
        (EVENT, 'EVENT'),
    )
    
    element_type = models.CharField("Type d'élément", max_length=50, choices=TYPE)
    title = models.CharField("Label", max_length=50, null=True)
    description = models.TextField("Description", null=True)
    folder = models.CharField("Folder", max_length=40, default="images/event_type", null=True, blank=True, editable=False)
    image = models.ImageField("Image", upload_to=upload_path_handler, blank=True, null=True)
    
    def __str__(self):
        return self.element_type

    class Meta:
            verbose_name = "Eléments - Type"
            verbose_name_plural = "Z. Page principale - Cartes 'Activité' / 'Stages' / 'Evénement' "

    
class Period(models.Model):
    
    period = models.CharField("Période", max_length=20, null=False)
    
    def __str__(self):
        return self.period

    class Meta:
            verbose_name = "Période"
            verbose_name_plural = "A. Périodes"   


class Activity_Animation_Type(models.Model):
    
    animation_type = models.CharField("Type d'animation (ex: sports, activité artistique, ...)", max_length=100, null=False)
    description = models.TextField("Présentation générale", null=True)
    folder = models.CharField("Folder", max_length=40, default="images/activity/animation_type", null=True, blank=True, editable=False)
    image = models.ImageField("Image", upload_to=upload_path_handler, blank=True, null=True)
    
    def __str__(self):
        return self.animation_type

    class Meta:
            verbose_name = "Animation - Type d'animation"
            verbose_name_plural = "1. Animations - Types d'animation"


class Activity_Animation(models.Model):
    
    name = models.CharField("Nom", max_length=100)
    animation_type = models.ForeignKey(Activity_Animation_Type, related_name="Animation", on_delete=models.SET_NULL, null=True)
    period = models.ForeignKey(Period, related_name="Animation", on_delete=models.SET_NULL, null=True, blank=True)
    disabled_friendly = models.BooleanField("Accessible handicap", default=None)
    new = models.BooleanField("Nouveau", default=None)
    available_in_both_cities = models.BooleanField("Existe à Mauguio ET à Carnon", default=None)
    folder = models.CharField("Folder", max_length=40, default="images/activity/animation/", null=True, blank=True, editable=False)
    image = models.ImageField("Image", upload_to=upload_path_handler, default="noimage.jpg")
    flash = models.CharField("Info flash", max_length=50, null=True, blank=True)
    description = models.TextField("Présentation générale", blank=True)
    notes = models.TextField("Notes spécifiques (certif. médical, license, ...)", null=True, blank=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Animation'
        verbose_name_plural = '2. Animations'

        
class Weekday(models.Model):
    
    LUNDI = 'Lundi'
    MARDI = 'Mardi'
    MERCREDI = 'Mercredi'
    JEUDI = 'Jeudi'
    VENDREDI = 'Vendredi'
    SAMEDI = 'Samedi'
    DIMANCHE = 'Dimanche'
    
    WEEKDAY_CHOICES = (
        (LUNDI, 'Lundi'),
        (MARDI, 'Mardi'),
        (MERCREDI, 'Mercredi'),
        (JEUDI, 'Jeudi'),
        (VENDREDI, 'Vendredi'),
        (SAMEDI, 'Samedi'),
        (DIMANCHE, 'Dimanche'),
    )
    
    day = models.CharField("Jour", max_length=10, choices=WEEKDAY_CHOICES)
    
    def __str__(self):
        return self.day

    class Meta:
            verbose_name = "Jour"
            verbose_name_plural = "F. Jours"


class Host(models.Model):
    
    firstname = models.CharField("Prénom", max_length=100, null=True)
    lastname = models.CharField("Nom", max_length=100, null=True)
    initials = models.CharField("Initiales", max_length=10, null=True)
    folder = models.CharField("Folder", max_length=40, default="images/hosts/", null=True, blank=True, editable=False)
    image = models.ImageField("Image", upload_to=upload_path_handler, default="noimage.jpg")
    resume = models.TextField("Présentation", null=True)
    
    def __str__(self):
        return '%s %s' % (self.firstname, self.lastname)
    
    class Meta:
        unique_together = ["firstname", "lastname"]

    class Meta:
            verbose_name = "Animateur"
            verbose_name_plural = "E. Animateurs"


class Age_Class(models.Model):
    
    age_class = models.CharField("Classe d'age", max_length=100, null=False, unique=True)
    
    def __str__(self):
        return self.age_class

    class Meta:
            verbose_name = "Age - Classe d'ages"
            verbose_name_plural = "B. Age - Classes d'ages"


class Age_Group(models.Model):
    
    age_class = models.ForeignKey(Age_Class, related_name="Age_Group", on_delete=models.SET_NULL, null=True)
    age_min = models.IntegerField("Age minimum", null=False)
    age_max = models.IntegerField("Age maximum", null=False)
    
    def __str__(self):
        return '%s - %s / %s' % (self.age_class, str(self.age_min), str(self.age_max))
    
    class Meta:
        unique_together = ["age_class", "age_min", "age_max"]
    
    class Meta:
            verbose_name = "Age - Groupe d'ages"
            verbose_name_plural = "C. Age - Groupes d'ages"


class Level(models.Model):
    
    level = models.CharField("Niveau", max_length=100, null=False, unique=True)
    
    def __str__(self):
        return self.level

    class Meta:
            verbose_name = 'Niveau'
            verbose_name_plural = 'D. Niveaux'


class City(models.Model):
    
    city = models.CharField("Ville", max_length=100, null=False, unique=True)

    def __str__(self):
        return self.city
        
    class Meta:
            verbose_name = "Ville"
            verbose_name_plural = "G. Villes"


class Venue(models.Model):
    
    name = models.CharField("Nom", max_length=100, null=False, unique=True)
    street_nb = models.CharField("N°", max_length=20, null=False, blank=True)
    street_name = models.CharField("Rue", max_length=200, null=False)
    city = models.ForeignKey(City, related_name="Venue", on_delete=models.SET_NULL, null=True)
    postcode = models.IntegerField("Code Postal", null=False)
    iframe_url_map = models.URLField("URL Google Iframe", max_length=500, null=True, blank=True)
    
    def __str__(self):
        return self.name

    class Meta:
            verbose_name = 'Lieu'
            verbose_name_plural = 'H. Lieux'


class Room(models.Model):
    
    venue = models.ForeignKey(Venue, related_name="Room", on_delete=models.SET_NULL, null=True)
    room_nb = models.CharField("Numéro de la Salle", max_length=100, null=True, blank=True)
    room_name = models.CharField("Nom de la Salle", max_length=100, null=True, blank=True)
    
    def __str__(self):
        return '%s - Salle %s - %s' % (self.venue, self.room_nb, self.room_name)

    class Meta:
        verbose_name = 'Salle'
        verbose_name_plural = 'I. Salles'


class Activity_Animation_Slot(models.Model):
    
    animation = models.ForeignKey(Activity_Animation, related_name="Slot", on_delete=models.SET_NULL, null=True)
    age_group = models.ForeignKey(Age_Group, related_name="Slot", on_delete=models.SET_NULL, null=True)
    level = models.ForeignKey(Level, related_name="Slot", on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField("Nom/Désignation", max_length=50, null=True, blank=True)
    new = models.BooleanField("Nouveau", default=None)
    host = models.ManyToManyField(Host, related_name="Slot", blank=True)
    day = models.ForeignKey(Weekday, related_name="Slot", on_delete=models.SET_NULL, null=True, blank=True)
    time_start = models.TimeField("Heure de début", null=True, blank=True)
    time_end = models.TimeField("Heure de fin", null=True, blank=True)
    room = models.ForeignKey(Room, related_name="Slot", on_delete=models.SET_NULL, null=True)
    description = models.TextField("Présentation (spécifique à ce crénau)", null=True, blank=True)
    rate_resident_1_name = models.CharField("MC - Tarif 1 - Désignation ", max_length=50, null=True, blank=True)
    rate_resident_1 = models.PositiveSmallIntegerField("MC - Tarif 1 - €", null=True, blank=True)
    rate_resident_2_name = models.CharField("MC - Tarif 2  - Désignation ", max_length=50, null=True, blank=True)
    rate_resident_2 = models.PositiveSmallIntegerField("MC - Tarif 2 - €", null=True, blank=True)
    rate_non_resident_1_name = models.CharField("Hors MC - Tarif 1 - Désignation ", max_length=50, null=True, blank=True)
    rate_non_resident_1 = models.PositiveSmallIntegerField("Hors MC - Tarif 1 - €", null=True, blank=True)
    rate_non_resident_2_name = models.CharField("Hors MC - Tarif 2 - Désignation ", max_length=50, null=True, blank=True)
    rate_non_resident_2 = models.PositiveSmallIntegerField("Hors MC - Tarif 2 - €", null=True, blank=True)
    notes = models.TextField("Notes particulières (spécifique à ce crénau)", null=True, blank=True)

    def __str__(self):
        return '%s - %s - %s/%s ans - %s - %s' % (self.age_group.age_class, self.animation,
                                                  self.age_group.age_min, self.age_group.age_max,
                                                  self.name, self.day)
    
    class Meta:
        verbose_name = 'Animation - Créneau'
        verbose_name_plural = '3. Animations - Créneaux'

    
class Activity_Registration(models.Model):
    
    participant = models.ForeignKey(User, related_name="RegistrationList", on_delete=models.SET_NULL, null=True)
    activity_slot = models.ForeignKey(Activity_Animation_Slot, related_name="RegistrationList",
                                      on_delete=models.SET_NULL, null=True)
    
    class Meta:
        unique_together = ["participant", "activity_slot"]
    
    def __str__(self):
        return 'Activity Slot Registration N° %s' % (self.id)
    
    class Meta:
        verbose_name = 'Inscription'
        verbose_name_plural = 'Inscriptions'
