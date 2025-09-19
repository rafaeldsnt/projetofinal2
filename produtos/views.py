from django.shortcuts import render, redirect
from produtos.models import Empregos
from produtos.forms import CadastroProducts
from django.contrib import messages


def home(request):
    
    jobs = Empregos.objects.all()
    
    total = len(jobs)
    
    return render(request, 'produtos/partials/home.html', {'jobs': jobs, 'total' : total} )
# Create your views here.

def registerProduct(request):
    titleform = "Cadastro de Oportunidade"
    
    if request.method == "POST":
        form = CadastroProducts(request.POST)
        template = "produtos/register.html"
        context = {}
        if form.is_valid(): 
            form.save()
            messages.success(request, 'Cadastro efetuado com sucesso!')
            return redirect('accounts:login')
    else:
        form = CadastroProducts()
        return render(request, 'produtos/register.html', {'form': form,'title' : titleform })