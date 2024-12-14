from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import FirstYearFirstSemesterCourses,FirstYearSecondSemesterCourse,SecondYearFirstSemesterCourses,SecondYearSecondSemesterCourses,ThirdYearFirstSemesterCourses,ThirdYearSecondSemesterCourses,FourthYearFirstSemesterCourses,FourthYearSecondSemesterCourses
# Register your models here.
@admin.register(FirstYearFirstSemesterCourses)
class FirstYearFirstSemesterCoursesAdmin(ModelAdmin):
    list_display = ['Subject_name','Subject_code','room_number']

@admin.register(FirstYearSecondSemesterCourse)
class FirstYearFirstSemesterCoursesAdmin(ModelAdmin):
    list_display = ['Subject_name','Subject_code','room_number']

@admin.register(SecondYearFirstSemesterCourses)
class SecondYearFirstSemesterCoursesAdmin(ModelAdmin):
    list_display = ['Subject_name','Subject_code','room_number']

@admin.register(SecondYearSecondSemesterCourses)
class SecondYearSecondSemesterCoursesAdmin(ModelAdmin):
    list_display = ['Subject_name','Subject_code','room_number']

@admin.register(ThirdYearFirstSemesterCourses)
class ThirdYearFirstSemesterCoursesAdmin(ModelAdmin):
    list_display = ['Subject_name','Subject_code','room_number']

@admin.register(ThirdYearSecondSemesterCourses)
class ThirdYearSecondSemesterCoursesAdmin(ModelAdmin):
    list_display = ['Subject_name','Subject_code','room_number']

@admin.register(FourthYearFirstSemesterCourses)
class FourthYearFirstSemesterCoursesAdmin(ModelAdmin):
    list_display = ['Subject_name','Subject_code','room_number']

@admin.register(FourthYearSecondSemesterCourses)
class FourthYearSecondSemesterCoursesAdmin(ModelAdmin):
    list_display = ['Subject_name','Subject_code','room_number'] 