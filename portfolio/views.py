from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Portfolio, Collaborative
from .forms import PortfolioForm, CollaborativeForm

def portfolio(request):
    """A view to render the Portfolio page"""

    portfolio = Portfolio.objects.all().order_by('-id')
    collaborative = Collaborative.objects.all().order_by('-id')

    template = 'portfolio/portfolio.html'
    context = {
        'portfolio': portfolio,
        'collaborative': collaborative,
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
    """A view to delete a project entries"""
    if not request.user.is_superuser:
        return redirect(reverse('home'))
    portfolio = get_object_or_404(Portfolio, pk=portfolio_id)
    portfolio.delete()
    messages.success(request, 'Project deleted!')
    return redirect(reverse('portfolio'))


@login_required
def add_collaborative(request):
    """A view to render the add Collaborative page"""
    if not request.user.is_superuser:
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = CollaborativeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project added!')
            return redirect(reverse('portfolio'))
        else:
            messages.error(request, 'There was an error adding this project') 
    else:
      form = CollaborativeForm()

    template = 'portfolio/add_collaborative.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_collaborative(request, collaborative_id):
    """A view to render the edit Collaborative page"""
    if not request.user.is_superuser:
        return redirect(reverse('home'))
    collaborative = get_object_or_404(Collaborative, pk=collaborative_id)
    if request.method == 'POST':
        form = CollaborativeForm(request.POST, request.FILES, instance=collaborative)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project updated!')
            return redirect(reverse('portfolio'))
        else:
            messages.error(request, 'There was an error updating this project') 
   
    else:
        form = CollaborativeForm(instance=collaborative)

    template = 'portfolio/edit_collaborative.html'
    context = {
        'form': form,
        'collaborative': collaborative,
    }

    return render(request, template, context)


@login_required
def delete_collaborative(request, collaborative_id):
    """A view to delete a collaborative entries"""
    if not request.user.is_superuser:
        return redirect(reverse('home'))
    collaborative = get_object_or_404(Collaborative, pk=collaborative_id)
    collaborative.delete()
    messages.success(request, 'Project deleted!')
    return redirect(reverse('portfolio'))