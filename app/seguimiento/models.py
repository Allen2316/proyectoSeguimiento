from django.db import models
import calendar
from django.contrib.auth.models import User

# Create your models here.


class Empresa(models.Model):
    id_empresa = models.AutoField(primary_key=True)
    direccion = models.CharField(max_length=50, null=False)
    ubicacion = models.CharField(max_length=100, null=False)
    contacto = models.CharField(max_length=50, null=False)
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name


class Informacion_laboral(models.Model):
    id_informacion_oferta_laboral = models.AutoField(primary_key=True)
    cargo_ocupar = models.CharField(max_length=50, null=False)
    remuneracion_economica = models.DecimalField(
        max_digits=8, decimal_places=2, null=False)
    actividades_desempenar = models.TextField(max_length=50, null=False)
    ciudad = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.cargo_ocupar


class Carrera(models.Model):
    lista_estado = (
        ('R', 'Rediseño'),
        ('S', 'Suspendida'),
        ('E', 'Ejecutandose')
    )

    lista_tipo = (
        ('T', 'Tecnico'),
        ('P', 'Profesional'),
        ('M', 'Medicina Humana'),
    )
    id_carrera = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=False)
    estado = models.CharField(max_length=30, choices=lista_estado, null=False)
    carrera_necesitada = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.nombre


class Encuesta_Laboral(models.Model):
    id_encuesta_laboral = models.AutoField(primary_key=True)
    fecha_pub = models.DateField('Fecha de publicación')

    def __str__(self):
        return 'Encuesta de %s' % str(self.fecha_pub)


class Oferta_Laboral(models.Model):
    id_oferta_laboral = models.AutoField(primary_key=True)

    informacion_laboral = models.ForeignKey(
        Informacion_laboral,
        on_delete=models.CASCADE,
    )

    empresa = models.ForeignKey(
        Empresa,
        on_delete=models.CASCADE,
    )

    encuesta = models.ForeignKey(
        Encuesta_Laboral,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="encuesta"
    )

    carrera = models.ForeignKey(
        Carrera, related_name="carrera", on_delete=models.CASCADE)

    def __str__(self):
        return '%s || %s en la empresa "%s"' % (self.carrera,self.informacion_laboral,
                                          self.empresa)


class Estudiante(models.Model):
    lista_estado = (
        ('E', 'Estudiante Egresado'),
        ('G', 'Estudiante Graduado')
    )
    id_estudiante = models.AutoField(primary_key=True)
    cedula = models.CharField(max_length=10, null=False, unique=True)
    telefono = models.CharField(max_length=10, unique=True)
    estado = models.CharField(max_length=20, choices=lista_estado, null=False)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, null=False)
    oferta = models.ManyToManyField(Oferta_Laboral, blank=True)
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)


class Pregunta(models.Model):
    id_pregunta = models.AutoField(primary_key=True)
    texto_pregunta = models.CharField(max_length=300)
    encuesta_laboral = models.ForeignKey(
        Encuesta_Laboral, on_delete=models.CASCADE)

    def __str__(self):
        return self.texto_pregunta


class Eleccion(models.Model):
    id_eleccion = models.AutoField(primary_key=True)
    texto_eleccion = models.IntegerField(null=False)
    votos = models.IntegerField(null=False, default=0)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return str(self.texto_eleccion)


class Periodo_Academico(models.Model):
    id_periodo_academico = models.AutoField(primary_key=True)
    fecha_inicio = models.DateTimeField('Fecha Incio', null=False)
    fecha_fin = models.DateTimeField('Fecha Fin', null=False)

    def __str__(self):

        return '%s, %s - %s, %s' % (calendar.month_name[self.fecha_inicio.month], self.fecha_inicio.year, calendar.month_name[self.fecha_fin.month], self.fecha_fin.year)


class Mejor_Graduado(models.Model):
    id_mejor_graduado = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(
        Estudiante,
        on_delete=models.CASCADE,
    )

    periodo_academico = models.ForeignKey(
        Periodo_Academico,
        on_delete=models.CASCADE,
    )
    nota_Grado = models.DecimalField(
        max_digits=5, decimal_places=2, null=False)

    def __str__(self):
        return str(self.id_mejor_graduado)


class Hoja_de_vida(models.Model):
    id_hoja_de_vida = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(
        Estudiante,
        on_delete=models.CASCADE, related_name='estudiante'
    )

    def __str__(self):
        return 'Hoja de vida %s' % str(self.id_hoja_de_vida)


class Logros_Personales(models.Model):
    id_logros_personales = models.AutoField(primary_key=True)
    hoja_de_vida = models.ForeignKey(
        Hoja_de_vida,
        on_delete=models.CASCADE,
        related_name='hojaLP'
    )
    tipo_logro = models.CharField(max_length=50, null=False)
    descripcion = models.TextField(max_length=100, null=False)

    def __str__(self):
        return str(self.id_logros_personales)


class Preferencias_Laborales(models.Model):
    id_preferencias_laborales = models.AutoField(primary_key=True)
    hoja_de_vida = models.ForeignKey(
        Hoja_de_vida,
        on_delete=models.CASCADE,
        related_name='hoja',
    )
    sector = models.CharField(max_length=100, null=False)
    aspiracion_salarial = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.sector


class Capacitaciones(models.Model):
    lista_tipoEv = (
        ('COF', 'Conferencia'),
        ('TA', 'Taller'),
        ('SE', 'Seminario'),
        ('CO', 'Congreso'),
        ('PA', 'Pasantia')
    )

    lista_tipoCer = (
        ('A', 'Aprobacion'),
        ('NA', 'Asistencia'),
        ('PA', 'Participacion')
    )

    id_capacitaciones = models.AutoField(primary_key=True)
    hoja_de_vida = models.ForeignKey(
        Hoja_de_vida,
        on_delete=models.CASCADE,
        related_name='hojaCap'
    )
    institucion = models.CharField(max_length=100, null=False)
    tipo_de_evento = models.CharField(
        max_length=50, choices=lista_tipoEv, null=False)
    area_de_estudio = models.CharField(max_length=100, null=False)
    nombre_de_evento = models.CharField(max_length=100, null=False)
    tipo_de_certificado = models.CharField(
        max_length=50, choices=lista_tipoCer, null=False)
    fecha_desde = models.DateField(null=False)
    fecha_hasta = models.DateField(null=False)
    dias = models.CharField(max_length=10, null=False)
    horas = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.nombre_de_evento


class Experiencia_Laboral(models.Model):
    lista_eleccion = (
        (False, 'No'),
        (True, 'Si'),
    )
    id_experiencia_laboral = models.AutoField(primary_key=True)
    hoja_de_vida = models.ForeignKey(
        Hoja_de_vida,
        on_delete=models.CASCADE,
        related_name='hojaEL'
    )
    institucion = models.CharField(max_length=100, null=False)
    tipo_de_institucion = models.CharField(max_length=100, null=False)
    area_de_trabajo = models.CharField(max_length=100, null=False)
    puesto = models.CharField(max_length=100, null=False)
    actividades = models.CharField(max_length=100, null=False)
    fecha_desde = models.DateField("Desde", null=False)
    fecha_hasta = models.DateField("Hasta", null=False)
    trabaja_actualmente_en_este_lugar = models.BooleanField(
        choices=lista_eleccion, default=False)

    def __str__(self):
        return self.puesto


class Instruccion_formal(models.Model):
    id_instruccion_formal = models.AutoField(primary_key=True)
    hoja_de_vida = models.ForeignKey(
        Hoja_de_vida,
        on_delete=models.CASCADE,
        related_name='hojaIF',
    )
    nivel_de_instruccion = models.CharField(max_length=100, null=False)
    instruccion_educativa = models.CharField(max_length=100, null=False)
    titulo_obtenido = models.CharField(max_length=100, null=False)
    no_del_registro_senescyt = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.titulo_obtenido


class Referencias_Personales(models.Model):
    id_referencias_personales = models.AutoField(primary_key=True)
    hoja_de_vida = models.ForeignKey(
        Hoja_de_vida,
        on_delete=models.CASCADE,
        related_name='hojaRP'
    )
    nombres = models.CharField(max_length=100, null=False)
    telefono = models.IntegerField(null=False)
    correo = models.EmailField(max_length=100, unique=True, null=False)

    def __str__(self):
        return self.nombres
