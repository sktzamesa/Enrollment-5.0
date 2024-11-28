from django.shortcuts import render
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
