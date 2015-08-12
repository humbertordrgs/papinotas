from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
	
	url(r'^$', views.ColegioIndex, name='ColegioIndex'),
	url(r'^send/(?P<tipo>[a-z]+)/(?P<dat>.+)*$', views.Send, name='Send'),
	url(r'^colegios/(?P<colegio_id>[0-9]+)/$', views.ColegioDetail, name='ColegioDetail'),
	url(r'^colegios/(?P<colegio_id>[0-9]+)/cursos/(?P<curso_id>[0-9]+)/$', views.CursoDetail, name='CursoDetail'),
	url(r'^colegios/(?P<colegio_id>[0-9]+)/cursos/(?P<curso_id>[0-9]+)/alumnos/(?P<alumno_id>[0-9]+)$', views.AlumnoDetail, name='AlumnoDetail'),

] 