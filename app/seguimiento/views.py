from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse_lazy
from app.seguimiento import models
from app.seguimiento import forms
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView

# Create your views here.


def dashboard(request):

    return render(request, 'seguimiento/dashboard.html')


# registros
class RegistrarCarrera(CreateView):
    model = models.Carrera
    template_name = 'seguimiento/FrmCarrera.html'
    form_class = forms.FrmCarrera
    success_url = reverse_lazy('lista_carrera')

    def get_context_data(self, **kwargs):
        context = super(RegistrarCarrera, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


class RegistrarPeriodoAcademico(CreateView):
    model = models.Periodo_Academico
    template_name = 'seguimiento/FrmPeriodo_Academico.html'
    form_class = forms.FrmPeriodo_Academico
    success_url = reverse_lazy('lista_periodo_academico')

    def get_context_data(self, **kwargs):
        context = super(RegistrarPeriodoAcademico,
                        self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


class RegistrarEstudiante(CreateView):
    model = models.Estudiante
    template_name = 'seguimiento/FrmEstudiante.html'
    form_class = forms.FrmEstudiante
    success_url = reverse_lazy('lista_estudiante')

    def get_context_data(self, **kwargs):
        context = super(RegistrarEstudiante, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


class RegistrarMejorGraduado(CreateView):
    model = models.Mejor_Graduado
    template_name = 'seguimiento/FrmMejor_Graduado.html'
    form_class = forms.FrmMejor_Graduado
    success_url = reverse_lazy('lista_mejor_graduado')

    def get_context_data(self, **kwargs):
        context = super(RegistrarMejorGraduado,
                        self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


class RegistrarEmpresa(CreateView):
    model = models.Empresa
    template_name = 'seguimiento/FrmEmpresa.html'
    form_class = forms.FrmEmpresa
    success_url = reverse_lazy('lista_empresa')

    def get_context_data(self, **kwargs):
        context = super(RegistrarEmpresa, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


class RegistrarOfertaLaboral(CreateView):
    model = models.Oferta_Laboral
    template_name = 'seguimiento/FrmOferta_Laboral.html'
    form_class = forms.FrmOferta_Laboral
    second_form_class = forms.FrmInformacion_laboral
    success_url = reverse_lazy('lista_oferta_laboral')

    def get_context_data(self, **kwargs):
        context = super(RegistrarOfertaLaboral,
                        self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)

        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            oferta = form.save(commit=False)
            oferta.informacion_laboral = form2.save()
            oferta.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))


class RegistrarEncuesta(CreateView):
    model = models.Pregunta
    template_name = 'seguimiento/FrmEncuesta_Laboral.html'
    form_class = forms.FrmEncuesta_Laboral
    second_form_class = forms.FrmPregunta
    success_url = reverse_lazy('lista_encuesta_laboral')

    def get_context_data(self, **kwargs):
        context = super(RegistrarEncuesta,
                        self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)

        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            encuesta = form2.save(commit=False)
            encuesta.encuesta_laboral = form.save()
            encuesta.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))


class RegistrarHojaDeVida(CreateView):
    model = models.Logros_Personales
    template_name = 'seguimiento/FrmHoja_de_vida.html'
    form_class = forms.FrmHoja_de_vida
    second_form_class = forms.FrmLogros_Personales1
    t_form_class = forms.FrmPreferencias_Laborales1
    f_form_class = forms.FrmCapacitaciones1
    fth_form_class = forms.FrmExperiencia_Laboral1
    s_form_class = forms.FrmInstruccion_formal1
    sth_form_class = forms.FrmReferencias_Personales1

    success_url = reverse_lazy('lista_hoja_de_vida')

    def get_context_data(self, **kwargs):
        context = super(RegistrarHojaDeVida,
                        self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)

        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)

        if 'form3' not in context:
            context['form3'] = self.t_form_class(self.request.GET)

        if 'form4' not in context:
            context['form4'] = self.f_form_class(self.request.GET)

        if 'form5' not in context:
            context['form5'] = self.fth_form_class(self.request.GET)

        if 'form6' not in context:
            context['form6'] = self.s_form_class(self.request.GET)

        if 'form7' not in context:
            context['form7'] = self.sth_form_class(self.request.GET)

        context['tam'] = 7
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        form3 = self.t_form_class(request.POST)
        form4 = self.f_form_class(request.POST)
        form5 = self.fth_form_class(request.POST)
        form6 = self.s_form_class(request.POST)
        form7 = self.sth_form_class(request.POST)

        if form.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid() and form5.is_valid() and form6.is_valid() and form7.is_valid():
            logros_personales = form2.save(commit=False)
            logros_personales.hoja_de_vida = form.save()

            preferencias_laborales = form3.save(commit=False)
            preferencias_laborales.hoja_de_vida = form.save()

            capacitaciones = form4.save(commit=False)
            capacitaciones.hoja_de_vida = form.save()

            experiencia_laboral = form5.save(commit=False)
            experiencia_laboral.hoja_de_vida = form.save()

            instruccion_formal = form6.save(commit=False)
            instruccion_formal.hoja_de_vida = form.save()

            referencias_personales = form7.save(commit=False)
            referencias_personales.hoja_de_vida = form.save()

            logros_personales.save()
            preferencias_laborales.save()
            capacitaciones.save()
            experiencia_laboral.save()
            instruccion_formal.save()
            referencias_personales.save()

            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3, form4=form4, form5=form5, form6=form6, form7=form7,))


""" class RegistrarHojaDeVida(CreateView):
    model = models.Hoja_de_vida
    template_name = 'seguimiento/FrmHoja_de_vida.html'
    form_class = forms.FrmHoja_de_vida
    success_url = reverse_lazy('lista_hoja_de_vida')

    def get_context_data(self, **kwargs):
        context = super(RegistrarHojaDeVida, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form)) """


class RegistrarLogrosPersonales(CreateView):
    model = models.Logros_Personales
    template_name = 'seguimiento/FrmLogros_Personales.html'
    form_class = forms.FrmLogros_Personales
    success_url = reverse_lazy('lista_logros_personales')

    def get_context_data(self, **kwargs):
        context = super(RegistrarLogrosPersonales,
                        self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


class RegistrarPreferenciasLaborales(CreateView):
    model = models.Preferencias_Laborales
    template_name = 'seguimiento/FrmPreferencias_Laborales.html'
    form_class = forms.FrmPreferencias_Laborales
    success_url = reverse_lazy('lista_preferencias_laborales')

    def get_context_data(self, **kwargs):
        context = super(RegistrarPreferenciasLaborales,
                        self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


class RegistrarCapacitaciones(CreateView):
    model = models.Capacitaciones
    template_name = 'seguimiento/FrmCapacitaciones.html'
    form_class = forms.FrmCapacitaciones
    success_url = reverse_lazy('lista_capacitaciones')

    def get_context_data(self, **kwargs):
        context = super(RegistrarCapacitaciones,
                        self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


class RegistrarExperienciaLaboral(CreateView):
    model = models.Experiencia_Laboral
    template_name = 'seguimiento/FrmExperiencia_Laboral.html'
    form_class = forms.FrmExperiencia_Laboral
    success_url = reverse_lazy('lista_experiencia_laboral')

    def get_context_data(self, **kwargs):
        context = super(RegistrarExperienciaLaboral,
                        self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


class RegistrarInstruccionFormal(CreateView):
    model = models.Instruccion_formal
    template_name = 'seguimiento/FrmInstruccion_formal.html'
    form_class = forms.FrmInstruccion_formal
    success_url = reverse_lazy('lista_instruccion_formal')

    def get_context_data(self, **kwargs):
        context = super(RegistrarInstruccionFormal,
                        self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


class RegistrarReferenciasPersonales(CreateView):
    model = models.Referencias_Personales
    template_name = 'seguimiento/FrmReferencias_Personales.html'
    form_class = forms.FrmReferencias_Personales
    success_url = reverse_lazy('lista_referencias_personales')

    def get_context_data(self, **kwargs):
        context = super(RegistrarReferenciasPersonales,
                        self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


# ediciones


class EditarCarrera(UpdateView):
    model = models.Carrera
    form_class = forms.FrmCarrera
    template_name = 'seguimiento/FrmCarrera.html'
    success_url = reverse_lazy('lista_carrera')


class EditarPeriodoAcademico(UpdateView):
    model = models.Periodo_Academico
    form_class = forms.FrmPeriodo_Academico
    template_name = 'seguimiento/FrmPeriodo_Academico.html'
    success_url = reverse_lazy('lista_periodo_academico')


class EditarEstudiante(UpdateView):
    model = models.Estudiante
    form_class = forms.FrmEstudiante
    template_name = 'seguimiento/FrmEstudiante.html'
    success_url = reverse_lazy('lista_estudiante')


class EditarMejorGraduado(UpdateView):
    model = models.Mejor_Graduado
    form_class = forms.FrmMejor_Graduado
    template_name = 'seguimiento/FrmMejor_Graduado.html'
    success_url = reverse_lazy('lista_mejor_graduado')


class EditarEmpresa(UpdateView):
    model = models.Empresa
    form_class = forms.FrmEmpresa
    template_name = 'seguimiento/FrmEmpresa.html'
    success_url = reverse_lazy('lista_empresa')


class EditarOfertaLaboral(UpdateView):
    model = models.Oferta_Laboral
    second_model = models.Informacion_laboral
    form_class = forms.FrmOferta_Laboral
    second_form_class = forms.FrmInformacion_laboral
    template_name = 'seguimiento/FrmOferta_Laboral.html'
    success_url = reverse_lazy('lista_oferta_laboral')

    def get_context_data(self, **kwargs):
        context = super(EditarOfertaLaboral, self).get_context_data(**kwargs)
        pk1 = self.kwargs.get('pk', 0)
        oferta = self.model.objects.get(id_oferta_laboral=pk1)
        info = self.second_model.objects.get(pk=oferta.informacion_laboral.pk)

        if 'form' not in context:
            context['form'] = self.form_class()

        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=info)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_oferta = kwargs['pk']
        oferta = self.model.objects.get(id_oferta_laboral=id_oferta)
        info = self.second_model.objects.get(pk=oferta.informacion_laboral.pk)
        form = self.form_class(request.POST, instance=oferta)
        form2 = self.second_form_class(request.POST, instance=info)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))


class EditarEncuesta(UpdateView):
    model = models.Encuesta_Laboral
    form_class = forms.FrmEncuesta_Laboral
    template_name = 'seguimiento/FrmEncuesta_Laboral.html'
    success_url = reverse_lazy('lista_encuesta_laboral')


class EditarHojaDeVida(UpdateView):
    model = models.Hoja_de_vida
    second_model = models.Logros_Personales
    third_model = models.Preferencias_Laborales
    four_model = models.Capacitaciones
    five_model = models.Experiencia_Laboral
    six_model = models.Instruccion_formal
    seven_model = models.Referencias_Personales

    form_class = forms.FrmHoja_de_vida
    second_form_class = forms.FrmLogros_Personales1
    third_form_class = forms.FrmPreferencias_Laborales1
    four_form_class = forms.FrmCapacitaciones1
    five_form_class = forms.FrmExperiencia_Laboral1
    six_form_class = forms.FrmInstruccion_formal1
    seven_form_class = forms.FrmReferencias_Personales1

    template_name = 'seguimiento/FrmHoja_de_vida.html'
    success_url = reverse_lazy('lista_hoja_de_vida')

    def get_context_data(self, **kwargs):
        context = super(EditarHojaDeVida,
                        self).get_context_data(**kwargs)

        id_hoja = self.kwargs.get('pk', 0)
        hoja = self.model.objects.get(pk=id_hoja)
        logro = self.second_model.objects.filter(hoja_de_vida=hoja.pk).first()

        preferencia = self.third_model.objects.filter(
            hoja_de_vida=hoja.pk).first()

        capacitacion = self.four_model.objects.filter(
            hoja_de_vida=hoja.pk).first()

        experiencia = self.five_model.objects.filter(
            hoja_de_vida=hoja.pk).first()

        instruccion = self.six_model.objects.filter(
            hoja_de_vida=hoja.pk).first()

        referencia = self.seven_model.objects.filter(
            hoja_de_vida=hoja.pk).first()

        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)

        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=logro)

        if 'form3' not in context:
            context['form3'] = self.third_form_class(instance=preferencia)

        if 'form4' not in context:
            context['form4'] = self.four_form_class(instance=capacitacion)

        if 'form5' not in context:
            context['form5'] = self.five_form_class(instance=experiencia)

        if 'form6' not in context:
            context['form6'] = self.six_form_class(instance=instruccion)

        if 'form7' not in context:
            context['form7'] = self.seven_form_class(instance=referencia)

        context['tam'] = 7
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_hoja = kwargs['pk']
        hoja = self.model.objects.get(pk=id_hoja)

        logro = self.second_model.objects.get(hoja_de_vida=hoja.pk)

        preferencia = self.third_model.objects.get(hoja_de_vida=hoja.pk)

        capacitacion = self.four_model.objects.get(hoja_de_vida=hoja.pk)

        experiencia = self.five_model.objects.get(hoja_de_vida=hoja.pk)

        instruccion = self.six_model.objects.get(hoja_de_vida=hoja.pk)

        referencia = self.seven_model.objects.get(hoja_de_vida=hoja.pk)

        form = self.form_class(request.POST, instance=hoja)
        form2 = self.second_form_class(request.POST, instance=logro)
        form3 = self.third_form_class(request.POST, instance=preferencia)
        form4 = self.four_form_class(request.POST, instance=capacitacion)
        form5 = self.five_form_class(request.POST, instance=experiencia)
        form6 = self.six_form_class(request.POST, instance=instruccion)
        form7 = self.seven_form_class(request.POST, instance=referencia)

        if form.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid() and form5.is_valid() and form6.is_valid() and form7.is_valid():
            form.save()
            form2.save()
            form3.save()
            form4.save()
            form5.save()
            form6.save()
            form7.save()

            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3, form4=form4, form5=form5, form6=form6, form7=form7))


""" class EditarHojaDeVida(UpdateView):
    model = models.Hoja_de_vida
    form_class = forms.FrmHoja_de_vida
    template_name = 'seguimiento/FrmHoja_de_vida.html'
    success_url = reverse_lazy('lista_hoja_de_vida') """


class EditarLogrosPersonales(UpdateView):
    model = models.Logros_Personales
    form_class = forms.FrmLogros_Personales
    template_name = 'seguimiento/FrmLogros_personales.html'
    success_url = reverse_lazy('lista_logros_personales')


class EditarPreferenciasLaborales(UpdateView):
    model = models.Preferencias_Laborales
    form_class = forms.FrmPreferencias_Laborales
    template_name = 'seguimiento/FrmPreferencias_Laborales.html'
    success_url = reverse_lazy('lista_preferencias_laborales')


class EditarCapacitaciones(UpdateView):
    model = models.Capacitaciones
    form_class = forms.FrmCapacitaciones
    template_name = 'seguimiento/FrmCapacitaciones.html'
    success_url = reverse_lazy('lista_capacitaciones')


class EditarExperienciaLaboral(UpdateView):
    model = models.Experiencia_Laboral
    form_class = forms.FrmExperiencia_Laboral
    template_name = 'seguimiento/FrmExperiencia_Laboral.html'
    success_url = reverse_lazy('lista_experiencia_laboral')


class EditarInstruccionFormal(UpdateView):
    model = models.Instruccion_formal
    form_class = forms.FrmInstruccion_formal
    template_name = 'seguimiento/FrmInstruccion_formal.html'
    success_url = reverse_lazy('lista_instruccion_formal')


class EditarReferenciasPersonales(UpdateView):
    model = models.Referencias_Personales
    form_class = forms.FrmReferencias_Personales
    template_name = 'seguimiento/FrmReferencias_Personales.html'
    success_url = reverse_lazy('lista_referencias_personales')
# eliminaciones


class EliminarCarrera(DeleteView):
    model = models.Carrera
    template_name = 'seguimiento/EliminarCarrera.html'
    success_url = reverse_lazy('lista_carrera')


class EliminarPeriodoAcademico(DeleteView):
    model = models.Periodo_Academico
    template_name = 'seguimiento/EliminarPeriodo_Academico.html'
    success_url = reverse_lazy('lista_periodo_academico')


class EliminarEstudiante(DeleteView):
    model = models.Estudiante
    template_name = 'seguimiento/EliminarEstudiante.html'
    success_url = reverse_lazy('lista_estudiante')


class EliminarMejorGraduado(DeleteView):
    model = models.Mejor_Graduado
    template_name = 'seguimiento/EliminarMejor_Graduado.html'
    success_url = reverse_lazy('lista_mejor_graduado')


class EliminarEmpresa(DeleteView):
    model = models.Empresa
    template_name = 'seguimiento/EliminarEmpresa.html'
    success_url = reverse_lazy('lista_empresa')


class EliminarOfertaLaboral(DeleteView):
    model = models.Oferta_Laboral
    template_name = 'seguimiento/EliminarOferta_Laboral.html'
    success_url = reverse_lazy('lista_oferta_laboral')


class EliminarEncuesta(DeleteView):
    model = models.Encuesta_Laboral
    template_name = 'seguimiento/EliminarEncuesta_Laboral.html'
    success_url = reverse_lazy('lista_encuesta_laboral')


class EliminarHojaDeVida(DeleteView):
    model = models.Hoja_de_vida
    template_name = 'seguimiento/EliminarHoja_de_vida.html'
    success_url = reverse_lazy('lista_hoja_de_vida')


class EliminarLogrosPersonales(DeleteView):
    model = models.Logros_Personales
    template_name = 'seguimiento/EliminarLogros_Personales.html'
    success_url = reverse_lazy('lista_logros_personales')


class EliminarPreferenciasLaborales(DeleteView):
    model = models.Preferencias_Laborales
    template_name = 'seguimiento/EliminarPreferencias_Laborales.html'
    success_url = reverse_lazy('lista_preferencias_laborales')


class EliminarCapacitaciones(DeleteView):
    model = models.Capacitaciones
    template_name = 'seguimiento/EliminarCapacitaciones.html'
    success_url = reverse_lazy('lista_capacitaciones')


class EliminarExperienciaLaboral(DeleteView):
    model = models.Experiencia_Laboral
    template_name = 'seguimiento/EliminarExperiencia_Laboral.html'
    success_url = reverse_lazy('lista_experiencia_laboral')


class EliminarInstruccionFormal(DeleteView):
    model = models.Instruccion_formal
    template_name = 'seguimiento/EliminarInstruccion_formal.html'
    success_url = reverse_lazy('lista_instruccion_formal')


class EliminarReferenciasPersonales(DeleteView):
    model = models.Referencias_Personales
    template_name = 'seguimiento/EliminarReferencias_Personales.html'
    success_url = reverse_lazy('lista_referencias_personales')
# listados


class ListarCarrera(ListView):
    model = models.Carrera
    template_name = 'seguimiento/ListaCarrera.html'


class ListarPeriodo_Academico(ListView):
    model = models.Periodo_Academico
    template_name = 'seguimiento/ListaPeriodo_Academico.html'


class ListarEstudiante(ListView):
    model = models.Estudiante
    template_name = 'seguimiento/ListaEstudiante.html'


class ListarMejor_Graduado(ListView):
    model = models.Mejor_Graduado
    template_name = 'seguimiento/ListaMejor_Graduado.html'


class ListarEmpresa(ListView):
    model = models.Empresa
    template_name = 'seguimiento/ListaEmpresa.html'


class ListarOfertaLaboral(ListView):
    model = models.Oferta_Laboral
    template_name = 'seguimiento/ListaOferta_Laboral.html'


class ListarOfertaLaboralIndex(ListView):
    model = models.Oferta_Laboral
    template_name = 'seguimiento/dashboard.html'


class ListarEncuestaLaboral(ListView):
    model = models.Encuesta_Laboral
    template_name = 'seguimiento/ListaEncuesta_Laboral.html'


class ListarHojaDeVida(ListView):
    model = models.Hoja_de_vida
    template_name = 'seguimiento/ListaHoja_de_vida.html'


class ListarLogrosPersonales(ListView):
    model = models.Logros_Personales
    template_name = 'seguimiento/ListaLogros_personales.html'


class ListarPreferenciasLaborales(ListView):
    model = models.Preferencias_Laborales
    template_name = 'seguimiento/ListaPreferencias_Laborales.html'


class ListarCapacitaciones(ListView):
    model = models.Capacitaciones
    template_name = 'seguimiento/ListaCapacitaciones.html'


class ListarExperienciaLaboral(ListView):
    model = models.Experiencia_Laboral
    template_name = 'seguimiento/ListaExperiencia_Laboral.html'


class ListarInstruccionFormal(ListView):
    model = models.Instruccion_formal
    template_name = 'seguimiento/ListaInstruccion_formal.html'


class ListarReferenciasPersonales(ListView):
    model = models.Referencias_Personales
    template_name = 'seguimiento/ListaReferencias_Personales.html'
