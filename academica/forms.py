from django import forms
from django.utils.safestring import mark_safe
from django.contrib.admin import ModelAdmin
from .models import Persona, Materia
from django.contrib.admin.widgets import FilteredSelectMultiple
from suit.widgets import SuitDateWidget
import pdb

class MateriasWidget(forms.widgets.Select):

  def __init__(self, attrs=None, choices=()):
    super(MateriasWidget, self).__init__(attrs)



  def render(self, name, value, attrs=None, choices=()):
    html = "<ul>"
    for choice in self.choices:
      html = html + "<li>" + choice.nombre + "</li>"
    html = html + "</ul>"
    return mark_safe(html);

  def setinstance(self, instance):
    self.instance = instance
    self.choices = Materia.objects.filter(docentes__id=self.instance.id)


class PersonaForm(forms.ModelForm):

  def __init__(self, *args, **kwargs):
    self.instance_id = None
    super(PersonaForm, self).__init__(*args, **kwargs)
    #self.fields['name'].required = False

    if kwargs.has_key('instance'):
        instance = kwargs['instance']

        self.fields['materias'].widget.setinstance(instance)
        if self.fields['materias'].widget.choices.count() == 0:
          self.fields['materias'].widget = forms.HiddenInput()
        #self.instance_id = instance.id
        # do something with the instance here if you want

  materias = forms.ChoiceField(choices=[],
    widget=MateriasWidget)

  class Meta:
    widgets = {
		  'fecha_alta': SuitDateWidget,
		  'fecha_baja': SuitDateWidget,
      }
    model = Persona
