from django.contrib import admin
from .models import Admission
from unfold.admin import ModelAdmin
from django.utils.html import format_html
from django.conf import settings
from import_export.admin import ImportExportModelAdmin
from unfold.contrib.import_export.forms import ExportForm, ImportForm, SelectableFieldsExportForm

@admin.register(Admission)
class Admin_admission(ModelAdmin,ImportExportModelAdmin):
    list_display = ['photo_display','full_name','Preferred_program', 'Type_of_applicant','Waitlist', 'Contact_number']
    search_fields = ['full_name', 'Given_name', 'Middle_name','Preferred_program']
    list_filter = ['Type_of_applicant','Preferred_program','Waitlist']
    date_hierarchy = 'publish_at'
    ordering = ['Type_of_applicant', 'publish_at']
    show_facets = admin.ShowFacets.ALWAYS
    import_form_class = ImportForm
    export_form_class = ExportForm
    def photo_display(self, obj):
        if obj.photo:
            return format_html(
                '<img src="{}" style="width: 50px; height: 50px; border-radius: 50%;" />',
                obj.photo.url
            )
        return "No Photo"
    photo_display.short_description = "Photo"