(주)상림기술 웹사이트 — 멀티페이지 정적 사이트

■ 실행
  index.html 을 브라우저로 열면 됩니다.
  폰트·라이브러리 모두 동봉되어 인터넷 없이 완전 동작합니다.

■ 페이지 구성 (총 15개)
  index.html                     메인
  company/greeting.html          회사소개 > 인사말 + 회사개요
  company/record.html            회사소개 > 구축사례 (25건)
  company/certification.html     회사소개 > 인증현황
  company/location.html          회사소개 > 오시는 길
  business/its.html              사업분야 > 지능형 교통체계
  business/bis.html              사업분야 > 버스정보 안내시스템
  business/evs.html              사업분야 > 긴급차량 우선신호 시스템
  business/ssz.html              사업분야 > 스마트 스쿨존 시스템
  product/vms.html               주요제품 > 도로교통 전광판(VMS)
  product/bit.html               주요제품 > 버스정보안내 전광판(BIT)
  product/ecs.html               주요제품 > 전기차 충전소 전광판
  product/gnss.html              주요제품 > 초정밀 모듈(GNSS)
  product/ptz.html               주요제품 > PTZ 카메라
  contact.html                   문의하기

■ 공통 자원
  assets/style.css     전체 스타일 (페이지마다 복사되지 않음)
  assets/app.js        헤더·모바일메뉴·스크롤 애니메이션·탭
  assets/globe.js      메인 전용 3D GNSS 지구본
  assets/img/          로고 3종
  fonts/               Pretendard Variable
  vendor/              three.js · GSAP · ScrollTrigger · Swiper

■ 페이지 추가·메뉴 수정 방법  ★중요
  build.py 상단의 NAV 목록만 고치고 아래를 실행하면
  전 페이지의 GNB·서브메뉴·푸터·브레드크럼이 한 번에 갱신됩니다.

      python3 build.py

  HTML 15개를 일일이 고칠 필요가 없습니다.
  (Python 3.12 이상 필요)

■ 각 페이지 구조
  헤더(고정) → 서브비주얼(제목+브레드크럼) → 서브메뉴(형제 페이지)
  → 본문 → 문의 유도 CTA → 푸터

  현재 위치는 GNB와 서브메뉴에 자동으로 강조 표시됩니다.

■ 확인 필요 (비워둔 항목)
  · 설립일 연도 — 원문에 "____년 04월 07일"
  · 인증현황 실제 목록
  · 사업자등록번호
  · 지도 임베드 코드 (오시는 길)
  · 실제 제품·현장 사진 (현재 SVG 그래픽 대체)

■ 문의 폼
  현재는 화면 구성용입니다. 실제 메일 발송에는 백엔드 연동이 필요합니다.
