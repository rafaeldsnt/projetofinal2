from django import forms
from produtos.models import Empregos



select_type = (
        (1, "CLT - 8 Horas"),
        (2, "Consultoria - 4 Horas")
)

class CadastroProducts(forms.ModelForm):
    class Meta:
        model = Empregos
        fields = [
            "title",
            "description",
            "location",
            "type_job",
            "category",
            "last_date",
            "company_name",
            "company_description",
            "website",
            "salary",
            "vacancy",
            "filled",
        ]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Título da vaga"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "location": forms.TextInput(attrs={"class": "form-control"}),
            "type_job": forms.Select(attrs={"class": "form-select form-control"}),  # select automático pelos choices
            "category": forms.TextInput(attrs={"class": "form-control"}),
            "last_date": forms.DateInput(attrs={"type": "datetime-local", "class": "form-control"}),
            "company_name": forms.TextInput(attrs={"class": "form-control"}),
            "company_description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "website": forms.URLInput(attrs={"class": "form-control"}),
            "salary": forms.NumberInput(attrs={"class": "form-control"}),
            "vacancy": forms.NumberInput(attrs={"class": "form-control"}),
            "filled": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
        
    
    
    
 

        
    
    