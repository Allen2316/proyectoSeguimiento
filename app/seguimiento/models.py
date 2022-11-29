from django.db import models

# Create your models here.


class Empresa(models.Model):
    id_empresa = models.AutoField(primary_key=True)
    nombre_empresa = models.CharField(max_length=50, null=False)
    direccion = models.CharField(max_length=50, null=False)
    ubicacion = models.CharField(max_length=100, null=False)
    contacto = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.nombre_empresa


class Informacion_laboral(models.Model):
    id_informacion_oferta_laboral = models.AutoField(primary_key=True)
    cargo_ocupar = models.CharField(max_length=50, null=False)
    remuneracion_economica = models.IntegerField(null=False)
    actividades_desempenar = models.TextField(max_length=50, null=False)
    ciudad = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.cargo_ocupar


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

    def __str__(self):
        return '%s en la empresa "%s"' % (self.informacion_laboral.cargo_ocupar,
                                          self.empresa.nombre_empresa)


class Encuesta_Laboral(models.Model):
    id_encuesta_laboral = models.AutoField(primary_key=True)
    fecha_pub = models.DateField('Fecha de publicación')
    oferta_laboral = models.ForeignKey(
        Oferta_Laboral,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return 'Encuesta para la oferta laboral "%s"' % (self.oferta_laboral)


class Pregunta(models.Model):
    id_pregunta = models.AutoField(primary_key=True)
    texto_pregunta = models.CharField(max_length=300)
    encuesta_laboral = models.ForeignKey(
        Encuesta_Laboral, on_delete=models.CASCADE)

    def __str__(self):
        return self.texto_pregunta


class Eleccion(models.Model):
    lista_eleccion = (
        (1, 'Muy Malo'),
        (2, 'Malo'),
        (3, 'Bueno'),
        (4, 'Muy Bueno'),
        (5, 'Excelente')
    )
    id_eleccion = models.AutoField(primary_key=True)
    texto_eleccion = models.IntegerField(max_length=1, choices=lista_eleccion, null=False)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    

    def __str__(self):
        return str(self.texto_eleccion)


class Carrera(models.Model):
    lista_estado = (
        ('R', 'Rediseño'),
        ('S', 'Suspendida'),
        ('E', 'Ejecutandose')
    )
    id_carrera = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=False)
    estado = models.CharField(max_length=20, choices=lista_estado, null=False)

    def __str__(self):
        return self.nombre


class Estudiante(models.Model):
    lista_estado = (
        ('E', 'Estudiante Egresado'),
        ('G', 'Estudiante Graduado')
    )
    id_estudiante = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=50, null=False)
    apellidos = models.CharField(max_length=50, null=False)
    telefono = models.CharField(max_length=10, unique=True)
    estado = models.CharField(max_length=20, choices=lista_estado, null=False)
    carrera = models.ForeignKey(
        Carrera,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return '%s %s' % (self.nombres, self.apellidos)


class Cuenta(models.Model):
    id_cuenta = models.AutoField(primary_key=True)

    estudiante = models.ForeignKey(
        Estudiante,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return str(self.id_cuenta)


class Periodo_Academico(models.Model):
    id_periodo_academico = models.AutoField(primary_key=True)
    fecha_incio = models.DateTimeField('Fecha Incio', null=False)
    fecha_fin = models.DateTimeField('Fecha Fin', null=False)

    def __str__(self):
        return str(self.id_periodo_academico)


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
    nota_Grado = models.IntegerField(null=False)

    def __str__(self):
        return str(self.id_mejor_graduado)


class Hoja_de_vida(models.Model):
    id_hoja_de_vida = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(
        Estudiante,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return str(self.id_hoja_de_vida)


class Logros_Personales(models.Model):
    id_logros_personales = models.AutoField(primary_key=True)
    hoja_de_vida = models.ForeignKey(
        Hoja_de_vida,
        on_delete=models.CASCADE,
    )
    tipo_logro = models.CharField(max_length=50, null=False)
    descripcion = models.TextField(max_length=50, null=False)

    def __str__(self):
        return str(self.id_logros_personales)


class Preferencias_Laborales(models.Model):
    id_preferencias_laborales = models.AutoField(primary_key=True)
    hoja_de_vida = models.ForeignKey(
        Hoja_de_vida,
        on_delete=models.CASCADE,
    )
    sector = models.CharField(max_length=10, null=False)
    aspiracion_salarial = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.sector


class Capacitaciones(models.Model):
    id_capacitaciones = models.AutoField(primary_key=True)
    hoja_de_vida = models.ForeignKey(
        Hoja_de_vida,
        on_delete=models.CASCADE,
    )
    institucion = models.CharField(max_length=10, null=False)
    tipo_de_evento = models.CharField(max_length=10, null=False)
    area_de_estudio = models.CharField(max_length=10, null=False)
    nombre_de_evento = models.CharField(max_length=10, null=False)
    tipo_de_certificado = models.CharField(max_length=10, null=False)
    fecha_desde = models.DateField(null=False)
    fecha_hasta = models.DateField(null=False)
    dias = models.CharField(max_length=10, null=False)
    horas = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.nombre_de_evento


class Experiencia_Laboral(models.Model):
    id_experiencia_laboral = models.AutoField(primary_key=True)
    hoja_de_vida = models.ForeignKey(
        Hoja_de_vida,
        on_delete=models.CASCADE,
    )
    institucion = models.CharField(max_length=10, null=False)
    tipo_de_institucion = models.CharField(max_length=10, null=False)
    area_de_trabajo = models.CharField(max_length=10, null=False)
    puesto = models.CharField(max_length=10, null=False)
    actividades = models.CharField(max_length=10, null=False)
    fecha_desde = models.DateField("Desde", null=False)
    fecha_hasta = models.DateField("Hasta", null=False)
    trabaja_actualmente_en_este_lugar = models.BooleanField(default=False)

    def __str__(self):
        return self.puesto


class Instruccion_formal(models.Model):
    id_instruccion_laboral = models.AutoField(primary_key=True)
    hoja_de_vida = models.ForeignKey(
        Hoja_de_vida,
        on_delete=models.CASCADE,
    )
    nivel_de_instruccion = models.CharField(max_length=10, null=False)
    instruccion_educativa = models.CharField(max_length=10, null=False)
    titulo_obtenido = models.CharField(max_length=10, null=False)
    no_del_registro_senescyt = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.titulo_obtenido


class Referencias_Personales(models.Model):
    id_referencias_personales = models.AutoField(primary_key=True)
    hoja_de_vida = models.ForeignKey(
        Hoja_de_vida,
        on_delete=models.CASCADE,
    )
    nombres = models.CharField(max_length=10, null=False)
    telefono = models.IntegerField(null=False)
    correo = models.EmailField(max_length=50, unique=True, null=False)

    def __str__(self):
        return self.nombres
