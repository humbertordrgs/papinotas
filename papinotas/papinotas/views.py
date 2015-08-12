from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
# Create your views here.

def autenticar(request):
	if request.POST:
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
		    if user.is_active:
		        login(request, user)
		        return HttpResponseRedirect(request.GET.get('next','/papiSMS'))
		        # Redirect to a success page.
		    else:
		        # Return a 'disabled account' error message
		       return ""
		else:
			return ""
def pony(request):
	if(request.GET):
		return  HttpResponse(request.GET)