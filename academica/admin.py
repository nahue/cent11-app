from django.contrib import admin
from models import Titulo, Carrera, Materia, Documento, Persona, Rol
from .forms import PersonaForm

class PersonaAdmin(admin.ModelAdmin):
  form = PersonaForm
  fieldsets = (
    ('Datos Personales', {
      'fields': ('roles',
                 'titulos',
                 'materias',
                 'codigo',
                 ('nombre',
                 'apellido'),
                 'documento_tipo',
                 'documento_numero',
                 'sexo',
                 'nacimiento_fecha',
                 'nacimiento_pais',
                 'nacimiento_provincia',
                 'nacimiento_ciudad',
                 'foto',
                 'fecha_alta',
                 'fecha_baja',
                 'titulo_secundario',
                 'observacion'
      )
    }),
    ('Contacto', {
      'classes': ('collapse','extrapretty'),
      'fields': ('email','domicilio','telefono')
    })
  )
  list_display = ('apellido','nombre','documento_numero')
  list_filter = ('roles','documento_tipo','nacimiento_pais','sexo')
  search_fields = ['apellido','nombre','documento_numero']
  filter_horizontal = ('roles','titulos')
  radio_fields = {'sexo': admin.HORIZONTAL}

  class Media:
    css = {
      'all': ('css/admin/persona_admin.css',)
    }

class CarreraAdmin(admin.ModelAdmin):
  pass

class MateriaAdmin(admin.ModelAdmin):
  filter_horizontal = ('docentes',)

class RolAdmin(admin.ModelAdmin):
  fields = ('nombre', 'personas')

admin.site.register(Titulo)
admin.site.register(Carrera, CarreraAdmin)
admin.site.register(Materia, MateriaAdmin)
admin.site.register(Documento)
admin.site.register(Rol)
admin.site.register(Persona, PersonaAdmin)
