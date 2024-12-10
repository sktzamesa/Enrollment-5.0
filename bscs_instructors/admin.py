from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import FirstYearInstructor
# Register your models here.
@admin.register(FirstYearInstructor)
class InstructorAdmin(ModelAdmin):
    list_display = ['First_name']
