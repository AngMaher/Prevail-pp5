from django.shortcuts import render
from .models import Classes


def classes(request):
    """A view to return the classes"""
    class_list = Classes.objects.all()

    return render(request, 'classes/classes.html', {'class_list': class_list})
