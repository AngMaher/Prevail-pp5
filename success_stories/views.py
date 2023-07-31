from django.shortcuts import render, get_object_or_404
from .models import Success_Stories


def stories(request):
    """A view to return the classes"""
    stories = Success_Stories.objects.all()

    return render(request, 'success_stories/success_stories.html', {'stories': stories})


def story_detail(request, story_id):
    """ A view to show individual product details """

    story = get_object_or_404(Success_Stories, pk=story_id)

    context = {
        'story': story,
    }

    return render(request, 'success_stories/story_detail.html', context)
