from django.shortcuts import render
from .models import Education, Work_experience, Interest

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
