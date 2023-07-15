from django import forms
from .models import Trabajadore, Evento, ReservasMesa, Blog, EditPerfil
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User



# Importo las tablas de models.py con sus atributos a forms.py

class trabajadorFormularios(forms.ModelForm):
    class Meta:
        model = Trabajadore
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'formInput'}),
            'apellido': forms.TextInput(attrs={'class': 'formInput'}),
            'sector': forms.TextInput(attrs={'class': 'formInput'}),
            'telefono': forms.TextInput(attrs={'class': 'formInput'}),
            'email': forms.EmailInput(attrs={'class': 'formInput'}),
            'fechaContratacion': forms.DateInput(attrs={'class': 'formInput'}),
            'salario': forms.NumberInput(attrs={'class': 'formInput'}),
            'foto_id': forms.FileInput(attrs={'class': 'formInput'}),
            'anotaciones': forms.Textarea(attrs={'rows': 2, 'cols': 25}),
        }


class reservacionFormularios(forms.ModelForm):
    class Meta:
        model = ReservasMesa
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'formInput'}),
            'apellido': forms.TextInput(attrs={'class': 'formInput'}),
            'fechaSolicitud': forms.DateInput(attrs={'class': 'formInput'}),
            'fechaReserva': forms.DateInput(attrs={'class': 'formInput'}),
            'horaReserva': forms.TimeInput(attrs={'class': 'formInput'}),
            'numeroPersonas': forms.NumberInput(attrs={'class': 'formInput'}),
            'telefono': forms.TextInput(attrs={'class': 'formInput'}),
            'email': forms.EmailInput(attrs={'class': 'formInput'}),
            'estado': forms.CheckboxInput(attrs={'class': 'formInput'}),
            'anotaciones': forms.Textarea(attrs={'rows': 2, 'cols': 25}),
        }

class eventoFormularios(forms.ModelForm):
    class Meta:
        model = Evento
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'formInput'}),
            'apellido': forms.TextInput(attrs={'class': 'formInput'}),
            'tipoEvento': forms.TextInput(attrs={'class': 'formInput'}),
            'privado': forms.CheckboxInput(attrs={'class': 'formInput'}),
            'fechaSolicitud': forms.DateInput(attrs={'class': 'formInput'}),
            'fechaEvento': forms.DateInput(attrs={'class': 'formInput'}),
            'horaEvento': forms.TimeInput(attrs={'class': 'formInput'}),
            'numeroInvitados': forms.NumberInput(attrs={'class': 'formInput'}),
            'telefono': forms.TextInput(attrs={'class': 'formInput'}),
            'email': forms.EmailInput(attrs={'class': 'formInput'}),
            'duracion': forms.TextInput(attrs={'class': 'formInput'}),
            'costo': forms.TextInput(attrs={'class': 'formInput'}),
            'estado': forms.CheckboxInput(attrs={'class': 'formInput'}),
            'anotaciones': forms.Textarea(attrs={'rows': 2, 'cols': 25}),
        }

class UserEditForm(UserChangeForm):
    # sector = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'formInput'}))
    # telefono = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'formInput'}))
    # fecha_contratacion = forms.DateField(widget=forms.DateInput(attrs={'class': 'formInput'}))
    # redes = forms.URLField(widget=forms.URLInput())
    # descripcion = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 25}))

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]



class EditPerfilForm(forms.ModelForm):
    class Meta:
        model = EditPerfil
        fields = ["sector", "telefono", "fecha_contratacion", "redes", "descripcion"]


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label="", widget=forms.PasswordInput(attrs={"placeholder": "Old password"}))
    new_password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={"placeholder": "New password"}))
    new_password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={"placeholder": "Confirmation new password"}))

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
        help_texts = {k: "" for k in fields}


class AvatarForm(forms.Form):
    avatar = forms.ImageField()


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['titulo', 'subtitulo', 'cuerpo', 'imagen', 'video', 'archivo_pdf']
        exclude = ['autor']
        widgets = {
            'cuerpo': forms.Textarea(attrs={'style': 'height: 274px; width: 1200px;'})
        }
