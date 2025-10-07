from django.shortcuts import render, redirect
from produtos.models import Empregos, Favorite, SpecialtyDefendant

from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

def home(request):
    
    jobs = Empregos.objects.all()
    
    total = len(jobs)
        
    return render(request, 'produtos/partials/home.html', {'jobs': jobs, "total" : total} )
# Create your views here.

def AboutUs(request):
    
    jobs = Empregos.objects.all()
        
    return render(request, 'produtos/about_us.html', {'jobs': jobs})

def listProduct(request):
     jobs = Empregos.objects.all()
     
     return render(request, 'produtos/produtos-list.html', {'jobs': jobs} )
 


 
def FavoriteListView(ListView):
    model = Favorite
    template_name = "jobs/employee/favorites.html"
    context_object_name = "favorites"

    def get_queryset(self):
        return self.model.objects.select_related("job__user").filter(soft_deleted=False, user=self.request.user)

class ProdutoCreateNew(CreateView):
    model = Empregos
    template_name = 'produtos/register.html'
    fields = ['title', 'description', 'location', 'job_option', 'category', 'last_date', 'category', 'specialtydefendant', 
               'company_name', 'company_description', 'website', 'salary', 'vacancy', 'filled']
    
    success_url = reverse_lazy('produtos:listProduct')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Cadastrar Nova Oportunidade'
        return context

def listAllProducts(request):
     jobs = Empregos.objects.all()
     
     return render(request, 'produtos/produtos-list-all.html', {'jobs': jobs} )  


class OportunityAllDetailView(DetailView):
    model = Empregos
    template_name = 'produtos/produto-details.html'
    context_object_name = 'job'

class ProdutoUpdateView(UpdateView):
    model = Empregos
    template_name = 'produtos/register.html'
    fields = ['title', 'description', 'location', 'job_option', 'category', 'last_date', 'category', 
               'company_name', 'company_description', 'website', 'salary', 'vacancy', 'filled']
    
    success_url = reverse_lazy('produtos:listProduct')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Produto'
        return context
    

class ProdutoDeleteView(DeleteView):
    model = Empregos
    template_name = 'produtos/produtos-delete.html'
    success_url = reverse_lazy('produtos:listProduct')
    context_object_name = 'produto'


class SpecialtyDefendantDetailView(ListView):
    model = SpecialtyDefendant
    template_name = 'produtos/SpecialtyDefendant-listt.html'
    ordering = ['identificacao']
    context_object_name = 'specialtys'
    success_url = reverse_lazy('produtos:listsperegister')
    paginate_by = 10 #
    

class SpecialtyDefendantCreateNew(CreateView):
    model = SpecialtyDefendant
    template_name = 'produtos/register-specialtydefendant.html'
    fields = ['identificacao', 'descricao']
    
    success_url = reverse_lazy('produtos:listsperegister')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Cadastrar Nova Especialidade'
        return context

class SpecialtyDefendantUpdateView(UpdateView):
    model = SpecialtyDefendant
    template_name = 'produtos/register-specialtydefendant.html'
    fields = ['identificacao', 'descricao']
    
    
    success_url = reverse_lazy('produtos:listsperegister')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Especialidade'
        return context

class SpecialtyDefendantDeleteView(DeleteView):
    model = SpecialtyDefendant
    template_name = 'produtos/produtos-delete.html'
    success_url = reverse_lazy('produtos:listProduct')
    context_object_name = 'specialtys'
    success_url = reverse_lazy('produtos:listsperegister')