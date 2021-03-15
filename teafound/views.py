# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from .models import Heros,CodeImages,Resource
# from django.shortcuts import render_to_response
from django.views.generic import DetailView

import datetime

# Create your views here.
def index(request):

	return render(request,'index.html')

def about(request):
    
	return render(request,'about.html')

def chemDetail(request):
	now = datetime.datetime.now()
	html = "<html><body>It is now %s.</body></html>" % now
	return HttpResponse(html)


def detail(request, job_id):
    try:
        job = Job.objects.get(pk=job_id)
        job.city_name = Cities[job.job_city][1]
        # logger.info('job retrieved from db :%s' % job_id)
    except Job.DoesNotExist:
        raise Http404("Job does not exist")
    return render(request, 'job.html', {'job': job})

# class ResumeDetailView(DetailView):
#     """      绠€鍘嗚鎯呴〉     """
#     model = Resume
#     template_name ='resume_detail.html'
#     # success_url = '/joblist/'

def show_all_heros(request):
	all_heros = CodeImages.objects.all()

	# for index in all_heros:
	# 	print(index.name,index.hp_max,index.hp_growth)

	# 鐎电ll_heroes鏉╂稖顢戦崚鍡涖€�
	try:
		page = request.GET.get('page', 10)
	except PageNotAnInteger:
		page = 1

	# objects = ['john', 'edward', 'josh', 'frank']

	# Provide Paginator with the request object for complete querystring generation

	# p = Paginator(objects, request=request)

	p = Paginator(all_heros,per_page = 2, request=request)
	page_heros = p.page(page)


	# print(all_heros)
	# html = "<html><body>It is now %s.</body></html>" % all_heros[0].name,all_heros[0].hp_max,all_heros[0].hp_growth

	return render(request,'tables.html',{
		'page_heros': page_heros,
		})


def show_some_images(request):
	all_images = CodeImages.objects.all()
	for index in all_images:
		print(index.chemstructcode,index.structure,index.EntryName)
	# print(all_images)
	# html = "<html><body>It is now %s.</body></html>" % all_images[0].name,all_images[0].hp_max,all_images[0].hp_growth
	return render(request,'showimages.html',{'all_images': all_images})

def search(request):

	q = request.GET.get('q')
	error_msg = ''
	try:
		post_list = Heros.objects.get(name__icontains=q)
	except Exception as error:
		print(error)
		return render(request, '404.html', {'error_msg': error_msg,'q':q})
	print(post_list)
	if not q:
		error_msg = '鐠囩柉绶崗銉ュ彠闁款喛鐦�'
		return render(request, '404.html', {'error_msg': error_msg,'q':q})


	return render(request, 'results.html', {'error_msg': error_msg,
											   'post_list': post_list})

def download(request):
    
	# q = request.GET.get('q')
	# error_msg = ''

	# if not q:
	# 	error_msg = '鐠囩柉绶崗銉ュ彠闁款喛鐦�'
	# 	return render(request, '404.html', {'error_msg': error_msg})

	course_resources = Resource.objects.all()
	print(dir(course_resources))
	return render(request, 'download.html', {'course_resources': course_resources})
# locals閸欐﹢鍣洪惃鍕浘閻€劌鏅�!!
# def books(request):
#     ###  娴犲窇odels閸欐牗鏆熼幑顔荤炊缂佹獩emplate  ###
#     n = Name.objects.all()
#     return render(request, 'bookslist.html', locals())

# fitter 閸戣姤鏆熼惃鍕暏閿燂拷?
 # 閹懏鍔呴崐鎯ф倻
# sent_avg =f" {T1.objects.aggregate(Avg('sentiment'))['sentiment__avg']:0.2f} "
# gte lte lt gt濞夈劍鍓版稉瀣灊缁惧灝鎮楅棃銏㈡畱閹垮秳缍�
# # 濮濓絽鎮滈弫浼村櫤
# queryset = T1.objects.values('sentiment')
# condtions = {'sentiment__gte': 0.5}
# plus = queryset.filter(**condtions).count()

# # 鐠愮喎鎮滈弫浼村櫤
# queryset = T1.objects.values('sentiment')
# condtions = {'sentiment__lt': 0.5}
# minus = queryset.filter(**condtions).count()
