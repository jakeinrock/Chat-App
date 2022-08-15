"""
Views for room app.
"""
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from core.models import Room, Message
from core.forms import CreateRoomForm


@login_required
def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'core/rooms.html', {'rooms': rooms})


@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:50]

    return render(request, 'core/room.html', {
        'room': room,
        'messages': messages
        }
    )


@login_required
def createroom(request):
    if request.method == 'POST':
        form = CreateRoomForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('rooms')
    else:
        form = CreateRoomForm()

    return render(request, 'core/createroom.html', {'form': form})
