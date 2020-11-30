from django.urls import path, include
from .views import SecretariaSignUpView, VentasSignUpView, GerenciaSignUpView, TallerSignUpView, ProfesionalSignUpView, home, SecretariaHome, ProfesionalHome, TallerHome, VentasHome, GerenciaHome, LoginView, SecretariaLogin, VentasLogin

urlpatterns = [
    path('', home.as_view(), name='home'),
    path('accounts/signup/secretaria/', SecretariaSignUpView.as_view(), name='secretaria_signup'),
    path('secretaria', SecretariaHome.as_view(), name='secretaria'),
    path('accounts/profile/secretaria', SecretariaLogin.as_view(), name='loginsecretaria'),
    path('accounts/signup/ventas/', VentasSignUpView.as_view(), name='ventas_signup'),
    path('ventas', VentasHome.as_view(), name='ventas'),
    path('ventas', VentasLogin.as_view(), name='loginventas'),
    path('accounts/signup/gerencia/', GerenciaSignUpView.as_view(), name='gerencia_signup'),
    path('gerencia', SecretariaHome.as_view(), name='gerencia'),
    path('accounts/signup/taller/', TallerSignUpView.as_view(), name='taller_signup'),
    path('taller', SecretariaHome.as_view(), name='taller'),
    path('accounts/signup/profesionales/', ProfesionalSignUpView.as_view(), name='profesionales_signup'),
    path('profesionales', SecretariaHome.as_view(), name='profesionales'),
]
