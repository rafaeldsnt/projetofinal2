from accounts.views import login, register, logout, Listusuarios
from django.urls import path
# Define o namespace para esta aplicação
app_name = 'accounts' 

# Create your views here.
urlpatterns = [
    path('', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('list-user', Listusuarios, name="listUsuarios" )
]