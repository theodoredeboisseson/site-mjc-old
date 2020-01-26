from django.db import models
from utils import upload_path_handler


class Files_Pseudostatic(models.Model):
    
    file_name = models.CharField("Fichier - Nom", max_length=100, null=True, blank=True)
    file_code = models.CharField("Fichier - Code", max_length=4, null=True, blank=True)
    folder = models.CharField("Folder", max_length=40, default="documents", null=True, blank=True, editable=False)
    file = models.FileField("Fichier - PDF", upload_to=upload_path_handler, null=True, blank=True)
    
    def __str__(self):
            return self.file_name
        
    class Meta:
        verbose_name = "Documents"
        verbose_name_plural = "2. Documents - Autres"
        

class Files_CR(models.Model):
    
    file_name = models.CharField("Fichier - Nom", max_length=100, null=False, blank=False)
    folder = models.CharField("Folder", max_length=40, default="documents-CR", null=True, blank=True, editable=False)
    file = models.FileField("Fichier - PDF", upload_to=upload_path_handler, max_length=100, null=True, blank=True)
    order = models.IntegerField("Ordre d'apparition", null=True, blank=True)
    
    def __str__(self):
            return '%s %s' % (self.order, self.file_name) 
        
    class Meta:
        verbose_name = "Documents"
        verbose_name_plural = "1. Documents - CR et similaires"
