from django.shortcuts import render

# Create your views here.


from .models import BusanDong
from .models import *



def BusanBuk_view(request):
    posts = BusanBuk.objects.all()
    return render(request, 'index.html', {"posts": posts})

def BusanDong_view(request):
    posts = BusanDong.objects.all()
    return render(request, 'index.html', {"posts": posts})

def BusanDongnae_view(request):
    posts = BusanDongnae.objects.all()
    return render(request, 'index.html', {"posts": posts})

def BusanJin_view(request):
    posts = BusanJin.objects.all()
    return render(request, 'index.html', {"posts": posts})

def BusanJung_view(request):
    posts = BusanJung.objects.all()
    return render(request, 'index.html', {"posts": posts})

def BusanNam_view(request):
    posts = BusanNam.objects.all()
    return render(request, 'index.html', {"posts": posts})

def BusanSaha_view(request):
    posts = BusanSaha.objects.all()
    return render(request, 'index.html', {"posts": posts})

def BusanSasang_view(request):
    posts = BusanSasang.objects.all()
    return render(request, 'index.html', {"posts": posts})

def BusanSeo_view(request):
    posts = BusanSeo.objects.all()
    return render(request, 'index.html', {"posts": posts})

def BusanSuyeong_view(request):
    posts = BusanSuyeong.objects.all()
    return render(request, 'index.html', {"posts": posts})

def BusanYeongdo_view(request):
    posts = BusanYeongdo.objects.all()
    return render(request, 'index.html', {"posts": posts})

def BusanYeonje_view(request):
    posts = BusanYeonje.objects.all()
    return render(request, 'index.html', {"posts": posts})

def ChungbukBoeun_view(request):
    posts = ChungbukBoeun.objects.all()
    return render(request, 'index.html', {"posts": posts})

def ChungbukCheongju_view(request):
    posts = ChungbukCheongju.objects.all()
    return render(request, 'index.html', {"posts": posts})

def ChungbukChungju_view(request):
    posts = ChungbukChungju.objects.all()
    return render(request, 'index.html', {"posts": posts})

def ChungbukDanyang_view(request):
    posts = ChungbukDanyang.objects.all()
    return render(request, 'index.html', {"posts": posts})

def ChungbukEumseong_view(request):
    posts = ChungbukEumseong.objects.all()
    return render(request, 'index.html', {"posts": posts})

def ChungbukJecheon_view(request):
    posts = ChungbukJecheon.objects.all()
    return render(request, 'index.html', {"posts": posts})

def ChungbukJincheon_view(request):
    posts = ChungbukJincheon.objects.all()
    return render(request, 'index.html', {"posts": posts})

def ChungbukOkjcheon_view(request):
    posts = ChungbukOkjcheon.objects.all()
    return render(request, 'index.html', {"posts": posts})

def ChungbukYeongdong_view(request):
    posts = ChungbukYeongdong.objects.all()
    return render(request, 'index.html', {"posts": posts})

def ChungnamAsan_view(request):
    posts = ChungnamAsan.objects.all()
    return render(request, 'index.html', {"posts": posts})

def ChungnamBoryeong_view(request):
    posts = ChungnamBoryeong.objects.all()
    return render(request, 'index.html', {"posts": posts})

def ChungnamBuyeo_view(request):
    posts = ChungnamBuyeo.objects.all()
    return render(request, 'index.html', {"posts": posts})

def ChungnamCheongyang_view(request):
    posts = ChungnamCheongyang.objects.all()
    return render(request, 'index.html', {"posts": posts})

def ChungnamGeumsan_view(request):
    posts = ChungnamGeumsan.objects.all()
    return render(request, 'index.html', {"posts": posts})

def ChungnamGongju_view(request):
    posts = ChungnamGongju.objects.all()
    return render(request, 'index.html', {"posts": posts})

def ChungnamGyeryong_view(request):
    posts = ChungnamGyeryong.objects.all()
    return render(request, 'index.html', {"posts": posts})

def ChungnamNonsan_view(request):
    posts = ChungnamNonsan.objects.all()
    return render(request, 'index.html', {"posts": posts})

def ChungnamSeocheon_view(request):
    posts = ChungnamSeocheon.objects.all()
    return render(request, 'index.html', {"posts": posts})

def ChungnamSeosan_view(request):
    posts = ChungnamSeosan.objects.all()
    return render(request, 'index.html', {"posts": posts})

def DaeguBuk_view(request):
    posts = DaeguBuk.objects.all()
    return render(request, 'index.html', {"posts": posts})

def DaeguDalseo_view(request):
    posts = DaeguDalseo.objects.all()
    return render(request, 'index.html', {"posts": posts})

def DaeguDalseong_view(request):
    posts = DaeguDalseong.objects.all()
    return render(request, 'index.html', {"posts": posts})

def DaeguJung_view(request):
    posts = DaeguJung.objects.all()
    return render(request, 'index.html', {"posts": posts})

def DaeguNam_view(request):
    posts = DaeguNam.objects.all()
    return render(request, 'index.html', {"posts": posts})

def DaeguSuseong_view(request):
    posts = DaeguSuseong.objects.all()
    return render(request, 'index.html', {"posts": posts})

def DaejeonDaedeok_view(request):
    posts = DaejeonDaedeok.objects.all()
    return render(request, 'index.html', {"posts": posts})

def DaejeonEast_view(request):
    posts = DaejeonEast.objects.all()
    return render(request, 'index.html', {"posts": posts})

def DaejeonWest_view(request):
    posts = DaejeonWest.objects.all()
    return render(request, 'index.html', {"posts": posts})

def DaejeonYuseong_view(request):
    posts = DaejeonYuseong.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GangwonDonghae_view(request):
    posts = GangwonDonghae.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GangwonGoseong_view(request):
    posts = GangwonGoseong.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GangwonHongcheon_view(request):
    posts = GangwonHongcheon.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GangwonHwacheon_view(request):
    posts = GangwonHwacheon.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GangwonInje_view(request):
    posts = GangwonInje.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GangwonJeongseon_view(request):
    posts = GangwonJeongseon.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GangwonPyeongchang_view(request):
    posts = GangwonPyeongchang.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GangwonWonju_view(request):
    posts = GangwonWonju.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GangwonYanggu_view(request):
    posts = GangwonYanggu.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GangwonYangyang_view(request):
    posts = GangwonYangyang.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GangwonYeongwol_view(request):
    posts = GangwonYeongwol.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GwangjuEast_view(request):
    posts = GwangjuEast.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GwangjuGwangsan_view(request):
    posts = GwangjuGwangsan.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GwangjuNorth_view(request):
    posts = GwangjuNorth.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GwangjuSouth_view(request):
    posts = GwangjuSouth.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GwangjuWest_view(request):
    posts = GwangjuWest.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeongbukAndong_view(request):
    posts = GyeongbukAndong.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeongbukBonghwa_view(request):
    posts = GyeongbukBonghwa.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeongbukCheongdo_view(request):
    posts = GyeongbukCheongdo.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeongbukChilgok_view(request):
    posts = GyeongbukChilgok.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeongbukGimcheon_view(request):
    posts = GyeongbukGimcheon.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeongbukGoryeong_view(request):
    posts = GyeongbukGoryeong.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeongbukGumi_view(request):
    posts = GyeongbukGumi.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeongbukGunwi_view(request):
    posts = GyeongbukGunwi.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeongbukGyeongju_view(request):
    posts = GyeongbukGyeongju.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeongbukGyeongsan_view(request):
    posts = GyeongbukGyeongsan.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeongbukMungyeong_view(request):
    posts = GyeongbukMungyeong.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeongbukPohang_view(request):
    posts = GyeongbukPohang.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeongbukSangju_view(request):
    posts = GyeongbukSangju.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeongbukUiseong_view(request):
    posts = GyeongbukUiseong.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeongbukUljin_view(request):
    posts = GyeongbukUljin.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeongbukUlleung_view(request):
    posts = GyeongbukUlleung.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeongbukYecheon_view(request):
    posts = GyeongbukYecheon.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeongbukYeongcheon_view(request):
    posts = GyeongbukYeongcheon.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeongbukYeongdeok_view(request):
    posts = GyeongbukYeongdeok.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeongbukYeongyang_view(request):
    posts = GyeongbukYeongyang.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeonggiAnsan_view(request):
    posts = GyeonggiAnsan.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeonggiAnseong_view(request):
    posts = GyeonggiAnseong.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeonggiAnyang_view(request):
    posts = GyeonggiAnyang.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeonggiBucheon_view(request):
    posts = GyeonggiBucheon.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeonggiDongducheon_view(request):
    posts = GyeonggiDongducheon.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeonggiGapyeong_view(request):
    posts = GyeonggiGapyeong.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeonggiGimpo_view(request):
    posts = GyeonggiGimpo.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeonggiGoyang_view(request):
    posts = GyeonggiGoyang.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeonggiGunpo_view(request):
    posts = GyeonggiGunpo.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeonggiGuri_view(request):
    posts = GyeonggiGuri.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeonggiGwangju_view(request):
    posts = GyeonggiGwangju.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeonggiGwangmyeong_view(request):
    posts = GyeonggiGwangmyeong.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeonggiHanam_view(request):
    posts = GyeonggiHanam.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeonggiHwaseong_view(request):
    posts = GyeonggiHwaseong.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeonggiIcheon_view(request):
    posts = GyeonggiIcheon.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeonggiNamyangju_view(request):
    posts = GyeonggiNamyangju.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeonggiOsan_view(request):
    posts = GyeonggiOsan.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeonggiPaju_view(request):
    posts = GyeonggiPaju.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeonggiPyeongtaek_view(request):
    posts = GyeonggiPyeongtaek.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeonggiSeongnam_view(request):
    posts = GyeonggiSeongnam.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeonggiSiheung_view(request):
    posts = GyeonggiSiheung.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeonggiSuwon_view(request):
    posts = GyeonggiSuwon.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeonggiUijeongbu_view(request):
    posts = GyeonggiUijeongbu.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeonggiYangju_view(request):
    posts = GyeonggiYangju.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeonggiYangpyeong_view(request):
    posts = GyeonggiYangpyeong.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeonggiYeoju_view(request):
    posts = GyeonggiYeoju.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeonggiYeoncheon_view(request):
    posts = GyeonggiYeoncheon.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeonggiYongin_view(request):
    posts = GyeonggiYongin.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeongnamChangwon_view(request):
    posts = GyeongnamChangwon.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeongnamGeoje_view(request):
    posts = GyeongnamGeoje.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeongbukCheongdo_view(request):
    posts = GyeongbukCheongdo.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeongnamGimhae_view(request):
    posts = GyeongnamGimhae.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeongnamGoseong_view(request):
    posts = GyeongnamGoseong.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeongnamHadong_view(request):
    posts = GyeongnamHadong.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeongnamHaman_view(request):
    posts = GyeongnamHaman.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeongnamHamyang_view(request):
    posts = GyeongnamHamyang.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeongnamJinju_view(request):
    posts = GyeongnamJinju.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeongnamMiryang_view(request):
    posts = GyeongnamMiryang.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeongnamNamhae_view(request):
    posts = GyeongnamNamhae.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeongnamSacheon_view(request):
    posts = GyeongnamSacheon.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeongnamTongyeong_view(request):
    posts = GyeongnamTongyeong.objects.all()
    return render(request, 'index.html', {"posts": posts})

def GyeongnamUiryeong_view(request):
    posts = GyeongnamUiryeong.objects.all()
    return render(request, 'index.html', {"posts": posts})

def IncheonEast_view(request):
    posts = IncheonEast.objects.all()
    return render(request, 'index.html', {"posts": posts})

def IncheonGanghwa_view(request):
    posts = IncheonGanghwa.objects.all()
    return render(request, 'index.html', {"posts": posts})

def IncheonGyeyang_view(request):
    posts = IncheonGyeyang.objects.all()
    return render(request, 'index.html', {"posts": posts})

def IncheonJunggu_view(request):
    posts = IncheonJunggu.objects.all()
    return render(request, 'index.html', {"posts": posts})

def IncheonOngjin_view(request):
    posts = IncheonOngjin.objects.all()
    return render(request, 'index.html', {"posts": posts})

def IncheonSoutheast_view(request):
    posts = IncheonSoutheast.objects.all()
    return render(request, 'index.html', {"posts": posts})

def IncheonWest_view(request):
    posts = IncheonWest.objects.all()
    return render(request, 'index.html', {"posts": posts})

def IncheonYeonsu_view(request):
    posts = IncheonYeonsu.objects.all()
    return render(request, 'index.html', {"posts": posts})

def JejuSeogwipo_view(request):
    posts = JejuSeogwipo.objects.all()
    return render(request, 'index.html', {"posts": posts})

def JeonbukBuan_view(request):
    posts = JeonbukBuan.objects.all()
    return render(request, 'index.html', {"posts": posts})

def JeonbukGochang_view(request):
    posts = JeonbukGochang.objects.all()
    return render(request, 'index.html', {"posts": posts})

def JeonbukGunsan_view(request):
    posts = JeonbukGunsan.objects.all()
    return render(request, 'index.html', {"posts": posts})

def JeonbukImsil_view(request):
    posts = JeonbukImsil.objects.all()
    return render(request, 'index.html', {"posts": posts})

def JeonbukJeongeup_view(request):
    posts = JeonbukJeongeup.objects.all()
    return render(request, 'index.html', {"posts": posts})

def JeonbukJinan_view(request):
    posts = JeonbukJinan.objects.all()
    return render(request, 'index.html', {"posts": posts})

def JeonbukSamwon_view(request):
    posts = JeonbukSamwon.objects.all()
    return render(request, 'index.html', {"posts": posts})

def JeonbukSunchang_view(request):
    posts = JeonbukSunchang.objects.all()
    return render(request, 'index.html', {"posts": posts})

def JeonbukWanju_view(request):
    posts = JeonbukWanju.objects.all()
    return render(request, 'index.html', {"posts": posts})

def JeonnamBoseong_view(request):
    posts = JeonnamBoseong.objects.all()
    return render(request, 'index.html', {"posts": posts})

def JeonnamGangjin_view(request):
    posts = JeonnamGangjin.objects.all()
    return render(request, 'index.html', {"posts": posts})

def JeonnamGoheung_view(request):
    posts = JeonnamGoheung.objects.all()
    return render(request, 'index.html', {"posts": posts})

def JeonnamGokseong_view(request):
    posts = JeonnamGokseong.objects.all()
    return render(request, 'index.html', {"posts": posts})

def JeonnamGurye_view(request):
    posts = JeonnamGurye.objects.all()
    return render(request, 'index.html', {"posts": posts})

def JeonnamHaenam_view(request):
    posts = JeonnamHaenam.objects.all()
    return render(request, 'index.html', {"posts": posts})

def JeonnamHampyeong_view(request):
    posts = JeonnamHampyeong.objects.all()
    return render(request, 'index.html', {"posts": posts})

def JeonnamHwasun_view(request):
    posts = JeonnamHwasun.objects.all()
    return render(request, 'index.html', {"posts": posts})

def JeonnamJangheung_view(request):
    posts = JeonnamJangheung.objects.all()
    return render(request, 'index.html', {"posts": posts})

def JeonnamJangseong_view(request):
    posts = JeonnamJangseong.objects.all()
    return render(request, 'index.html', {"posts": posts})

def JeonnamMokpo_view(request):
    posts = JeonnamMokpo.objects.all()
    return render(request, 'index.html', {"posts": posts})

def JeonnamSuncheon_view(request):
    posts = JeonnamSuncheon.objects.all()
    return render(request, 'index.html', {"posts": posts})

def JeonnamWando(request):
    posts = JeonnamWando.objects.all()
    return render(request, 'index.html', {"posts": posts})

def JeonnamYeongam_view(request):
    posts = JeonnamYeongam.objects.all()
    return render(request, 'index.html', {"posts": posts})

def JeonnamYeonggwang_view(request):
    posts = JeonnamYeonggwang.objects.all()
    return render(request, 'index.html', {"posts": posts})

def JeonnamYeosu_view(request):
    posts = JeonnamYeosu.objects.all()
    return render(request, 'index.html', {"posts": posts})

def Sejong_view(request):
    posts = Sejong.objects.all()
    return render(request, 'index.html', {"posts": posts})

def SeoulDobong_view(request):
    posts = SeoulDobong.objects.all()
    return render(request, 'index.html', {"posts": posts})

def SeoulDongjak_view(request):
    posts = SeoulDongjak.objects.all()
    return render(request, 'index.html', {"posts": posts})

def SeoulEunpyeong_view(request):
    posts = SeoulEunpyeong.objects.all()
    return render(request, 'index.html', {"posts": posts})

def SeoulGangdong_view(request):
    posts = SeoulGangdong.objects.all()
    return render(request, 'index.html', {"posts": posts})

def SeoulGangnam_view(request):
    posts = SeoulGangnam.objects.all()
    return render(request, 'index.html', {"posts": posts})

def SeoulGangseo_view(request):
    posts = SeoulGangseo.objects.all()
    return render(request, 'index.html', {"posts": posts})

def SeoulGeumcheon_view(request):
    posts = SeoulGeumcheon.objects.all()
    return render(request, 'index.html', {"posts": posts})

def SeoulGuro_view(request):
    posts = SeoulGuro.objects.all()
    return render(request, 'index.html', {"posts": posts})

def SeoulGwanak_view(request):
    posts = SeoulGwanak.objects.all()
    return render(request, 'index.html', {"posts": posts})

def SeoulJongro_view(request):
    posts = SeoulJongro.objects.all()
    return render(request, 'index.html', {"posts": posts})

def SeoulJungnang_view(request):
    posts = SeoulJungnang.objects.all()
    return render(request, 'index.html', {"posts": posts})

def SeoulMapo_view(request):
    posts = SeoulMapo.objects.all()
    return render(request, 'index.html', {"posts": posts})

def SeoulNowon_view(request):
    posts = SeoulNowon.objects.all()
    return render(request, 'index.html', {"posts": posts})

def SeoulSeocho_view(request):
    posts = SeoulSeocho.objects.all()
    return render(request, 'index.html', {"posts": posts})

def SeoulSeodaemun_view(request):
    posts = SeoulSeodaemun.objects.all()
    return render(request, 'index.html', {"posts": posts})

def SeoulSeongbuk_view(request):
    posts = SeoulSeongbuk.objects.all()
    return render(request, 'index.html', {"posts": posts})

def SeoulSeongdong_view(request):
    posts = SeoulSeongdong.objects.all()
    return render(request, 'index.html', {"posts": posts})

def SeoulSongpa_view(request):
    posts = SeoulSongpa.objects.all()
    return render(request, 'index.html', {"posts": posts})

def SeoulYangcheon_view(request):
    posts = SeoulYangcheon.objects.all()
    return render(request, 'index.html', {"posts": posts})

def SeoulYeongdeungpo_view(request):
    posts = SeoulYeongdeungpo.objects.all()
    return render(request, 'index.html', {"posts": posts})

def SeoulYongsan_view(request):
    posts = SeoulYongsan.objects.all()
    return render(request, 'index.html', {"posts": posts})

def UlsanEast_view(request):
    posts = UlsanEast.objects.all()
    return render(request, 'index.html', {"posts": posts})

def UlsanNorth_view(request):
    posts = UlsanNorth.objects.all()
    return render(request, 'index.html', {"posts": posts})

def UlsanSouth_view(request):
    posts = UlsanSouth.objects.all()
    return render(request, 'index.html', {"posts": posts})

def UlsanUlju_view(request):
    posts = UlsanUlju.objects.all()
    return render(request, 'index.html', {"posts": posts})