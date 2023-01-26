from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.admin.widgets import AutocompleteSelect
from django.contrib import admin
from django.views.generic.edit import UpdateView
from app.seguimiento.models import Carrera, Estudiante, Periodo_Academico, Empresa, Informacion_laboral, Oferta_Laboral, Encuesta_Laboral, Pregunta, Eleccion,  Mejor_Graduado, Hoja_de_vida, Logros_Personales, Preferencias_Laborales, Capacitaciones, Experiencia_Laboral, Instruccion_formal, Referencias_Personales
from django.contrib.auth.models import User


class FrmLogin(forms.Form):

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}), label='Usuario')
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control'}), label='Contraseña')


class FrmUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username']

        labels = {
            'first_name': 'Nombres',
            'last_name': 'Apellidos',
            'username': 'Usuario',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }


class FrmUserEd(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username']

        labels = {
            'first_name': 'Nombres',
            'last_name': 'Apellidos',
            'username': 'Usuario',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }


class FrmUserEmp(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'username']

        labels = {
            'first_name': 'Nombre de Empresa',
            'username': 'Usuario',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }


class FrmUserEmpEd(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'username']

        labels = {
            'first_name': 'Nombre de Empresa',
            'username': 'Usuario',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }


class FrmCarrera(forms.ModelForm):
    class Meta:
        model = Carrera
        fields = ['nombre', 'estado']

        labels = {
            'nombre': 'Nombre de la carrera',
            'estado': 'Estado de la carrera',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
        }


class FrmEstudiante(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['telefono',
                  'cedula',
                  'estado',
                  'carrera']

        labels = {
            'cedula': 'Cedula',
            'telefono': 'Telefono',
            'estado': 'Estado',
            'carrera': 'Carrera',
        }

        widgets = {
            'cedula': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'autofocus':True}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'carrera': forms.Select(attrs={'class': 'form-control'}),
        }


class FrmEstudianteUpdate(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['telefono',
                  'cedula',
                  'estado',
                  'carrera',
                  'oferta']

        labels = {
            'telefono': 'Telefono',
            'cedula': 'Cedula',
            'estado': 'Estado',
            'carrera': 'Carrera',
            'oferta': 'Oferta Laboral',
        }

        widgets = {
            'cedula': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'carrera': forms.Select(attrs={'class': 'form-control'}),
            'oferta': forms.CheckboxSelectMultiple(attrs={'class': 'form-group'}),
        }

    """ def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['oferta'].queryset = user.userE.carrera.filter() """


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
        fields = ['estudiante', 'nota_Grado', 'periodo_academico']

        labels = {
            'estudiante': 'Estudiante',
            'nota_Grado': 'Nota de grado',
            'periodo_academico': 'Periodo Academico',
        }

        widgets = {
            'estudiante': forms.Select(attrs={'class': 'form-control'}),
            'nota_Grado': forms.NumberInput(attrs={'class': 'form-control'}),
            'periodo_academico': forms.Select(attrs={'class': 'form-control'}),
        }


class FrmEmpresa(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['direccion', 'ubicacion', 'contacto']

        labels = {
            'ubicacion': 'Ubicacion',
            'contacto': 'Contacto'

        }

        widgets = {
            'direccion': forms.TextInput(attrs={'class': 'form-control','autofocus':True}),
            'ubicacion': forms.TextInput(attrs={'class': 'form-control'}),
            'contacto': forms.TextInput(attrs={'class': 'form-control'}),
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
            'cargo_ocupar': forms.TextInput(attrs={'class': 'form-control'}),
            'remuneracion_economica': forms.NumberInput(attrs={'class': 'form-control'}),
            'actividades_desempenar': forms.TextInput(attrs={'class': 'form-control'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
        }


class FrmOferta_Laboral(forms.ModelForm):
    class Meta:
        model = Oferta_Laboral
        fields = ['empresa', 'encuesta', 'carrera']

        labels = {
            'empresa': 'Empresa',
            'encuesta': 'Encuesta',
            'carrera': 'Carrera'
        }

        widgets = {
            'empresa': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'encuesta': forms.Select(attrs={'class': 'form-control'}),
            'carrera': forms.Select(attrs={'class': 'form-group'}),

        }

    def __init__(self, *args, **kwargs):
        super(FrmOferta_Laboral, self).__init__(*args, **kwargs)
        self.fields['empresa'].widget.attrs['readonly'] = True


class FrmOferta_LaboralAdmin(forms.ModelForm):
    class Meta:
        model = Oferta_Laboral
        fields = ['empresa', 'encuesta', 'carrera']

        labels = {
            'empresa': 'Empresa',
            'encuesta': 'Encuesta',
            'carrera': 'Carrera',

        }

        widgets = {
            'empresa': AutocompleteSelect(Oferta_Laboral._meta.get_field('empresa'), admin.site,
                                          attrs={'class': 'form-control', 'placeholder': 'Selecione'}),
            'encuesta': forms.Select(attrs={'class': 'form-control'}),
            'carrera': forms.Select(attrs={'class': 'form-group'}),
        }


class FrmEncuesta_Laboral(forms.ModelForm):
    class Meta:
        model = Encuesta_Laboral
        fields = ['fecha_pub']

        labels = {
            'fecha_pub': 'Fecha de encuenta',
        }

        widgets = {
            'fecha_pub': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


class FrmPregunta(forms.ModelForm):
    class Meta:
        model = Pregunta
        fields = ['texto_pregunta']

        labels = {
            'texto_pregunta': 'Texto de la pregunta',

        }

        widgets = {
            'texto_pregunta': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'escriba su pregunta'}),
        }


class FrmEleccion(forms.ModelForm):
    class Meta:
        model = Eleccion
        fields = ['texto_eleccion', 'pregunta']

        labels = {
            'texto_eleccion': 'Eliga su respuesta',
            'pregunta': 'Seleccione a que pregunta es',

        }

        widgets = {
            'texto_eleccion': forms.RadioSelect(attrs={'class': 'form-check'}),
            'pregunta': forms.Select(attrs={'class': 'form-control'}),
        }


class FrmHoja_de_vida(forms.ModelForm):
    class Meta:
        model = Hoja_de_vida
        fields = ['estudiante']

        labels = {
            'estudiante': 'Estudiante',

        }

        widgets = {
            'estudiante': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }

    def __init__(self, *args, **kwargs):
        super(FrmHoja_de_vida, self).__init__(*args, **kwargs)
        self.fields['estudiante'].widget.attrs['readonly'] = True


class FrmHoja_de_vidaAdmin(forms.ModelForm):
    class Meta:
        model = Hoja_de_vida
        fields = ['estudiante']

        labels = {
            'estudiante': 'Estudiante',

        }

        widgets = {
            'estudiante': AutocompleteSelect(Hoja_de_vida._meta.get_field('estudiante'), admin.site,
                                             attrs={'class': 'form-control', 'placeholder': 'Selecione'}),
        }


class FrmLogros_Personales(forms.ModelForm):
    class Meta:
        model = Logros_Personales
        fields = ['hoja_de_vida', 'tipo_logro', 'descripcion']

        labels = {
            'hoja_de_vida': 'Hoja de vida',
            'tipo_logro': 'Tipo de logro',
            'descripcion': 'Descripcion',


        }

        widgets = {
            'hoja_de_vida': forms.Select(attrs={'class': 'form-control'}),
            'tipo_logro': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),

        }


class FrmPreferencias_Laborales(forms.ModelForm):
    class Meta:
        model = Preferencias_Laborales
        fields = ['hoja_de_vida', 'sector', 'aspiracion_salarial']

        labels = {
            'hoja_de_vida': 'Hoja de vida',
            'sector': 'Sector',
            'aspiracion_salarial': 'Aspiracion Salarial',


        }

        widgets = {
            'hoja_de_vida': forms.Select(attrs={'class': 'form-control'}),
            'sector': forms.TextInput(attrs={'class': 'form-control'}),
            'aspiracion_salarial': forms.TextInput(attrs={'class': 'form-control'}),

        }


class FrmCapacitaciones(forms.ModelForm):
    class Meta:
        model = Capacitaciones
        fields = ['hoja_de_vida',
                  'institucion',
                  'tipo_de_evento',
                  'area_de_estudio',
                  'nombre_de_evento',
                  'tipo_de_certificado',
                  'fecha_desde',
                  'fecha_hasta',
                  'dias',
                  'horas',
                  ]

        labels = {
            'hoja_de_vida': 'Hoja de vida',
            'institucion': 'Institucion',
            'tipo_de_evento': 'Tipo de evento',
            'area_de_estudio': 'Area de estudio',
            'nombre_de_evento': 'Nombre de evento',
            'tipo_de_certificado': 'Tipo de certificado',
            'fecha_desde': 'Fecha desde',
            'fecha_hasta': 'Fecha hasta',
            'dias': 'Total de dias',
            'horas': 'Total de horas',


        }

        widgets = {
            'hoja_de_vida': forms.Select(attrs={'class': 'form-control'}),
            'institucion': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_de_evento': forms.Select(attrs={'class': 'form-control'}),
            'area_de_estudio': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_de_evento': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_de_certificado': forms.Select(attrs={'class': 'form-control'}),
            'fecha_desde': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_hasta': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'dias': forms.NumberInput(attrs={'class': 'form-control'}),
            'horas': forms.NumberInput(attrs={'class': 'form-control'}),

        }


class FrmExperiencia_Laboral(forms.ModelForm):
    class Meta:
        model = Experiencia_Laboral
        fields = ['hoja_de_vida',
                  'institucion',
                  'tipo_de_institucion',
                  'area_de_trabajo',
                  'puesto',
                  'actividades',
                  'fecha_desde',
                  'fecha_hasta',
                  'trabaja_actualmente_en_este_lugar',
                  ]

        labels = {
            'hoja_de_vida': 'Hoja de vida',
            'institucion': 'Institucion',
            'tipo_de_institucion': 'Tipo de Institucion',
            'area_de_trabajo': 'Area de trabajo',
            'puesto': 'Puesto',
            'actividades': 'actividades',
            'fecha_desde': 'Fecha desde',
            'fecha_hasta': 'Fecha hasta',
            'trabaja_actualmente_en_este_lugar': 'Trabaja actualmente en este lugar',


        }

        widgets = {
            'hoja_de_vida': forms.Select(attrs={'class': 'form-control'}),
            'institucion': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_de_institucion': forms.TextInput(attrs={'class': 'form-control'}),
            'area_de_trabajo': forms.TextInput(attrs={'class': 'form-control'}),
            'puesto': forms.TextInput(attrs={'class': 'form-control'}),
            'actividades': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_desde': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_hasta': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'trabaja_actualmente_en_este_lugar': forms.Select(attrs={'class': 'form-control'}),

        }


class FrmInstruccion_formal(forms.ModelForm):
    class Meta:
        model = Instruccion_formal
        fields = ['hoja_de_vida',
                  'nivel_de_instruccion',
                  'instruccion_educativa',
                  'titulo_obtenido',
                  'no_del_registro_senescyt',
                  ]

        labels = {
            'hoja_de_vida': 'Hoja de vida',
            'nivel_de_instruccion': 'Nivel de instruccion',
            'instruccion_educativa': 'Instruccion educativa',
            'titulo_obtenido': 'Titulo obtenido',
            'no_del_registro_senescyt': 'Nro. del registro del senescyt',


        }

        widgets = {
            'hoja_de_vida': forms.Select(attrs={'class': 'form-control'}),
            'nivel_de_instruccion': forms.TextInput(attrs={'class': 'form-control'}),
            'instruccion_educativa': forms.TextInput(attrs={'class': 'form-control'}),
            'titulo_obtenido': forms.TextInput(attrs={'class': 'form-control'}),
            'no_del_registro_senescyt': forms.TextInput(attrs={'class': 'form-control'}),

        }


class FrmReferencias_Personales(forms.ModelForm):
    class Meta:
        model = Referencias_Personales
        fields = ['hoja_de_vida',
                  'nombres',
                  'telefono',
                  'correo',
                  ]

        labels = {
            'hoja_de_vida': 'Hoja de vida',
            'nombres': 'Nombres',
            'telefono': 'Telefono',
            'correo': 'Correo',


        }

        widgets = {
            'hoja_de_vida': forms.Select(attrs={'class': 'form-control'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.TextInput(attrs={'class': 'form-control'}),

        }


# Formularios sin hoja de vida


class FrmLogros_Personales1(forms.ModelForm):
    class Meta:
        model = Logros_Personales
        fields = ['tipo_logro', 'descripcion']

        labels = {
            'hoja_de_vida': 'Hoja de vida',
            'tipo_logro': 'Tipo de logro',
            'descripcion': 'Descripcion',


        }

        widgets = {
            'tipo_logro': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),

        }


class FrmPreferencias_Laborales1(forms.ModelForm):
    class Meta:
        model = Preferencias_Laborales
        fields = ['sector', 'aspiracion_salarial']

        labels = {

            'sector': 'Sector',
            'aspiracion_salarial': 'Aspiracion Salarial',


        }

        widgets = {

            'sector': forms.TextInput(attrs={'class': 'form-control'}),
            'aspiracion_salarial': forms.TextInput(attrs={'class': 'form-control'}),

        }


class FrmCapacitaciones1(forms.ModelForm):
    class Meta:
        model = Capacitaciones
        fields = [
            'institucion',
            'tipo_de_evento',
            'area_de_estudio',
            'nombre_de_evento',
            'tipo_de_certificado',
            'fecha_desde',
            'fecha_hasta',
            'dias',
            'horas',
        ]

        labels = {

            'institucion': 'Institucion',
            'tipo_de_evento': 'Tipo de evento',
            'area_de_estudio': 'Area de estudio',
            'nombre_de_evento': 'Nombre de evento',
            'tipo_de_certificado': 'Tipo de certificado',
            'fecha_desde': 'Fecha desde',
            'fecha_hasta': 'Fecha hasta',
            'dias': 'Total de dias',
            'horas': 'Total de horas',


        }

        widgets = {
            'institucion': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_de_evento': forms.Select(attrs={'class': 'form-control'}),
            'area_de_estudio': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_de_evento': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_de_certificado': forms.Select(attrs={'class': 'form-control'}),
            'fecha_desde': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_hasta': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'dias': forms.NumberInput(attrs={'class': 'form-control'}),
            'horas': forms.NumberInput(attrs={'class': 'form-control'}),

        }


class FrmExperiencia_Laboral1(forms.ModelForm):
    class Meta:
        model = Experiencia_Laboral
        fields = [
            'institucion',
            'tipo_de_institucion',
            'area_de_trabajo',
            'puesto',
            'actividades',
            'fecha_desde',
            'fecha_hasta',
            'trabaja_actualmente_en_este_lugar',
        ]

        labels = {

            'institucion': 'Institucion',
            'tipo_de_institucion': 'Tipo de Institucion',
            'area_de_trabajo': 'Area de trabajo',
            'puesto': 'Puesto',
            'actividades': 'Actividades',
            'fecha_desde': 'Fecha desde',
            'fecha_hasta': 'Fecha hasta',
            'trabaja_actualmente_en_este_lugar': 'Trabaja actualmente en este lugar',


        }

        widgets = {
            'institucion': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_de_institucion': forms.TextInput(attrs={'class': 'form-control'}),
            'area_de_trabajo': forms.TextInput(attrs={'class': 'form-control'}),
            'puesto': forms.TextInput(attrs={'class': 'form-control'}),
            'actividades': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_desde': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_hasta': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'trabaja_actualmente_en_este_lugar': forms.Select(attrs={'class': 'form-control'}),

        }


class FrmInstruccion_formal1(forms.ModelForm):
    class Meta:
        model = Instruccion_formal
        fields = [
            'nivel_de_instruccion',
            'instruccion_educativa',
            'titulo_obtenido',
            'no_del_registro_senescyt',
        ]

        labels = {
            'nivel_de_instruccion': 'Nivel de instruccion',
            'instruccion_educativa': 'Instruccion educativa',
            'titulo_obtenido': 'Titulo obtenido',
            'no_del_registro_senescyt': 'Nro. del registro del senescyt',


        }

        widgets = {
            'nivel_de_instruccion': forms.TextInput(attrs={'class': 'form-control'}),
            'instruccion_educativa': forms.TextInput(attrs={'class': 'form-control'}),
            'titulo_obtenido': forms.TextInput(attrs={'class': 'form-control'}),
            'no_del_registro_senescyt': forms.TextInput(attrs={'class': 'form-control'}),

        }


class FrmReferencias_Personales1(forms.ModelForm):
    class Meta:
        model = Referencias_Personales
        fields = [
            'nombres',
            'telefono',
            'correo',
        ]

        labels = {

            'nombres': 'Nombres',
            'telefono': 'Telefono',
            'correo': 'Correo',


        }

        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.TextInput(attrs={'class': 'form-control'}),

        }
