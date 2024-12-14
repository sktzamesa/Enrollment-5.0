from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
urlpatterns=[
    path('',include('django.contrib.auth.urls')),
    path('home/', views.home, name='home'),
    path('about/',views.about,name = 'about'),
    path('grades/',views.grades,name = 'grades'),
    path('course/',views.course,name = 'course'),
    path('teacher_profile/',views.teacher_profile,name = 'teacher_profile'),
    path('course_details/',views. course_details,name = 'course_details'),
    path('teacher/',views.teacher,name = 'teacher'),
    path('contact/',views.contact,name = 'contact'),
    path('student_profile/',views.student_profile,name = 'student_profile'),
    path('update_profile/',views.update_profile,name = 'update_profile'),
]