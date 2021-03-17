# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from .models import CodeImages,Resource,Chemistry
from django.http import HttpResponseRedirect, Http404
# from django.shortcuts import render_to_response
from django.views.generic import DetailView

from datetime import date

from haystack.generic_views import SearchView

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
#     """      缂備胶濮崑鎾绘煕濡儤顥℃い鏇熺洴楠炲棝宕ㄥǎ顑藉亾閿燂拷     """
#     model = Resume
#     template_name ='resume_detail.html'
#     # success_url = '/joblist/'

def show_all_heros(request):
	all_heros = CodeImages.objects.all()

	# for index in all_heros:
	# 	print(index.name,index.hp_max,index.hp_growth)

	# 闂佽娴烽弫鎼侇敆閻栧潤_heroes闂佸搫顦弲婊呯矙閺嶎厹鈧線骞嬮敃鈧粈鍡涙煕閳╁啰鈼ら柍褜鍓ㄩ幏锟�
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


class MySearchView(SearchView):
	"""My custom search view."""
	template_name = 'search/search.html'
	
	def get_queryset(self):
		queryset = super(MySearchView, self).get_queryset()
		# further filter queryset based on some set of criteria
		return queryset
		# return queryset.filter(pub_date__gte=date(2015, 1, 1))

	def get_context_data(self, *args, **kwargs):
		context = super(MySearchView, self).get_context_data(*args, **kwargs)
		# do something
		return context

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
		error_msg = '闂佽崵濮村ú銊╁蓟婢跺本顐芥い鎾卞灩缁€鍌炴煏婢跺牆鍔氱憸鎵█濮婂搫鈻庨幆褎鐏曢梺浼欒閹凤拷'
		return render(request, '404.html', {'error_msg': error_msg,'q':q})

	return render(request, 'results.html', {'error_msg': error_msg,
											   'post_list': post_list})

def download(request):
	
	# q = request.GET.get('q')
	# error_msg = ''

	# if not q:
	# 	error_msg = '闂佽崵濮村ú銊╁蓟婢跺本顐芥い鎾卞灩缁€鍌炴煏婢跺牆鍔氱憸鎵█濮婂搫鈻庨幆褎鐏曢梺浼欒閹凤拷'
	# 	return render(request, '404.html', {'error_msg': error_msg})

	course_resources = Resource.objects.all()
	print(dir(course_resources))
	return render(request, 'download.html', {'course_resources': course_resources})
# locals闂備礁鎲￠悷锕傛晝閵忋倕闂繛宸簼閸庡秹鏌涢弴銊ヤ航婵炲瓨锕㈤弻锝夊焵椤掆偓婵″ジ鏌￠崪鍐╁!!
# def books(request):
#     ###  濠电偛顕慨瀵哥玻閸ｅシels闂備礁鎲￠悷锕傛偋濡ゅ懎姹查柣鏃傚帶缁犲弶銇勯弮鍥у惞闁绘劕锕︾槐鎾存媴閸︻厼鏄mplate  ###
#     n = Name.objects.all()
#     return render(request, 'bookslist.html', locals())

# fitter 闂備礁鎲￠崹鍏兼叏閵堝姹查柣鏂垮悑閸庡秹鏌涢弴銊ュ箺闁哄棗绻橀弻銊╂偆閸屾稑顏�?
 # 闂備浇顕栭崹浼村箠韫囨稑绀夐柛娑欐綑绾惧綊鏌熼鍡楀閳ь剨鎷�
# sent_avg =f" {T1.objects.aggregate(Avg('sentiment'))['sentiment__avg']:0.2f} "
# gte lte lt gt婵犵數鍋涢ˇ顓㈠礉瀹ュ绀堥柣妤€鐗忛埢鏃堟倵閿濆簼绨婚柣蹇擄功缁辨帡骞嗚娴犮垽鏌熼绛嬫疁婵☆偄鍟存慨鈧柕蹇ョ磿閺嗙娀姊洪悷鎵虎缂佸纾槐鐐烘晸閿燂拷
# # 婵犳鍠楃换鎰緤娴犲绠栨繝濠傜墕閺嬩礁霉閸忓吋缍戞繛鍜冩嫹
# queryset = T1.objects.values('sentiment')
# condtions = {'sentiment__gte': 0.5}
# plus = queryset.filter(**condtions).count()

# # 闂佽崵濮甸崝妤呭窗鎼淬劌绠栨繝濠傜墕閺嬩礁霉閸忓吋缍戞繛鍜冩嫹
# queryset = T1.objects.values('sentiment')
# condtions = {'sentiment__lt': 0.5}
# minus = queryset.filter(**condtions).count()
