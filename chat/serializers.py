from rest_framework import serializers
from .models import Room, Participant, SessionLog

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'code', 'name', 'created_at']


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ['id', 'room', 'username', 'role', 'joined_at']


class SessionLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = SessionLog
        fields = ['id', 'participant', 'start_time', 'end_time', 'duration']
