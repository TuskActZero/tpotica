from django.contrib import admin
from .models import User, Paciente, Profesional, Ventas, Gerencia, Taller, Turno , HistorialMedico, Pedido, Lente, Secretaria
 
#  Register your models here.
 
class UserAdmin(admin.ModelAdmin):
    model = User
    field = '__all__'

class PacienteAdmin(admin.ModelAdmin):
    model = Paciente
    field = '__all__'

class SecretariaAdmin(admin.ModelAdmin):
    model = Secretaria
    field = '__all__'


admin.site.register(User, UserAdmin)
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Secretaria, SecretariaAdmin)