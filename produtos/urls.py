from produtos.views import (home, listProduct, FavoriteListView, AboutUs,
                           ProdutoUpdateView, ProdutoDeleteView, ProdutoCreateNew, SpecialtyDefendantCreateNew,
                           SpecialtyDefendantDetailView, SpecialtyDefendantUpdateView,  SpecialtyDefendantDeleteView, 
                           listAllProducts, OportunityAllDetailView, AppliedjobCreateNew)
from django.urls import path


app_name = 'produtos' 

urlpatterns = [
    path('', home, name='home'), 
    path('register/', ProdutoCreateNew.as_view() , name='register'),
    path('listProduts/', listProduct, name='listProduct' ),
    path('listProduts/<int:pk>/editar/', ProdutoUpdateView.as_view(), name='produto_update'),
    path('listProduts/<int:pk>/deletar/',  ProdutoDeleteView.as_view(), name='produto_delete'),
    path("favorites", FavoriteListView, name="employee-favorites"),
    
    path('listdetails/<int:pk>/', OportunityAllDetailView.as_view(), name='listdetails'),
    
    path('applyjob/', AppliedjobCreateNew.as_view(), name='applytojob'),
    
    path('allproducts/', listAllProducts , name='allproducts'),
   
    path('aboutus/', AboutUs, name='aboutus'), 
   
    path('specialt/', SpecialtyDefendantCreateNew.as_view() , name='speregister'),
    path('listsperegister/', SpecialtyDefendantDetailView.as_view(), name='listsperegister' ),
    path('listsperegister/<int:pk>/editar/', SpecialtyDefendantUpdateView.as_view(), name='speregister_update'),
    path('listsperegister/<int:pk>/deletar/',  SpecialtyDefendantDeleteView.as_view(), name='speregister_delete'),
    
]