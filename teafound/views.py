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
#     """      缂傚倸鍊搁崐鎼佸磹閻戣姤鍤勯柤绋跨仛閸欏繑銇勯幘鍗炵仼缁炬儳顭烽弻鐔煎礈瑜忕敮娑㈡煟閹惧瓨绀冨ǎ鍥э躬椤㈡稑饪伴崘銊ヮ瀱婵＄偑鍊戦崕顕€宕滃┑瀣﹂柛鏇ㄥ灠閸楁娊鏌ｉ弮鍌氬妺闁告帗绋戣灃闁绘﹢娼ф禒婊勪繆椤愶絿绠撻柣锝囧厴婵℃悂濡烽崶褔鍙勬い銏＄墵閹稿﹥寰勬径濠庢闂傚倷娴囧▔鏇㈠闯閿曞倸绠柨鐕傛嫹     """
#     model = Resume
#     template_name ='resume_detail.html'
#     # success_url = '/joblist/'

def show_all_heros(request):
	all_heros = CodeImages.objects.all()

	# for index in all_heros:
	# 	print(index.name,index.hp_max,index.hp_growth)

	# 闂傚倸鍊搁崐宄懊归崶顒夋晪鐟滃秹婀侀梺缁樺灱濡嫰寮告笟鈧弻鐔兼⒒鐎垫瓕绐楅梺杞扮濡繈寮婚敐澶婂唨鐟滃孩顨滈惀寤籩roes闂傚倸鍊搁崐椋庣矆娓氣偓楠炴牠顢曚綅閸ヮ剦鏁冮柨鏇楀亾闁汇倗鍋撶换婵囩節閸屾稑娅ч梺娲诲幗閻熲晠寮婚垾鎰佸悑閹肩补鈧磭顔夐梻渚€鈧偛鑻崢鍝ョ磼閼搁潧鍝洪柣娑卞枤閳ь剨缍嗛崰妤呭疾濠靛鐓冪憸婊堝礈濞戞艾鍨濋柛顐犲劚楠炪垺绻涢幋鐐垫噮闁告﹢浜跺娲棘閵夛附鐝旈梺鍝ュ枍閸楁娊宕洪敐澶娢у璺侯儑閸樻捇鎮峰⿰鍕煉鐎规洘绮撴俊鎼佸煛娴ｄ警鍞甸梻浣芥硶閸ｏ箓骞忛敓锟�
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
		error_msg = '闂傚倸鍊搁崐宄懊归崶褏鏆﹂柛顭戝亝閸欏繘鏌℃径瀣婵炲樊浜滄儫闂佸疇妗ㄥù鍥箺閺囩喓绡€闁靛骏绲剧涵楣冩煛閸偄澧存い銏℃礋閹崇偤濡烽敐鍕泿闂備浇顫夐崕鍐茬暦椤掑嫭鍊堕柍鍝勫暟绾惧ジ鏌嶈閸撶喎鐣烽幒妤佸€烽悗鐢登圭敮鎯р攽閻橆喖鐏辨繛澶嬬洴閹囧幢濞戞顦┑顔角规ご鎼佸窗閹扮増鐓欐繛鍫濈仢閺嬫盯鏌嶇拠鑼闁逛究鍔嶇换婵嬪磼濞戞瑥鍓甸梻浣哥枃椤曆囨煀閿濆宓侀柛鈩冨嚬濡插ジ姊虹拠鑼婵炶尙鍠庨～蹇涙倻濡警鍤ゅ┑鐐叉鐢晠宕ラ崨瀛樷拺闁荤喐婢樺▓鈺呮煙閸戙倖瀚�'
		return render(request, '404.html', {'error_msg': error_msg,'q':q})

	return render(request, 'results.html', {'error_msg': error_msg,
											   'post_list': post_list})

def download(request):
	
	# q = request.GET.get('q')
	# error_msg = ''

	# if not q:
	# 	error_msg = '闂傚倸鍊搁崐宄懊归崶褏鏆﹂柛顭戝亝閸欏繘鏌℃径瀣婵炲樊浜滄儫闂佸疇妗ㄥù鍥箺閺囩喓绡€闁靛骏绲剧涵楣冩煛閸偄澧存い銏℃礋閹崇偤濡烽敐鍕泿闂備浇顫夐崕鍐茬暦椤掑嫭鍊堕柍鍝勫暟绾惧ジ鏌嶈閸撶喎鐣烽幒妤佸€烽悗鐢登圭敮鎯р攽閻橆喖鐏辨繛澶嬬洴閹囧幢濞戞顦┑顔角规ご鎼佸窗閹扮増鐓欐繛鍫濈仢閺嬫盯鏌嶇拠鑼闁逛究鍔嶇换婵嬪磼濞戞瑥鍓甸梻浣哥枃椤曆囨煀閿濆宓侀柛鈩冨嚬濡插ジ姊虹拠鑼婵炶尙鍠庨～蹇涙倻濡警鍤ゅ┑鐐叉鐢晠宕ラ崨瀛樷拺闁荤喐婢樺▓鈺呮煙閸戙倖瀚�'
	# 	return render(request, '404.html', {'error_msg': error_msg})

	course_resources = Resource.objects.all()
	print(dir(course_resources))
	return render(request, 'download.html', {'course_resources': course_resources})
# locals闂傚倸鍊搁崐鎼佸磹妞嬪海鐭嗗〒姘ｅ亾妤犵偛顦甸弫鎾绘偐閸愯弓鐢婚梻浣瑰濞叉牠宕愯ぐ鎺戠柧婵犻潧顑嗛悡蹇涚叓閸パ屽剰闁逞屽墯濞茬喎顫忔繝姘兼晬婵炴垶姘ㄩ鏇㈡倵閻熸澘顥忛柛鐘虫礈閼鸿鲸绺介崨濠勫幈闁硅壈鎻槐鏇熸櫏闂備礁鎼張顒勬儎椤栨凹鍤曢柟缁㈠枛鎯熼梺闈涱槶閸婃盯宕洪崨顔剧瘈闁汇垽娼ф禒婊堟煟鎺抽崝鎴﹀极閸愵喖顫呴柕鍫濇嚀閹芥洟姊洪幐搴ｇ畵妞わ富鍨堕幃鐐哄垂椤愮姳绨婚梺鐟版惈濡绂嶉悙顒傜瘈缁剧増菤閸嬫捇鎮欓挊澶夊垝闂備礁鎼惌澶屾崲濠靛棛鏆︽い蹇撶墕缁€鍐煃鏉炴壆璐板ù纭锋嫹!!
# def books(request):
#     ###  濠电姷鏁告慨鐑藉极閹间礁纾绘繛鎴欏焺閺佸銇勯幘璺烘瀾闁告瑥绻橀幃妤呮濞戞瑦鍠愰梺缁樼矊椤兘寮诲☉銏℃櫜闁告侗鍋勬禒鐠璴s闂傚倸鍊搁崐鎼佸磹妞嬪海鐭嗗〒姘ｅ亾妤犵偛顦甸弫鎾绘偐閸愯弓鐢婚梻浣瑰濞叉牠宕愯ぐ鎺戠；閻庯綆鍋傜换鍡涙煏閸繃鍣洪柛锝堫潐閹便劎鎲撮崟顓炲绩闂佸搫鐭夌紞浣割嚕椤曗偓瀹曟帒顫濋璺ㄥ笡缂傚倸鍊烽懗鑸垫叏閺夋埈鍤曢柛顐ｆ礀妗呴梺鍛婃处閸ㄦ壆鐚惧澶嬬厱闁靛鍨甸崯顖炲磿椤忓牊鈷掑ù锝堟鐢盯鏌涢弮鈧ú鐔煎极閸愵喗鏅滈柣鎰靛墻濞肩喖姊虹憴鍕姢闁宦板妽閸掑﹪骞橀鐣屽幈闂佹寧妫侀褔鐛弽顓熺厸闁告洖鐏氶悵鐚皃late  ###
#     n = Name.objects.all()
#     return render(request, 'bookslist.html', locals())

# fitter 闂傚倸鍊搁崐鎼佸磹妞嬪海鐭嗗〒姘ｅ亾妤犵偛顦甸弫鎾绘偐閹绘帞鈧參姊虹粙璺ㄧ闁告艾顑夊畷锝堢疀濞戞瑧鍘梺鍓插亝缁诲秴危閸涘﹥鍙忛悷娆忓閸欌偓闂佸搫鐭夌紞浣割嚕椤掑嫬鍨傛い鏃囨閳ь剦鍨跺铏圭矙閸ф鈧绱掓径濠勭Ш鐎殿喛顕ч埥澶愬閻樻彃绁梻渚€娼ф灙闁稿氦浜划璇裁洪鍛嫼闂佸憡绻傜€氼參藟濠婂懐纾肩紓浣癸公閼拌法鈧鍠栭…閿嬩繆閹间礁鐓涢柛灞剧煯缁ㄤ粙姊绘担鍛靛綊寮甸鍌滅煓闁硅揪瀵岄弫鍌炴煥閻曞倹瀚�?
 # 闂傚倸鍊搁崐鎼佸磹瀹勬噴褰掑炊椤掑鏅梺鍝勭▉閸樺ジ宕归崒姣綊宕楅崗鑲╃▏缂備胶濮锋繛鈧柣鎿冨亰瀹曞爼濡歌濡插牏绱撴担鎻掍壕婵犮垼鍩栭崝鏍偂閺囩喓绠鹃柟瀵稿仧閹冲嫮绱撳鍡楃仼闁汇儺浜獮鍡氼槾缂佸妞介弻鈥崇暆閳ь剟宕伴弽顓溾偓浣糕槈閵忕姴鑰垮┑掳鍊愰崑鎾淬亜韫囧﹥娅婇柡灞界Х椤т線鏌涢幘鍗炲妤犵偛绻橀弫鎾绘晸閿燂拷
# sent_avg =f" {T1.objects.aggregate(Avg('sentiment'))['sentiment__avg']:0.2f} "
# gte lte lt gt婵犵數濮烽弫鍛婃叏閻戣棄鏋侀柟闂寸绾剧粯绻涢幋鏃€鍤嶉柛銉墻閺佸洭鏌曡箛鏇炐ユい锔诲櫍閹鐛崹顔煎濡炪倧瀵岄崹宕囧垝閸儱閱囬柕澶涘閸樿棄鈹戞幊閸婃劙宕戦幘缁樼厽婵°倐鍋撶紒缁橈耿瀹曟椽濮€閵堝懐鐫勯梺鍓插亞閸犲酣鍩€椤掑倹鏆柡灞诲妼閳规垿宕卞▎蹇撴瘓缂傚倷闄嶉崝宀勨€﹂悜钘夎摕闁挎繂鐗忛悿鈧梺鐟扮仢鐎氼剚鎱ㄥ☉姘辩＝濞达絼绮欓崫娲偨椤栥倗绡€闁绘侗鍣ｅ畷鍗烆潩閸忓す顒€鈹戦悙宸殶濠殿喕鍗冲畷瑙勭鐎ｎ亣鎽曢梺缁樻⒒閳峰牓寮繝鍕＜婵炴垶锕╅崕鎰版煟閵堝嫮顦﹂柍瑙勫灴閸┿儵宕卞鍓х泿闂備礁鎽滈崰搴ㄦ偤閵娾晛绠為柕濞炬櫅閻掑灚銇勯幒鎴濐仾闁绘挸绻橀悡顐﹀炊閵夈儱濮㈢紒鐐劤濞硷繝寮婚敓鐘插耿婵炲棗绻嗛弸鍛攽椤旂》鏀绘俊鐐扮矙楠炲啴鎮滈挊澶岊吋濡炪倖姊瑰Σ鎺戭瀶閸濄儳纾介柛灞剧懅椤︼附銇勯敂璇茬仯濠㈣娲熼、姗€鎮╅幇浣圭稐闂備胶绮崝妤呭磿閵堝鐤鹃柟闂寸劍閻撱儵鏌ｉ弴鐐测偓鍦偓姘炬嫹
# # 婵犵數濮烽弫鍛婃叏閻㈠壊鏁婇柡宥庡幖缁愭淇婇妶鍛殲鐎规洘鐓￠弻鐔兼焽閿曗偓閺嬫稓绱掗煬鎻掆偓鏇㈡箒闂佺粯锚濡﹪宕曡箛鏇犵＜闁绘ê纾晶顒傜磼缂佹绠栫紒缁樼箞瀹曟帒饪伴崘鐐瘒闂傚倷绀侀幖顐︻敄閸曨厾鐭嗗〒姘ｅ亾婵犫偓娓氣偓濮婅櫣绮欑捄銊ь唶闂佸憡鑹鹃鍥╂閻愬搫绠ｉ柣鎰暩椤旀洟姊洪崨濠勭煀闁哥噥鍨抽埀顒佺啲閹凤拷
# queryset = T1.objects.values('sentiment')
# condtions = {'sentiment__gte': 0.5}
# plus = queryset.filter(**condtions).count()

# # 闂傚倸鍊搁崐宄懊归崶褏鏆﹂柛顭戝亝閸欏繘鏌ｉ姀鈶跺湱绮堟径瀣╃箚闁靛牆鎳忛崳鍦磼閹邦収娈滄鐐寸墪鑿愭い鎺嗗亾濠德ゅ亹缁辨帡鎮╁畷鍥ь潷缂備胶绮换鍐崲濠靛纾兼繝濠傚枤閺嗩偊姊绘担鍛婃儓妞ゆ垵瀚划鍫熺瑹閳ь剙锕㈡笟鈧铏圭矙鐠恒劎顔囬梺鍛婅壘椤戝洨妲愰悙鍝勭闁绘劗鏁搁鏇㈡⒑閸涘﹦鐭婇柛鐕佸灣閳ь剚鐔幏锟�
# queryset = T1.objects.values('sentiment')
# condtions = {'sentiment__lt': 0.5}
# minus = queryset.filter(**condtions).count()
