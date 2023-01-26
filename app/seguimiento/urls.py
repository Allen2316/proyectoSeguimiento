from django.urls import path
from app.seguimiento import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from app.seguimiento import forms

urlpatterns = [
    path('', views.logueo, name="logueo"),
    path('deslogueo', auth_views.LogoutView.as_view(
        template_name="login.html"), name='deslogueo'),
    path('dashboard', login_required(
        views.ListarOfertaLaboralIndex.as_view()), name="lista_oferta_laboral_index"),
    path('dashboard', login_required(views.dashboard), name='index'),
    path('oferta_laboral/<pk>/', login_required(
        views.ListarOfertaLaboralTotal.as_view()), name="oferta_laboral"),

    # registros
    path('registro_carrera/', login_required(views.RegistrarCarrera.as_view()),
         name="registro_carrera"),
    path('registro_periodo_academico/', login_required(views.RegistrarPeriodoAcademico.as_view()),
         name="registro_periodo_academico"),
    path('registro_estudiante/', login_required(views.RegistrarEstudiante.as_view()),
         name="registro_estudiante"),
    path('registro_mejor_graduado/', login_required(views.RegistrarMejorGraduado.as_view()),
         name="registro_mejor_graduado"),
    path('registro_empresa/', login_required(views.RegistrarEmpresa.as_view()),
         name="registro_empresa"),

    path('registro_oferta_laboral/', login_required(views.RegistrarOfertaLaboral.as_view()),
         name="registro_oferta_laboral"),

    path('admins/registro_oferta_laboral/', login_required(views.RegistrarOfertaLaboralAdmin.as_view()),
         name="registro_oferta_laboralAdmin"),

    path('registro_encuesta_laboral/', login_required(views.RegistrarEncuesta.as_view()),
         name="registro_encuesta_laboral"),
    ####

    #path('registro_eleccion/', views.RegistrarEleccion, name="registro_eleccion"),

    path('registro_eleccion/<int:id_oferta_laboral>/',
         views.RegistrarEleccionf, name="registro_eleccionFRM"),

    path('voto/', views.voto, name="voto"),


    path('registro_hoja_de_vida/', login_required(views.RegistrarHojaDeVida.as_view()),
         name="registro_hoja_de_vida"),

     
     path('admins/registro_hoja_de_vida/', login_required(views.RegistrarHojaDeVidaAdmin.as_view()),
         name="registro_hoja_de_vidaAdmin"),

    ##
    path('registro_logros_personales/', login_required(views.RegistrarLogrosPersonales.as_view()),
         name="registro_logros_personales"),
    path('registro_preferencias_laborales/', login_required(views.RegistrarPreferenciasLaborales.as_view()),
         name="registro_preferencias_laborales"),
    path('registro_capacitaciones/', login_required(views.RegistrarCapacitaciones.as_view()),
         name="registro_capacitaciones"),
    path('registro_experiencia_laboral/', login_required(views.RegistrarExperienciaLaboral.as_view()),
         name="registro_experiencia_laboral"),
    path('registro_instruccion_formal/', login_required(views.RegistrarInstruccionFormal.as_view()),
         name="registro_instruccion_formal"),
    path('registro_referencias_personales/', login_required(views.RegistrarReferenciasPersonales.as_view()),
         name="registro_referencias_personales"),

    # Updates
    path('editar_carrera/<pk>/',
         login_required(views.EditarCarrera.as_view()), name="editar_carrera"),
    path('editar_periodo_academico/<pk>/',
         login_required(views.EditarPeriodoAcademico.as_view()), name="editar_periodo_academico"),
    path('editar_estudiante/<pk>/',
         login_required(views.EditarEstudiante.as_view()), name="editar_estudiante"),
    path('editar_mejor_graduado/<pk>/',
         login_required(views.EditarMejorGraduado.as_view()), name="editar_mejor_graduado"),
    path('editar_empresa/<pk>/',    
         login_required(views.EditarEmpresa.as_view()), name="editar_empresa"),
    
    path('editar_oferta_laboral/<pk>/',
         login_required(views.EditarOfertaLaboral.as_view()), name="editar_oferta_laboral"),

    path('admins/editar_oferta_laboral/<pk>/',
         login_required(views.EditarOfertaLaboralAdmin.as_view()), name="editar_oferta_laboralAdmin"),


    path('editar_encuesta_laboral/<pk>/',
         login_required(views.EditarEncuesta.as_view()), name="editar_encuesta_laboral"),
    path('editar_hoja_de_vida/<pk>/',
         login_required(views.EditarHojaDeVida.as_view()), name="editar_hoja_de_vida"),
    ##
    path('editar_logros_personales/<pk>/',
         login_required(views.EditarLogrosPersonales.as_view()), name="editar_logros_personales"),
    path('editar_preferencias_laborales/<pk>/',
         login_required(views.EditarPreferenciasLaborales.as_view()), name="editar_preferencias_laborales"),
    path('editar_capacitaciones/<pk>/',
         login_required(views.EditarCapacitaciones.as_view()), name="editar_capacitaciones"),
    path('editar_experiencia_laboral/<pk>/',
         login_required(views.EditarExperienciaLaboral.as_view()), name="editar_experiencia_laboral"),
    path('editar_instruccion_formal/<pk>/',
         login_required(views.EditarInstruccionFormal.as_view()), name="editar_instruccion_formal"),
    path('editar_referencias_personales/<pk>/',
         login_required(views.EditarReferenciasPersonales.as_view()), name="editar_referencias_personales"),

    # Eliminar
    path('eliminar_carrera/<pk>/',
         login_required(views.EliminarCarrera.as_view()), name="eliminar_carrera"),
    path('eliminar_periodo_academico/<pk>/',
         login_required(views.EliminarPeriodoAcademico.as_view()), name="eliminar_periodo_academico"),
    path('eliminar_estudiante/<pk>/',
         login_required(views.EliminarEstudiante.as_view()), name="eliminar_estudiante"),
    path('eliminar_mejor_graduado/<pk>/',
         login_required(views.EliminarMejorGraduado.as_view()), name="eliminar_mejor_graduado"),
    path('eliminar_empresa/<pk>/',
         login_required(views.EliminarEmpresa.as_view()), name="eliminar_empresa"),
    path('eliminar_oferta_laboral/<pk>/',
         login_required(views.EliminarOfertaLaboral.as_view()), name="eliminar_oferta_laboral"),
    path('eliminar_encuesta_laboral/<pk>/',
         login_required(views.EliminarEncuesta.as_view()), name="eliminar_encuesta_laboral"),
    path('eliminar_hoja_de_vida/<pk>/',
         login_required(views.EliminarHojaDeVida.as_view()), name="eliminar_hoja_de_vida"),
    ##
    path('eliminar_logros_personales/<pk>/',
         login_required(views.EliminarLogrosPersonales.as_view()), name="eliminar_logros_personales"),
    path('eliminar_preferencias_laborales/<pk>/',
         login_required(views.EliminarPreferenciasLaborales.as_view()), name="eliminar_preferencias_laborales"),
    path('eliminar_capacitaciones/<pk>/',
         login_required(views.EliminarCapacitaciones.as_view()), name="eliminar_capacitaciones"),
    path('eliminar_experiencia_laboral/<pk>/',
         login_required(views.EliminarExperienciaLaboral.as_view()), name="eliminar_experiencia_laboral"),
    path('eliminar_instruccion_formal/<pk>/',
         login_required(views.EliminarInstruccionFormal.as_view()), name="eliminar_instruccion_formal"),
    path('eliminar_referencias_personales/<pk>/',
         login_required(views.EliminarReferenciasPersonales.as_view()), name="eliminar_referencias_personales"),

    # listas
    path('lista_carrera/', login_required(views.ListarCarrera.as_view()),
         name="lista_carrera"),
    path('lista_estudiante/', login_required(views.ListarEstudiante.as_view()),
         name="lista_estudiante"),
    path('lista_periodo_academico/', login_required(views.ListarPeriodo_Academico.as_view()),
         name="lista_periodo_academico"),
    path('lista_mejor_graduado/', login_required(views.ListarMejor_Graduado.as_view()),
         name="lista_mejor_graduado"),
    path('lista_empresa/', login_required(views.ListarEmpresa.as_view()),
         name="lista_empresa"),
    path('lista_oferta_laboral/', login_required(views.ListarOfertaLaboral.as_view()),
         name="lista_oferta_laboral"),
    path('lista_encuesta_laboral/', login_required(views.ListarEncuestaLaboral.as_view()),
         name="lista_encuesta_laboral"),
    path('lista_eleccion/', login_required(views.ListarEleccion.as_view()),
         name="lista_eleccion"),
    path('lista_hoja_de_vida/', login_required(views.ListarHojaDeVida.as_view()),
         name="lista_hoja_de_vida"),
    ##
    path('lista_logros_personales/', login_required(views.ListarLogrosPersonales.as_view()),
         name="lista_logros_personales"),
    path('lista_preferencias_laborales/', login_required(views.ListarPreferenciasLaborales.as_view()),
         name="lista_preferencias_laborales"),
    path('lista_capacitaciones/', login_required(views.ListarCapacitaciones.as_view()),
         name="lista_capacitaciones"),
    path('lista_experiencia_laboral/', login_required(views.ListarExperienciaLaboral.as_view()),
         name="lista_experiencia_laboral"),
    path('lista_instruccion_formal/', login_required(views.ListarInstruccionFormal.as_view()),
         name="lista_instruccion_formal"),
    path('lista_referencias_personales/', login_required(views.ListarReferenciasPersonales.as_view()),
         name="lista_referencias_personales"),    

### Seleccionar oferta en dashboard
     path('selecionar/oferta/<pk>', views.SeleccionarOferta,
         name="seleccionaroferta"),    

## ver hoja de vida de estudiante postulado
     path('estudiante/postulado/<pk>', login_required(views.ListarHojaDeVidaEstudiante.as_view()),
         name="estudiantepostulado"),    
]
