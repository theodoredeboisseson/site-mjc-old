from django.contrib import admin
from .models import Slides, PagePseudoStatic, PageFile


admin.site.register(Slides)
admin.site.register(PagePseudoStatic)
admin.site.register(PageFile)

