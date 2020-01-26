from django.db import models
from django.utils import timezone
from django.utils.text import slugify
# from dateutil.parser    import parse


def upload_path_handler(instance, filename):
    return "images/news/{title}/{file}".format(title=slugify(instance.title), file=slugify(filename))


class News(models.Model):
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to=upload_path_handler, blank=True, null=True)
    file = models.FileField("PDF", upload_to='files/news/', null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
