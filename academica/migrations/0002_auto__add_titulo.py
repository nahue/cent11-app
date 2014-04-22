# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Titulo'
        db.create_table(u'academica_titulo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('nombre_institucion', self.gf('django.db.models.fields.CharField')(default='', max_length=200)),
            ('nivel', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
        ))
        db.send_create_signal(u'academica', ['Titulo'])


    def backwards(self, orm):
        # Deleting model 'Titulo'
        db.delete_table(u'academica_titulo')


    models = {
        u'academica.carrera': {
            'Meta': {'object_name': 'Carrera'},
            'codigo': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'fecha_desde': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'fecha_hasta': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'nombre_corto': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'resolucion_plan': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'})
        },
        u'academica.documento': {
            'Meta': {'object_name': 'Documento'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'academica.materia': {
            'Meta': {'object_name': 'Materia'},
            'anio': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'aprobadas_para_cursar': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30', 'blank': 'True'}),
            'aprobadas_para_rendir': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30', 'blank': 'True'}),
            'carrera': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'to': u"orm['academica.Carrera']", 'null': 'True', 'blank': 'True'}),
            'codigo': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'cursadas_para_cursar': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30', 'blank': 'True'}),
            'cursadas_para_rendir': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30', 'blank': 'True'}),
            'duracion': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'horas_catedra': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'nombre_corto': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'})
        },
        u'academica.persona': {
            'Meta': {'object_name': 'Persona'},
            'apellido': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'codigo': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'documento_numero': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'documento_tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['academica.Documento']"}),
            'domicilio': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'fecha_alta': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_baja': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'foto': ('django.db.models.fields.files.ImageField', [], {'default': "'imagenes/default/alumnos/alumno_default.jpg'", 'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nacimiento_ciudad': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'nacimiento_fecha': ('django.db.models.fields.DateField', [], {}),
            'nacimiento_pais': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'nacimiento_provincia': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'observacion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'roles': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['academica.Rol']", 'symmetrical': 'False'}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'titulo_secundario': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'academica.rol': {
            'Meta': {'object_name': 'Rol'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'academica.titulo': {
            'Meta': {'object_name': 'Titulo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nivel': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'nombre': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'nombre_institucion': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'})
        }
    }

    complete_apps = ['academica']