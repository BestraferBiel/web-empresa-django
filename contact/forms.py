from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre', required=True,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe tu nombre'}), max_length=100, min_length=3)
    email = forms.EmailField(label='Email', required=True,widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Escribe tu email'}), max_length=100, min_length=3)
    message = forms.CharField(label='Mensaje', required=True,widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}), max_length=1000, min_length=3)