# 공공데이터를 활용한 전국 공중 화장실 위치 및 정보 제공 서비스
*  개발기간 : 2021.02.08 ~ 2021.02.23
*  개발인원 : 5명

## 주제 선정 이유
* 사용할 수 있는 주변의 화장실을 급하게 찾았던 경험
* 공중화장실 중 장애인, 어린이가 이용할 수 있는 화장실 현황 분석

## 개발 환경
* Client
  * HTML5
  * CSS3
  * JavaScript
* Server
  * Django
* Database
  * MariaDB
* Map API
  * Naver Map API

## 데이터 수집
*  화장실 위치정보
*  화장실 상세정보
*  공공데이터 포털
*  https://www.data.go.kr/tcs/lms/liv/selectLocationView.do


## 기능
### Main Page
![화장실1](https://user-images.githubusercontent.com/52616995/114037060-91f52300-98bb-11eb-92fc-7b4bc6570c9a.png)
* 사용자 주변 화장실 검색 기능
* 조건설정을 통한 화장실 검색 기능

### 사용자 주변 화장실 검색 기능
![화장실3](https://user-images.githubusercontent.com/52616995/114037635-1f387780-98bc-11eb-9dc0-ec00224607cc.png)
![화장실2](https://user-images.githubusercontent.com/52616995/114037505-04fe9980-98bc-11eb-98c0-674de92ff8a6.png)
* 사용자가 현재 위치한 지역의 화장실 지도 출력
* 사용자와 가장 가까운 화장실의 정보 자동 출력
