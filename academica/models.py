# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext as _


class Titulo(models.Model):

    SECUNDARIO = 1
    TERCIARIO = 2
    UNIVERSITARIO = 3
    POSTGRADO = 4

    NIVEL = (
        (SECUNDARIO, 'Secundario'),
        (TERCIARIO, 'Terciario'),
        (UNIVERSITARIO, 'Universitario'),
        (POSTGRADO, 'PostGrado')
    )

    nombre = models.CharField(max_length=100, default='')
    nombre_institucion = models.CharField(max_length=200, default='')
    nivel = models.IntegerField(max_length=1, choices=NIVEL, default=0)


class Carrera(models.Model):
    nombre = models.CharField(max_length=200, default='')
    nombre_corto = models.CharField(max_length=100, default='')
    codigo = models.CharField(max_length=10, default='', unique=True)
    fecha_desde = models.DateField(null=True, blank=True)
    fecha_hasta = models.DateField(null=True, blank=True)
    resolucion_plan = models.CharField(max_length=30, default='', blank=True)

    def __str__(self):
        return self.nombre + ' [' + self.codigo + ']'


class Documento(models.Model):
    tipo = models.CharField(max_length=40)

    def __str__(self):
        return self.tipo


class Rol(models.Model):
    nombre = models.CharField(max_length=20)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Roles"


class Persona(models.Model):
    SEXO = (
        ('M', 'Masculino'),
        ('F', 'Femenino')
    )
    codigo = models.CharField(max_length=10, default='', blank=True)
    nombre = models.CharField(max_length=30, default='')
    apellido = models.CharField(max_length=30, default='')
    documento_tipo = models.ForeignKey(Documento)
    documento_numero = models.CharField(
        max_length=15,
        verbose_name="Nro Documento")
    nacimiento_fecha = models.DateField(_('nacimiento_fecha'))
    nacimiento_pais = models.CharField(
        verbose_name=_('nacimiento_pais'),
        max_length=30,
        blank=True)
    nacimiento_provincia = models.CharField(
        verbose_name=_('nacimiento_provincia'),
        max_length=30,
        blank=True)
    nacimiento_ciudad = models.CharField(
        verbose_name=_('nacimiento_ciudad'),
        max_length=30,
        blank=True)
    email = models.EmailField()
    domicilio = models.CharField(max_length=30)
    telefono = models.CharField(max_length=15)
    sexo = models.CharField(max_length=1, choices=SEXO)
    fecha_alta = models.DateField(
        verbose_name=_('fecha_alta'),
        null=True,
        blank=True)
    fecha_baja = models.DateField(null=True, blank=True)
    titulo_secundario = models.CharField(max_length=30)
    observacion = models.TextField(blank=True, null=True)
    foto = models.ImageField(
        upload_to='imagenes/alumnos/',
        default='imagenes/default/alumnos/alumno_default.jpg',
        blank=True)
    roles = models.ManyToManyField(Rol)
    titulos = models.ManyToManyField(Titulo, blank=True)

    def nombre_completo(self):
        return self.nombre + ' ' + self.apellido

    def __unicode__(self):
        return self.nombre_completo()


class Materia(models.Model):
    CUATRIMESTRAL = 1
    ANUAL = 2
    MATERIA_DURACION = (
        (CUATRIMESTRAL, 'Cuatrimestral'),
        (ANUAL, 'Anual'),
    )
    nombre = models.CharField(max_length=30, default='')
    nombre_corto = models.CharField(max_length=10, default='')
    codigo = models.CharField(max_length=10, default='', unique=True)
    duracion = models.IntegerField(choices=MATERIA_DURACION, default=0)
    horas_catedra = models.IntegerField(default=0)
    anio = models.IntegerField(default=0, verbose_name="Año")
    cursadas_para_cursar = models.CharField(
        max_length=30,
        default='',
        blank=True)
    aprobadas_para_cursar = models.CharField(
        max_length=30,
        default='',
        blank=True)
    cursadas_para_rendir = models.CharField(
        max_length=30,
        default='',
        blank=True)
    aprobadas_para_rendir = models.CharField(
        max_length=30,
        default='',
        blank=True)
    carrera = models.ForeignKey(Carrera, blank=True, null=True, default=0)
    docentes = models.ManyToManyField(Persona)

    def __unicode__(self):
        return self.nombre + ' [' + self.codigo + ']'
