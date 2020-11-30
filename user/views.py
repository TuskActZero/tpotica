from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView, FormView 
from django.urls import reverse_lazy
from django.contrib.auth import login, logout as do_logout
from .forms import SecretariaSignUpForm, GerenciaSignUpForm, VentasSignUpForm, ProfesionalSignUpForm, TallerSignUpForm, User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
# Create your views here.


# home basico

class home(TemplateView):
    template_name = 'home.html'

class SecretariaSignUpView(CreateView):
    model = User
    form_class = SecretariaSignUpForm
    template_name = 'registration/registro.html'

    def get_context_data(self, **kwargs):
        kwargs['sector'] = 'secretaria'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('secretaria')

class SecretariaHome(TemplateView):
    template_name = 'secretaria.html'

class SecretariaLogin(LoginView):
    redirect_field_name = 'secretaria'
    template_name = 'secretaria.html'

# ----------------------------------------

class GerenciaSignUpView(CreateView):
    model = User
    form_class = GerenciaSignUpForm
    template_name = 'registration/registro.html'

    def get_context_data(self, **kwargs):
        kwargs['sector'] = 'Gerencia'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('gerencia')

class GerenciaHome(TemplateView):
    template_name = 'gerencia.html'

#--------------------------------------

class VentasSignUpView(CreateView):
    model = User
    form_class = VentasSignUpForm
    template_name = 'registration/registro.html'

    def get_context_data(self, **kwargs):
        kwargs['sector'] = 'ventas'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('ventas')

class VentasHome(TemplateView):
    template_name = 'ventas.html'

class VentasLogin(LoginView):
    def get_success_url(self):
        user = self.request.user.username
        return reverse_lazy('ventas')

#--------------------------------------------

class ProfesionalSignUpView(CreateView):
    model = User
    form_class = ProfesionalSignUpForm
    template_name = 'registration/registro.html'

    def get_context_data(self, **kwargs):
        kwargs['sector'] = 'profesional'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('profesionales')

class ProfesionalHome(TemplateView):
    template_name = 'profesionales.html'


#------------------------------------------------------

class TallerSignUpView(CreateView):
    model = User
    form_class = TallerSignUpForm
    template_name = 'registration/registro.html'

    def get_context_data(self, **kwargs):
        kwargs['sector'] = 'taller'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('taller')

class TallerHome(TemplateView):
    template_name = 'taller.html'

#-----------------------------------------------

def logout(request):
    do_logout(request)
    return redirect('/')

