from django.shortcuts import render, redirect
from produtos.models import Empregos
from produtos.forms import CadastroProducts
from django.contrib import messages


def home(request):
    
    jobs = Empregos.objects.all()
    
    return render(request, 'produtos/partials/home.html', {'jobs': jobs} )
# Create your views here.


def registerProduct(request):
    form = CadastroProducts()
    titleform = "Cadastro de Oportunidade"
    
    if request.method == 'POST':
        form = CadastroProducts(request.POST)
    
        if form.is_valid():
            titlef = form['title'].value()
            descriptionf = form['description'].value()
            #locationnf= form['location'].value()
            #categorynf= form['category'].value()
            #last_datenf = form['last_date'].value()
            #company_namenf= form['company_name'].value()
            #company_descriptionnf = form['company_description'].value()
            #websitenf = form['website'].value()
            #vacancynf = form['vacancy'].value()
            #salarynf = form['salary'].value()
            #statusnf = form['status'].value()
            
            empregos = Empregos.objects.create(
                title = titlef,
                description = descriptionf,
                #location = locationnf,
                #category = categorynf,
                #last_date = last_datenf,
                #company_name = company_namenf,
                #company_description = company_descriptionnf,
                #website = websitenf,
                #vacancy = int(vacancynf),
                #salary = int(salarynf),
                #status = statusnf,
            )
            empregos.save()
            messages.success(request, 'Cadastro efetuado com sucesso!')
            return redirect('accounts:login')
             
    return render(request, 'produtos/register.html', {'form': form,'title' : titleform })
    
    
