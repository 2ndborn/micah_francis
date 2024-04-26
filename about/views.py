from django.shortcuts import render

def about(request):
    """A view to render the about me page"""
    return render(request, 'about/about.html')
