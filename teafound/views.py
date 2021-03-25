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
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

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
#     """      缂傚倸鍊烽懗鑸垫叏椤撱垹纾婚柟鍓х帛閻撴洘淇婇婊冨妺妞ゃ儮鍓濋妵鍕即閻旂儤鍒涘Δ鐘靛仜濡繂鐣烽妸銉囧酣顢栭挊澶夊闂佽法鍣﹂幏锟�     """
#     model = Resume
#     template_name ='resume_detail.html'
#     # success_url = '/joblist/'

def show_all_heros(request):
	all_heros = CodeImages.objects.all()

	# for index in all_heros:
	# 	print(index.name,index.hp_max,index.hp_growth)

	# 闂傚倷娴囬褍霉閻戣棄鏋侀柟闂寸贰閺佸棝鏌ｉ弽褎楗痏heroes闂傚倷绀侀幖顐λ囬锕€鐤炬繝濠傛噽閻瑩鏌″搴″箲闁逞屽厸缁舵岸鐛€ｎ喗鏅濋柍褜鍓涚划鍫ュ幢濞戞瑧鍘遍梺鏂ユ櫅閸熶即鍩ｉ妶澶嬬厓鐟滄粓宕滈妸鈺佺闁跨噦鎷�
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
		# logger.info("%s has been found",queryset)
		return queryset
		# return queryset.filter(pub_date__gte=date(2015, 1, 1))

	def get_context_data(self, *args, **kwargs):
		context = super(MySearchView, self).get_context_data(*args, **kwargs)
		logger.info("%s has been found",context)
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
		error_msg = '闂傚倷娴囧畷鍨叏閺夋嚚娲Ω閳轰浇鎽曟繝銏ｆ硾閺堫剟顢曢懞銉ｄ簻闁规儳宕悘鈺冪磼閳ь剟宕掗悙瀵稿帾婵犮垼娉涢悧鍡涘礉濮樿鲸鍠愰柟娈垮枛閳诲牊鎱ㄦ繝鍌涙儓闁宠閰ｉ獮鍡氼槼闁诲繑娲熷鐑樺濞嗘帩鍚呴梺鐟板殩閹凤拷'
		return render(request, '404.html', {'error_msg': error_msg,'q':q})

	return render(request, 'results.html', {'error_msg': error_msg,
											   'post_list': post_list})

def download(request):
	
	# q = request.GET.get('q')
	# error_msg = ''

	# if not q:
	# 	error_msg = '闂傚倷娴囧畷鍨叏閺夋嚚娲Ω閳轰浇鎽曟繝銏ｆ硾閺堫剟顢曢懞銉ｄ簻闁规儳宕悘鈺冪磼閳ь剟宕掗悙瀵稿帾婵犮垼娉涢悧鍡涘礉濮樿鲸鍠愰柟娈垮枛閳诲牊鎱ㄦ繝鍌涙儓闁宠閰ｉ獮鍡氼槼闁诲繑娲熷鐑樺濞嗘帩鍚呴梺鐟板殩閹凤拷'
	# 	return render(request, '404.html', {'error_msg': error_msg})

	course_resources = Resource.objects.all()
	print(dir(course_resources))
	return render(request, 'download.html', {'course_resources': course_resources})
# locals闂傚倸鍊风粈渚€骞夐敓鐘冲仭闁挎洖鍊归弲婵嬫煏韫囧鈧洟姊婚娑氱鐎瑰壊鍠曠花濂告煕鎼达紕效闁哄本鐩鎾Ω閵夈倛鍩呮繝鐢靛仜閻°劑鏁冮姀銈呰摕闁挎繂顦悞鍨亜閹哄棗浜炬繝纰樷偓鐐藉仮闁哄矉绻濆畷顏堝礃閳轰緡浼�!!
# def books(request):
#     ###  濠电姷鏁搁崑娑㈩敋椤撶喐鍙忛悗闈涙憸閻滃鏌涢敐鍛仭els闂傚倸鍊风粈渚€骞夐敓鐘冲仭闁挎洖鍊归崑瀣繆閵堝懏鍣规慨瑙勭叀閺岋綁寮崒姘粯缂備胶濮村鍫曞Φ閸曨垰绫嶉柛銉戝啯鍎梻浣虹帛閸旀洟鏁冮敂鐐潟闁规儳鐡ㄦ刊鎾煕閿旇骞栭柡鍕垫珪mplate  ###
#     n = Name.objects.all()
#     return render(request, 'bookslist.html', locals())

# fitter 闂傚倸鍊风粈渚€骞夐敓鐘插瀭闁稿繐鍚嬮崣蹇涙煏閸繍妲告慨瑙勭叀閺岋綁寮崹顔藉€梺绋块缁夊綊寮诲☉銏犲嵆闁靛ǹ鍎辩粻娲⒑閸濆嫭顥滅紒缁橈耿瀵濡搁埡鍌氫簽闂佺ǹ鏈粙鎴︻敂閿燂拷?
 # 闂傚倸鍊峰ù鍥敋閺嶎厼鍨傚ù鍏兼綑缁犵娀鐓崶銊р槈缂佲偓婢舵劖鐓曟繛鎴炵懄缂嶆垹鐥幆褏绉洪柡宀€鍠栭、娑㈠幢濡も偓椤忊晠鏌嶈閸撱劑骞忛敓锟�
# sent_avg =f" {T1.objects.aggregate(Avg('sentiment'))['sentiment__avg']:0.2f} "
# gte lte lt gt婵犵數濮烽弫鎼佸磻濞戔懞鍥敇閵忕姷顦悗骞垮劚椤︻垳绮堥崼銉︾厽婵°倐鍋撻柣妤€绻橀崺銏ゅ籍閸喎鈧敻鏌ㄥ┑鍡欏嚬缂併劌顭烽弻锝堢疀閹垮嫬濮涚紓浣介哺鐢繝鐛崱姘兼Ь婵炲濮伴崹浠嬪蓟閻旂⒈鏁婄紒娑橆儐閻や礁鈹戦埥鍡椾簻闁哥喎鐡ㄩ幈銊╁焵椤掑嫭鐓忛煫鍥ュ劤绾惧潡鏌￠崱娆忊枅婵﹥妞介幃鐑藉箥椤旀槒妾哥紓鍌欑椤︻垳澹曢鐘愁潟闁绘劗鍎ら弲鎼佹煥閻曞倹瀚�
# # 婵犵數濮甸鏍窗濡ゅ啯宕查柟閭﹀枛缁躲倕霉閻樺樊鍎忕紒鐘崇墬缁绘繃绻濋崒婊冾暫闂佸搫顑勭粈渚€婀侀梺绋跨箰閸氬绱為幋鐐电闁告粌鍟€氾拷
# queryset = T1.objects.values('sentiment')
# condtions = {'sentiment__gte': 0.5}
# plus = queryset.filter(**condtions).count()

# # 闂傚倷娴囧畷鍨叏閻㈢ǹ绀夋俊銈呮噹缁愭骞栧ǎ顒€濡肩紒鐘崇墬缁绘繃绻濋崒婊冾暫闂佸搫顑勭粈渚€婀侀梺绋跨箰閸氬绱為幋鐐电闁告粌鍟€氾拷
# queryset = T1.objects.values('sentiment')
# condtions = {'sentiment__lt': 0.5}
# minus = queryset.filter(**condtions).count()
