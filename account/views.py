from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate,login
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from bscs_student.models import BSCSStudent
from account.models import Profile
# Create your views here.
@login_required
def home(request):
    profile = get_object_or_404(Profile, User_Student_Profile=request.user)
    firstyearstudent = get_object_or_404(
        BSCSStudent,
        Student=profile
    )
    return render(
        request,
        "account/home.html",
        {
            'firstyearstudent':firstyearstudent,
        }
    )

@login_required
def nav(request):
    # Ensure the user has an associated profile
    student_profile = get_object_or_404(Profile, User_Student_Profile=request.user)

    return render(
        request,
        "base/base_nav_side.html",
        {
            "student_profile": student_profile,  # Pass the profile to the template
        }
    )

@login_required
def about(request):

    return render(
        request,
        'account/about.html',
    )
@login_required
def grades(request):
    return render(
        request,
        'account/grades.html',
    )
@login_required
def course(request):
    return render(
        request,
        'account/course.html',
    )
@login_required
def teacher_profile(request):
    return render(
        request,
        'account/teacher_profile.html',
    )
@login_required
def course_details(request):
    return render(
        request,
        'account/course_details.html',
    )
@login_required
def teacher(request):
    return render(
        request,
        'account/teacher.html',
    )
@login_required
def contact(request):
    return render(
        request,
        'account/contact.html',
    )
@login_required
def student_profile(request):
    return render(
        request,
        'account/student_profile.html',
    )
@login_required
def update_profile(request):
    return render(
        request,
        'account/update_profile.html',
    )