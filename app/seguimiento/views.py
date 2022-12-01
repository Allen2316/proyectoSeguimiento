from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse_lazy
from app.seguimiento import models
from app.seguimiento import forms
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView

# Create your views here.


def dashboard(request):
    if request.method == 'GET':
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
        context = super(RegistrarOfertaLaboral, self).get_context_data(**kwargs)
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

# ediciones


# eliminaciones


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
