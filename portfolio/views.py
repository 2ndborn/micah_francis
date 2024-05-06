from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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


@login_required
def add_portfolio(request):
    """A view to render the add Portfolio page"""
    if not request.user.is_superuser:
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project added!')
            return redirect(reverse('portfolio'))
        else:
            messages.error(request, 'There was an error adding this project') 
    else:
      form = PortfolioForm()

    template = 'portfolio/add_portfolio.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_portfolio(request, portfolio_id):
    """A view to render the edit Portfolio page"""
    if not request.user.is_superuser:
        return redirect(reverse('home'))
    portfolio = get_object_or_404(Portfolio, pk=portfolio_id)
    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES, instance=portfolio)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project updated!')
            return redirect(reverse('portfolio'))
        else:
            messages.error(request, 'There was an error updating this project') 
   
    else:
        form = PortfolioForm(instance=portfolio)

    template = 'portfolio/edit_portfolio.html'
    context = {
        'form': form,
        'portfolio': portfolio,
    }

    return render(request, template, context)


@login_required
def delete_portfolio(request, portfolio_id):
    """A view to delete Education entries"""
    if not request.user.is_superuser:
        return redirect(reverse('home'))
    portfolio = get_object_or_404(Portfolio, pk=portfolio_id)
    portfolio.delete()
    return redirect(reverse('about'))