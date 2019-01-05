from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from  .forms import ContactForm

def index(request):

    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            try:
                send_mail(name, message, email, ['remylanier91@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid Header found')
            return redirect('success')
    return  render(request,'index.html', {'form': form})

def successView(request):
    return  HttpResponse("Success! Thank you for your message. Reply will be soon")