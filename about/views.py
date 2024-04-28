from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import About, Education, Work_experience, Interest

from .forms import AboutForm, EducationForm, InterestForm

def about(request):
   """A view to render the about me page"""

   about = About.objects.all()
   education = Education.objects.all()
   work_experience = Work_experience.objects.all()
   interests = Interest.objects.all()

   context = {
      'about': about,
      'education': education,
      'interests': interests,
      'work_experience': work_experience,
   }

   return render(request, 'about/about.html', context)


def edit_about(request, about_id):
   """A view to edit the About section"""

   about = get_object_or_404(About, pk=about_id)
   if request.method == 'POST':
      form = AboutForm(request.POST, request.FILES, instance=about)
      if form.is_valid():
         form.save()
         return redirect(reverse('about'))
   
   else:
      form = AboutForm(instance=about)

   template = 'about/edit_about.html'
   context = {
      'form': form,
   }

   return render(request, template, context)


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

   template = 'about/edit_education.html'
   context = {
      'form': form,
   }

   return render(request, template, context)

   
def delete_education(request, education_id):
   """A view to delete Education entries"""

   education = get_object_or_404(Education, pk=education_id)
   education.delete()
   return redirect(reverse('about'))


def add_interest(request):
   """A view to add to the Interest section"""

   if request.method == 'POST':
      form = InterestForm(request.POST, request.FILES)
      if form.is_valid():
         form.save()
         return redirect(reverse('about'))
   
   else:
      form = InterestForm()

   template = 'about/add_interest.html'
   context = {
      'form': form,
   }

   return render(request, template, context)


def edit_interest(request, interest_id):
   """A view to edit Interest entries"""

   interest = get_object_or_404(Interest, pk=interest_id)
   if request.method == 'POST':
      form = InterestForm(request.POST, request.FILES, instance=interest)
      if form.is_valid():
         form.save()
         return redirect(reverse('about'))
   
   else:
      form = InterestForm(instance=interest)

   template = 'about/edit_interest.html'
   context = {
      'form': form,
   }

   return render(request, template, context)


def delete_interest(request, interest_id):
   """A view to delete Interest entries"""

   interest = get_object_or_404(Interest, pk=interest_id)
   interest.delete()
   return redirect(reverse('about'))