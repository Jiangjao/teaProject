# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from .models import CodeImages,Resource,Chemistry
from django.http import HttpResponseRedirect, Http404
# from django.shortcuts import render_to_response
from django.views.generic import DetailView

import datetime

# Create your views here.
def index(request):

	return render(request,'index.html')

def about(request):
    
	return render(request,'about.html')

def chemDetail(request,cid):
	try:
		Chemicial = Chemistry.objects.get(pk=cid)
		print(Chemicial.molecularweight)
	except Chemicial.DoesNotExist:
		raise Http404("Chemicial does not exist")
	return render(request, 'chem_detail.html', {'Chemicial': Chemicial})



def detail(request, job_id,Job,Cities):
    try:
        job = Job.objects.get(pk=job_id)
        job.city_name = Cities[job.job_city][1]
        # logger.info('job retrieved from db :%s' % job_id)
    except Job.DoesNotExist:
        raise Http404("Job does not exist")
    return render(request, 'job.html', {'job': job})

# class ResumeDetailView(DetailView):
#     """      缁犫偓閸樺棜顕涢幆鍛淬€�     """
#     model = Resume
#     template_name ='resume_detail.html'
#     # success_url = '/joblist/'

def show_all_heros(request):
	all_heros = CodeImages.objects.all()

	# for index in all_heros:
	# 	print(index.name,index.hp_max,index.hp_growth)

	# 閻庣數顒爈l_heroes閺夆晜绋栭、鎴﹀礆閸℃稏鈧拷
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
		post_list = CodeImages.objects.get(name__icontains=q)
	except Exception as error:
		print(error)
		return render(request, '404.html', {'error_msg': error_msg,'q':q})
	print(post_list)
	if not q:
		error_msg = '閻犲洨鏌夌欢顓㈠礂閵夈儱褰犻梺娆惧枦閻︼拷'
		return render(request, '404.html', {'error_msg': error_msg,'q':q})


	return render(request, 'results.html', {'error_msg': error_msg,
											   'post_list': post_list})

def download(request):
    
	# q = request.GET.get('q')
	# error_msg = ''

	# if not q:
	# 	error_msg = '閻犲洨鏌夌欢顓㈠礂閵夈儱褰犻梺娆惧枦閻︼拷'
	# 	return render(request, '404.html', {'error_msg': error_msg})

	course_resources = Resource.objects.all()
	print(dir(course_resources))
	return render(request, 'download.html', {'course_resources': course_resources})
# locals闁告瑦锕㈤崳娲儍閸曨偒娴橀柣鈧妼閺咃拷!!
# def books(request):
#     ###  濞寸姴绐噊dels闁告瑦鐗楅弳鐔煎箲椤旇崵鐐婄紓浣圭崺emplate  ###
#     n = Name.objects.all()
#     return render(request, 'bookslist.html', locals())

# fitter 闁告垼濮ら弳鐔兼儍閸曨厽鏆忛柨鐕傛嫹?
 # 闁诡垰鎳忛崝鍛村磹閹勫€�
# sent_avg =f" {T1.objects.aggregate(Avg('sentiment'))['sentiment__avg']:0.2f} "
# gte lte lt gt婵炲鍔嶉崜鐗堢▔鐎ｎ亜鐏婄紒鎯х仢閹妫冮姀銏＄暠闁瑰灝绉崇紞锟�
# # 婵繐绲介幃婊堝极娴兼潙娅�
# queryset = T1.objects.values('sentiment')
# condtions = {'sentiment__gte': 0.5}
# plus = queryset.filter(**condtions).count()

# # 閻犳劗鍠庨幃婊堝极娴兼潙娅�
# queryset = T1.objects.values('sentiment')
# condtions = {'sentiment__lt': 0.5}
# minus = queryset.filter(**condtions).count()
