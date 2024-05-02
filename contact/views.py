from django.shortcuts import render, redirect, reverse
from .models import Contact
from .forms import ContactForm
from django.core.mail import send_mail


def contact(request):
   """A view to render the contact page"""

   if request.method == 'POST':
      subject = request.POST['subject']
      message = request.POST['message']
      email = request.POST['email']

      send_mail = (
         'subject',
         'message',
         'email',
      )
      
      return render(request,'contact/contact.html')
   
   else:
     return render(request, 'contact/contact.html')