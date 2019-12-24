from django.contrib import admin
from .models import Social_Family, Social


class Social_FamilyAdmin(admin.ModelAdmin):  
    list_display = ['family',]
    ordering = ('family',)


admin.site.register(Social_Family, Social_FamilyAdmin)
admin.site.register(Social)
