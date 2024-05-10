from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import About, Education, Work_experience, Interest
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import AboutForm, EducationForm, Work_experienceForm, InterestForm


def about(request):
   """A view to render the about me page"""

   about = About.objects.all()
   education = Education.objects.all().order_by('-from_date')
   work_experience = Work_experience.objects.all().order_by('-from_date')
   interests = Interest.objects.all()

   context = {
      'about': about,
      'education': education,
      'interests': interests,
      'work_experience': work_experience,
   }

   return render(request, 'about/about.html', context)


@login_required
def add_about(request):
   """A view to add executive summary section"""
   if not request.user.is_superuser:
      messages.error(request, 'Sorry, you are not authorised to view this page')
      return redirect(reverse('home'))
   if request.method == 'POST':
      form = AboutForm(request.POST, request.FILES)
      if form.is_valid():
         form.save()
         messages.success(request, 'About added!')
         return redirect(reverse('about'))
      else:
         messages.error(request, 'Failed to add Executieve Summary. Please ensure the form is valid.')
   
   else:
      form = AboutForm()

   template = 'about/add_about.html'
   context = {
      'form': form,
   }

   return render(request, template, context)


@login_required
def edit_about(request, about_id):
   """A view to edit the About section"""
   if not request.user.is_superuser:
      messages.error(request, 'Sorry, you are not authorised to view this page')
      return redirect(reverse('home'))
   about = get_object_or_404(About, pk=about_id)
   if request.method == 'POST':
      form = AboutForm(request.POST, request.FILES, instance=about)
      if form.is_valid():
         form.save()
         messages.info(request, 'About me updated!')
         return redirect(reverse('about'))
      else:
         messages.info(request, 'Failed to update About me. Please ensure the form is valid.')
   
   else:
      form = AboutForm(instance=about)

   template = 'about/edit_about.html'
   context = {
      'form': form,
   }

   return render(request, template, context)


@login_required   
def delete_about(request, about_id):
   """A view to delete Executive Summary entries"""
   if not request.user.is_superuser:
      messages.error(request, 'Sorry, you are not authorised to view this page')
      return redirect(reverse('home'))
   about = get_object_or_404(About, pk=about_id)
   about.delete()
   messages.success(request, 'Executive Summary deleted!')
   return redirect(reverse('about'))


@login_required
def add_education(request):
   """A view to add to the Education section"""
   if not request.user.is_superuser:
      messages.error(request, 'Sorry, you are not authorised to view this page')
      return redirect(reverse('home'))
   if request.method == 'POST':
      form = EducationForm(request.POST, request.FILES)
      if form.is_valid():
         form.save()
         messages.info(request, 'Education added!')
         return redirect(reverse('about'))
      else:
         messages.info(request, 'Failed to add Education. Please ensure the form is valid.')
   
   else:
      form = EducationForm()

   template = 'about/add_education.html'
   context = {
      'form': form,
   }

   return render(request, template, context)


@login_required
def edit_education(request, education_id):
   """A view to edit Education entries"""
   if not request.user.is_superuser:
      messages.error(request, 'Sorry, you are not authorised to view this page')
      return redirect(reverse('home'))
   education = get_object_or_404(Education, pk=education_id)
   if request.method == 'POST':
      form = EducationForm(request.POST, request.FILES, instance=education)
      if form.is_valid():
         form.save()
         messages.info(request, 'Education updated!')
         return redirect(reverse('about'))
      else:
         messages.info(request, 'Failed to update Education. Please ensure the form is valid.')
   
   else:
      form = EducationForm(instance=education)

   template = 'about/edit_education.html'
   context = {
      'form': form,
   }

   return render(request, template, context)


@login_required   
def delete_education(request, education_id):
   """A view to delete Education entries"""
   if not request.user.is_superuser:
      messages.error(request, 'Sorry, you are not authorised to view this page')
      return redirect(reverse('home'))
   education = get_object_or_404(Education, pk=education_id)
   education.delete()
   messages.info(request, 'Education deleted!')
   return redirect(reverse('about'))


@login_required
def add_work(request):
   """A view to add Work Experience entries"""
   if not request.user.is_superuser:
      messages.error(request, 'Sorry, you are not authorised to view this page')
      return redirect(reverse('home'))
   if request.method == 'POST':
      form = Work_experienceForm(request.POST, request.FILES)
      if form.is_valid():
         form.save()
         messages.info(request, 'Work Experience added!')
         return redirect(reverse('about'))
      else:
         messages.info(request, 'Failed to add Work Experience. Please ensure the form is valid.')
   else:
      form = Work_experienceForm()

   template = 'about/add_work.html'
   context = {
      'form': form,
   }

   return render(request, template, context)


@login_required
def edit_work(request, work_id):
   """A view to edit Work experience entries"""
   if not request.user.is_superuser:
      messages.error(request, 'Sorry, you are not authorised to view this page')
      return redirect(reverse('home'))
   work = get_object_or_404(Work_experience, pk=work_id)
   if request.method == 'POST':
      form = Work_experienceForm(request.POST, request.FILES, instance=work)
      if form.is_valid():
         form.save()
         messages.info(request, 'Work Experience updated!')
         return redirect(reverse('about'))
      else:
         messages.info(request, 'Failed to update Work Experience. Please ensure the form is valid.')
   
   else:
      form = Work_experienceForm(instance=work)

   template = 'about/edit_work.html'
   context = {
      'form': form,
   }

   return render(request, template, context)


@login_required
def delete_work(request, work_id):
   """A view to delete a Work Experience entries"""
   if not request.user.is_superuser:
      messages.error(request, 'Sorry, you are not authorised to view this page')
      return redirect(reverse('home'))
   work = get_object_or_404(Work_experience, pk=work_id)
   work.delete()
   messages.info(request, 'Work Experience deleted!')
   return redirect(reverse('about'))


@login_required
def add_interest(request):
   """A view to add to the Interest section"""
   if not request.user.is_superuser:
      messages.error(request, 'Sorry, you are not authorised to view this page')
      return redirect(reverse('home'))
   if request.method == 'POST':
      form = InterestForm(request.POST, request.FILES)
      if form.is_valid():
         form.save()
         messages.info(request, 'Interest added!')
         return redirect(reverse('about'))
      else:
         messages.info(request, 'Failed to add Interest. Please ensure the form is valid.')
   
   else:
      form = InterestForm()

   template = 'about/add_interest.html'
   context = {
      'form': form,
   }

   return render(request, template, context)


@login_required
def edit_interest(request, interest_id):
   """A view to edit Interest entries"""
   if not request.user.is_superuser:
      messages.error(request, 'Sorry, you are not authorised to view this page')
      return redirect(reverse('home'))
   interest = get_object_or_404(Interest, pk=interest_id)
   if request.method == 'POST':
      form = InterestForm(request.POST, request.FILES, instance=interest)
      if form.is_valid():
         form.save()
         messages.info(request, 'Interest updated!')
         return redirect(reverse('about'))
      else:
         messages.info(request, 'Failed to update Interest. Please ensure the form is valid.')
   
   else:
      form = InterestForm(instance=interest)

   template = 'about/edit_interest.html'
   context = {
      'form': form,
   }

   return render(request, template, context)


def delete_interest(request, interest_id):
   """A view to delete Interest entries"""
   if not request.user.is_superuser:
      messages.error(request, 'Sorry, you are not authorised to view this page')
      return redirect(reverse('home'))
   interest = get_object_or_404(Interest, pk=interest_id)
   interest.delete()
   messages.info(request, 'Interest deleted!')
   return redirect(reverse('about'))