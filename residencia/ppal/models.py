# -*- encoding: utf-8 -*-
#encoding= utf-8
import os, sys

from django.db import models
from django.db.models.fields import PositiveIntegerField
from django.db.models.fields import PositiveSmallIntegerField
from django.db.models.fields import DateField
from parametricas.models import Tipo

class Especialidad(models.Model):
    codigo = PositiveIntegerField()
    nombre = models.CharField(max_length=50)
    cantidad_A = PositiveIntegerField('cantidad de Años')
    tipo = PositiveSmallIntegerField()
    class Meta:
	verbose_name = "Especialidad"
	verbose_name_plural = "Especialidades"

    def __unicode__(self):
        return self.nombre

class Localidad(models.Model):
    
    nombre = models.CharField(max_length=50)
    
    class Meta:
	verbose_name = "Localidad"        
	verbose_name_plural = "Localidades"

    def __unicode__(self):
        return self.nombre
    
class Institucion(models.Model):
   
    nombre = models.CharField(max_length=70)
    localidad = models.ForeignKey('Localidad')
    director = models.CharField(max_length=50)
    secretaria = models.CharField(max_length=50)
    telefonos = models.CharField(max_length=50)
    OtrosContactos = models.TextField('Otros Contactos', blank = True)
    class Meta:
	    verbose_name = "Institución"
	    verbose_name_plural = "Instituciones"
    	
    def __unicode__(self):
        return self.nombre
    
class ResidenciaAut(models.Model):
    tipo_choice = (
        ('C', 'Colegio'),
        ('M', 'Mixta'),    
    )
    tipoI_choice = (
        ('U', 'Pública'),
        ('P', 'Privada'),    
    )
    tipoInst= models.CharField(max_length=2, choices=tipoI_choice, blank = False, default='P')
    expediente =  models.CharField('N° de Expediente del Ministerio de Salud',max_length=12, null = True, blank = True, default='0-0-00',help_text='####-####/##')
    a_Comienzo =  PositiveSmallIntegerField('Año')
    especialidad = models.ForeignKey(Especialidad, related_name='+', null = True, blank = True)
    institucion =  models.ForeignKey('Institucion', related_name='+', null =  True, blank = True)
    cantA_1 = PositiveSmallIntegerField('1er. Año')
    cantA_2 = PositiveSmallIntegerField('2do. Año')
    cantA_3 = PositiveSmallIntegerField('3er. Año')
    cantA_4 = PositiveSmallIntegerField('4to. Año')
    jefeResidentes = PositiveSmallIntegerField('Jefe de Residentes')
    fechaEvaluacColMed = DateField('Fecha de Evaluación', blank = True, null = False)
    fechaEvaluacMixta = DateField('Fecha de Evaluación Mixta', blank = True, null = True)
    fechaCeseActividad = DateField('Fecha de Vencimiento Acreditación', blank = True, null = True)
    jefeServicio = models.CharField('Jefe de Servicio',max_length=50, blank = True, null = True)
    coordinador = models.CharField('Coordinador',max_length=50, blank = True, null = True)
    asesorDocente = models.CharField('Asesor Docente', max_length=150, blank = True)
    tipo = models.CharField(max_length=2, choices=tipo_choice, blank = True)
    memo = 	models.TextField('memo', null=True, blank=True)
    jefedocencia = models.CharField('Jefe Docencia', max_length=150, blank = True)
    instructor = 	models.CharField('Instructor de Residentes', max_length=150, blank=True)
    class Meta:
	verbose_name = "Residencia"        
	verbose_name_plural = "Residencias"
    ordering = ["a_Comienzo"]
    def getDirector(self):
        return self.institucion.director 
    getDirector.short_description = ("Director")   
    def get_absolute_url(self):
            return u'/edita/%d' % self.id 
    def __unicode__(self):
        return unicode(self.a_Comienzo)
    
    def fechaEvalNoNula(self):
        if not self.fechaEvaluacColMed:
            return ''
        else:
            return self.fechaEvaluacColMed.strftime("%d/%m/%Y")
    def fechaCeseActividadNoNula(self):
        if not self.fechaCeseActividad:
            return ''
        else:
            return self.fechaCeseActividad.strftime("%d/%m/%Y")
    def memoNoNulo(self):
        if not self.memo:
            return '.'
        else:
            return self.memo
    def nombreTipo(self):
        if self.tipo == 'C':
            return 'Colegio'
        else:
            return 'Mixto'      
    def sumaCantA(self):
        return self.cantA_1+self.cantA_2+self.cantA_3+self.cantA_4+self.jefeResidentes
    def sumaGral(self):
		return sum(self.cantA_1)
    def getInstitucion(self):
		if not self.institucion:
			return ''
		else:
		    return self.institucion.nombre
    def getEspecialidad(self):
		if not self.especialidad:
			return ''
		else:
			 return self.especialidad.nombre
    def getJefeServicio(self):
		if not self.jefeServicio:
			return ''
		else:
		    return self.jefeServicio
    def getJefeDocencia(self):
		if not self.jefedocencia:
			return ''
		else:
			 return self.jefedocencia
    def getAsesorDocente(self):
		if not self.asesorDocente:
			return ''
		else:
			 return self.asesorDocente
    def getCoordinador(self):
		if not self.coordinador:
			return ''
		else:
			 return self.coordinador
    def getInstructor(self):
	   if not self.instructor:
			return ''
	   else:
			 return self.instructor
  	 
class ResidenteManager(models.Manager):
    def most_current_for_date(self, date):
        return super(ResidenteManager, self).get_query_set()
            
class Residente(models.Model):    
   nombre = models.CharField(max_length=50)
   apellido = models.CharField(max_length=50)
   tipoR = models.IntegerField()   
   residencia= models.ForeignKey(ResidenciaAut, related_name='+') 
   active = ResidenteManager()
   def __unicode__(self):
        return unicode(self.nombre +" " +self.apellido)
   def getInstitucion(self):
	   return self.residencia.institucion
	   
   def getEspecialidad(self):
	   return self.residencia.especialidad
