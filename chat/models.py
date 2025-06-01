from django.db import models
import uuid
class ChatParticipantRoleChoices(models.TextChoices):
    HOST = 'host', 'Host'
    GUEST = 'guest', 'Guest'
class Room(models.Model):
    code = models.CharField(max_length=8, unique=True, default=uuid.uuid4().hex[:8].upper())
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Participant(models.Model):
    ROLE_CHOICES = [
        ('HOST', 'Host'),
        ('GUEST', 'Guest'),
    ]
    room = models.ForeignKey(Room, related_name="participants", on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    role = models.CharField(max_length=5, choices=ChatParticipantRoleChoices.choices,
        default=ChatParticipantRoleChoices.GUEST)
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('room', 'username')  # Un participant ne peut pas avoir le même nom dans une salle

    def __str__(self):
        return f"{self.username} ({self.role}) in {self.room.name}"


class SessionLog(models.Model):
    participant = models.ForeignKey(Participant, related_name="session_logs", on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)

    def __str__(self):
        return f"SessionLog for {self.participant.username} in {self.participant.room.name}"
