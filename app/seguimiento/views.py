from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404, reverse
from django.urls import reverse_lazy
from app.seguimiento import models
from app.seguimiento import forms
from django.db.models import F
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.core.serializers import json
from django.contrib.auth.hashers import make_password

# Create your views here.


def logueo(request):
    if request.method == 'POST':
        formulario = forms.FrmLogin(request.POST)
        if formulario.is_valid():
            usuario = request.POST['username']
            clave = request.POST['password']
            user = authenticate(username=usuario, password=clave)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('lista_oferta_laboral_index'))
                else:
                    return HttpResponseRedirect(reverse(''))
            else:
                messages.warning(request, 'Usuario y/o contraseña incorrecta')
    else:
        formulario = forms.FrmLogin()
    context = {
        'form': formulario
    }
    return render(request, 'login.html', context)


@login_required
def dashboard(request):
    return render(request, 'seguimiento/dashboard.html')


# registros
class RegistrarCarrera(CreateView):
    model = models.Carrera
    template_name = 'seguimiento/FrmCarrera.html'
    form_class = forms.FrmCarrera
    success_url = reverse_lazy('lista_carrera')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(RegistrarCarrera, self).dispatch(*args, **kwargs)

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
    second_form_class = forms.FrmUser
    success_url = reverse_lazy('lista_estudiante')

    def get_context_data(self, **kwargs):
        context = super(RegistrarEstudiante, self).get_context_data(**kwargs)
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
            estudiante = form.save(commit=False)
            estudiante.user = form2.save()
            estudiante.save()
            group = Group.objects.get(name='GrupoEstudiante')
            estudiante.user.groups.add(group)
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))


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
    second_form_class = forms.FrmUserEmp
    success_url = reverse_lazy('lista_empresa')

    def get_context_data(self, **kwargs):
        context = super(RegistrarEmpresa, self).get_context_data(**kwargs)
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
            emp = form.save(commit=False)
            emp.user = form2.save()
            emp.save()
            group = Group.objects.get(name='GrupoEmpresa')
            emp.user.groups.add(group)
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

    def get_initial(self):
        empresa = models.Empresa.objects.get(
            pk=self.request.user.empresa.pk)
        return {'empresa': empresa}


class RegistrarOfertaLaboralAdmin(CreateView):
    model = models.Oferta_Laboral
    template_name = 'seguimiento/FrmOferta_Laboral.html'
    form_class = forms.FrmOferta_LaboralAdmin
    second_form_class = forms.FrmInformacion_laboral
    success_url = reverse_lazy('lista_oferta_laboral')

    def get_context_data(self, **kwargs):
        context = super(RegistrarOfertaLaboralAdmin,
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


@login_required
def RegistrarEleccionf(request, id_oferta_laboral):
    try:
        oferta = get_object_or_404(models.Oferta_Laboral,
                                   id_oferta_laboral=id_oferta_laboral)

        # encuesta = oferta.encuesta_set.all()
        encuesta = get_object_or_404(
            models.Encuesta_Laboral,
            id_encuesta_laboral=oferta.encuesta.id_encuesta_laboral)

        pregunta = encuesta.pregunta_set.all()

        context = {
            'pregunta': pregunta,
            # 'eleccion': eleccion,
        }
    # pregunta[1].eleccion_set.all()
    except:
        context = {
            'error_message': 'Error al ejecutar porque la oferta no tiene ninguna encuesta',
            # 'eleccion': eleccion,
        }

    return render(request, 'seguimiento/FrmEleccion.html', context)


@login_required
def voto(request):
    valores = request.POST
    lista = []
    id_p = []

    for i in valores:
        lista.append(request.POST[i])
        id_p.append(i)

    lista.pop(0)
    id_p.pop(0)

    cont = 0
    for pre in id_p:
        pregunta = get_object_or_404(models.Pregunta, pk=pre)
        try:
            opcion_elegida = pregunta.eleccion_set.get(pk=lista[cont])
        except (KeyError, models.Eleccion.DoesNotExist):
            return render(request, 'seguimiento/FrmEleccion.html', {
                'lista': lista,
                'id_p': id_p,
                'error_message': 'No seleccionó una opción.',
            })
        else:
            opcion_elegida.votos += 1
            opcion_elegida.save()
            cont += 1

    return HttpResponseRedirect(reverse('lista_oferta_laboral_index',))


class RegistrarHojaDeVida(CreateView):
    #!TODO hacer aca
    #model = models.Logros_Personales
    model = models.Hoja_de_vida
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

    def get_initial(self):
        print(self.request.user.estudiante.pk)
        estudiante = models.Estudiante.objects.get(
            pk=self.request.user.estudiante.pk)
        return {'estudiante': estudiante}

    """ def get_initial(self):
        empresa = models.Empresa.objects.get(
            pk=self.request.user.empresa.pk)
        return {'empresa': empresa} """


class RegistrarHojaDeVidaAdmin(CreateView):
    #!TODO hacer aca
    #model = models.Logros_Personales
    model = models.Hoja_de_vida
    template_name = 'seguimiento/FrmHoja_de_vida.html'
    form_class = forms.FrmHoja_de_vidaAdmin
    second_form_class = forms.FrmLogros_Personales1
    t_form_class = forms.FrmPreferencias_Laborales1
    f_form_class = forms.FrmCapacitaciones1
    fth_form_class = forms.FrmExperiencia_Laboral1
    s_form_class = forms.FrmInstruccion_formal1
    sth_form_class = forms.FrmReferencias_Personales1

    success_url = reverse_lazy('lista_hoja_de_vida')

    def get_context_data(self, **kwargs):
        context = super(RegistrarHojaDeVidaAdmin,
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

    """ def get_queryset(self):
        base_qs = super(EditarEstudiante, self).get_queryset()
        return base_qs.get(user=self.request.user) """

    model = models.Estudiante
    second_model = User
    #form_class = forms.FrmEstudianteUpdate(user=get_queryset())
    form_class = forms.FrmEstudianteUpdate
    second_form_class = forms.FrmUserEd
    template_name = 'seguimiento/FrmEstudiante.html'
    success_url = reverse_lazy('lista_estudiante')

    def __init__(self, *args, **kwargs):
        super(EditarEstudiante, self).__init__(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(EditarEstudiante, self).get_context_data(**kwargs)

        pk1 = self.kwargs.get('pk', 0)
        est = self.model.objects.get(pk=pk1)
        user = self.second_model.objects.get(pk=est.user.pk)

        if 'form' not in context:
            context['form'] = self.form_class()

        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=user)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_est = kwargs['pk']
        est = self.model.objects.get(pk=id_est)
        user = self.second_model.objects.get(pk=est.user.pk)
        form = self.form_class(request.POST, instance=est)
        form2 = self.second_form_class(request.POST, instance=user)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))


class EditarMejorGraduado(UpdateView):
    model = models.Mejor_Graduado
    form_class = forms.FrmMejor_Graduado
    template_name = 'seguimiento/FrmMejor_Graduado.html'
    success_url = reverse_lazy('lista_mejor_graduado')


class EditarEmpresa(UpdateView):
    model = models.Empresa
    second_model = User
    form_class = forms.FrmEmpresa
    second_form_class = forms.FrmUserEmpEd
    template_name = 'seguimiento/FrmEmpresa.html'
    success_url = reverse_lazy('lista_empresa')

    def get_context_data(self, **kwargs):
        context = super(EditarEmpresa, self).get_context_data(**kwargs)
        pk1 = self.kwargs.get('pk', 0)
        emp = self.model.objects.get(pk=pk1)
        user = self.second_model.objects.get(pk=emp.user.pk)

        if 'form' not in context:
            context['form'] = self.form_class()

        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=user)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        pk = kwargs['pk']
        emp = self.model.objects.get(pk=pk)
        user = self.second_model.objects.get(pk=emp.user.pk)
        form = self.form_class(request.POST, instance=emp)
        form2 = self.second_form_class(request.POST, instance=user)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))


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


class EditarOfertaLaboralAdmin(UpdateView):
    model = models.Oferta_Laboral
    second_model = models.Informacion_laboral
    form_class = forms.FrmOferta_LaboralAdmin
    second_form_class = forms.FrmInformacion_laboral
    template_name = 'seguimiento/FrmOferta_Laboral.html'
    success_url = reverse_lazy('lista_oferta_laboral')

    def get_context_data(self, **kwargs):
        context = super(EditarOfertaLaboralAdmin,
                        self).get_context_data(**kwargs)
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

    def get_queryset(self, **kwargs):
        if not self.request.user.is_superuser:
            qs = super().get_queryset(**kwargs)
            try:
                return qs.filter(empresa_id=self.request.user.empresa.pk)
            except:
                return qs.all()
        else:
            qs = super().get_queryset(**kwargs)
            return qs.all()


class ListarOfertaLaboralIndex(ListView):
    model = models.Oferta_Laboral
    template_name = 'seguimiento/dashboard.html'

    def get_queryset(self, **kwargs):
        if not self.request.user.is_superuser:
            qs = super().get_queryset(**kwargs)
            try:
                return qs.filter(empresa_id=self.request.user.empresa.pk)
            except:
                return qs.all()
        else:
            qs = super().get_queryset(**kwargs)
            return qs.all()

###


class ListarOfertaLaboralTotal(ListView):
    model = models.Oferta_Laboral
    template_name = 'seguimiento/oferta_laboral.html'

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(pk=self.kwargs['pk'])

## ver estudiante postulado
class ListarHojaDeVidaEstudiante(ListView):
    model = models.Estudiante
    template_name = 'seguimiento/hoja_de_vida.html'

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(pk=self.kwargs['pk'])


class ListarEncuestaLaboral(ListView):
    model = models.Encuesta_Laboral
    template_name = 'seguimiento/ListaEncuesta_Laboral.html'


class ListarEleccion(ListView):
    model = models.Eleccion
    template_name = 'seguimiento/ListaEleccion.html'


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


# buscadores
@login_required
def SeleccionarOferta(request, pk):

    oferta = models.Oferta_Laboral.objects.get(pk=pk)

    estudiante = models.Estudiante.objects.get(pk=request.user.estudiante.pk)

    try:
        ofEst = estudiante.oferta.get(pk=pk)        
        estudiante.oferta.remove(oferta)
    except Exception as e:
        estudiante.oferta.add(oferta)
    

    return HttpResponseRedirect(reverse('lista_oferta_laboral_index',))
