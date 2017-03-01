# -*- encoding: utf-8 -*-
#encoding= utf-8
from ppal.models import ResidenciaAut
from django.db.models import Sum
from django.shortcuts import render_to_response
from ppal.forms import *
from django.shortcuts import render
totalGral = ResidenciaAut.objects.all().aggregate(Sum('cantA_1'))
total2Gral= ResidenciaAut.objects.all().aggregate(Sum('cantA_2'))
total3Gral= ResidenciaAut.objects.all().aggregate(Sum('cantA_3'))
total4Gral= ResidenciaAut.objects.all().aggregate(Sum('cantA_4'))
totalJefeGral= ResidenciaAut.objects.all().aggregate(Sum('jefeResidentes'))
def aEvaluacion(request,template_name='ppal/ListadoResidencias.html'):
    residencia_list = ResidenciaAut.objects.all().order_by('fechaEvaluacColMed','institucion')
    tot=0
    for r in residencia_list:
         tot = tot+ r.jefeResidentes + r.cantA_1 + r.cantA_2+r.cantA_3+r.cantA_4
    totres=0
    for r in residencia_list:
         totres = totres+  r.cantA_1 + r.cantA_2+r.cantA_3+r.cantA_4
    return render_to_response(template_name, {
        'residencias': residencia_list,
        'titulo':'Colegio de Médicos IX Distrito',
        'suma1':totalGral,
        'suma2':total2Gral,
        'suma3':total3Gral,
        'suma4':total4Gral,
        'sumaJefe':totalJefeGral,
        'sumatotal':tot,
        'sumaResidentes':totres,
        'milink':'../evalPrint',
     }) 
def aEvaluacionPrint(request,template_name='ppal/ListadoResidenciasPrint.html'):
    residencia_list = ResidenciaAut.objects.all().order_by('-fechaEvaluacColMed')
    tot=0
    for r in residencia_list:
         tot = tot+ r.jefeResidentes + r.cantA_1 + r.cantA_2+r.cantA_3+r.cantA_4
    totres=0
    for r in residencia_list:
         totres = totres+  r.cantA_1 + r.cantA_2+r.cantA_3+r.cantA_4
    return render_to_response(template_name, {
        'residencias': residencia_list,
        'titulo':'Colegio de Médicos IX Distrito',
        'suma1':totalGral,
        'suma2':total2Gral,
        'suma3':total3Gral,
        'suma4':total4Gral,
        'sumaJefe':totalJefeGral,
        'sumatotal':tot,
        'sumaResidentes':totres,
        'milink':'../evalPrint',
     }) 
def residenciaDet(request,template_name='ppal/ListadoResidenciasDetallado.html'):
    residencia_list = ResidenciaAut.objects.all().order_by('-a_Comienzo','institucion')
    tot=0
    for r in residencia_list:
         tot = tot+ r.jefeResidentes + r.cantA_1 + r.cantA_2+r.cantA_3+r.cantA_4
    totres=0
    for r in residencia_list:
         totres = totres+  r.cantA_1 + r.cantA_2+r.cantA_3+r.cantA_4
    return render_to_response(template_name, {
        'residencias': residencia_list,
        'titulo':'Colegio de Médicos IX Distrito',
        'milink':'../detalladoprint',
        'suma1':totalGral,
        'suma2':total2Gral,
        'suma3':total3Gral,
        'suma4':total4Gral,
        'sumaJefe':totalJefeGral,
        'sumatotal': tot,
        'sumaResidentes':totres,
     })
def residenciaDetPrint(request,template_name='ppal/ListadoResidenciasDetalladoPrint.html'):
    residencia_list = ResidenciaAut.objects.all().order_by('-a_Comienzo','institucion')
    tot=0
    for r in residencia_list:
         tot = tot+ r.jefeResidentes + r.cantA_1 + r.cantA_2+r.cantA_3+r.cantA_4
    totres=0
    for r in residencia_list:
         totres = totres+  r.cantA_1 + r.cantA_2+r.cantA_3+r.cantA_4
    return render_to_response(template_name, {
        'residencias': residencia_list,
        'titulo':'Colegio de Médicos IX Distrito',
        
        'suma1':totalGral,
        'suma2':total2Gral,
        'suma3':total3Gral,
        'suma4':total4Gral,
        'sumaJefe':totalJefeGral,
        'sumatotal': tot,
        'sumaResidentes':totres,
     })
total = ResidenciaAut.objects.filter(a_Comienzo=2016).aggregate(Sum('cantA_1'))
total2= ResidenciaAut.objects.filter(a_Comienzo=2016).aggregate(Sum('cantA_2'))
total3= ResidenciaAut.objects.filter(a_Comienzo=2016).aggregate(Sum('cantA_3'))
total4= ResidenciaAut.objects.filter(a_Comienzo=2016).aggregate(Sum('cantA_4'))
totalJres=ResidenciaAut.objects.filter(a_Comienzo=2016).aggregate(Sum('jefeResidentes'))     
def residenciasCant2016(request,template_name='ppal/ListadoResidenciasCantidad.html' ):
    residencia_list = ResidenciaAut.objects.filter(a_Comienzo=2016).order_by('a_Comienzo','institucion')
    
    tot=0
    for r in residencia_list:
         tot = tot+ r.jefeResidentes + r.cantA_1 + r.cantA_2+r.cantA_3+r.cantA_4
    totres=0
    for r in residencia_list:
         totres = totres+  r.cantA_1 + r.cantA_2+r.cantA_3+r.cantA_4
    return render_to_response(template_name, {
        'residencias': residencia_list,
        'suma1':total,
        'suma2':total2,
        'suma3':total3,
        'suma4':total4,
        'sumaJefe':totalJres,
        'sumatotal':tot,
        'sumaResidentes':totres,
        'titulo':'2016',
        'milink':'../2016Cantprint',
    })
       
def residenciasCant2016Print(request,template_name='ppal/ListadoResidenciasCantidadPrint.html' ):
    residencia_list = ResidenciaAut.objects.filter(a_Comienzo=2016).order_by('a_Comienzo','institucion')
    tot=0
    for r in residencia_list:
         tot = tot+ r.jefeResidentes + r.cantA_1 + r.cantA_2+r.cantA_3+r.cantA_4
    totres=0
    for r in residencia_list:
         totres = totres+  r.cantA_1 + r.cantA_2+r.cantA_3+r.cantA_4
    
    return render_to_response(template_name, {
        'residencias': residencia_list,
        'titulo':'Colegio de Médicos IX Distrito',
        'suma1':total,
        'suma2':total2,
        'suma3':total3,
        'suma4':total4,
        'sumaJefe':totalJres,
        'sumatotal': tot,
        'sumaResidentes':totres,
     })
def formularioCant(request ):
    if request.method == 'POST':
       
        form = AForm(request.POST)
        if form.is_valid():
      
          return render_to_response('ppal/ListadoResidenciasCantidadPrint.html', {'a':form.cleaned_data['ano'],'link':'/reporteGral/3'})
        else: 
           return render(request, 'ppal/ListadoResidenciasCantidadPrint.html', {'a':0,'form': form,'link':'/reporteGral/2'})
    else:
        form = AForm()
        return render(request, 'ppal/ListadoResidenciasCantidadPrint.html', {'a':0,'form': form,'link':'/reporteGral/1'})

def formulariobCant(request,ano ):
   
    if request.method == 'POST':
        form = AForm(request.POST)
        if form.is_valid():
          ano = form.cleaned_data['ano']
          residencia_list = ResidenciaAut.objects.filter(a_Comienzo=ano).order_by('a_Comienzo','institucion')
          total1 = ResidenciaAut.objects.filter(a_Comienzo=ano).aggregate(Sum('cantA_1'))
          total2 = ResidenciaAut.objects.filter(a_Comienzo=ano).aggregate(Sum('cantA_2'))
          total3 =ResidenciaAut.objects.filter(a_Comienzo=ano).aggregate(Sum('cantA_3'))
          total4 = ResidenciaAut.objects.filter(a_Comienzo=ano).aggregate(Sum('cantA_4')) 
          totalJres=ResidenciaAut.objects.filter(a_Comienzo=ano).aggregate(Sum('jefeResidentes'))
          tot=0
          for r in residencia_list:
             tot = tot+ r.jefeResidentes + r.cantA_1 + r.cantA_2+r.cantA_3+r.cantA_4
          totres=0
          for r in residencia_list:
             totres = totres+  r.cantA_1 + r.cantA_2+r.cantA_3+r.cantA_4
          return render_to_response('ppal/ListadoResidenciasCantidadPrint.html', {
             'residencias': residencia_list,
             'titulo':'2013',
             'milink':'reporte/'+ano+'print',
             'suma1':total1,
             'suma2':total2,
             'suma3':total3,
             'suma4':total4,
             'sumaJefe':totalJres,
             'sumatotal':tot,
             'sumaResidentes':totres,
           })

        else: 
          return render(request, 'ppal/ListadoResidenciasCantidadPrint.html', {'a':0,'form': form,'link':'/form/'})
    else:
        form = AForm()
        return render(request, 'ppal/ListadoResidenciasCantidadPrint.html', {'a':0,'form': form,'link':'/form/'})
        residencia_list = ResidenciaAut.objects.filter(a_Comienzo=a).order_by('a_Comienzo','institucion')
        total1 = ResidenciaAut.objects.filter(a_Comienzo=ano).aggregate(Sum('cantA_1'))
        total2 = ResidenciaAut.objects.filter(a_Comienzo=ano).aggregate(Sum('cantA_2'))
        total3 =ResidenciaAut.objects.filter(a_Comienzo=ano).aggregate(Sum('cantA_3'))
        total4 = ResidenciaAut.objects.filter(a_Comienzo=ano).aggregate(Sum('cantA_4')) 
        totalJres=ResidenciaAut.objects.filter(a_Comienzo=ano).aggregate(Sum('jefeResidentes'))
        return render_to_response('ppal/ListadoResidenciasCantidadPrint.html', {
             'residencias': residencia_list,
             'titulo':'2013',
             'milink':'../2013print',
             'suma1':total1,
             'suma2':total2,
             'suma3':total3,
             'suma4':total4,
             'sumaJefe':totalJres,
         })
