from django.contrib import admin
from worker.models import *
from biometric.models import Biometric



class BiometricInLine(admin.StackedInline):
	model = Biometric
	extra = 0

class EmploymentInline(admin.TabularInline):
	model = Employment
	extra = 0

class SeminarInline(admin.TabularInline):
	model = Seminar
	extra = 0

class SchoolInline(admin.TabularInline):
	model = School
	extra = 0

class ChildrenInline(admin.TabularInline):
	model = Children
	extra = 0

class SpouseInline(admin.TabularInline):
	model = Spouse
	extra = 0

class MallWorkerInline(admin.TabularInline):
	model = MallWorker
	extra = 0

class WorkerAdmin(admin.ModelAdmin):

	list_filter = ['date_added', 'firstname']

	list_display= [
		'id','lastname','firstname', 'date_added',
		'agency','get_mall'
	]
	list_display_links = ['agency']
	search_fields = ['lastname', 'firstname']
	inlines = [
		EmploymentInline, SeminarInline,
		SchoolInline, SpouseInline, 
		ChildrenInline, BiometricInLine,
		MallWorkerInline
	]

class MallWorkerAdmin(admin.ModelAdmin):
	list_filter = ['mall__mall']
	list_display = ['id','mall','worker',]
	list_display_links = ['mall', 'worker']
	search_fields = ['worker__firstname', 'mall__mall']


admin.site.register(Worker, WorkerAdmin)
admin.site.register(MallWorker, MallWorkerAdmin)
admin.site.register(Mall)
admin.site.register(Agency)
