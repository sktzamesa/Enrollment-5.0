from django.urls import path
from . import views
app_name = 'admission'
urlpatterns = [
    path('admission',views.admission,name = 'admission'),
    path('data-privacy/',views.data_privacy,name='data_privacy'),
    path('admission_complete/',views.admission_complete,name='admission_complete')
]