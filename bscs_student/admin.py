from django.contrib import admin
from bscs_student.models import FirstYearStudent
from unfold.admin import ModelAdmin
# Register your models here.
@admin.register(FirstYearStudent)
class FirstYearStudentAdmin(ModelAdmin):
    list_display = ['Full_name','StudentID','year_section','Type_of_student']
    search_fields = ['Full_name','StudentID']
    list_filter = ['year_section','Type_of_student']