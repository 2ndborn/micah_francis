from django.shortcuts import render
from .models import Interest

def about(request):
    """A view to render the about me page"""

    interests = Interest.objects.all()

    context = {
       'interests': interests
    }

    return render(request, 'about/about.html', context)
