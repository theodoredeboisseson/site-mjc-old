from django.test import TestCase
from .models import Workshop_Animation_Type, Workshop_Animation, Workshop_Animation_Slot
from activities.models import Age_Group


class TestWorkshopModels(TestCase):
    
    def test_animation_type(self):
        
        animation_type = Workshop_Animation_Type(animation_type="test")
        self.assertEqual(str(animation_type), "test")
        
    def test_workshop_animation(self):
        
        animation_type = Workshop_Animation_Type(animation_type="someType")
        workshop_animation = Workshop_Animation(name="someName", animation_type=animation_type)
        self.assertEqual(str(workshop_animation), "someType - someName")
    
    def test_workshop_animation_slot(self):
        
        animation_type = Workshop_Animation_Type(animation_type="someType")
        workshop_animation = Workshop_Animation(name="someName", animation_type=animation_type)
        age_group = Age_Group(age_min=10, age_max=12)
        workshop_animation_slot = Workshop_Animation_Slot(workshop_animation=workshop_animation,
                                                          name="someSlotName",
                                                          age_group=age_group)
        self.assertEqual(str(workshop_animation_slot), "someType - someName - someSlotName - None - 10 / 12")
