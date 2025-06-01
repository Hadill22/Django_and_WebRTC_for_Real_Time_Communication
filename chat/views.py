from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Room, Participant, SessionLog
from .serializers import RoomSerializer, ParticipantSerializer, SessionLogSerializer
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RoomForm, JoinRoomForm

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated]


class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
    permission_classes = [IsAuthenticated]

class SessionLogViewSet(viewsets.ModelViewSet):
    queryset = SessionLog.objects.all()
    serializer_class = SessionLogSerializer
    permission_classes = [IsAuthenticated]


def create_room(request):
    room = None
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save()
    else:
        form = RoomForm()
    return render(request, 'chat/room.html', {'form': form, 'room': room})



def join_room(request):
    room = None
    if request.method == 'POST':
        form = JoinRoomForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            room = Room.objects.filter(code=code).first()
            if room:
              return redirect('chat_room', room_id=room.code)
            else:
                form.add_error('code', "Aucune Room trouvée avec ce code.")
    else:
        form = JoinRoomForm()

    return render(request, 'chat/join_room.html', {'form': form})



def chat_room(request, room_id):
    room = get_object_or_404(Room, code=room_id)
    return render(request, 'chat/chat_room.html', {'room': room})

