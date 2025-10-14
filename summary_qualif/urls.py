from summary_qualif.views import (listResumeCV, ResumeCV_CreateView, ResumeCV_EditView)
from django.urls import path


app_name = 'summary_qualif' 

urlpatterns = [
    
    path('resumecv/', listResumeCV , name='listResumeCV'),
    path('register/', ResumeCV_CreateView.as_view() , name='register'),
    path('resumecvedit/<int:pk>/editar/', ResumeCV_EditView.as_view() , name='editregister'),
]