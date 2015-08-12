from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import *
from django.template.context_processors import csrf
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
import requests
# Create your views here.

@login_required
def Send(request,tipo,dat):
	if(request.POST):
		ls=[]
		i=1

		alum= [x.split("_")[1]for x in request.POST if "user_" in x] #kawaii
		for e in alum:
			us=Alumno.objects.get(pk=e)
			ls.append({"Mobile":us.numero, "Message":request.POST['content']})

		payload = {'username': 'papitest5', 'password': 'clavetest2','data':json.dumps(ls)}
		headers = {'content-type': 'application/x-www-form-urlencoded'}
		r = requests.post("http://52.3.188.254/Send.php", headers=headers,data=payload)
		return HttpResponse(r)

	else:

		if(tipo=="colegio"):
			cursos=Curso.objects.filter(colegio=dat)
		elif(tipo=="curso"):
			cursos=Curso.objects.filter(pk=dat)
		else:
			curso=Alumno.objects.get(pk=dat)
		
		if(tipo!="alumno"):
			res=[]
			for e in cursos:
				res+=Alumno.objects.filter(curso=e)
			return render(request, 'papiSMS/send.html', {'data':res})
		else:
			
			return render(request, 'papiSMS/send.html', {'data':[curso]})
			
@login_required	
def ColegioIndex(request):
	if request.user.is_authenticated():
		colegios_list = Colegio.objects.all()
		context = {'colegios_list': colegios_list}
		return render(request, 'papiSMS/colegios_index.html', context)

@login_required
def ColegioDetail(request,colegio_id):
	cursos_list = Curso.objects.filter(colegio=colegio_id)
	context = {'cursos_list': cursos_list}
	return render(request, 'papiSMS/colegios_detail.html', context)

@login_required
def CursoDetail(request,colegio_id,curso_id):
	alumnos_list = Alumno.objects.filter(curso=curso_id)
	context = {'alumnos_list': alumnos_list}
	return render(request, 'papiSMS/cursos_detail.html', context)

@login_required
def AlumnoDetail(request,colegio_id,curso_id,alumno_id):
	context = {'alumno': Alumno.objects.get(id=alumno_id)}
	return render(request, 'papiSMS/alumnos_detail.html', context)	


