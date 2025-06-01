from django import forms
from .models import Room

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name']  # ou ['code'] si le nom n'est pas obligatoire

class JoinRoomForm(forms.Form):
    code = forms.CharField(label="Code de la Room", max_length=50)