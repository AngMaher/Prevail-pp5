from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Success_Stories
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import StoryForm


def stories(request):
    """A view to return Success Stories"""
    stories = Success_Stories.objects.all()

    return render(request, 'success_stories/success_stories.html', {'stories': stories})


def story_detail(request, story_id):
    """ A view to show individual Stories """

    story = get_object_or_404(Success_Stories, pk=story_id)

    context = {
        'story': story,
    }

    return render(request, 'success_stories/story_detail.html', context)


@login_required
def add_story(request):
    """ Add a new class """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == "POST":
        form = StoryForm(request.POST, request.FILES)
        if form.is_valid():
            story = form.save()
            messages.success(request, 'Successfully added new Class!')
            return redirect(reverse('stories'))
        else:
            messages.error(request, 'Failed to add a \
                 class. Please ensure the form is valid')
    else:
        form = StoryForm()

    template = 'success_stories/add_story.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_story(request, story_id):
    """Edit a Story details"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    story = get_object_or_404(Success_Stories, pk=story_id)
    if request.method == 'POST':
        form = StoryForm(request.POST, request.FILES, instance=story)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated the story')
            return redirect('stories')
        else:
            messages.error(request, 'Failed to update class. \
                    Please ensure the form is valid.')
    else:
        form = StoryForm(instance=story)
        messages.info(request, f'You are editing \
                Story for {story.name}')

    template = 'success_stories/edit_story.html'
    context = {
        'form': form,
        'story': story,
    }

    return render(request, template, context)


@login_required
def delete_story(request, story_id):
    """Delete Story"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    story = get_object_or_404(Success_Stories, pk=story_id)
    if request.method == 'POST':
        story.delete()
        messages.success(request, f'Class {story.name} has \
                    been deleted!')
        return redirect(reverse('stories'))

    template = 'success_stories/delete_story.html'
    context = {
        'story': story,
    }

    return render(request, template, context)
