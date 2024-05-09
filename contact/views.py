from django.shortcuts import render, redirect, reverse
from .models import Contact
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


def contact(request):
   """A view to render the contact page"""
   contact_form = ContactForm(request.POST or None)
   if request.method == 'POST' and contact_form.is_valid():
      name = contact_form.cleaned_data['name']
      subject = contact_form.cleaned_data['subject']
      message = contact_form.cleaned_data['message']
      email = contact_form.cleaned_data['email']
      recipient_list = [settings.EMAIL_HOST_USER]

      send_mail(
         subject,
         message,
         email,
         recipient_list,
         fail_silently=False,
      )
      messages.success(request, 'Your message has been sent!')
      return redirect('contact')  # Redirect to a success page

   # This handles both GET requests and POST requests where the form is not valid
   if request.method == 'POST':
      messages.error(request, 'There was an error with your form.')
   return render(request, 'contact/contact.html', {'contact': contact_form})
