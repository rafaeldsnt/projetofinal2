from .views import (listNoticesforuser)
from django.urls import path


app_name = 'noticeboard' 

urlpatterns = [
    path('listNotices/', listNoticesforuser, name='listProduct' ), 
]