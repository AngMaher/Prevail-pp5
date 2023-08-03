from django.shortcuts import render
from classes.models import Classes


def membership(request):
    """A view to return the index page"""

    counties = Classes.objects.all()

    return render(request, 'membership/membership.html', {'counties': counties})
