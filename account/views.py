from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate,login
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from bscs_student.models import FirstYearFirstSemesterStudent
# Create your views here.
@login_required
def dashboard(request):
    firstyearstudent = get_object_or_404(
        FirstYearFirstSemesterStudent,
        Student=request.user
    )
    return render(
        request,
        "account/dashboard.html",
        {
            'section':'dashboard',
            'firstyearstudent':firstyearstudent,
        }
    )
@login_required
def about(request):
    return render(
        request,
        'account/about.html',
    )