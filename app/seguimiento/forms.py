from django import forms
from django.views.generic.edit import UpdateView
from app.seguimiento.models import Empresa, Informacion_laboral, Oferta_Laboral, Encuesta_Laboral, Pregunta, Eleccion, Carrera, Estudiante, Cuenta, Periodo_Academico, Mejor_Graduado, Hoja_de_vida, Logros_Personales, Preferencias_Laborales, Capacitaciones, Experiencia_Laboral, Instruccion_formal, Referencias_Personales


class FrmCarrera(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'estado']

        labels = {
            'nombre': 'Nombre de la Carera',            
            'estado': 'Esado de la Carrera',

        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Juan'}),
            'es': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Perez'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '098989897'}),'estado':forms.Select(attrs={'class':'form-control'})            
        }

class FrmEstudiante(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apelido', 'telefono', 'estado', 'carrera']

        labels = {
            'nombre': 'Nombres',
            'apellido': 'Apellidos',
            'telefono': 'Telefono',
            'estado': 'Estado',
            'carrera': 'Carrera',

        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Juan'}),            'estado':forms.Select(attrs={'class':'form-control'})            
        }
