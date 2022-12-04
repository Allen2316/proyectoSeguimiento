from django.urls import path
from app.seguimiento import views

urlpatterns = [
    path('', views.dashboard, name='index'),
    
    #registros
    path('registro_carrera/', views.RegistrarCarrera.as_view(), name="registro_carrera"),
    path('registro_periodo_academico/', views.RegistrarPeriodoAcademico.as_view(), name="registro_periodo_academico"),
    path('registro_estudiante/', views.RegistrarEstudiante.as_view(), name="registro_estudiante"),    
    path('registro_mejor_graduado/', views.RegistrarMejorGraduado.as_view(), name="registro_mejor_graduado"),    
    path('registro_empresa/', views.RegistrarEmpresa.as_view(), name="registro_empresa"),    
    path('registro_oferta_laboral/', views.RegistrarOfertaLaboral.as_view(), name="registro_oferta_laboral"),    
    path('registro_encuesta_laboral/', views.RegistrarEncuesta.as_view(), name="registro_encuesta_laboral"),    
    path('registro_hoja_de_vida/', views.RegistrarHoja_de_vida.as_view(), name="registro_hoja_de_vida"),  
    
    #Updates  
    path('editar_carrera/<pk>/', views.EditarCarrera.as_view(), name="editar_carrera"),  
    path('editar_periodo_academico/<pk>/', views.EditarPeriodoAcademico.as_view(), name="editar_periodo_academico"),
    path('editar_estudiante/<pk>/', views.EditarEstudiante.as_view(), name="editar_estudiante"),
    path('editar_mejor_graduado/<pk>/', views.EditarMejorGraduado.as_view(), name="editar_mejor_graduado"),
    path('editar_empresa/<pk>/', views.EditarEmpresa.as_view(), name="editar_empresa"),
    path('editar_oferta_laboral/<pk>/', views.EditarOfertaLaboral.as_view(), name="editar_oferta_laboral"),
    path('editar_encuesta_laboral/<pk>/', views.EditarEncuesta.as_view(), name="editar_encuesta_laboral"),
    path('editar_hoja_de_vida/<pk>/', views.EditarHoja_de_vida.as_view(), name="editar_hoja_de_vida"),

    #Eliminar
    path('eliminar_carrera/<pk>/', views.EliminarCarrera.as_view(), name="eliminar_carrera"),  
    path('eliminar_periodo_academico/<pk>/', views.EliminarPeriodoAcademico.as_view(), name="eliminar_periodo_academico"),
    path('eliminar_estudiante/<pk>/', views.EliminarEstudiante.as_view(), name="eliminar_estudiante"),  
    path('eliminar_mejor_graduado/<pk>/', views.EliminarMejorGraduado.as_view(), name="eliminar_mejor_graduado"),
    path('eliminar_empresa/<pk>/', views.EliminarEmpresa.as_view(), name="eliminar_empresa"),
    path('eliminar_oferta_laboral/<pk>/', views.EliminarOfertaLaboral.as_view(), name="eliminar_oferta_laboral"),
    path('eliminar_encuesta_laboral/<pk>/', views.EliminarEncuesta.as_view(), name="eliminar_encuesta_laboral"),
    path('eliminar_hoja_de_vida/<pk>/', views.EliminarHoja_de_vida.as_view(), name="eliminar_hoja_de_vida"),

    #listas
    path('lista_carrera/', views.ListarCarrera.as_view(), name="lista_carrera"),
    path('lista_estudiante/', views.ListarEstudiante.as_view(), name="lista_estudiante"),
    path('lista_periodo_academico/', views.ListarPeriodo_Academico.as_view(), name="lista_periodo_academico"),
    path('lista_mejor_graduado/', views.ListarMejor_Graduado.as_view(), name="lista_mejor_graduado"),
    path('lista_empresa/', views.ListarEmpresa.as_view(), name="lista_empresa"),
    path('lista_oferta_laboral/', views.ListarOfertaLaboral.as_view(), name="lista_oferta_laboral"),
    path('lista_encuesta_laboral/', views.ListarEncuestaLaboral.as_view(), 
    name="lista_encuesta_laboral"),
    path('lista_hoja_de_vida/', views.ListarHoja_de_vida.as_view(), name="lista_hoja_de_vida"),
]

