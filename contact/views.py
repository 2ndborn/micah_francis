from django.shortcuts import render, redirect, reverse
from .models import Contact
from .forms import ContactForm
from django.core.mail import send_mail


def contact(request):
   """A view to render the contact page"""
   
   if request.method == 'POST':
      name = request.POST['name']
      subject = request.POST['subject']
      message = request.POST['message']
      email = request.POST['email']

      send_mail(
         name,
         subject,
         message,
         email,
         ['micah.francis69@googlemail.com'],
         fail_silently=False,
      )
      
      template = 'contact/contact.html'
      context = {
         'name': name
      }
      return render(request,'contact/contact.html', context)
   
   else:
     return render(request, 'contact/contact.html')