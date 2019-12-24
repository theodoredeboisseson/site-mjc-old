from django.contrib import admin
from .models import Elements_Type, Activity_Animation_Type, Activity_Animation, Weekday, Period, Host, \
                    Age_Class, Age_Group, Level, City, Venue, Room, Activity_Animation_Slot


class Age_ClassAdmin(admin.ModelAdmin):  
    list_display = ['age_class']
    ordering = ('age_class',)
   
    
class Age_GroupAdmin(admin.ModelAdmin):  
    list_display = ['age_class', 'age_min', 'age_max']
    ordering = ('age_class', 'age_min', 'age_max')


class LevelAdmin(admin.ModelAdmin):  
    list_display = ['level']
    ordering = ('level', )


class RoomAdmin(admin.ModelAdmin):  
    list_display = ['venue', 'room_nb', 'room_name']
    ordering = ('venue', 'room_nb', 'room_name')


class HostAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'image', 'resume']
    ordering = ('firstname', 'lastname')
 

class Activity_Animation_TypeAdmin(admin.ModelAdmin):
    list_display = ['animation_type']
    ordering = ('animation_type',)
    

class WeekdayAdmin(admin.ModelAdmin):
    list_display = ['day', 'id']
    ordering = ('id',)
    

class Activity_AnimationAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ('name',)


class Activity_Animation_SlotAdmin(admin.ModelAdmin):
    list_display = ['animation', 'day', 'time_start', 'time_end', 'age_group', 'name']
    ordering = ('animation', 'day', 'time_start', 'time_end', 'age_group', 'name')


admin.site.register(Elements_Type)
admin.site.register(Activity_Animation_Type, Activity_Animation_TypeAdmin)
admin.site.register(Activity_Animation, Activity_AnimationAdmin)
admin.site.register(Weekday,WeekdayAdmin)
admin.site.register(Period)
admin.site.register(Host, HostAdmin)
admin.site.register(Age_Class, Age_ClassAdmin)
admin.site.register(Age_Group, Age_GroupAdmin)
admin.site.register(Level, LevelAdmin)
admin.site.register(City)
admin.site.register(Venue)
admin.site.register(Room, RoomAdmin)
admin.site.register(Activity_Animation_Slot, Activity_Animation_SlotAdmin)
