from django.contrib import messages
from django.shortcuts import render,redirect
from .forms import AdmissionForm
from django.contrib.auth.decorators import login_required

def data_privacy(request):
    return render(
        request,
        'admission/applicant/data_privacy.html'
    )
def admission(request):
    if request.method == 'POST':
        form = AdmissionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Your form have been successfully submitted')
            return redirect('admission:admission_complete')

        else:
            messages.error(request, 'There was an error with your submission. Please correct the errors below.')

    else:
        form = AdmissionForm()

    return render(
        request,
        'admission/applicant/admission_form.html',
        {
            'form': form,
        }
    )
def admission_complete(request):
    return render(
        request,
        'admission/applicant/submitted.html',
    )
# Create your views here.
