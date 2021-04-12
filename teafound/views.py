# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from .models import CodeImages,Resource,Chemistry
from django.http import HttpResponseRedirect, Http404
# from django.shortcuts import render_to_response
from django.views.generic import DetailView
import csv
from django.http import StreamingHttpResponse
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

class Echo:
	"""An object that implements just the write method of the file-like
	interface.
	"""
	def write(self, value):
		"""Write the value by returning it, instead of storing in a buffer."""
		return value

def chemDetail(request,cid):
	try:
		Chemicial = Chemistry.objects.get(cid=cid)
		#  type: [dict]
		resource = Chemistry.objects.filter(cid=cid).values() 
		print(resource)
		print(type(Chemicial))
		print('---')
		pseudo_buffer = Echo()
		writer = csv.writer(pseudo_buffer)
		router = request.get_full_path().split('/')[2]
		response = StreamingHttpResponse((writer.writerow(row) for row in resource[0]),
									 content_type="text/csv")
		print(response)
		response['Content-Disposition'] = 'attachment; filename= router +"somefilename.csv"'
		print(Chemicial.molecularweight)
		
		# course_resources = Resource.objects.all()
		print('22333')
		# print(router)
	except Chemicial.DoesNotExist:
		raise Http404("Chemicial does not exist")
	return render(request, 'chem_detail.html', {"Chemicial":Chemicial,"response":resource[0],})



def detail(request, job_id,Job,Cities):
	try:
		job = Job.objects.get(pk=job_id)
		job.city_name = Cities[job.job_city][1]
		# logger.info('job retrieved from db :%s' % job_id)
	except Job.DoesNotExist:
		raise Http404("Job does not exist")
	return render(request, 'job.html', {'job': job})

# class ResumeDetailView(DetailView):
#     """      缂傚倸鍊搁崐鎼佸磹閹间礁纾归柣鎴ｅГ閸ゅ嫰鏌ょ粙璺ㄤ粵闁告瑥绻戦妵鍕箻閸楃偟浠肩紒鐐劤椤兘寮婚悢鐓庣鐟滃繒鏁☉銏＄厽闁规儳鐡ㄧ粈鍐ㄇ庨崶褝韬い銏＄☉楗即宕橀妸銉€卞┑锛勫亼閸婃垿宕曢鈧畷婊冣攽鐎ｎ€箓鏌涢弴銊ョ仩闁告濞婇弻锝夊籍閸屾艾濡洪梺鍛婂笚缁嬫垼鐏冮梺缁橈耿濞佳勭濠婂嫪绻嗘い鎰剁悼缁犳捇鏌ｉ敐鍥у幋濠碘剝鎮傛俊鐑藉炊瑜旈崣鍕亜閵忥紕澧甸柟绋匡攻瀵板嫭寰勬繝搴㈩棥闂傚倸鍊峰ù鍥р枖閺囥垹闂柨鏇炲€哥粻顖炴煥閻曞倹瀚�     """
#     model = Resume
#     template_name ='resume_detail.html'
#     # success_url = '/joblist/'

def show_all_heros(request):
	all_heros = CodeImages.objects.all()

	# for index in all_heros:
	# 	print(index.name,index.hp_max,index.hp_growth)

	# 闂傚倸鍊搁崐鎼佸磹瀹勬噴褰掑炊椤掑鏅悷婊冪Ч濠€渚€姊虹紒妯虹伇婵☆偄瀚板鍛婄瑹閳ь剟寮婚悢鍏尖拻閻庡灚鐡曠粣妤呮⒑鏉炴壆顦︽俊顐ｇ箞瀵鏁愭径濠傚敤閻熸粌瀛╅〃婊堟儉瀵ょ暴roes闂傚倸鍊搁崐鎼佸磹妞嬪海鐭嗗〒姘ｅ亾妤犵偞鐗犻、鏇氱秴闁搞儺鍓﹂弫鍐煥閺囨浜鹃梺姹囧€楅崑鎾舵崲濠靛洨绡€闁稿本绋戝▍褔姊哄ú璇插箺闁荤啿鏅犲濠氬灳閹颁礁鎮戦柟鑲╄ˉ閳ь剙纾澶愭⒒娓氣偓閳ь剛鍋涢懟顖炲储閸濄儳纾奸柤鎼佹涧閸濇椽鏌ｅ☉鍗炴灓闁逞屽墾缂嶅棝宕板Δ鍛柧婵犻潧顑嗛悡鍐喐濠婂牆绀堟繛鎴炶壘閸ㄦ繈鏌涢鐘插姎妤犵偑鍨虹换娑㈠箣閻愬灚鍣梺鍛婏耿娴滆泛顫忓ú顏勬闁靛闄勯悵鏃堟⒑閸濄儱鏋嶉柛妤佸▕瀹曟椽鏁愭径濞⒀冾熆鐠轰警鍎戦柛妯绘崌閹嘲饪伴崟顓犵厜閻庤娲樼划鎾翠繆閹间礁鐓涘ù锝勮閸炵敻姊绘担鑺ョ《闁革綇绠撻獮蹇涙晸閿燂拷
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
		error_msg = '闂傚倸鍊搁崐鎼佸磹瀹勬噴褰掑炊瑜忛弳锕傛煕椤垵浜濋柛娆忕箻閺屸剝寰勭€ｎ亝顔呭┑鐐叉▕娴滄粍鍎梻浣哥枃濡椼劌霉閸ヮ剙绠洪柡鍥╁枔缁♀偓闂侀潧楠忕徊鍓ф兜妤ｅ啯鐓涢柛顐亜婢у瓨銇勯姀鈩冪闁瑰磭鍋ゆ俊鐑芥晲閸曨厾娉块梻鍌欐祰椤宕曢崘鑼殾妞ゆ帒瀚崐鍫曟煃閸濆嫬鏆熺痪鎯с偢閺屽秷顧侀柛鎾跺枎閻ｇ兘骞掑Δ浣糕偓鐑芥倵閻㈢櫥鍦暜閹€鏀介柣姗嗗枛閻忚鲸绻涙径瀣创闁诡啫鍥у耿婵炴垶顭囬ˇ顔尖攽椤旇瑙勩仈閹间礁绐楅柟鎵閻撴瑦绻涢崼婵堜虎闁哄鐩弻宥囨嫚閼碱剙顤€闂侀€涚┒閸斿秶鎹㈠┑瀣＜婵炴垶鐟ラ崜鐢告⒒娴ｅ摜鏋冩い鏇嗗洦鐓€闁挎繂顦卞畵渚€鏌涢埄鍐ㄥ毈婵℃彃銈稿铏规嫚閼碱剛顔夊┑鐐跺皺閸犲酣锝炶箛娑欏€绘俊顖欒閸ゃ倕鈹戦悙鍙夘棡閻㈩垪鏅犲畷銉╁川鐎涙ǚ鎷洪梺鑽ゅ枑濠㈡ê鈻撻埡鍛厵闁告垯鍊栫€氾拷'
		return render(request, '404.html', {'error_msg': error_msg,'q':q})

	return render(request, 'results.html', {'error_msg': error_msg,
											   'post_list': post_list})



# cid 如何获取？？
def download(request):
	"""A view that streams a large CSV file."""
	# Generate a sequence of rows. The range is based on the maximum number of
	# rows that can be handled by a single sheet in most spreadsheet
	# applications.
	# rows = Chemistry.objects.get(cid=cid)
	router = request.get_full_path()
	print('22333')
	print(router)
	rows = (["Row {}".format(idx), str(idx)] for idx in range(65536))
	# course_resources = Chemistry.objects.get()
	course_resources = Resource.objects.all()
	pseudo_buffer = Echo()
	writer = csv.writer(pseudo_buffer)
	response = StreamingHttpResponse((writer.writerow(row) for row in rows),
									 content_type="text/csv")
	# response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
	return render(request, 'download.html', {'course_resources': course_resources})

# def download(request):
	
# 	# q = request.GET.get('q')
# 	# error_msg = ''

# 	# if not q:
# 	# 	error_msg = '闂傚倸鍊搁崐鎼佸磹瀹勬噴褰掑炊瑜忛弳锕傛煕椤垵浜濋柛娆忕箻閺屸剝寰勭€ｎ亝顔呭┑鐐叉▕娴滄粍鍎梻浣哥枃濡椼劌霉閸ヮ剙绠洪柡鍥╁枔缁♀偓闂侀潧楠忕徊鍓ф兜妤ｅ啯鐓涢柛顐亜婢у瓨銇勯姀鈩冪闁瑰磭鍋ゆ俊鐑芥晲閸曨厾娉块梻鍌欐祰椤宕曢崘鑼殾妞ゆ帒瀚崐鍫曟煃閸濆嫬鏆熺痪鎯с偢閺屽秷顧侀柛鎾跺枎閻ｇ兘骞掑Δ浣糕偓鐑芥倵閻㈢櫥鍦暜閹€鏀介柣姗嗗枛閻忚鲸绻涙径瀣创闁诡啫鍥у耿婵炴垶顭囬ˇ顔尖攽椤旇瑙勩仈閹间礁绐楅柟鎵閻撴瑦绻涢崼婵堜虎闁哄鐩弻宥囨嫚閼碱剙顤€闂侀€涚┒閸斿秶鎹㈠┑瀣＜婵炴垶鐟ラ崜鐢告⒒娴ｅ摜鏋冩い鏇嗗洦鐓€闁挎繂顦卞畵渚€鏌涢埄鍐ㄥ毈婵℃彃銈稿铏规嫚閼碱剛顔夊┑鐐跺皺閸犲酣锝炶箛娑欏€绘俊顖欒閸ゃ倕鈹戦悙鍙夘棡閻㈩垪鏅犲畷銉╁川鐎涙ǚ鎷洪梺鑽ゅ枑濠㈡ê鈻撻埡鍛厵闁告垯鍊栫€氾拷'
# 	# 	return render(request, '404.html', {'error_msg': error_msg})

# 	course_resources = Resource.objects.all()
# 	print(dir(course_resources))
# 	return render(request, 'download.html', {'course_resources': course_resources})
# locals闂傚倸鍊搁崐鎼佸磹閹间礁纾瑰瀣捣閻棗銆掑锝呬壕濡ょ姷鍋涢ˇ鐢稿极閹剧粯鍋愰柛鎰紦閻㈠姊绘担鐟邦嚋婵炲弶鐗犲畷鎰亹閹烘垹鏌у┑鐘绘涧椤戝棝鎮¤箛娑氬彄闁搞儜灞藉壈闂侀€炲苯澧繛鑼枎椤繑绻濆鍏兼櫖濠电偞鍨跺銊╊敊閺囥垺鍊甸柣鐔告緲椤ュ繘鏌涢悩铏闁奸缚椴哥缓浠嬪川婵犲嫬骞堥梺纭呭閹活亞妲愰弴鐔告珡闂傚倷绀侀幖顐﹀嫉椤掑嫭鍎庢い鏍ㄥ嚬閸ゆ洟鏌熺紒銏犳灈閹喖姊洪棃娑辨Ф闁稿﹥鐩畷娲川椤斿墽鐦堥梺姹囧灲濞佳勭濠婂牊鐓熼幒鎶藉礉閹达箑鏋侀柛鎰靛枛椤懘鏌曢崼婵囧殌闁硅姤娲熷娲箰鎼达絿鐣靛銈忓瘜閸ㄥ爼骞冮悙鍝勫瀭妞ゆ劗濮崇花濠氭⒑閻熺増鎯堟俊顐ｎ殕缁傚秹鎮欓鍌滅槇缂佸墽澧楄彜闁稿鎹囬幃娆撴寠婢跺鍨濋梻鍌欑閹碱偊鎯屾径灞惧床婵犻潧妫涢弳锔姐亜韫囨挾澧曠紒鈧崘顔界厓閺夌偞澹嗙拹鏉棵圭涵閿嬪!!
# def books(request):
#     ###  婵犵數濮烽弫鍛婃叏閻戣棄鏋侀柟闂寸绾剧粯绻涢幋娆忕労闁轰礁顑嗛妵鍕箻鐠虹儤鐎鹃梺鍛婄懃缁绘﹢骞冨Δ鍛棃婵炴垶鐟﹂崰鎰版⒑缂佹鐭婃い顓犲厴瀵鈽夐姀鈩冩珳闂佸憡渚楅崑鍕閻犵挻s闂傚倸鍊搁崐鎼佸磹閹间礁纾瑰瀣捣閻棗銆掑锝呬壕濡ょ姷鍋涢ˇ鐢稿极閹剧粯鍋愰柛鎰紦閻㈠姊绘担鐟邦嚋婵炲弶鐗犲畷鎰亹閹烘垹锛涢柣搴秵閸嬪倻鎹㈤崱娑欑厪闁割偅绻冮崳娲煕閿濆牜娼愰柟渚垮妿閹叉挳宕熼鐐茬哗闂備礁鎼惌澶岀礊娴ｅ壊鍤曟い鏇楀亾鐎规洘甯掗～婵嬵敄鐠恒劌绗＄紓鍌氬€搁崐鐑芥嚄閼稿灚鍙忛柡澶嬪焾閸ゆ洟鏌涢锝嗙濡楀懘姊洪崨濠冨闁搞劍澹嗛悮鎯ь吋婢跺鍘遍梺闈涱槹閸ㄧ敻宕鐐茬？妞ゅ繐鐗婇埛鎺懨归敐鍫燁仩閻㈩垱鐩弻娑㈠籍閳ь剙煤閻旂厧鏋侀柛鎰靛枟閺呮粓鏌ｉ幇闈涘⒒婵炶偐鍠栧铏规喆閸曨偄濮㈤梺瀹︽澘濡介柛鎺戯躬楠炴﹢顢欓悾灞藉箞闂備焦瀵уΛ渚€顢氳閻涱噣寮介鐔哄幐闂佸憡娲栭悘姘舵偟閻氱殐late  ###
#     n = Name.objects.all()
#     return render(request, 'bookslist.html', locals())

# fitter 闂傚倸鍊搁崐鎼佸磹閹间礁纾瑰瀣捣閻棗銆掑锝呬壕濡ょ姷鍋涢ˇ鐢稿极閹剧粯鍋愰柟缁樺笧閳ь剦鍙冨铏圭矙鐠恒劎顔囬梺鍛婅壘椤戝鐣烽敐鍫㈢杸婵炴垶鐟ч崢顏堟⒑閸撴彃浜濈紒璇茬Т鍗遍柛娑橈攻閸欏繘鎮峰▎蹇擃伀闁告瑢鍋撻梻浣告惈閻绱炴担鍓插殨妞ゆ帒瀚崹鍌涖亜閺冨洦顥夐柍褜鍓﹂崹璺侯潖閾忓湱鐭欓柛褎顨忛埀顒侇殘缁辨帗寰勬繝鍕ㄩ悗娈垮枦椤曆囧煡婢舵劕顫呴柣妯诲絻缁侇噣姊绘笟鈧褎鐏欓梺绋挎唉娴滎剛鍒掔拠瑁佹椽顢旈崨顏呭闂備礁鎲＄换鍌溾偓姘煎弮钘熸繝濠傛噽绾捐偐绱撴担鐧稿叕闁兼媽娉曢埀顒侇問閸犳牠鈥﹂柨瀣╃箚闁归棿绀侀悡娑㈡煕鐏炲墽鐓紒銊ょ矙濮婄粯鎷呴崨闈涚秺瀵敻顢楅崒婊呯厯闂佺鎻€靛矂寮崒鐐寸叆闁绘洖鍊圭€氾拷?
 # 闂傚倸鍊搁崐鎼佸磹閹间礁纾圭€瑰嫭鍣磋ぐ鎺戠倞妞ゆ帒顦伴弲顏堟⒑閸濆嫮鈻夐柛妯恒偢瀹曞綊宕掑В顓炵秺瀹曟宕楅懖鈺冣枏缂傚倷鑳舵慨閿嬬箾閳ь剟鏌ｉ幙鍐ㄤ喊鐎规洖鐖兼俊姝岊槷婵℃彃鐗忕槐鎾存媴閹绘帊澹曞┑鐘灱閸╂牠宕濋弽顓熷亗闁哄洨鍠撶粻楣冩煙鐎电ǹ浠ч柟鍐插缁辨挸顓奸崱妤冧患闂佹眹鍎烘禍顏堢嵁閸℃凹妲剧紓浣割槹濡炰粙寮婚垾宕囨殕闁逞屽墴瀹曚即寮介婧惧亾娴ｇ硶妲堥柕蹇曞Т閼板灝鈹戞幊閸婃劙宕戦幘娣簻闊洤锕ュ▍濠囨煛鐏炵晫啸妞ぱ傜窔閺屾盯骞橀崡鐐差潎濡ょ姷鍋涚换姗€寮幘缁樻櫢闁跨噦鎷�
# sent_avg =f" {T1.objects.aggregate(Avg('sentiment'))['sentiment__avg']:0.2f} "
# gte lte lt gt濠电姷鏁告慨鐑藉极閸涘﹥鍙忛柣鎴ｆ閺嬩線鏌熼梻瀵割槮缁惧墽绮换娑㈠箣閺冣偓閸ゅ秹鏌涢妷顔煎⒒闁轰礁娲弻鏇＄疀閺囩倫銉︺亜閿旇娅嶉柟顔筋殜閻涱噣宕归鐓庮潛婵＄偑鍊х€靛矂宕瑰畷鍥у灊闁割偁鍎遍柋鍥煏婢舵稑顩柛妯挎閳规垶骞婇柛濠冨姍瀹曟垿骞樼紒妯煎幗濠德板€愰崑鎾剁磼缂佹﹫鑰跨€规洘妞芥慨鈧柕鍫濇噽閻嫰姊洪崜鎻掍簽闁哥姴閰ｉ崺鈧い鎺戝€归弳顒勬煛鐏炶濡奸柍瑙勫灴瀹曞崬鈻庤箛鎾寸槗缂傚倸鍊烽梽宥夊礉瀹€鍕ㄢ偓锕傛倻閽樺鎽曢梺鎸庣箓閻楀繘鎮块埀顒勬⒑閻熸壆浠㈤悗姘煎墯閹便劌鈽夊杈╋紳婵炶揪绲肩划娆撳传濞差亝鍋ㄦい鏍ュ€楃弧鈧梺缁樹緱閸ｏ絽鐣烽崡鐑嗘僵闁稿繐銇欓鈧埞鎴︽倷瀹割喖娈舵繝娈垮枙閸楀啿鐣风憴鍕浄閻庯綆浜ｉ幗鏇㈡⒑缂佹ɑ鈷掗柍宄扮墦瀵偅绻濋崟顓狅紲濠电偞鍨堕敃鈺呭磿閹扮増鐓熼柕鍫濆椤︼箓鏌嶇憴鍕伌闁糕斂鍎靛畷鍗烆渻閸撗呮晨闂傚倷绀侀幗婊堝窗鎼淬劍鍋ら柕濞炬櫅缁犵偤鏌曟繛鐐珔闁绘帒鐏氶妵鍕箳閹存繍浠鹃梺缁樻尭缁绘﹢鎮￠锕€鐐婇柕澶堝劚婵垻绱掗悙顒€鍔ゆ繛纭风節瀵鏁撻悩鎻掕€垮┑鐐叉缁诲棝寮搁崨顓涙斀妞ゆ梻銆嬮弨缁樹繆閻愭壆鐭欐鐐插暣閹粓鎸婃径宀婂悑婵＄偑鍊栧鐟拔ｉ幒鎴€堕柛婵勫劤绾句粙鏌涚仦鍓ф噮妞わ讣闄勯妵鍕晜鐠囪尙浠繝銏ｎ潐濞茬喖銆佸鈧幃鈺呭箛娴ｅ湱绋愰梻鍌欒兌缁垶宕濆Δ鍛？闁靛牆顦悿楣冩煙闂傚鍔嶉柣鎾卞劦閺岋綁寮撮悙娴嬪亾閸︻厸鍋撳鐐
# # 濠电姷鏁告慨鐑藉极閸涘﹥鍙忛柣銏犲閺佸﹪鏌″搴″箹缂佹劖顨嗘穱濠囧Χ閸涱厽娈查悗瑙勬礃閻擄繝寮婚悢鍏肩劷闁挎洍鍋撻柡瀣〒缁辨帡鐓幓鎺嗗亾閺囥垺绠掗梻浣虹帛閿氭俊顖氾躬瀹曟洝绠涢弴鐘碉紲闂佺粯锚绾绢厽鏅堕鍌滅＜缂備焦顭囩粻鏍磼缂佹绠炵€规洘甯掗オ浼村礃閻愵剚鐦掗梻鍌氬€风粈渚€骞栭锔绘晞闁告洦鍘鹃惌鍡椼€掑锝呬壕濠电姭鍋撳〒姘ｅ亾婵﹨娅ｇ划娆戞崉閵娧屽敹闂備礁鎲￠懝楣冾敄閸モ晜顫曢柣鎰惈缁狅綁鏌ｉ幇顔芥毄妞ゆ梹娲熷娲川婵犲嫮鐓€闂佸摜鍣ラ崹鎶藉焵椤掍胶鍟查柟鍑ゆ嫹
# queryset = T1.objects.values('sentiment')
# condtions = {'sentiment__gte': 0.5}
# plus = queryset.filter(**condtions).count()

# # 闂傚倸鍊搁崐鎼佸磹瀹勬噴褰掑炊瑜忛弳锕傛煕椤垵浜濋柛娆忕箻閺岋綁濮€閳惰泛婀辩划鍫熷緞鐎ｂ晝绠氶梺闈涚墕閹冲繘宕抽崷顓犵＜闁归偊鍙庡▓婊勵殽閻愬澧懣鎰亜閹哄棗浜炬繝寰枫倕浜圭紒杈ㄥ浮閹晛鐣烽崶褜娼风紓鍌欒兌缁垳鎹㈤崘顏呭床婵犻潧顑呯壕鍏肩節婵犲倸鏋ら柡鍡╁亰濮婄粯鎷呴崨濠冨創濡炪倖鍨电€氼喚鍒掗崼鐔虹懝闁逞屽墮閿曘垺绗熼埀顒€顫忛搹鍦煓閻犳亽鍔庨鍥⒑閸涘﹨澹樻い鎴濇川濡叉劙鎮欓崫鍕吅闂佺粯鍔楅弫鎼侇敊閺囥垺鈷戦柛娑橈功閻﹪鏌涢悤浣哥仯闁逞屽墯閻旑剟骞忛敓锟�
# queryset = T1.objects.values('sentiment')
# condtions = {'sentiment__lt': 0.5}
# minus = queryset.filter(**condtions).count()
