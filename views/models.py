from django.db import models


class Slides(models.Model):
    
    slide_title = models.CharField("Diapo - Titre", max_length=100, null=True, blank=True)
    slide_subtitle = models.CharField("Diapo - Sous titre", max_length=150, null=True, blank=True)
    image = models.ImageField("Diapo - Image", upload_to="images/carousel", blank=True, null=True)
    
    def __str__(self):
            return 'Diapositive %s' % (self.slide_title)
        
    class Meta:
        verbose_name = "Diapositive"
        verbose_name_plural = "Caroussel (Bandeau défilant)"
