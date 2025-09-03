from django import forms

select_type = (
        (1, "CLT - 8 Horas"),
        (2, "Consultoria - 4 Horas")
)

class CadastroProducts(forms.Form):
    title=forms.CharField(
        label='Nome do Cargo', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: Desenvolvedor C#, Desenvolvedor JS ',
            }
        )
    )
    
    description=forms.CharField(
        label='Descrição do Cargo', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: Como finalidade desenvolver sistemas utilizando a tecnologia ',
            }
        )
    )
    
    location=forms.CharField(
        label='Local de Trabalho', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: Remoto ou no escritório da empresa situado em São Paulo ',
            }
        )
    )
    
    
    #type=forms.ChoiceField(
    #        label="Qual é o tipo de contratação ?",
    #        choices=select_type, 
    #        widget=forms.ChoiceField,
    #        required=True
    #    )
	
    
    category = forms.CharField(
        label='Categoria', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: Analista de Desenvolvimento/Desenvolvedor/Agile Master',
            }
        )
    )
    
    last_date=forms.DateField(
        required=True, 
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'type': 'date'
                }
            )
        
    )
    
    company_name=forms.CharField(
        label='Nome da Empresa', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nome da Empresa',
            }
        )
    )
    
    company_description=forms.CharField(
        label='Descrição da Empresa', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Descrição da Empresa',
            }
        )
    )
    
    website=forms.CharField(
        label='Website da Empresa', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Website da Empresa',
            }
        )
    )
    
    vacancy=forms.IntegerField(
        label="Quantidade de Vagas",
        min_value='1',
        max_value='10',
    )
    
    salary=forms.FloatField(
        label="Salario oferecido",
        min_value=0.01,
        max_value=10000.00,
        required=True,
        help_text="Ex. Informe o Salário oferecido!"
    )
    
    status=forms.BooleanField(
        label="A vaga está ativa ?", 
        required=True, 
        initial=False
    )
  
    
    
 

        
    
    