from django.shortcuts import render

def portfolio(request):
    """A view to render the Portfolio page"""
    return render(request, 'portfolio/portfolio.html')