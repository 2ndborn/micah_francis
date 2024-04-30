from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Portfolio
from .forms import PortfolioForm

def portfolio(request):
    """A view to render the Portfolio page"""

    portfolio = Portfolio.objects.all()

    template = 'portfolio/portfolio.html'
    context = {
        'portfolio': portfolio,
    }

    return render(request, template, context)


def add_portfolio(request):
    """A view to render the add Portfolio page"""

    if request.method == 'POST':
      form = PortfolioForm(request.POST, request.FILES)
      if form.is_valid():
         form.save()
         return redirect(reverse('portfolio'))
   
    else:
      form = PortfolioForm()

    template = 'portfolio/add_portfolio.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_portfolio(request, portfolio_id):
    """A view to render the edit Portfolio page"""

    portfolio = get_object_or_404(Portfolio, pk=portfolio_id)
    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES, instance=portfolio)
        if form.is_valid():
            form.save()
        return redirect(reverse('portfolio'))
   
    else:
        form = PortfolioForm(instance=portfolio)

    template = 'portfolio/edit_portfolio.html'
    context = {
        'form': form,
        'portfolio': portfolio,
    }

    return render(request, template, context)


def delete_portfolio(request, portfolio_id):
   """A view to delete Education entries"""

   portfolio = get_object_or_404(Portfolio, pk=portfolio_id)
   portfolio.delete()
   return redirect(reverse('about'))