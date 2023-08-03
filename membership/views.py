from django.shortcuts import render
from classes.models import Classes
from classes.views import class_detail


def membership(request):
    """A view to return the index page"""

    counties = Classes.objects.all()
    template = 'membership/membership.html'

    return render(request, template, {'counties': counties})
