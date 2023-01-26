from django.contrib import admin
from .models import Empresa, Informacion_laboral, Oferta_Laboral, Encuesta_Laboral, Pregunta, Eleccion, Carrera, Estudiante, Periodo_Academico, Mejor_Graduado, Hoja_de_vida, Logros_Personales, Preferencias_Laborales, Capacitaciones, Experiencia_Laboral, Instruccion_formal, Referencias_Personales
# Register your models here.


class PreguntaInline(admin.TabularInline):
    model = Pregunta
    extra = 3


class Encuesta_Laboral_Admin(admin.ModelAdmin):
    fieldsets = [
        ('Informacion de fecha', {'fields': [
         'fecha_pub'], }),
    ]
    inlines = [PreguntaInline]

    list_display = ('fecha_pub',)
    list_filter = ['fecha_pub']
    search_fields = ['texto_pregunta']


class estudianteAdminSearch(admin.ModelAdmin):
    search_fields = ['cedula']


class hojaAdmin(admin.ModelAdmin):
    autocomplete_fields = ['estudiante']



class empresaAdminSearch(admin.ModelAdmin):
    search_fields = ['contacto']


class ofertaAdmin(admin.ModelAdmin):
    autocomplete_fields = ['empresa']





admin.site.register(
    Encuesta_Laboral, Encuesta_Laboral_Admin)
admin.site.register(Eleccion)
admin.site.register(Empresa, empresaAdminSearch)
admin.site.register(Informacion_laboral)
admin.site.register(Oferta_Laboral, ofertaAdmin)
admin.site.register(Carrera)
admin.site.register(Estudiante, estudianteAdminSearch)
admin.site.register(Periodo_Academico)
admin.site.register(Mejor_Graduado)
admin.site.register(Hoja_de_vida, hojaAdmin)
admin.site.register(Logros_Personales)
admin.site.register(Preferencias_Laborales)
admin.site.register(Capacitaciones)
admin.site.register(Experiencia_Laboral)
admin.site.register(Instruccion_formal)
admin.site.register(Referencias_Personales)
