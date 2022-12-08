# Generated by Django 4.1.3 on 2022-12-08 03:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id_carrera', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('estado', models.CharField(choices=[('R', 'Rediseño'), ('S', 'Suspendida'), ('E', 'Ejecutandose')], max_length=30)),
                ('tipo', models.CharField(choices=[('T', 'Tecnico'), ('P', 'Profesional'), ('M', 'Medicina Humana')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id_empresa', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_empresa', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('ubicacion', models.CharField(max_length=100)),
                ('contacto', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Encuesta_Laboral',
            fields=[
                ('id_encuesta_laboral', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_pub', models.DateField(verbose_name='Fecha de publicación')),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id_estudiante', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=10, unique=True)),
                ('estado', models.CharField(choices=[('E', 'Estudiante Egresado'), ('G', 'Estudiante Graduado')], max_length=20)),
                ('carrera', models.ManyToManyField(to='seguimiento.carrera')),
            ],
        ),
        migrations.CreateModel(
            name='Hoja_de_vida',
            fields=[
                ('id_hoja_de_vida', models.AutoField(primary_key=True, serialize=False)),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seguimiento.estudiante')),
            ],
        ),
        migrations.CreateModel(
            name='Informacion_laboral',
            fields=[
                ('id_informacion_oferta_laboral', models.AutoField(primary_key=True, serialize=False)),
                ('cargo_ocupar', models.CharField(max_length=50)),
                ('remuneracion_economica', models.DecimalField(decimal_places=2, max_digits=6)),
                ('actividades_desempenar', models.TextField(max_length=50)),
                ('ciudad', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Periodo_Academico',
            fields=[
                ('id_periodo_academico', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_inicio', models.DateTimeField(verbose_name='Fecha Incio')),
                ('fecha_fin', models.DateTimeField(verbose_name='Fecha Fin')),
            ],
        ),
        migrations.CreateModel(
            name='Referencias_Personales',
            fields=[
                ('id_referencias_personales', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=100)),
                ('telefono', models.IntegerField()),
                ('correo', models.EmailField(max_length=100, unique=True)),
                ('hoja_de_vida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seguimiento.hoja_de_vida')),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id_pregunta', models.AutoField(primary_key=True, serialize=False)),
                ('texto_pregunta', models.CharField(max_length=300)),
                ('encuesta_laboral', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seguimiento.encuesta_laboral')),
            ],
        ),
        migrations.CreateModel(
            name='Preferencias_Laborales',
            fields=[
                ('id_preferencias_laborales', models.AutoField(primary_key=True, serialize=False)),
                ('sector', models.CharField(max_length=100)),
                ('aspiracion_salarial', models.DecimalField(decimal_places=2, max_digits=6)),
                ('hoja_de_vida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seguimiento.hoja_de_vida')),
            ],
        ),
        migrations.CreateModel(
            name='Oferta_Laboral',
            fields=[
                ('id_oferta_laboral', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(choices=[('T', 'Tecnico'), ('P', 'Profesional'), ('M', 'Medicina Humana')], max_length=20)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seguimiento.empresa')),
                ('encuesta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seguimiento.encuesta_laboral')),
                ('informacion_laboral', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seguimiento.informacion_laboral')),
            ],
        ),
        migrations.CreateModel(
            name='Mejor_Graduado',
            fields=[
                ('id_mejor_graduado', models.AutoField(primary_key=True, serialize=False)),
                ('nota_Grado', models.DecimalField(decimal_places=2, max_digits=5)),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seguimiento.estudiante')),
                ('periodo_academico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seguimiento.periodo_academico')),
            ],
        ),
        migrations.CreateModel(
            name='Logros_Personales',
            fields=[
                ('id_logros_personales', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_logro', models.CharField(max_length=50)),
                ('descripcion', models.TextField(max_length=100)),
                ('hoja_de_vida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seguimiento.hoja_de_vida')),
            ],
        ),
        migrations.CreateModel(
            name='Instruccion_formal',
            fields=[
                ('id_instruccion_formal', models.AutoField(primary_key=True, serialize=False)),
                ('nivel_de_instruccion', models.CharField(max_length=100)),
                ('instruccion_educativa', models.CharField(max_length=100)),
                ('titulo_obtenido', models.CharField(max_length=100)),
                ('no_del_registro_senescyt', models.CharField(max_length=100)),
                ('hoja_de_vida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seguimiento.hoja_de_vida')),
            ],
        ),
        migrations.CreateModel(
            name='Experiencia_Laboral',
            fields=[
                ('id_experiencia_laboral', models.AutoField(primary_key=True, serialize=False)),
                ('institucion', models.CharField(max_length=100)),
                ('tipo_de_institucion', models.CharField(max_length=100)),
                ('area_de_trabajo', models.CharField(max_length=100)),
                ('puesto', models.CharField(max_length=100)),
                ('actividades', models.CharField(max_length=100)),
                ('fecha_desde', models.DateField(verbose_name='Desde')),
                ('fecha_hasta', models.DateField(verbose_name='Hasta')),
                ('trabaja_actualmente_en_este_lugar', models.BooleanField(choices=[(False, 'No'), (True, 'Si')], default=False)),
                ('hoja_de_vida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seguimiento.hoja_de_vida')),
            ],
        ),
        migrations.AddField(
            model_name='estudiante',
            name='oferta',
            field=models.ManyToManyField(blank=True, null=True, to='seguimiento.oferta_laboral'),
        ),
        migrations.CreateModel(
            name='Eleccion',
            fields=[
                ('id_eleccion', models.AutoField(primary_key=True, serialize=False)),
                ('texto_eleccion', models.IntegerField()),
                ('votos', models.IntegerField()),
                ('pregunta', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='seguimiento.pregunta')),
            ],
        ),
        migrations.CreateModel(
            name='Capacitaciones',
            fields=[
                ('id_capacitaciones', models.AutoField(primary_key=True, serialize=False)),
                ('institucion', models.CharField(max_length=100)),
                ('tipo_de_evento', models.CharField(max_length=100)),
                ('area_de_estudio', models.CharField(max_length=100)),
                ('nombre_de_evento', models.CharField(max_length=100)),
                ('tipo_de_certificado', models.CharField(max_length=100)),
                ('fecha_desde', models.DateField()),
                ('fecha_hasta', models.DateField()),
                ('dias', models.CharField(max_length=10)),
                ('horas', models.CharField(max_length=10)),
                ('hoja_de_vida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seguimiento.hoja_de_vida')),
            ],
        ),
    ]
