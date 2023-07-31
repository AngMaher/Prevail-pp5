from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Classes
from .forms import ClassesForm
from django.contrib.auth.decorators import login_required


def classes(request):
    """A view to return the classes"""
    class_list = Classes.objects.all()

    return render(request, 'classes/classes.html', {'class_list': class_list})


@login_required
def add_classes(request):
    """ Add a new class """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == "POST":
        form = ClassesForm(request.POST, request.FILES)
        if form.is_valid():
            classes = form.save()
            messages.success(request, 'Successfully added new Class!')
            return redirect(reverse('classes'))
        else:
            messages.error(request, 'Failed to add a class. Please ensure the form is valid')
    else:
        form = ClassesForm()

    template = 'classes/add_classes.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_classes(request, classes_id):
    """Edit a Class details"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    classes = get_object_or_404(Classes, pk=classes_id)
    if request.method == 'POST':
        form = ClassesForm(request.POST, request.FILES, instance=classes)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated the class')
            return redirect('classes')
        else:
            messages.error(request, 'Failed to update class. Please ensure the form is valid.')
    else:
        form = ClassesForm(instance=classes)
        messages.info(request, f'You are editing class for {classes.leader_name}')

    template = 'classes/edit_classes.html'
    context = {
        'form': form,
        'classes': classes,
    }

    return render(request, template, context)


@login_required
def delete_classes(request, classes_id):
    """Delete classs"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    classes = get_object_or_404(Classes, pk=classes_id)
    if request.method == 'POST':
        classes.delete()
        messages.success(request, f'Class {classes.leader_name} has been deleted!')
        return redirect(reverse('classes'))

    template = 'classes/delete_classes.html'
    context = {
        'classes': classes,
    }

    return render(request, template, context)
