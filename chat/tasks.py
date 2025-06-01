from celery import shared_task
from .models import Room
from datetime import timedelta
from django.utils import timezone

@shared_task
def delete_inactive_rooms():
    threshold = timezone.now() - timedelta(minutes=30)
    deleted_count, _ = Room.objects.filter(created_at__lt=threshold).delete()
    return f"{deleted_count} rooms supprimées pour inactivité"
