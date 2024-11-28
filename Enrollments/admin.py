from django.contrib import admin
from .models import Admission,Regular
from unfold.admin import ModelAdmin
from django.utils.html import format_html
from django.conf import settings

@admin.register(Admission)
class Admin_admission(ModelAdmin):
    list_display = ['photo_display','full_name', 'Given_name', 'Middle_name', 'Type_of_applicant', 'Contact_number']
    search_fields = ['full_name', 'Given_name', 'Middle_name']

    def photo_display(self, obj):
        if obj.photo:
            return format_html(
                '<img src="{}" style="width: 50px; height: 50px; border-radius: 50%;" />',
                obj.photo.url
            )
        return "No Photo"
    photo_display.short_description = "Photo"

@admin.register(Regular)
class RegularAdmin(ModelAdmin):
    list_display = ['Student_Regular']

# Register your models here.
