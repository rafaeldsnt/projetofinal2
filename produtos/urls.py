from produtos.views import home, registerProduct, listProduct
from django.urls import path


app_name = 'produtos' 

urlpatterns = [
    path('', home, name='home'), 
    path('register/', registerProduct , name='register'),
    path('listProduts/', listProduct, name='listProduct' )
    
]