from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http  import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required


def account_login(request):
	if not request.user.is_authenticated():
		context = {'hello': 'hello'}
		if request.POST:
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponseRedirect('/')
				else:
					return HttpResponse('User account not active')
			else:
				return HttpResponse('Invalid Login')
		else:
			return render(request, 'account/login.html', context)
	else:
		return HttpResponseRedirect('/')

@login_required
def account_logout(request):
	logout(request)
	return HttpResponse('<h1>Logged Out</h1>')
