from django.db import models
from utils import upload_path_handler
from ckeditor.fields import RichTextField


class Slides(models.Model):
    
    slide_title = models.CharField("Diapo - Titre", max_length=100, null=True, blank=True)
    slide_subtitle = models.CharField("Diapo - Sous titre", max_length=150, null=True, blank=True)
    folder = models.CharField("Folder", max_length=40, default="images/carousel/", null=True, blank=True, editable=False)
    image = models.ImageField("Diapo - Image", upload_to=upload_path_handler, blank=True, null=True)
    
    def __str__(self):
            return 'Diapositive %s' % (self.slide_title)
        
    class Meta:
        verbose_name = "Diapositive"
        verbose_name_plural = "Caroussel (Bandeau défilant)"

class PageSection(models.Model):

    content = RichTextField()