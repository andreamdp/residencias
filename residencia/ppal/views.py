# -*- encoding: utf-8 -*-
#encoding= utf-8
from django.shortcuts import render
from django.views.generic.base import TemplateView
from ppal.models import ResidenciaAut
from ppal.forms import *
from django.views import generic
from django.views.generic import UpdateView,CreateView 
from django.views.generic.list import ListView
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import redirect
from django import template
from django.shortcuts import get_object_or_404
register = template.Library()  

def detail(request, residenciaaut_id):
    try:
        residencia = ResidenciaAut.objects.get(pk=residenciaaut_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'admin/ppal/residenciaaut/ficha.html', {'residencia': residencia})
def residente_listPrint(request,residenciaaut_id,template_name='admin/ppal/residente/printList.html' ):
    residentes_list = Residente.active.filter(residencia_id=residenciaaut_id).order_by('tipoR')
    return render_to_response(template_name, {
        'residentes': residentes_list,
        'idR:': request.user.is_authenticated(),
        'residencia': ResidenciaAut.objects.filter(id=residenciaaut_id)
    })
def residente_list(request,residenciaaut_id,template_name='admin/ppal/residente/list.html' ):
    residentes_list = Residente.active.filter(residencia_id=residenciaaut_id).order_by('tipoR')
    return render_to_response(template_name, {
        'residentes': residentes_list,
        'idR:': request.user.is_authenticated(),
        'residencia': ResidenciaAut.objects.filter(id=residenciaaut_id)
    })
def residente_edit1(request,residenciaaut_id, residente_id):
    residente = get_object_or_404(Residente, pk=residente_id)
    form = ResidenteForm1(request.POST or None, instance=residente)
    if form.is_valid():
        residente = form.save()
        return redirect('/ppal/residenciaaut/'+residenciaaut_id+'/lista/')

    return render_to_response('admin/ppal/residente/edit.html',
                              {'form': form,
                               'residente_id': residente_id},
                              context_instance=RequestContext(request))
def residente_edit2(request,residenciaaut_id, residente_id):
    residente = get_object_or_404(Residente, pk=residente_id)
    form = ResidenteForm2(request.POST or None, instance=residente)
    if form.is_valid():
        residente = form.save()
        return redirect('/ppal/residenciaaut/'+residenciaaut_id+'/lista/')

    return render_to_response('admin/ppal/residente/edit.html',
                              {'form': form,
                               'residente_id': residente_id},
                              context_instance=RequestContext(request))
def residente_edit3(request,residenciaaut_id, residente_id):
    residente = get_object_or_404(Residente, pk=residente_id)
    form = ResidenteForm3(request.POST or None, instance=residente)
    if form.is_valid():
        residente = form.save()
        return redirect('/ppal/residenciaaut/'+residenciaaut_id+'/lista/')

    return render_to_response('admin/ppal/residente/edit.html',
                              {'form': form,
                               'residente_id': residente_id},
                              context_instance=RequestContext(request))
def residente_edit4(request,residenciaaut_id, residente_id):
    residente = get_object_or_404(Residente, pk=residente_id)
    form = ResidenteForm4(request.POST or None, instance=residente)
    if form.is_valid():
        residente = form.save()
        return redirect('/ppal/residenciaaut/'+residenciaaut_id+'/lista/')

    return render_to_response('admin/ppal/residente/edit.html',
                              {'form': form,
                               'residente_id': residente_id},
                              context_instance=RequestContext(request))							  
def residente_delete(request,residenciaaut_id, residente_id):
    residente = get_object_or_404(Residente, pk=residente_id)
    residente.delete()
    return redirect('/ppal/residenciaaut/'+residenciaaut_id+'/lista/')

@csrf_protect
@register.inclusion_tag('ppal/residente/add.html', takes_context=True)
def residente1_add(request, residenciaaut_id,form_class=ResidenteForm1, template_name='ppal/residente/add.html'):
    if request.POST:
        form = form_class(request.POST)
        if form.is_valid():
            residente = form.save()
            return redirect('residente_list',residenciaaut_id)
    else:
       form = ResidenteForm1(initial={'residencia': residenciaaut_id})  
    return render_to_response(template_name,{'form':form,'idResidencia':residenciaaut_id},context_instance=RequestContext(request))

@csrf_protect
def residente2_add(request, residenciaaut_id,form_class=ResidenteForm2, template_name='admin/ppal/residente/add.html'):
    if request.POST:
        form = form_class(request.POST)
        if form.is_valid():
            residente = form.save()
            return redirect('residente_list',residenciaaut_id)
    else:
       form = ResidenteForm2(initial={'residencia': residenciaaut_id})
    return render_to_response(template_name,{'form':form,'idResidencia':residenciaaut_id},context_instance=RequestContext(request))   
@csrf_protect

def residente3_add(request, residenciaaut_id,form_class=ResidenteForm3, template_name='admin/ppal/residente/add.html'):
    if request.POST:
        form = form_class(request.POST)
        if form.is_valid():
            residente = form.save()
            return redirect('residente_list',residenciaaut_id)
    else:
       form = ResidenteForm3(initial={'residencia': residenciaaut_id})
    return render_to_response(template_name,{'form':form,'idResidencia':residenciaaut_id},context_instance=RequestContext(request))
@csrf_protect

def residente4_add(request, residenciaaut_id,form_class=ResidenteForm4, template_name='admin/ppal/residente/add.html'):
    if request.POST:
        form = form_class(request.POST)
        if form.is_valid():
            residente = form.save()
            return redirect('residente_list',residenciaaut_id)
    else:
       form = ResidenteForm4(initial={'residencia': residenciaaut_id})
    return render_to_response(template_name,{'form':form,'idResidencia':residenciaaut_id},context_instance=RequestContext(request))

@csrf_protect
def jefeResidente_add(request, residenciaaut_id,form_class=JefeResidenteForm, template_name='admin/ppal/residente/add.html'):
    if request.POST:
        form = form_class(request.POST)
        if form.is_valid():
            residente = form.save()
            return redirect('residente_list',residenciaaut_id)
    else:
       form = JefeResidenteForm(initial={'residencia': residenciaaut_id})
    return render_to_response(template_name,{'form':form,'idResidencia':residenciaaut_id},context_instance=RequestContext(request))   

# ========================                R E S I D E N C I A S       =============================================
from django.db.models import Sum
from django.db.models import F
total = ResidenciaAut.objects.filter(a_Comienzo=2016).aggregate(Sum('cantA_1'))
total2= ResidenciaAut.objects.filter(a_Comienzo=2016).aggregate(Sum('cantA_2'))
total3= ResidenciaAut.objects.filter(a_Comienzo=2016).aggregate(Sum('cantA_3'))
total4= ResidenciaAut.objects.filter(a_Comienzo=2016).aggregate(Sum('cantA_4'))
totalJres=ResidenciaAut.objects.filter(a_Comienzo=2016).aggregate(Sum('jefeResidentes'))

def formulario(request ):
    if request.method == 'POST':
       
        form = AForm(request.POST)
        if form.is_valid():
      
          return render_to_response('ppal/resporyear.html', {'a':form.cleaned_data['ano'],'link':'/reporteGral/3'})
        else: 
           return render(request, 'ppal/resporyear.html', {'a':0,'form': form,'link':'/reporteGral/2'})
    else:
        form = AForm()
        return render(request, 'ppal/resporyear.html', {'a':0,'form': form,'link':'/reporteGral/1'})

def formulariob(request,ano ):
   
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
          return render_to_response('ppal/ListadoResidencias.html', {
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
          return render(request, 'ppal/resporyear.html', {'a':0,'form': form,'link':'/form/'})
    else:
        form = AForm()
        return render(request, 'ppal/resporyear.html', {'a':0,'form': form,'link':'/form/'})
        residencia_list = ResidenciaAut.objects.filter(a_Comienzo=a).order_by('a_Comienzo','institucion')
        total1 = ResidenciaAut.objects.filter(a_Comienzo=ano).aggregate(Sum('cantA_1'))
        total2 = ResidenciaAut.objects.filter(a_Comienzo=ano).aggregate(Sum('cantA_2'))
        total3 =ResidenciaAut.objects.filter(a_Comienzo=ano).aggregate(Sum('cantA_3'))
        total4 = ResidenciaAut.objects.filter(a_Comienzo=ano).aggregate(Sum('cantA_4')) 
        totalJres=ResidenciaAut.objects.filter(a_Comienzo=ano).aggregate(Sum('jefeResidentes'))
        return render_to_response('ppal/ListadoResidencias.html', {
             'residencias': residencia_list,
             'titulo':'2013',
             'milink':'../2013print',
             'suma1':total1,
             'suma2':total2,
             'suma3':total3,
             'suma4':total4,
             'sumaJefe':totalJres,
         })
'''def formularioPrint(request,ano ):     
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
      return render_to_response('ppal/ListadoResidencias.html', {
             'residencias': residencia_list,
             'titulo':'2013',
             'milink':'../2013print',
             'suma1':total1,
             'suma2':total2,
             'suma3':total3,
             'suma4':total4,
             'sumaJefe':totalJres,
         })
   '''  
     # return render_to_response('ppal/ListadoResidenciasPrint.html', {
      #  'residencias': residencia_list, }) 
        #'titulo':'Colegio de Médicos IX Distrito',
        #'suma1':total1,
        #'suma2':total2,
        #'suma3':total3,
        #'suma4':total4,
        #'sumaJefe':totalJres,
        #'sumatotal': tot,
        #'sumaResidentes':totres,   
        


def residencias2016Print(request,template_name='ppal/ListadoResidenciasPrint.html' ):
    residencia_list = ResidenciaAut.objects.filter(a_Comienzo=2016).order_by('a_Comienzo','institucion')
    return render_to_response(template_name, {
        'residencias': residencia_list,
        'titulo':'2016',
        'suma1':total,
        'suma2':total2,
        'suma3':total3,
        'suma4':total4,
       # 'sumatotal':total+total2+total3+total4,
    })
total2015 = ResidenciaAut.objects.filter(a_Comienzo=2015).aggregate(Sum('cantA_1'))
total22015= ResidenciaAut.objects.filter(a_Comienzo=2016).aggregate(Sum('cantA_2'))
total32015= ResidenciaAut.objects.filter(a_Comienzo=2015).aggregate(Sum('cantA_3'))
total42015= ResidenciaAut.objects.filter(a_Comienzo=2015).aggregate(Sum('cantA_4'))

def residencias2015Print(request,template_name='ppal/ListadoResidenciasPrint.html' ):
    residencia_list = ResidenciaAut.objects.filter(a_Comienzo=2015).order_by('a_Comienzo','institucion')
    return render_to_response(template_name, {
        'residencias': residencia_list,
        'titulo':'2015',
        'suma1':total2015,
        'suma2':total22015,
        'suma3':total32015,
        'suma4':total42015,
    })
total2014 = ResidenciaAut.objects.filter(a_Comienzo=2014).aggregate(Sum('cantA_1'))
total22014= ResidenciaAut.objects.filter(a_Comienzo=2014).aggregate(Sum('cantA_2'))
total32014= ResidenciaAut.objects.filter(a_Comienzo=2014).aggregate(Sum('cantA_3'))
total42014= ResidenciaAut.objects.filter(a_Comienzo=2014).aggregate(Sum('cantA_4'))

def residencias2014Print(request,template_name='ppal/ListadoResidenciasPrint.html' ):
    residencia_list = ResidenciaAut.objects.filter(a_Comienzo=2014).order_by('a_Comienzo','institucion')
    return render_to_response(template_name, {
        'residencias': residencia_list,
        'titulo':'2014',
        'suma1':total2014,
        'suma2':total22014,
        'suma3':total32014,
        'suma4':total42014,
    })
total2013 = ResidenciaAut.objects.filter(a_Comienzo=2013).aggregate(Sum('cantA_1'))
total22013= ResidenciaAut.objects.filter(a_Comienzo=2013).aggregate(Sum('cantA_2'))
total32013= ResidenciaAut.objects.filter(a_Comienzo=2013).aggregate(Sum('cantA_3'))
total42013= ResidenciaAut.objects.filter(a_Comienzo=2013).aggregate(Sum('cantA_4'))

def residencias2013Print(request,template_name='ppal/ListadoResidenciasPrint.html' ):
    residencia_list = ResidenciaAut.objects.filter(a_Comienzo=2013).order_by('a_Comienzo','institucion')
    return render_to_response(template_name, {
        'residencias': residencia_list,
        'titulo':'../2013',
        'suma1':total2013,
        'suma2':total22013,
        'suma3':total32013,
        'suma4':total42013,
    })
total2012 = ResidenciaAut.objects.filter(a_Comienzo=2012).aggregate(Sum('cantA_1'))
total22012= ResidenciaAut.objects.filter(a_Comienzo=2012).aggregate(Sum('cantA_2'))
total32012= ResidenciaAut.objects.filter(a_Comienzo=2012).aggregate(Sum('cantA_3'))
total42012= ResidenciaAut.objects.filter(a_Comienzo=2012).aggregate(Sum('cantA_4'))

def residencias2012Print(request,template_name='ppal/ListadoResidenciasPrint.html' ):
    residencia_list = ResidenciaAut.objects.filter(a_Comienzo=2012).order_by('a_Comienzo','institucion')
    return render_to_response(template_name, {
        'residencias': residencia_list,
        'titulo':'2012',
        'suma1':total2012,
        'suma2':total22012,
        'suma3':total32012,
        'suma4':total42012,
    })




