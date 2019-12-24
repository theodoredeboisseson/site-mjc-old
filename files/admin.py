from django.contrib import admin
from .models import Files_Pseudostatic, Files_CR


class Files_CRAdmin(admin.ModelAdmin):  
    list_display = ['order', 'file_name']
    ordering = ('order', )


admin.site.register(Files_Pseudostatic)
admin.site.register(Files_CR, Files_CRAdmin)
