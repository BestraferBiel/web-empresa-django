from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm

# Create your views here.
def contact(request):
    CForm=ContactForm()
    if request.method == 'POST':
        CForm=ContactForm(data=request.POST)
        if CForm.is_valid():
            name = CForm.cleaned_data['name']
            email = CForm.cleaned_data['email']
            message = CForm.cleaned_data['message']
            CForm = ContactForm()
            #supongamos que todo salio ok ahora redirigimos a la pagina de inicio
            return redirect(reverse('contact')+ '?ok')
    return render(request, "contact/contact.html",{'form':CForm})