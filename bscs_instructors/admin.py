from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Instructor
# Register your models here.
@admin.register(Instructor)
class InstructorAdmin(ModelAdmin):
    list_display = ['First_name']
