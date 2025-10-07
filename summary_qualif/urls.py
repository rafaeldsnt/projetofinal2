from summary_qualif.views import (listResumeCV, ResumeCV_CreateView)
from django.urls import path


app_name = 'summary_qualif' 

urlpatterns = [
    
    path('resumecv/', listResumeCV , name='listResumeCV'),
    path('register/', ResumeCV_CreateView.as_view() , name='register'),
]