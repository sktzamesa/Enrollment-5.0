from django.contrib import admin
from .models import FirstYearSection,SecondYearSection,ThirdYearSection,FourthYearSection
from unfold.admin import ModelAdmin
# Register your models here.
@admin.register(FirstYearSection)
class FirstYearSectionAdmin(ModelAdmin):
    list_display = ['first_year_section']

@admin.register(SecondYearSection)
class SecondYearSectionAdmin(ModelAdmin):
    list_display = ['second_year_section']


@admin.register(ThirdYearSection)
class ThirdYearSection_admin(ModelAdmin):
    list_display = ['ThirdYearSection']

@admin.register(FourthYearSection)
class FourthYearSection_admin(ModelAdmin):
    list_display = ['FourthYearSection']