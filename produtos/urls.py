from produtos.views import home, registerProduct
from django.urls import path


app_name = 'produtos' 

urlpatterns = [
    path('', home, name='home'), 
    path('register/', registerProduct , name='register'),
]