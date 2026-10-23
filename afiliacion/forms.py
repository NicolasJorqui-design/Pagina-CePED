from django import forms
from .models import SolicitudAfiliacion

class SolicitudAfiliacionForm(forms.ModelForm):
    class Meta:
        model = SolicitudAfiliacion
        fields = [
            'institucion', 'entidad_propietaria', 'provincia', 'localidad',
            'email', 'telefono', 'responsable_contacto', 'motivo', 'mensaje'
        ]
        widgets = {
            'institucion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la institución'}),
            'entidad_propietaria': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entidad propietaria'}),
            'provincia': forms.TextInput(attrs={'class': 'form-control'}),
            'localidad': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ejemplo@correo.com'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'responsable_contacto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre, Apellido y Cargo'}),
            'motivo': forms.Select(attrs={'class': 'form-select'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }