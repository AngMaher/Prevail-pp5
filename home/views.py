from django.shortcuts import render


def index(request):
    """A view to return the index page"""
    return render(request, 'home/index.html')


def about(request):
    """A view to return the how it works page"""
    return render(request, 'home/how_it_works.html')


def policy(request):
    """A view to see the privacy policy"""
    return render(request, 'home/privacy_policy.html')
