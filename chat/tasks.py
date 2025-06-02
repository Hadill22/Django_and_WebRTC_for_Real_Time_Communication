import noisereduce as nr
import librosa
import soundfile as sf
import os
from celery import shared_task
from .models import Room
from datetime import timedelta
from django.utils import timezone

@shared_task
def denoise_audio(file_path):
    try:
        # Charger l'audio
        y, sr = librosa.load(file_path, sr=None)

        # Réduire le bruit
        reduced_noise = nr.reduce_noise(y=y, sr=sr)

        # Créer un nouveau fichier avec suffixe
        output_path = file_path.replace(".wav", ".denoised.wav")

        # Sauvegarder le fichier nettoyé
        sf.write(output_path, reduced_noise, sr)

        return f"Fichier nettoyé : {output_path}"
    except Exception as e:
        return f"Erreur traitement audio : {str(e)}"
def delete_inactive_rooms():
    threshold = timezone.now() - timedelta(minutes=30)
    deleted_count, _ = Room.objects.filter(created_at__lt=threshold).delete()
    return f"{deleted_count} rooms supprimées pour inactivité"
