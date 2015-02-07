from django.shortcuts import render
from worker.models import Worker, Agency, Mall
from django.db.models import Q

def index(request):
	query = 'Hello'
	context = {'hello': query}
	if 'q' in request.GET:
		query = request.GET['q']
		workers = Worker.objects.filter(Q(firstname__icontains=query) | Q(lastname__icontains=query) | Q(security_license_number__icontains=query) | Q(sex__icontains=query))
		malls = Mall.objects.filter(Q(mall__icontains=query))
		#agencies = Agency.objects.filter(Q(agency__icontains))


		context['hello'] = query
		context['workers'] = workers
		context['malls'] = malls
		context['searching'] = True



	return render(request, 'search/index.html', context)

def search(request):
    query = request.GET['q']
    t = loader.get_template('template/results.html')
    c = Context({ 'query': query,})
    return HttpResponse(t.render(c))