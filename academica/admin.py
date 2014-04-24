from django.contrib import admin
from models import Titulo, Carrera, Materia, Documento, Persona, Rol
from .forms import PersonaForm
from django import forms

class PersonaAdmin(admin.ModelAdmin):
  form = PersonaForm
  fieldsets = (
    ('Datos Personales', {
      'fields': (
                 ('documento_tipo','documento_numero'),
                 ('apellido','nombre'),
                 'codigo',
                 'roles',
                 'titulos',
                 'materias',
                 
                 
                 
                 
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
  list_display = ('documento_numero','apellido','nombre','fecha_alta','nacimiento_fecha')
  list_filter = ('roles','documento_tipo','nacimiento_pais','sexo')
  search_fields = ['apellido','nombre','documento_numero']
  filter_horizontal = ('titulos',)
  radio_fields = {'sexo': admin.HORIZONTAL}

  def formfield_for_manytomany(self, db_field, request=None, **kwargs):
    if db_field.name == 'roles':
        kwargs['widget'] = forms.CheckboxSelectMultiple
        kwargs['help_text'] = ''

    return db_field.formfield(**kwargs)

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
