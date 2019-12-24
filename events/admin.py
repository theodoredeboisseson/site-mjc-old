from django.contrib import admin
from .models import Event_Family, Event


class Event_FamilyAdmin(admin.ModelAdmin):  
    list_display = ['family',]
    ordering = ('family',)


admin.site.register(Event_Family, Event_FamilyAdmin)
admin.site.register(Event)
