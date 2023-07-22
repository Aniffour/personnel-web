from django.shortcuts import redirect, render
from django.views import View
from . forms import ContactFORM ,ServicesFORM
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
class home(View) :
    def get(self , request): 
        return render(request , 'core/home.html')

    

class contact(View) : 
    def get(self  , request): 
        forms = ContactFORM()
        return render(request , 'core/contact.html',  {'forms':forms})
    
    def post(self , request):
        forms = ContactFORM(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            subject =forms.cleaned_data['subject']
            email = forms.cleaned_data['email']
            sent =EmailMessage(subject=f'Username : {username} | {subject}' , from_email=settings.EMAIL_HOST_USER , to=['as58201@gmail.com'] , reply_to=[email])
            sent.send()
            messages.success(request , 'Email has been send !')
        else :
            messages.error(request , 'Somethings invalid !')
        return redirect('home')

class services(View) : 
    def get(self  , request): 
        forms = ServicesFORM()
        return render(request , 'core/services.html',  {'forms':forms})
    
    def post(self , request):
        forms = ServicesFORM(request.POST)
        print(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            serverces =forms.cleaned_data['serverces']
            email = forms.cleaned_data['email']
            sent =EmailMessage(subject=f'servece | username : {username} | {serverces}' , from_email=settings.EMAIL_HOST_USER , to=['as58201@gmail.com'] , reply_to=[email])
            sent.send()
            messages.success(request , 'Serverce has been send , i will contact you !')
        else :
            messages.error(request , 'Somethings invalid !')
        return redirect('home')