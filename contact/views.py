from django.shortcuts import render, redirect, reverse
from .models import Contact
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


def contact(request):
   """A view to render the contact page"""
   contact = ContactForm(request.POST or None)
   if request.method == 'POST' and contact.is_valid():
      name = request.POST['name']
      subject = request.POST['subject']
      message = request.POST['message']
      email = request.POST['email']
      recipient_list = [settings.EMAIL_HOST_USER]

      send_mail(
         subject,
         message,
         email,
         recipient_list,
         fail_silently=False,
      )
      messages.success(request, 'Your message has been sent!')

      template = 'contact/contact.html'
      context = {
         'name': name,
         'contact': contact,
      }
      return render(request, template, context)
   else:
      if request.method == 'POST':
         messages.error(request, 'There was an error with your form.')
         return render(request, 'contact/contact.html', {'contact': ContactForm()})