
from .views import (HRdecisionDetailView, HRdecisionUpdateView)
from django.urls import path


app_name = 'rhmanager' 

urlpatterns = [
    path('listorders/', HRdecisionDetailView.as_view() , name='listorderurs'),
    path('listorders/<int:pk>/editar/', HRdecisionUpdateView.as_view(), name='editorderurs'),
]