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
		Chemicial = Chemistry.objects.get(cid=cid)
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
#     """      缂傚倸鍊搁崐鐑芥嚄閼稿灚鍙忔い鎾卞灩绾惧鏌熼崜褏甯涢柣鎾存礃娣囧﹪顢涘⿰鍐ㄥ濡炪們鍎崜婵嬪Φ閸曨垰鍗抽柣鏃傚劋閸掓稑螖閻橀潧浠滄俊顐ｇ箓閻ｇ兘濡搁妷鍥ч叄椤㈡牠鎸婃径澶婎棜闂備浇娉曢崳锕傚箯閿燂拷     """
#     model = Resume
#     template_name ='resume_detail.html'
#     # success_url = '/joblist/'

def show_all_heros(request):
	all_heros = CodeImages.objects.all()

	# for index in all_heros:
	# 	print(index.name,index.hp_max,index.hp_growth)

	# 闂傚倸鍊峰ù鍥敋瑜嶉湁闁绘垼妫勯弸渚€鏌熼梻瀵歌窗闁轰礁妫濋弻锝夊冀瑜庢鐥廻eroes闂傚倸鍊风粈渚€骞栭位鍥敃閿曗偓閻ょ偓绻濇繝鍌涘櫧闁活厽鐟╅弻鈥愁吋鎼粹€崇闂侀€炲苯鍘哥紒鑸靛哺閻涱喚鈧綆鍠楅弲婵嬫煃瑜滈崜娑氬垝閸儱骞㈡繛鎴炵懅閸橀亶姊洪弬銉︽珔闁哥喍鍗抽崺锝夊Χ婢跺鍘撻悷婊勭矒瀹曟粓濡搁埡浣侯唵闂佽法鍣﹂幏锟�
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
		error_msg = '闂傚倸鍊峰ù鍥х暦閸偅鍙忛柡澶嬪殮濞差亜惟闁宠桨娴囬幗鏇熺節閵忥絾纭鹃柡鍫墴椤㈡洟鎳為妷锝勭盎闂佽鍎冲畷顒勬倶閳哄啰纾奸柍褜鍓熷畷鎺楁倷鐎电ǹ甯惧┑鐘灱濞夋盯鎮ч崱娑樼婵ǹ椴搁崰鎰版煙濞堝灝鏋涢柍璇茬墛閹便劍绻濋崒娑欏創闂佸疇顕ч柊锝夌嵁閸℃凹妲奸梺璇茬箲濞茬喎顫忛悜妯侯嚤婵炲棙甯╅崥鍛存⒑閻熸澘娈╅柟鍑ゆ嫹'
		return render(request, '404.html', {'error_msg': error_msg,'q':q})

	return render(request, 'results.html', {'error_msg': error_msg,
											   'post_list': post_list})

def download(request):
	
	# q = request.GET.get('q')
	# error_msg = ''

	# if not q:
	# 	error_msg = '闂傚倸鍊峰ù鍥х暦閸偅鍙忛柡澶嬪殮濞差亜惟闁宠桨娴囬幗鏇熺節閵忥絾纭鹃柡鍫墴椤㈡洟鎳為妷锝勭盎闂佽鍎冲畷顒勬倶閳哄啰纾奸柍褜鍓熷畷鎺楁倷鐎电ǹ甯惧┑鐘灱濞夋盯鎮ч崱娑樼婵ǹ椴搁崰鎰版煙濞堝灝鏋涢柍璇茬墛閹便劍绻濋崒娑欏創闂佸疇顕ч柊锝夌嵁閸℃凹妲奸梺璇茬箲濞茬喎顫忛悜妯侯嚤婵炲棙甯╅崥鍛存⒑閻熸澘娈╅柟鍑ゆ嫹'
	# 	return render(request, '404.html', {'error_msg': error_msg})

	course_resources = Resource.objects.all()
	print(dir(course_resources))
	return render(request, 'download.html', {'course_resources': course_resources})
# locals闂傚倸鍊搁崐椋庣矆娓氣偓楠炲鏁撻悩鍐蹭画闂佹寧娲栭崐褰掑疾濠靛鐓忛煫鍥ь儏閳ь剚娲熷濠氼敍濞戞氨顔曢悗鐟板閸犳洜鑺辨總鍛婄厱閹艰揪绱曟晥闂佸搫鏈惄顖氼嚕閹绢喖惟闁靛鍊涢崺鍛節閻㈤潧浠滈柣掳鍔戦弫鍐閵堝懓鎽曢梺鎸庣箓椤︻垶鎮為崹顐犱簻闁瑰搫妫楁禍鐐節绾版ǚ鍋撻悙钘変划闂佸搫鐭夌换婵嗙暦椤忓牆绀冮柍杞扮贰娴硷拷!!
# def books(request):
#     ###  婵犵數濮烽弫鎼佸磻濞戙埄鏁嬫い鎾跺枑閸欏繘鎮楅棃娑欐喐闁绘粌顭烽弻娑㈡晲閸涱偄浠璭ls闂傚倸鍊搁崐椋庣矆娓氣偓楠炲鏁撻悩鍐蹭画闂佹寧娲栭崐褰掑磻鐎ｎ偂绻嗛柕鍫濇噺閸ｈ鎱ㄧ憴鍕弨闁哄矉缍佸顕€宕掑顑跨帛缂傚倷鑳舵慨鏉戭嚕閸洖桅闁告洦鍨扮猾宥夋煕閵夋垵鍟崕顏堟⒒娴ｈ櫣甯涢柛鏃€娲熼弫鍐晜閻愵剦娼熼梺瑙勫劤閻°劍鍒婇幘顔界厱闁挎棁顕ч獮鏍煛閸曞灚鐝猰plate  ###
#     n = Name.objects.all()
#     return render(request, 'bookslist.html', locals())

# fitter 闂傚倸鍊搁崐椋庣矆娓氣偓楠炲鏁撻悩鎻掔€梺绋跨箰閸氬宕ｈ箛娑欑厪闁割偅绻嶅Σ鍛婃叏鐟欏嫮鍙€闁哄矉缍佸顒勫垂椤旇棄鈧垶姊虹粙鍧楊€楃紒澶婄秺瀵鈽夐姀鐘插祮闂侀潧枪閸庤京绮诲ú顏呪拺闁告繂瀚ˉ婊呯磼缂佹﹫鑰跨€殿喖顭锋俊鎼佸煛閸屾矮绨介梻浣呵归張顒傜矙閹达富鏁傞柨鐕傛嫹?
 # 闂傚倸鍊搁崐宄懊归崶顒夋晪闁哄稁鍘奸崹鍌毭归崗鍏肩稇缂佺姷濞€閻擃偊宕堕妸褉妲堢紓浣插亾濠㈣埖鍔栭悡鏇熺箾閹寸偟鎳勭紓宥嗗灩閻ヮ亪骞嗚缁夋椽鏌″畝鈧崰鏍€佸☉銏犲耿婵°倐鍋撴い蹇婃櫊閺屽秷顧侀柛鎾卞姂楠炲繘鏁撻敓锟�
# sent_avg =f" {T1.objects.aggregate(Avg('sentiment'))['sentiment__avg']:0.2f} "
# gte lte lt gt濠电姷鏁告慨鐑藉极閹间礁纾绘繛鎴旀嚍閸ヮ剦鏁囬柕蹇曞Х椤︻噣鎮楅獮鍨姎妞わ富鍨崇划鍫ュ醇閵夛妇鍘藉┑掳鍊愰崑鎾绘煟濡も偓缁绘﹢宕洪姀銈呯睄闁割偆鍠庨埀顒傛暬閺屻劌鈹戦崱娆忓毈缂備降鍔岄…鐑藉蓟閿濆牏鐤€闁瑰灝瀚慨娑氱磽娴ｄ粙鍝洪悽顖ょ節閻涱噣宕卞鍏夹┑鐐差嚟婵即宕规禒瀣摕闁绘梻鈷堥弫濠勭磼濞戞﹩鍎愰柣銈勭閳规垿鍩ラ崱妞剧盎闂佸摜鍠庨悺銊╁箞閵娾晛鐒垫い鎺戝閻撳繘鐓崶銉ュ姢缁炬儳娼￠弻锟犲幢濞嗗繆鏋呭┑顔硷攻濡炰粙骞冮悜钘夌妞ゆ梹妲掑鍝ョ磽閸屾瑧顦︽い锔诲灣婢规洟顢橀悩鎰佹綗闂佺粯鍔楅崕銈夊疾閹间焦鐓ラ柣鏇炲€圭€氾拷
# # 濠电姷鏁告慨鐢割敊閺嶎厼绐楁俊銈呭暞瀹曟煡鏌熼柇锕€鏋涚紒韬插€曢湁闁绘ê妯婇崕蹇曠磼閻樺磭澧紒缁樼箖缁绘繈宕掑⿰鍐炬毇闂備礁鎼鍕矆娓氣偓濠€渚€姊虹粙璺ㄧ闁告艾顑囩槐鐐哄箣閻愮數顔曢梺鍛婄矊閸燁垳鈧熬鎷�
# queryset = T1.objects.values('sentiment')
# condtions = {'sentiment__gte': 0.5}
# plus = queryset.filter(**condtions).count()

# # 闂傚倸鍊峰ù鍥х暦閸偅鍙忛柣銏⑶圭粈澶嬩繆閵堝懏鍣圭紒鎰殜楠炴牕菐椤掆偓婵¤偐绱掗悩宕囧缂佺粯绻冪换婵嬪磼濠婂喚鏆梻浣告惈椤戝嫮绮堟笟鈧﹢渚€姊虹粙璺ㄧ闁告艾顑囩槐鐐哄箣閻愮數顔曢梺鍛婄矊閸燁垳鈧熬鎷�
# queryset = T1.objects.values('sentiment')
# condtions = {'sentiment__lt': 0.5}
# minus = queryset.filter(**condtions).count()
