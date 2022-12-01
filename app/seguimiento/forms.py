from django import forms
from django.views.generic.edit import UpdateView
from app.seguimiento.models import Carrera, Estudiante, Periodo_Academico, Empresa, Informacion_laboral, Oferta_Laboral, Encuesta_Laboral, Pregunta, Eleccion, Cuenta,  Mejor_Graduado, Hoja_de_vida, Logros_Personales, Preferencias_Laborales, Capacitaciones, Experiencia_Laboral, Instruccion_formal, Referencias_Personales


class FrmCarrera(forms.ModelForm):
    class Meta:
        model = Carrera
        fields = ['nombre', 'estado']

        labels = {
            'nombre': 'Nombre de la Carera',
            'estado': 'Esado de la Carrera',

        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Desarrollo de Software'}),
            'estado': forms.Select(attrs={'class': 'form-control'})
        }


class FrmEstudiante(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombres', 'apellidos', 'telefono', 'estado', 'carrera']

        labels = {
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'telefono': 'Telefono',
            'estado': 'Estado',
            'carrera': 'Carrera',

        }

        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Juan'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Perez'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '098989897'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'carrera': forms.Select(attrs={'class': 'form-control'}),
        }


class FrmPeriodo_Academico(forms.ModelForm):
    class Meta:
        model = Periodo_Academico
        fields = ['fecha_inicio', 'fecha_fin']

        labels = {
            'fecha_inicio': 'Fecha Inicio',
            'fecha_fin': 'Fecha Fin',
        }

        widgets = {
            'fecha_inicio': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'date'}, ),
            'fecha_fin': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


class FrmMejor_Graduado(forms.ModelForm):
    class Meta:
        model = Mejor_Graduado
        fields = ['nota_Grado', 'estudiante', 'periodo_academico']

        labels = {
            'nota_Grado': 'Nota Grado',
            'estudiante': 'Estudiante',
            'periodo_academico': 'Periodo Academico',

        }

        widgets = {
            'nota_Grado': forms.NumberInput(attrs={'class': 'form-control'}),
            'estudiante': forms.Select(attrs={'class': 'form-control'}),
            'periodo_academico': forms.Select(attrs={'class': 'form-control'}),
        }


class FrmEmpresa(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['nombre_empresa', 'direccion', 'ubicacion', 'contacto']

        labels = {
            'nombre_empresa': 'Nombre',
            'direccion': 'Direccion',
            'ubicacion': 'Ubicacion',
            'contacto': 'Contacto'

        }

        widgets = {
            'nombre_empresa': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Empresa Ejemplo'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Av. Cuxibamba'}),
            'ubicacion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Loja'}),
            'contacto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '098989897'}),
        }


class FrmInformacion_laboral(forms.ModelForm):
    class Meta:
        model = Informacion_laboral
        fields = ['cargo_ocupar', 'remuneracion_economica',
                  'actividades_desempenar', 'ciudad']

        labels = {
            'cargo_ocupar': 'Cargo Ocupar',
            'remuneracion_economica': 'Remuneracion Economica',
            'actividades_desempenar': 'Actividades a Desempenar',
            'ciudad': 'Ciudad'

        }

        widgets = {
            'cargo_ocupar': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Desarrollador'}),
            'remuneracion_economica': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '520'}),
            'actividades_desempenar': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Programar aplicaciones'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Loja'}),
        }


class FrmOferta_Laboral(forms.ModelForm):
    class Meta:
        model = Oferta_Laboral
        fields = [ 'empresa']

        labels = {            
            'empresa': 'Empresa',

        }

        widgets = {            
            'empresa': forms.Select(attrs={'class': 'form-control'}),
        }
