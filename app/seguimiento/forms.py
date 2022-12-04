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
        fields = ['empresa']

        labels = {
            'empresa': 'Empresa',

        }

        widgets = {
            'empresa': forms.Select(attrs={'class': 'form-control'}),
        }


class FrmEncuesta_Laboral(forms.ModelForm):
    class Meta:
        model = Encuesta_Laboral
        fields = ['fecha_pub', 'oferta_laboral']

        labels = {
            'fecha_pub': 'Fecha de encuenta',
            'oferta_laboral': 'Selecione la oferta laboral',
        }

        widgets = {
            'fecha_pub': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'date'}),
            'oferta_laboral': forms.Select(attrs={'class': 'form-control'}),
        }


class FrmPregunta(forms.ModelForm):
    class Meta:
        model = Pregunta
        fields = ['texto_pregunta']

        labels = {
            'texto_pregunta': 'Texto de la pregunta',

        }

        widgets = {
            'texto_pregunta': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'pregunta aqui'}),
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
            'texto_eleccion': forms.TextInput(attrs={'class': 'form-control'}),
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
            'estudiante': forms.Select(attrs={'class': 'form-control'}),
        }


class FrmLogros_Personales(forms.ModelForm):
    class Meta:
        model = Logros_Personales
        fields = ['tipo_logro', 'descripcion']

        labels = {
            'tipo_logro': 'Tipo de logro',
            'descripcion': 'Descripcion',
          

        }

        widgets = {
            'tipo_logro': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
           
        }


class FrmPreferencias_Laborales(forms.ModelForm):
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


class FrmCapacitaciones(forms.ModelForm):
    class Meta:
        model = Capacitaciones
        fields = ['institucion',
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
            'tipo_de_evento': forms.TextInput(attrs={'class': 'form-control'}),
            'area_de_estudio': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_de_evento': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_de_certificado': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_desde': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_hasta': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'dias': forms.NumberInput(attrs={'class': 'form-control'}),
            'horas': forms.NumberInput(attrs={'class': 'form-control'}),
           
        }


class FrmExperiencia_Laboral(forms.ModelForm):
    class Meta:
        model = Experiencia_Laboral
        fields = ['institucion',
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
            'actividades': 'actividades',
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


class FrmInstruccion_formal(forms.ModelForm):
    class Meta:
        model = Instruccion_formal
        fields = ['nivel_de_instruccion',
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


class FrmReferencias_Personales(forms.ModelForm):
    class Meta:
        model = Referencias_Personales
        fields = ['nombres',
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