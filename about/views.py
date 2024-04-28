from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Education, Work_experience, Interest

from .forms import EducationForm

def about(request):
   """A view to render the about me page"""

   education = Education.objects.all()
   work_experience = Work_experience.objects.all()
   interests = Interest.objects.all()

   context = {
      'education': education,
      'interests': interests,
      'work_experience': work_experience,
   }

   return render(request, 'about/about.html', context)


def add_education(request):
   """A view to add to the Education section"""

   if request.method == 'POST':
      form = EducationForm(request.POST, request.FILES)
      if form.is_valid():
         form.save()
         return redirect(reverse('about'))
   
   else:
      form = EducationForm()

   template = 'about/add_education.html'
   context = {
      'form': form,
   }

   return render(request, template, context)


def edit_education(request, education_id):
   """A view to edit Education entries"""

   education = get_object_or_404(Education, pk=education_id)
   if request.method == 'POST':
      form = EducationForm(request.POST, request.FILES, instance=education)
      if form.is_valid():
         form.save()
         return redirect(reverse('about'))
   
   else:
      form = EducationForm(instance=education)

   context = {
      'form': form,
   }

   return render(request, 'about/edit_education.html', context)