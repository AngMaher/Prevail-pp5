from django.shortcuts import render, redirect, reverse, get_object_or_404
from classes.models import Classes
from classes.views import class_detail
from .forms import MembershipForm
from django.contrib import messages
from django.template.loader import render_to_string
from django.conf import settings
from .models import Membership


def membership(request):
    """A view to return the index page"""

    counties = Classes.objects.all()
    template = 'membership/membership.html'

    return render(request, template, {'counties': counties})


def class_register(request):
    """ Register for a class """
    form_class = MembershipForm

    form = form_class(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully registered for class! \
                    - An Email will be sent with your details.')
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Failed to register for \
                 class. Please ensure the form is valid')
    else:
        form = MembershipForm()

    template = 'membership/class_register.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
