from django.contrib.auth import authenticate,login
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def dashboard(request):
    return render(
        request,
        "account/dashboard.html",
        {'section':'dashboard'}
    )
@login_required
def about(request):
    return render(
        request,
        'account/about.html',
    )