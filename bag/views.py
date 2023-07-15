from django.shortcuts import render


def view_bag(request):
    """Add view to return the bag page"""
    return render(request, 'bag/bag.html')