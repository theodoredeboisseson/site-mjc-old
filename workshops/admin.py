from django.contrib import admin
from .models import Workshop_Animation_Type, Workshop_Animation, Workshop_Animation_Slot


admin.site.register(Workshop_Animation_Type)
admin.site.register(Workshop_Animation)
admin.site.register(Workshop_Animation_Slot)
