from django.contrib import admin
from bscs_student.models import BSCSStudent
from unfold.admin import ModelAdmin
# Register your models here.
@admin.register(BSCSStudent)
class FirstYearFirstSemesterStudentAdmin(ModelAdmin):
    list_display = ['Student','Type_of_student']
    search_fields = ['Student']
    list_filter = ['First_year_section','Type_of_student']
