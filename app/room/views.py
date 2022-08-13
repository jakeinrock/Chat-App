"""
Views for room app.
"""
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from core.models import Room


@login_required
def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'core/rooms.html', {'rooms': rooms})
