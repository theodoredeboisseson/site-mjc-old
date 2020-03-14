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
        verbose_name_plural = "1. Page principale - Bandeau défilant"

class LandingPageMessage(models.Model):

    INFO = 'info'
    SUCCESS = 'success'
    WARNING = 'warning'
    DANGER = 'danger'

    CATEGORY = [
        (INFO, 'INFO (Bleu)'),
        (SUCCESS, 'POSITIF (Vert)'),
        (WARNING, 'ATTENTION (Orange)'),
        (DANGER, 'DANGER (Rouge)'),
    ]

    title = models.CharField("Titre", max_length=100, null=True, blank=True)
    category = models.CharField("Couleur", max_length=100, choices=CATEGORY, default=INFO, null=True)
    message = RichTextField("Message", null=True, blank=False)
    order = models. IntegerField("Ordre", null=True, blank=False)

    def __str__(self):
        return f'Message N° {self.order} - {self.title}'

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "2. Page Principale - Messages Importants"

class PagePseudoStatic(models.Model):

    name = models.CharField("Nom", max_length=100, null=True, blank=True)
    content = RichTextField()

    def __str__(self):
        return '%s' % (self.name) 

    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "3. Pages - Texte"


class PageFile(models.Model):
    
    page =  models.ForeignKey(PagePseudoStatic, related_name="pagefile", on_delete=models.SET_NULL, null=True)
    file_name = models.CharField("Fichier - Nom", max_length=100, null=True, blank=True)
    file_code = models.CharField("Fichier - Code", max_length=4, null=True, blank=True)
    folder = models.CharField("Folder", max_length=40, default="documents", null=True, blank=True, editable=False)
    file = models.FileField("Fichier - PDF", upload_to=upload_path_handler, null=True, blank=True)
    
    def __str__(self):
            return f'{self.page} - {self.file_name}'
        
    class Meta:
        verbose_name = "Documents"
        verbose_name_plural = "4. Pages - Documents"