from django.urls import path
from app.seguimiento import views

urlpatterns = [
    path('', views.ListarOfertaLaboralIndex.as_view(), name="lista_oferta_laboral_index"),
    path('', views.dashboard, name='index'),
    
    #registros
    path('registro_carrera/', views.RegistrarCarrera.as_view(), name="registro_carrera"),
    path('registro_periodo_academico/', views.RegistrarPeriodoAcademico.as_view(), name="registro_periodo_academico"),
    path('registro_estudiante/', views.RegistrarEstudiante.as_view(), name="registro_estudiante"),    
    path('registro_mejor_graduado/', views.RegistrarMejorGraduado.as_view(), name="registro_mejor_graduado"),    
    path('registro_empresa/', views.RegistrarEmpresa.as_view(), name="registro_empresa"),    
    path('registro_oferta_laboral/', views.RegistrarOfertaLaboral.as_view(), name="registro_oferta_laboral"),    
    path('registro_encuesta_laboral/', views.RegistrarEncuesta.as_view(), name="registro_encuesta_laboral"),    
    path('registro_eleccion/', views.RegistrarEleccion, name="registro_eleccion"),    
    path('registro_eleccion/<pk>', views.RegistrarEleccionf, name="registro_eleccionFRM"),    
    path('registro_hoja_de_vida/', views.RegistrarHojaDeVida.as_view(), name="registro_hoja_de_vida"),  
    ##
    path('registro_logros_personales/', views.RegistrarLogrosPersonales.as_view(), name="registro_logros_personales"),    
    path('registro_preferencias_laborales/', views.RegistrarPreferenciasLaborales.as_view(), name="registro_preferencias_laborales"), 
    path('registro_capacitaciones/', views.RegistrarCapacitaciones.as_view(), name="registro_capacitaciones"), 
    path('registro_experiencia_laboral/', views.RegistrarExperienciaLaboral.as_view(), name="registro_experiencia_laboral"), 
    path('registro_instruccion_formal/', views.RegistrarInstruccionFormal.as_view(), name="registro_instruccion_formal"),
    path('registro_referencias_personales/', views.RegistrarReferenciasPersonales.as_view(), name="registro_referencias_personales"),
    
    #Updates  
    path('editar_carrera/<pk>/', views.EditarCarrera.as_view(), name="editar_carrera"),  
    path('editar_periodo_academico/<pk>/', views.EditarPeriodoAcademico.as_view(), name="editar_periodo_academico"),
    path('editar_estudiante/<pk>/', views.EditarEstudiante.as_view(), name="editar_estudiante"),
    path('editar_mejor_graduado/<pk>/', views.EditarMejorGraduado.as_view(), name="editar_mejor_graduado"),
    path('editar_empresa/<pk>/', views.EditarEmpresa.as_view(), name="editar_empresa"),
    path('editar_oferta_laboral/<pk>/', views.EditarOfertaLaboral.as_view(), name="editar_oferta_laboral"),
    path('editar_encuesta_laboral/<pk>/', views.EditarEncuesta.as_view(), name="editar_encuesta_laboral"),
    path('editar_hoja_de_vida/<pk>/', views.EditarHojaDeVida.as_view(), name="editar_hoja_de_vida"),
    ##
    path('editar_logros_personales/<pk>/', views.EditarLogrosPersonales.as_view(), name="editar_logros_personales"),    
    path('editar_preferencias_laborales/<pk>/', views.EditarPreferenciasLaborales.as_view(), name="editar_preferencias_laborales"),
    path('editar_capacitaciones/<pk>/', views.EditarCapacitaciones.as_view(), name="editar_capacitaciones"),
    path('editar_experiencia_laboral/<pk>/', views.EditarExperienciaLaboral.as_view(), name="editar_experiencia_laboral"),
    path('editar_instruccion_formal/<pk>/', views.EditarInstruccionFormal.as_view(), name="editar_instruccion_formal"),
    path('editar_referencias_personales/<pk>/', views.EditarReferenciasPersonales.as_view(), name="editar_referencias_personales"),

    #Eliminar
    path('eliminar_carrera/<pk>/', views.EliminarCarrera.as_view(), name="eliminar_carrera"),  
    path('eliminar_periodo_academico/<pk>/', views.EliminarPeriodoAcademico.as_view(), name="eliminar_periodo_academico"),
    path('eliminar_estudiante/<pk>/', views.EliminarEstudiante.as_view(), name="eliminar_estudiante"),  
    path('eliminar_mejor_graduado/<pk>/', views.EliminarMejorGraduado.as_view(), name="eliminar_mejor_graduado"),
    path('eliminar_empresa/<pk>/', views.EliminarEmpresa.as_view(), name="eliminar_empresa"),
    path('eliminar_oferta_laboral/<pk>/', views.EliminarOfertaLaboral.as_view(), name="eliminar_oferta_laboral"),
    path('eliminar_encuesta_laboral/<pk>/', views.EliminarEncuesta.as_view(), name="eliminar_encuesta_laboral"),
    path('eliminar_hoja_de_vida/<pk>/', views.EliminarHojaDeVida.as_view(), name="eliminar_hoja_de_vida"),
    ##
    path('eliminar_logros_personales/<pk>/', views.EliminarLogrosPersonales.as_view(), name="eliminar_logros_personales"),
    path('eliminar_preferencias_laborales/<pk>/', views.EliminarPreferenciasLaborales.as_view(), name="eliminar_preferencias_laborales"),
    path('eliminar_capacitaciones/<pk>/', views.EliminarCapacitaciones.as_view(), name="eliminar_capacitaciones"),
    path('eliminar_experiencia_laboral/<pk>/', views.EliminarExperienciaLaboral.as_view(), name="eliminar_experiencia_laboral"),
    path('eliminar_instruccion_formal/<pk>/', views.EliminarInstruccionFormal.as_view(), name="eliminar_instruccion_formal"),
    path('eliminar_referencias_personales/<pk>/', views.EliminarReferenciasPersonales.as_view(), name="eliminar_referencias_personales"),

    #listas
    path('lista_carrera/', views.ListarCarrera.as_view(), name="lista_carrera"),
    path('lista_estudiante/', views.ListarEstudiante.as_view(), name="lista_estudiante"),
    path('lista_periodo_academico/', views.ListarPeriodo_Academico.as_view(), name="lista_periodo_academico"),
    path('lista_mejor_graduado/', views.ListarMejor_Graduado.as_view(), name="lista_mejor_graduado"),
    path('lista_empresa/', views.ListarEmpresa.as_view(), name="lista_empresa"),
    path('lista_oferta_laboral/', views.ListarOfertaLaboral.as_view(), name="lista_oferta_laboral"),    
    path('lista_encuesta_laboral/', views.ListarEncuestaLaboral.as_view(), name="lista_encuesta_laboral"),
    path('lista_eleccion/', views.ListarEleccion.as_view(), name="lista_eleccion"),
    path('lista_hoja_de_vida/', views.ListarHojaDeVida.as_view(), name="lista_hoja_de_vida"),
    ##
    path('lista_logros_personales/', views.ListarLogrosPersonales.as_view(), name="lista_logros_personales"),
    path('lista_preferencias_laborales/', views.ListarPreferenciasLaborales.as_view(), name="lista_preferencias_laborales"),
    path('lista_capacitaciones/', views.ListarCapacitaciones.as_view(), name="lista_capacitaciones"),
    path('lista_experiencia_laboral/', views.ListarExperienciaLaboral.as_view(), name="lista_experiencia_laboral"),
    path('lista_instruccion_formal/', views.ListarInstruccionFormal.as_view(), name="lista_instruccion_formal"),
    path('lista_referencias_personales/', views.ListarReferenciasPersonales.as_view(), name="lista_referencias_personales"),

]

