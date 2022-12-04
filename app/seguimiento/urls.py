from django.urls import path
from app.seguimiento import views

urlpatterns = [
    path('', views.dashboard, name='index'),
    path('registro_carrera/', views.RegistrarCarrera.as_view(), name="registro_carrera"),
    path('registro_periodo_academico/', views.RegistrarPeriodoAcademico.as_view(), name="registro_periodo_academico"),
    path('registro_estudiante/', views.RegistrarEstudiante.as_view(), name="registro_estudiante"),    
    path('registro_mejor_graduado/', views.RegistrarMejorGraduado.as_view(), name="registro_mejor_graduado"),    
    path('registro_empresa/', views.RegistrarEmpresa.as_view(), name="registro_empresa"),    
    path('registro_oferta_laboral/', views.RegistrarOfertaLaboral.as_view(), name="registro_oferta_laboral"),    
    path('registro_encuesta_laboral/', views.RegistrarEncuesta.as_view(), name="registro_encuesta_laboral"),    
    path('registro_hoja_de_vida/', views.RegistrarHoja_de_vida.as_view(), name="registro_hoja_de_vida"),    
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

