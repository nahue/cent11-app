# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Carrera'
        db.create_table(u'academica_carrera', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(default='', max_length=30)),
            ('nombre_corto', self.gf('django.db.models.fields.CharField')(default='', max_length=10)),
            ('codigo', self.gf('django.db.models.fields.CharField')(default='', max_length=10)),
            ('fecha_desde', self.gf('django.db.models.fields.DateField')(null=True)),
            ('fecha_hasta', self.gf('django.db.models.fields.DateField')(null=True)),
            ('resolucion_plan', self.gf('django.db.models.fields.CharField')(default='', max_length=30)),
        ))
        db.send_create_signal(u'academica', ['Carrera'])

        # Adding model 'Materia'
        db.create_table(u'academica_materia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(default='', max_length=30)),
            ('nombre_corto', self.gf('django.db.models.fields.CharField')(default='', max_length=10)),
            ('codigo', self.gf('django.db.models.fields.CharField')(default='', max_length=10)),
            ('duracion', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('horas_catedra', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('anio', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('cursadas_para_cursar', self.gf('django.db.models.fields.CharField')(default='', max_length=30, blank=True)),
            ('aprobadas_para_cursar', self.gf('django.db.models.fields.CharField')(default='', max_length=30, blank=True)),
            ('cursadas_para_rendir', self.gf('django.db.models.fields.CharField')(default='', max_length=30, blank=True)),
            ('aprobadas_para_rendir', self.gf('django.db.models.fields.CharField')(default='', max_length=30, blank=True)),
            ('carrera', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['academica.Carrera'], null=True, blank=True)),
        ))
        db.send_create_signal(u'academica', ['Materia'])

        # Adding model 'Documento'
        db.create_table(u'academica_documento', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal(u'academica', ['Documento'])

        # Adding model 'Rol'
        db.create_table(u'academica_rol', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'academica', ['Rol'])

        # Adding model 'Persona'
        db.create_table(u'academica_persona', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('codigo', self.gf('django.db.models.fields.CharField')(default='', max_length=10)),
            ('nombre', self.gf('django.db.models.fields.CharField')(default='', max_length=30)),
            ('apellido', self.gf('django.db.models.fields.CharField')(default='', max_length=30)),
            ('documento_tipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['academica.Documento'])),
            ('documento_numero', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('nacimiento_fecha', self.gf('django.db.models.fields.DateField')()),
            ('nacimiento_pais', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('nacimiento_provincia', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('nacimiento_ciudad', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('domicilio', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('sexo', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('fecha_alta', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('fecha_baja', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('titulo_secundario', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('observacion', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('foto', self.gf('django.db.models.fields.files.ImageField')(default='imagenes/default/alumnos/alumno_default.jpg', max_length=100)),
        ))
        db.send_create_signal(u'academica', ['Persona'])

        # Adding M2M table for field roles on 'Persona'
        m2m_table_name = db.shorten_name(u'academica_persona_roles')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('persona', models.ForeignKey(orm[u'academica.persona'], null=False)),
            ('rol', models.ForeignKey(orm[u'academica.rol'], null=False))
        ))
        db.create_unique(m2m_table_name, ['persona_id', 'rol_id'])


    def backwards(self, orm):
        # Deleting model 'Carrera'
        db.delete_table(u'academica_carrera')

        # Deleting model 'Materia'
        db.delete_table(u'academica_materia')

        # Deleting model 'Documento'
        db.delete_table(u'academica_documento')

        # Deleting model 'Rol'
        db.delete_table(u'academica_rol')

        # Deleting model 'Persona'
        db.delete_table(u'academica_persona')

        # Removing M2M table for field roles on 'Persona'
        db.delete_table(db.shorten_name(u'academica_persona_roles'))


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
            'foto': ('django.db.models.fields.files.ImageField', [], {'default': "'imagenes/default/alumnos/alumno_default.jpg'", 'max_length': '100'}),
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
        }
    }

    complete_apps = ['academica']