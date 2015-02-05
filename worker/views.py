from django.shortcuts import render, get_object_or_404
from worker.models import Worker, Mall, MallWorker, Agency
from django.http import Http404
#/workers -- index
## link to all workers
## link to all agencies
## link to all malls

def index(request):
	context = {'hello': 'hello'}
	return render(request, 'worker/index.html', context)

def workers_index(request):
	workers_all = Worker.objects.all()
	context = {'objects': workers_all}
	return render(request,'worker/workers_all.html', context)

def workers(request):
	workers_all = Worker.objects.all()
	context = {'objects': workers_all}
	return render(request,'worker/workers_all.html', context)

def workers_solo(request, worker_id):
	worker = get_object_or_404(Worker, pk=worker_id)
	context = {'object': worker}
	return render(request,'worker/workers_solo.html', context)

def workers_search(request, search):
	pass

def mall(request):
	malls = Mall.objects.all()
	context = {'objects': malls}
	return render(request, 'mall/malls.html', context)

def mall_solo(request, mall_id):
	mall = get_object_or_404(Mall, pk=mall_id)
	name_of_mall = mall.mall
	#workers = MallWorker.objects.filter(mall.mall='blox')
	workers = MallWorker.objects.filter(mall__mall=name_of_mall)

	#mall = Mall.objects.get(pk=mall_id)
	context = {
	'objects': workers,
	'mall':mall,
	}
	return render(request, 'mall/mall_solo.html', context)

def agency(request):
	agencies = Agency.objects.all()
	context = { 'objects' : agencies}
	return render(request, 'agency/agency_all.html', context)

def agency_solo(request, agency_id):
	agency = get_object_or_404(Agency, pk=agency_id)
	
	context = {'object': agency}
	return render(request, 'agency/agency_solo.html', context)


# workers all
#/workers/w
## Specific worker
#workers/w/id

# all malls
#workers/m
## specific mall
# /workers/m/id

# all agency
## /workers/a
## specific agency
# /workers/a/id