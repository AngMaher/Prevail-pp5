from django.shortcuts import render


def success_stories(request):
    """A view to return the index page"""
    return render(request, 'success_stories/success_stories.html')
