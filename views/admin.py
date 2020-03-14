from django.contrib import admin
from .models import Slides, LandingPageMessage, PagePseudoStatic, PageFile


class LandingPageMessageAdmin(admin.ModelAdmin):  
    ordering = ('order',)


admin.site.register(Slides)
admin.site.register(LandingPageMessage, LandingPageMessageAdmin)
admin.site.register(PagePseudoStatic)
admin.site.register(PageFile)

