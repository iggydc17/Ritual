from django import forms
from .models import Mensaje, Conversacion


class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['contenido']
        widgets = {
            'contenido': forms.TextInput(attrs={
                'class': 'message-input',
                'style': 'width: 90%; padding: 8px; border: 1px solid black; border-radius: 5px; outline: none;'
            })
        }

class ConversacionForm(forms.ModelForm):
    class Meta:
        model = Conversacion
        fields = ['emisor','receptor']