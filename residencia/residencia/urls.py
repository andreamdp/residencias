# -*- encoding: utf-8 -*-
"""residencia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import include, url,patterns 
from django.contrib import admin
from ppal.views import *
from ppal.vResidencias import *
admin.autodiscover()

urlpatterns = patterns('',
  url(r'form/$', formulario), 
  url(r'reporteGral/(?P<ano>\d+)$', formulariob), 
 # url(r'reporteGral/(?P<ano>\d+)print/$', formularioPrint),
 # url(r'reporte/2012/$', residencias2012),
  url(r'reporte/2012print/$',residencias2012Print),
 # url(r'reporte/2013/$', residencias2013),
  url(r'reporte/2013print/$',residencias2013Print),
 # url(r'reporte/2014/$', residencias2014),
  url(r'reporte/2014print/$', residencias2014Print),
 # url(r'reporte/2015/$', residencias2015),
  url(r'reporte/2015print/$',residencias2015Print), 
 # url(r'reporte/2016/$', residencias2016),
  url(r'reporte/2016print/$',residencias2016Print),
  url(r'cantidad/$',residenciasCant2016), 
 # url(r'cantidad/$',formularioCant),
  url(r'2016Cantprint/$',residenciasCant2016Print), 
  url(r'reporteA_evaluacion/$',aEvaluacion),
  url(r'evalPrint/$',aEvaluacionPrint),
  url(r'detallado/$',residenciaDet),
  url(r'detalladoprint/$',residenciaDetPrint),
  url(r'^ppal/residenciaaut/(?P<residenciaaut_id>\d+)/lista/residente_edit1/(?P<residente_id>\d+)/$', residente_edit1),
  url(r'^ppal/residenciaaut/(?P<residenciaaut_id>\d+)/lista/residente_edit2/(?P<residente_id>\d+)/$', residente_edit2),
  url(r'^ppal/residenciaaut/(?P<residenciaaut_id>\d+)/lista/residente_edit3/(?P<residente_id>\d+)/$', residente_edit3),
  url(r'^ppal/residenciaaut/(?P<residenciaaut_id>\d+)/lista/residente_edit4/(?P<residente_id>\d+)/$', residente_edit4),
  url(r'^ppal/residenciaaut/(?P<residenciaaut_id>\d+)/lista/residente_delete/(?P<residente_id>\d+)/$',residente_delete),
  url(r'(?P<residenciaaut_id>\d+)/residente1/$', residente1_add),
  url(r'(?P<residenciaaut_id>\d+)/residente2/$', residente2_add),
  url(r'(?P<residenciaaut_id>\d+)/residente3/$', residente3_add),
  url(r'(?P<residenciaaut_id>\d+)/residente4/$', residente4_add),
  url(r'(?P<residenciaaut_id>\d+)/jefeResidente/$', jefeResidente_add),
  url(r'^ppal/residenciaaut/(?P<residenciaaut_id>\d+)/lista/$', residente_list,name='residente_list'),
  url(r'(?P<residenciaaut_id>\d+)/listaR/$', residente_listPrint,name='residente_listPrint'),
  url(r'(?P<residenciaaut_id>\d+)/ficha/$', detail,name='detalle'),
  url('', include(admin.site.urls)),
#]
)
admin.site.site_header = 'Residencias Colegio de Médicos IX Distrito'
