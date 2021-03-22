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
#     """      缂傚倷鑳舵慨顓㈠磻閹剧粯鐓曟俊顖滃劋椤モ剝銇勯弴鐔烘创妤犵偛妫濆畷銊デ庨钘変壕闁跨噦鎷�     """
#     model = Resume
#     template_name ='resume_detail.html'
#     # success_url = '/joblist/'

def show_all_heros(request):
	all_heros = CodeImages.objects.all()

	# for index in all_heros:
	# 	print(index.name,index.hp_max,index.hp_growth)

	# 闂備浇顕уù鐑藉极閹间緡鏁嗛柣鏍ф饯_heroes闂備礁鎼ˇ顐﹀疾濠婂懐鐭欓柡宥庡幑閳ь兛绶氶獮瀣晝閳ь剛绮堥崱娑欑厱闁斥晛鍟伴埣銈夋煃瑜滈崜銊╁箯閿燂拷
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
		error_msg = '闂備浇宕垫慨鏉懨洪妸鈺佽摕濠㈣泛鏈鑺ャ亜閹惧崬鐏╃紒鈧崒鐐寸厪濠㈣泛鐗嗛崝姘辨喐閹殿喖鈻堟慨濠傛惈閳诲酣骞嗚閻忔洟姊烘导娆掝吅闁瑰嚖鎷�'
		return render(request, '404.html', {'error_msg': error_msg,'q':q})

	return render(request, 'results.html', {'error_msg': error_msg,
											   'post_list': post_list})

def download(request):
	
	# q = request.GET.get('q')
	# error_msg = ''

	# if not q:
	# 	error_msg = '闂備浇宕垫慨鏉懨洪妸鈺佽摕濠㈣泛鏈鑺ャ亜閹惧崬鐏╃紒鈧崒鐐寸厪濠㈣泛鐗嗛崝姘辨喐閹殿喖鈻堟慨濠傛惈閳诲酣骞嗚閻忔洟姊烘导娆掝吅闁瑰嚖鎷�'
	# 	return render(request, '404.html', {'error_msg': error_msg})

	course_resources = Resource.objects.all()
	print(dir(course_resources))
	return render(request, 'download.html', {'course_resources': course_resources})
# locals闂傚倷绀侀幉锟犳偡閿曞倹鏅濋柕蹇嬪€曢梻顖涚箾瀹割喕绨奸柛搴＄Ч閺屾盯寮撮妸銉よ埅濠电偛鐡ㄩ敃銏ゅ蓟閿濆鐒垫い鎺嗗亾濠碘€炽偢閺岋繝宕崘鈺侇伓!!
# def books(request):
#     ###  婵犵數鍋涢顓熸叏鐎靛摜鐜婚柛锝呫偡els闂傚倷绀侀幉锟犳偡閿曞倹鍋嬫俊銈呮噹濮规煡鏌ｉ弮鍌氬付缂佺姴寮堕妵鍕籍閸パ冩優闂佺粯鍔曢敃锔炬閹惧瓨濯撮柛锔诲幖閺勵櫕mplate  ###
#     n = Name.objects.all()
#     return render(request, 'bookslist.html', locals())

# fitter 闂傚倷绀侀幉锟犲垂閸忓吋鍙忛柕鍫濐槸濮规煡鏌ｉ弬鍨倯闁稿骸绉归弻娑㈠即閵娿儱绠洪梺鍝勬缁绘﹢寮婚妸鈺傚亞闁稿本绋戦锟�?
 # 闂傚倷娴囬鏍垂娴兼潙绠犻煫鍥ㄧ☉缁€澶愭煕濞戞瑦缍戠痪鎯х秺閺岀喖顢涢崱妤€顏╅柍褜鍓ㄩ幏锟�
# sent_avg =f" {T1.objects.aggregate(Avg('sentiment'))['sentiment__avg']:0.2f} "
# gte lte lt gt濠电姷鏁搁崑娑⑺囬銏犵鐎广儱顦粈鍫ユ煟濡も偓閻楀繘鍩㈤弮鍫熷€甸柨婵嗙凹缁ㄥ鏌ｈ箛鎿勫姛缂佽鲸甯￠獮鍡氼槾濞寸姰鍨介弻鐔碱敊缁涘鐤佸┑鈽嗗亜閸熷瓨鎱ㄩ埀顒勬煏韫囥儳纾块柡鍡欏█濮婃椽鎮烽幍顔昏檸缂備礁顦壕顓犳閻愮儤鏅搁柨鐕傛嫹
# # 濠电姵顔栭崰妤冩崲閹邦喖绶ゅù鐘差儏缁犳牗绻濇繝鍌滃闁哄绀侀湁闁稿繐鍚嬬紞鎴炵箾閸滃啯瀚�
# queryset = T1.objects.values('sentiment')
# condtions = {'sentiment__gte': 0.5}
# plus = queryset.filter(**condtions).count()

# # 闂備浇宕垫慨鐢稿礉濡ゅ懎绐楅幖娣妼缁犳牗绻濇繝鍌滃闁哄绀侀湁闁稿繐鍚嬬紞鎴炵箾閸滃啯瀚�
# queryset = T1.objects.values('sentiment')
# condtions = {'sentiment__lt': 0.5}
# minus = queryset.filter(**condtions).count()
