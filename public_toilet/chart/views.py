from django.shortcuts import render
import numpy as np
from matplotlib import pyplot as plt
import os
from .models import *

def chart_view(request):    # 전국 도별 화장실 개수 그래프
    plt.clf()
    posts = AllToiletNum.objects.all()
    values = AllToiletNum.objects.values()
    length = len(values) # 지역개수
    plt.rcParams['font.family'] = 'Malgun Gothic'

    x = np.arange(length)
    location = []
    toilet_num = []
    print(x)

    for i in values:
        location.append(i["location"])
        toilet_num.append(i["toilet_num"])

    plt.bar(x, toilet_num, width=0.6)
    plt.xticks(x, location, fontsize=5, rotation=45)
    plt.ylabel('화장실 수', fontsize='10')

    plt.title('전국 도별 화장실 개수')

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    plt.savefig(BASE_DIR + '\\static\\img\\chart.png', dpi=300)

    return render(request, 'chart.html', {"posts": posts})

def option_chart(request):
    plt.clf()
    city = request.GET.get('city')
    values = []
    location = []
    toilet_num = []
    disabled_toilet_num = []
    plt.rcParams['font.family'] = 'Malgun Gothic'

    if city == "서울특별시":
        location = ["도봉구", "동작구", "은평구", "강동구", "강남구", "강서구", "금천구", "구로구",
                    "관악구", "종로구", "중랑구", "마포구", "노원구", "서초구", "서대문구", "성북구",
                    "성동구", "송파구", "양천구", "용산구"]
        values.append(SeoulDobong.objects.values())
        values.append(SeoulDongjak.objects.values())
        values.append(SeoulEunpyeong.objects.values())
        values.append(SeoulGangdong.objects.values())
        values.append(SeoulGangnam.objects.values())
        values.append(SeoulGangseo.objects.values())
        values.append(SeoulGeumcheon.objects.values())
        values.append(SeoulGuro.objects.values())
        values.append(SeoulGwanak.objects.values())
        values.append(SeoulJongro.objects.values())
        values.append(SeoulJungnang.objects.values())
        values.append(SeoulMapo.objects.values())
        values.append(SeoulNowon.objects.values())
        values.append(SeoulSeocho.objects.values())
        values.append(SeoulSeodaemun.objects.values())
        values.append(SeoulSeongbuk.objects.values())
        values.append(SeoulSeongdong.objects.values())
        values.append(SeoulSongpa.objects.values())
        values.append(SeoulYangcheon.objects.values())
        values.append(SeoulYongsan.objects.values())


    elif city == "부산광역시":
        location = ["북구", "동구", "동내구", "부산진구", "남구", "사하구", "사상구", "수성구",
                    "서구", "수영구", "영도구", "연제구"]
        values.append(BusanBuk.objects.values())
        values.append(BusanDong.objects.values())
        values.append(BusanDongnae.objects.values())
        values.append(BusanJin.objects.values())
        values.append(BusanJung.objects.values())
        values.append(BusanNam.objects.values())
        values.append(BusanSaha.objects.values())
        values.append(BusanSasang.objects.values())
        values.append(BusanSeo.objects.values())
        values.append(BusanSuyeong.objects.values())
        values.append(BusanYeongdo.objects.values())
        values.append(BusanYeonje.objects.values())

    elif city == "대구광역시":
        location = ["북구", "달서구", "달성군", "중구", "남구", "수성구"]
        values.append(DaeguBuk.objects.values())
        values.append(DaeguDalseo.objects.values())
        values.append(DaeguDalseong.objects.values())
        values.append(DaeguJung.objects.values())
        values.append(DaeguNam.objects.values())
        values.append(DaeguSuseong.objects.values())

    elif city == "인천광역시":
        location = ["동구", "강화군", "중구", "옹진군", "남동구", "서구", "연수구"]
        values.append(IncheonEast.objects.values())
        values.append(IncheonGanghwa.objects.values())
        values.append(IncheonJunggu.objects.values())
        values.append(IncheonOngjin.objects.values())
        values.append(IncheonSoutheast.objects.values())
        values.append(IncheonWest.objects.values())
        values.append(IncheonYeonsu.objects.values())

    elif city == "광주광역시":
        location = ["동구", "광산구", "북구", "남구", "서구"]
        values.append(GwangjuEast.objects.values())
        values.append(GwangjuGwangsan.objects.values())
        values.append(GwangjuNorth.objects.values())
        values.append(GwangjuSouth.objects.values())
        values.append(GwangjuWest.objects.values())

    elif city == "대전광역시":
        location = ["대덕구", "동구", "서구", "유성구"]
        values.append(DaejeonDaedeok.objects.values())
        values.append(DaejeonEast.objects.values())
        values.append(DaejeonWest.objects.values())
        values.append(DaejeonYuseong.objects.values())

    elif city == "울산광역시":
        location = ["동구", "남구", "동구", "울주군"]
        values.append(UlsanEast.objects.values())
        values.append(UlsanSouth.objects.values())
        values.append(UlsanEast.objects.values())
        values.append(UlsanUlju.objects.values())

    elif city == "경기도":
        location = ["안산시", "안성시", "안양시", "부천시", "동두천시", "가평군", "김포시",
                    "고양시", "군포시", "구리시", "광주시", "광명시", "하남시", "화성시",
                    "이천시", "남양주시", "오산시", "파주시", "평택시", "성남시", "시흥시",
                    "수원시", "의정부시", "양주시", "양평군", "여주시", "연천군", "용인시"]
        values.append(GyeonggiAnsan.objects.values())
        values.append(GyeonggiAnseong.objects.values())
        values.append(GyeonggiAnyang.objects.values())
        values.append(GyeonggiBucheon.objects.values())
        values.append(GyeonggiDongducheon.objects.values())
        values.append(GyeonggiGapyeong.objects.values())
        values.append(GyeonggiGimpo.objects.values())
        values.append(GyeonggiGoyang.objects.values())
        values.append(GyeonggiGunpo.objects.values())
        values.append(GyeonggiGuri.objects.values())
        values.append(GyeonggiGwangju.objects.values())
        values.append(GyeonggiGwangmyeong.objects.values())
        values.append(GyeonggiHanam.objects.values())
        values.append(GyeonggiHwaseong.objects.values())
        values.append(GyeonggiIcheon.objects.values())
        values.append(GyeonggiNamyangju.objects.values())
        values.append(GyeonggiOsan.objects.values())
        values.append(GyeonggiPaju.objects.values())
        values.append(GyeonggiPyeongtaek.objects.values())
        values.append(GyeonggiSeongnam.objects.values())
        values.append(GyeonggiSiheung.objects.values())
        values.append(GyeonggiSuwon.objects.values())
        values.append(GyeonggiUijeongbu.objects.values())
        values.append(GyeonggiYangju.objects.values())
        values.append(GyeonggiYangpyeong.objects.values())
        values.append(GyeonggiYeoju.objects.values())
        values.append(GyeonggiYeoncheon.objects.values())
        values.append(GyeonggiYongin.objects.values())

    elif city == "강원도":
        location = ["동해시", "고성군", "홍천군", "화천군", "인제군", "정선군", "평창군",
                    "원주시", "양구군", "양양군", "영월군"]
        values.append(GangwonDonghae.objects.values())
        values.append(GangwonGoseong.objects.values())
        values.append(GangwonHongcheon.objects.values())
        values.append(GangwonHwacheon.objects.values())
        values.append(GangwonInje.objects.values())
        values.append(GangwonJeongseon.objects.values())
        values.append(GangwonPyeongchang.objects.values())
        values.append(GangwonWonju.objects.values())
        values.append(GangwonYanggu.objects.values())
        values.append(GangwonYangyang.objects.values())
        values.append(GangwonYeongwol.objects.values())

    elif city == "충청북도":
        location = ["부은군", "청주시", "충주시", "단양군", "음성군", "제천시", "진천군",
                    "옥천군", "영동군"]
        values.append(ChungbukBoeun.objects.values())
        values.append(ChungbukCheongju.objects.values())
        values.append(ChungbukChungju.objects.values())
        values.append(ChungbukDanyang.objects.values())
        values.append(ChungbukEumseong.objects.values())
        values.append(ChungbukJecheon.objects.values())
        values.append(ChungbukJincheon.objects.values())
        values.append(ChungbukOkjcheon.objects.values())
        values.append(ChungbukYeongdong.objects.values())

    elif city == "충청남도":
        location = ["아산시", "보령군", "부여군", "청양군", "금산군", "공주시", "계룡시", "논산시",
                    "서천군", "서산시"]
        values.append(ChungnamAsan.objects.values())
        values.append(ChungnamBoryeong.objects.values())
        values.append(ChungnamBuyeo.objects.values())
        values.append(ChungnamCheongyang.objects.values())
        values.append(ChungnamGeumsan.objects.values())
        values.append(ChungnamGongju.objects.values())
        values.append(ChungnamGyeryong.objects.values())
        values.append(ChungnamNonsan.objects.values())
        values.append(ChungnamSeocheon.objects.values())
        values.append(ChungnamSeosan.objects.values())

    elif city == "전라북도":
        location = ["부안군", "고창군", "군산시", "임실군", "정읍시", "진안군", "남원시",
                    "순창군", "완주군"]
        values.append(JeonbukBuan.objects.values())
        values.append(JeonbukGochang.objects.values())
        values.append(JeonbukGunsan.objects.values())
        values.append(JeonbukImsil.objects.values())
        values.append(JeonbukJeongeup.objects.values())
        values.append(JeonbukJinan.objects.values())
        values.append(JeonbukSamwon.objects.values())
        values.append(JeonbukSunchang.objects.values())
        values.append(JeonbukWanju.objects.values())


    elif city == "전라남도":
        location = ["보성군", "강진군", "고흥군", "곡성군", "구례군", "해남군", "함평군",
                    "화순군", "장흥군", "목포시", "순천시", "완도군", "영암군", "영광군",
                    "여수시"]
        values.append(JeonnamBoseong.objects.values())
        values.append(JeonnamGangjin.objects.values())
        values.append(JeonnamGoheung.objects.values())
        values.append(JeonnamGokseong.objects.values())
        values.append(JeonnamGurye.objects.values())
        values.append(JeonnamHaenam.objects.values())
        values.append(JeonnamHampyeong.objects.values())
        values.append(JeonnamHwasun.objects.values())
        values.append(JeonnamJangheung.objects.values())
        values.append(JeonnamMokpo.objects.values())
        values.append(JeonnamSuncheon.objects.values())
        values.append(JeonnamWando.objects.values())
        values.append(JeonnamYeongam.objects.values())
        values.append(JeonnamYeonggwang.objects.values())
        values.append(JeonnamYeosu.objects.values())

    elif city == "경상북도":
        location = ["안동군", "봉화군", "청도군", "칠곡군", "김천시", "고령군", "구미시",
                    "군위군", "경산시", "경주시", "문경시", "포항시", "상주군", "의성군",
                    "울진군", "울릉군", "예천군", "영천군", "영덕군", "영양군"]
        values.append(GyeongbukAndong.objects.values())
        values.append(GyeongbukBonghwa.objects.values())
        values.append(GyeongbukCheongdo.objects.values())
        values.append(GyeongbukChilgok.objects.values())
        values.append(GyeongbukGimcheon.objects.values())
        values.append(GyeongbukGoryeong.objects.values())
        values.append(GyeongbukGumi.objects.values())
        values.append(GyeongbukGunwi.objects.values())
        values.append(GyeongbukGyeongsan.objects.values())
        values.append(GyeongbukGyeongju.objects.values())
        values.append(GyeongbukMungyeong.objects.values())
        values.append(GyeongbukPohang.objects.values())
        values.append(GyeongbukSangju.objects.values())
        values.append(GyeongbukUiseong.objects.values())
        values.append(GyeongbukUljin.objects.values())
        values.append(GyeongbukUlleung.objects.values())
        values.append(GyeongbukYecheon.objects.values())
        values.append(GyeongbukYeongcheon.objects.values())
        values.append(GyeongbukYeongdeok.objects.values())
        values.append(GyeongbukYeongyang.objects.values())

    elif city == "경상남도":
        location = ["창원시", "거제시", "김해시", "고성군", "하동군", "함안군", "함양군", "진주시",
                    "밀양시", "남해군", "사천시", "통영군", "의령군"]
        values.append(GyeongnamChangwon.objects.values())
        values.append(GyeongnamGeoje.objects.values())
        values.append(GyeongnamGimhae.objects.values())
        values.append(GyeongnamGoseong.objects.values())
        values.append(GyeongnamHadong.objects.values())
        values.append(GyeongnamHaman.objects.values())
        values.append(GyeongnamHamyang.objects.values())
        values.append(GyeongnamJinju.objects.values())
        values.append(GyeongnamMiryang.objects.values())
        values.append(GyeongnamNamhae.objects.values())
        values.append(GyeongnamSacheon.objects.values())
        values.append(GyeongnamTongyeong.objects.values())
        values.append(GyeongnamUiryeong.objects.values())

    elif city == "제주특별자치도":
        location = ["서귀포시"]
        values.append(JejuSeogwipo.objects.values())

    length = len(values)
    x = np.arange(length)


    for i in values:
        count = 0
        disabledCount = 0
        for j in i:
            count = count + 1
            if j["male_disabled_toilet_public_toiletnum"]!=0 and j["female_disabled_toilet_num"]!=0:
                disabledCount = disabledCount + 1

        toilet_num.append(count)
        disabled_toilet_num.append(disabledCount)

    plt.bar(x, toilet_num, width=0.2)
    plt.bar(x+0.2, disabled_toilet_num, width=0.2)
    plt.xticks(x, location, fontsize=5, rotation=45)

    plt.ylabel('화장실 수', fontsize='10')
    plt.title(city + " 화장실 그래프")


    print(values[0][0]["male_disabled_toilet_public_toiletnum"])

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    plt.savefig(BASE_DIR + '\\static\\img\\chart_option.png', dpi=300)

    return render(request, 'chart_option.html')


