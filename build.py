# -*- coding: utf-8 -*-
"""
(주)상림기술 웹사이트 정적 페이지 생성기
--------------------------------------------------
공통 헤더·서브비주얼·서브메뉴·CTA·푸터를 한 곳에서 관리하고
각 페이지의 본문만 갈아끼워 15개 페이지를 만듭니다.

메뉴를 바꾸려면 아래 NAV 만 수정하면 전 페이지에 반영됩니다.
  python3 build.py
"""
import os, re, shutil

ROOT = os.path.dirname(os.path.abspath(__file__))

# ============================================================
# 사이트 구조 — 이 목록이 곧 GNB·푸터·서브메뉴·사이트맵
# ============================================================
NAV_KO = [
    ("회사소개", "company", [
        ("인사말",         "company/greeting.html"),
        ("연혁",           "company/history.html"),
        ("조직도",         "company/organization.html"),
        ("구축사례",       "company/record.html"),
        ("인증현황",       "company/certification.html"),
        ("파트너사",       "company/partners.html"),
        ("오시는 길",      "company/location.html"),
    ]),
    ("사업분야", "business", [
        ("지능형 교통체계",        "business/its.html"),
        ("버스정보 안내시스템",     "business/bis.html"),
        ("긴급차량 우선신호 시스템", "business/evs.html"),
        ("스마트 스쿨존 시스템",    "business/ssz.html"),
    ]),
    ("주요제품", "product", [
        ("도로교통 전광판(VMS)",     "product/vms.html"),
        ("버스정보안내 전광판(BIT)", "product/bit.html"),
        ("전기차 충전소 전광판",     "product/ecs.html"),
        ("초정밀 모듈(GNSS)",        "product/gnss.html"),
        ("PTZ 카메라",               "product/ptz.html"),
        ("상황판(대시보드)",         "product/dashboard.html"),
    ]),
    ("문의하기", "contact", [
        ("문의하기", "contact.html"),
    ]),
]

NAV_EN = [
    ("Company", "company", [
        ("CEO Message",      "company/greeting.html"),
        ("History",          "company/history.html"),
        ("Organization",     "company/organization.html"),
        ("Track Record",     "company/record.html"),
        ("Certifications",   "company/certification.html"),
        ("Partners",         "company/partners.html"),
        ("Directions",       "company/location.html"),
    ]),
    ("Business", "business", [
        ("Intelligent Transport System (ITS)", "business/its.html"),
        ("Bus Information System (BIS)",       "business/bis.html"),
        ("Emergency Vehicle Priority Signal",  "business/evs.html"),
        ("Smart School Zone",                  "business/ssz.html"),
    ]),
    ("Products", "product", [
        ("Variable Message Sign (VMS)", "product/vms.html"),
        ("Bus Information Terminal (BIT)", "product/bit.html"),
        ("EV Charging Station Display", "product/ecs.html"),
        ("High-Precision GNSS Module", "product/gnss.html"),
        ("PTZ Camera", "product/ptz.html"),
        ("Control Wall Dashboard", "product/dashboard.html"),
    ]),
    ("Contact", "contact", [
        ("Contact Us", "contact.html"),
    ]),
]

LANG = "ko"                     # 빌드 중 현재 언어
def NAV():  return NAV_KO if LANG == "ko" else NAV_EN
def LD():   return "" if LANG == "ko" else "en/"

UI = {
 "ko": dict(
   home="홈", menu_open="메뉴 열기", mobile_menu="모바일 메뉴", to_top="맨 위로",
   cta_h="교통 시스템 도입을 검토 중이신가요?",
   cta_p="사업 요구사항을 알려주시면 상림기술이 최적의 솔루션을 제안드립니다.",
   cta_btn="문의하기",
   foot_way="오시는 길",
   foot_hq="본사 · SK테크노파크 D동 1507호",
   foot_ft="공장 · SK테크노파크 D동 1508호",
   foot_addr="경기도 광명시 하안로 60",
   foot_slogan="축적된 기술력으로 더 안전한 길과<br>더 나은 교통시스템을 만듭니다.",
   foot_biz="%s · 대표이사 임상일 · 사업자등록번호 %s",
   cw_open="온라인 상담 열기", cw_tip="무엇을 도와드릴까요?",
   cw_title="상림기술 상담", cw_reply="보통 1영업일 이내 회신", cw_close="닫기",
   cw_call="전화", cw_mail="이메일", cw_form="문의 양식",
   htmllang="ko",
 ),
 "en": dict(
   home="Home", menu_open="Open menu", mobile_menu="Mobile menu", to_top="Back to top",
   cta_h="Planning a traffic system project?",
   cta_p="Tell us your requirements and SangLim Technologies will propose the right solution.",
   cta_btn="Contact us",
   foot_way="Directions",
   foot_hq="Head Office · SK Techno Park D-1507",
   foot_ft="Factory · SK Techno Park D-1508",
   foot_addr="60 Haan-ro, Gwangmyeong-si, Gyeonggi-do, Korea",
   foot_slogan="Building safer roads and better traffic<br>systems with proven engineering.",
   foot_biz="%s · CEO Lim Sang-il · Business Reg. No. %s",
   cw_open="Open live enquiry", cw_tip="How can we help?",
   cw_title="SangLim Support", cw_reply="Usually replies within 1 business day", cw_close="Close",
   cw_call="Call", cw_mail="Email", cw_form="Form",
   htmllang="en",
 ),
}
def U(k): return UI[LANG][k]

COMPANY_EN = "SangLim Technologies Co., Ltd."
def CO(): return COMPANY if LANG == "ko" else COMPANY_EN

COMPANY = "(주)상림기술"
TEL, MAIL = "02-2083-1333", "ceo@sanglim.co.kr"
BIZNO = "197-87-02040"   # 환경표지 인증서에서 확인
FOUNDED = "2021년 04월 07일"
STAFF      = "46명"          # 재직인원 (일반현황 2026)
TECH_STAFF = "26명"          # 그중 기술자
BIZ_FIELDS = ("정보통신공사업 · 소프트웨어사업 · 엔지니어링사업<br>"
              "지능형 교통시스템(ITS) · 긴급교통신호제어시스템 · 스마트교차로 · 통합관제시스템")
ADDR_HQ = "경기도 광명시 하안로 60, 광명 SK테크노파크 D동 1507호"
ADDR_FT = "경기도 광명시 하안로 60, 광명 SK테크노파크 D동 1508호"
ADDR_HQ_EN = "SK Techno Park D-1507, 60 Haan-ro, Gwangmyeong-si, Gyeonggi-do, Republic of Korea"
ADDR_FT_EN = "SK Techno Park D-1508, 60 Haan-ro, Gwangmyeong-si, Gyeonggi-do, Republic of Korea"
TAGLINE = "축적된 기술력과 도전정신으로 더 나은 교통시스템을 만들어 갑니다."


def _ver():
    """페이지 내용·CSS·JS 중 하나라도 바뀌면 값이 바뀌는 캐시 무효화 토큰.

    예전에는 style.css / app.js 만 봤기 때문에, 글귀만 고친 배포에서는 토큰이
    그대로였고 브라우저가 옛 HTML 을 계속 보여 줬습니다. 생성기 소스까지 포함합니다.
    """
    import hashlib
    h = hashlib.md5()
    for f in ("assets/style.css", "assets/app.js", "build.py", "content_en.py"):
        fp = os.path.join(ROOT, f)
        if os.path.exists(fp):
            h.update(open(fp, "rb").read())
    # 제품 이미지가 교체되면 토큰이 바뀌도록 파일명·크기·수정시각을 함께 반영합니다
    imgdir = os.path.join(ROOT, "assets/img/prod")
    if os.path.isdir(imgdir):
        for name in sorted(os.listdir(imgdir)):
            st = os.stat(os.path.join(imgdir, name))
            h.update(("%s:%d:%d" % (name, st.st_size, int(st.st_mtime))).encode())
    return h.hexdigest()[:8]


V = _ver()


def rel(path):
    """페이지 깊이에 맞는 상대경로 접두사. 영문판은 en/ 아래라 한 단계 깊다."""
    return "../" * (LD() + path).count("/")


# ------------------------------------------------------------
# 공통 조각
# ------------------------------------------------------------

def lang_links(p, url):
    """KR / EN 토글 — 같은 페이지의 반대 언어판으로 이동합니다."""
    ko_href = p + url
    en_href = p + "en/" + url
    ko_cls = ' class="on"' if LANG == "ko" else ""
    en_cls = ' class="on"' if LANG == "en" else ""
    return ('<a href="%s"%s>KR</a><span>/</span><a href="%s"%s>EN</a>'
            % (ko_href, ko_cls, en_href, en_cls))


def header(cur, p, url="index.html"):
    items = []
    for label, key, kids in NAV():
        active = " class=\"cur\"" if key == cur else ""
        top = p + LD() + kids[0][1]
        if len(kids) > 1:
            sub = "".join(f'<li><a href="{p}{LD()}{u}">{t}</a></li>' for t, u in kids)
            items.append(
                f'<li{active}><a href="{top}">{label}</a>'
                f'<div class="gnb-2dep"><ul>{sub}</ul></div></li>')
        else:
            items.append(f'<li{active}><a href="{top}">{label}</a></li>')
    return f'''<header class="header" id="header">
  <div class="header-inner">
    <a href="{p}{LD()}index.html" class="logo">
      <img class="lg-white" src="{p}assets/img/logo-h-white.png" alt="{CO()}">
      <img class="lg-color" src="{p}assets/img/logo-h.png" alt="{CO()}">
    </a>
    <nav><ul class="gnb">{"".join(items)}</ul></nav>
    <div class="header-util">
      <div class="lang">{lang_links(p, url)}</div>
      <button class="navtog" id="navtog" aria-label="{U('menu_open')}" aria-expanded="false"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>
<div class="drawer-dim" id="dim"></div>
<aside class="drawer" id="drawer" aria-label="{U('mobile_menu')}"></aside>'''


def subvis(title, cur, url, p):
    """서브 비주얼 + 브레드크럼"""
    sect = next(n for n in NAV() if n[1] == cur)
    crumb = (f'<a href="{p}{LD()}index.html">{U("home")}</a><i></i>'
             f'<a href="{p}{LD()}{sect[2][0][1]}">{sect[0]}</a>')
    if len(sect[2]) > 1:
        crumb += f'<i></i><span class="cur">{title}</span>'
    return f'''<section class="subvis">
  <span class="orb o1"></span><span class="orb o2"></span>
  <div class="subvis-inner">
    <h1>{title}</h1>
    <div class="crumb">{crumb}</div>
  </div>
</section>'''


def subnav(cur, url, p):
    sect = next(n for n in NAV() if n[1] == cur)
    if len(sect[2]) < 2:
        return ""
    parts = []
    for t, u in sect[2]:
        on = ' class="on"' if u == url else ''
        parts.append('<li><a href="%s%s%s"%s>%s</a></li>' % (p, LD(), u, on, t))
    li = "".join(parts)
    return f'<nav class="subnav"><ul>{li}</ul></nav>'


def cta(p):
    return f'''<section class="section cta">
  <div class="area" data-reveal>
    <h2>{U("cta_h")}</h2>
    <p>{U("cta_p")}</p>
    <a href="{p}{LD()}contact.html" class="btn btn-primary">{U("cta_btn")}
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
  </div>
</section>'''


def footer(p):
    cols = ""
    for label, key, kids in NAV()[:3]:
        li = "".join(f'<li><a href="{p}{LD()}{u}">{t}</a></li>' for t, u in kids)
        cols += f'<div><h4>{label}</h4><ul>{li}</ul></div>'
    cols += (f'<div><h4>{U("foot_way")}</h4><ul>'
             f'<li>{U("foot_hq")}</li>'
             f'<li>{U("foot_ft")}</li>'
             f'<li>{U("foot_addr")}</li></ul></div>')
    return f'''<footer class="footer" id="footer">
  <div class="area-wrap">
    <div class="footer-top">
      <div class="footer-brand">
        <img class="footer-logo" src="{p}assets/img/logo-v-white.png" alt="{CO()}">
        <p>{U("foot_slogan")}</p>
        <p style="margin-top:16px;font-size:.86rem">
          T. <a href="tel:0220831333">{TEL}</a><br>
          E. <a href="mailto:{MAIL}">{MAIL}</a></p>
      </div>
      <nav class="footer-map">{cols}</nav>
    </div>
    <div class="footer-bottom">
      <span>{U("foot_biz") % (CO(), BIZNO)}<br>{ADDR_HQ if LANG=="ko" else ADDR_HQ_EN}</span>
      <span>Copyright &copy; SangLim Technologies. All rights Reserved.</span>
    </div>
  </div>
</footer>
<button class="to-top" id="totop" aria-label="{U('to_top')}">
  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M12 19V5M6 11l6-6 6 6"/></svg>
</button>'''



# 제품 실사 (회사소개서 25ver 에서 추출)
PROD_IMG = {
  "vms":  ("도형식 도로교통 전광판(VMS)",                "contain"),
  "vmsx": ("도형식 도로교통 전광판 내부 구조 — 분해도",  "contain"),
  "bit":  ("버스정보안내 전광판(BIT) 표출 화면",          "contain"),
  "bitx": ("버스정보안내 전광판 내부 구조 — 분해도",   "contain"),
  "ecs":  ("전기차 충전소 전광판 설치 현장",              "cover"),
  "gnss": ("초정밀 GNSS 모듈 본체",                       "contain"),
  "gnssx":("초정밀 GNSS 모듈 내부 구조 — 분해도",       "contain"),
  "ptz":  ("PTZ 회전형 보안 카메라",                      "contain"),
  "ptzx": ("PTZ 회전형 보안 카메라 내부 구조 — 분해도", "contain"),
  "evs":  ("긴급차량 우선신호 안내 전광판",               "contain"),
  "evs2": ("긴급차량 우선신호 시스템 — 119 구급·소방차",   "contain"),
  "ssz2": ("어린이보호구역 스마트 스쿨존 안내",            "cover"),
  "ssz":  ("스마트 스쿨존 안전시스템 표출 화면",          "cover"),
  "its":  ("지능형 교통체계(ITS) 구성도",                 "contain"),
  "bis":  ("버스정보 안내시스템(BIS) 구성도",             "contain"),
  "aboutviz": ("버스정보안내 전광판 · 스마트 스쿨존 · 긴급차량 우선신호", "contain"),
}

# 아코디언에서 마우스를 올리면 두 번째 이미지로 부드럽게 교차 전환됩니다.
# (두 이미지는 캔버스 크기가 동일해야 위치가 어긋나지 않습니다)
PROD_ALT = {"vms": "vmsx", "bit": "bitx", "gnss": "gnssx", "ptz": "ptzx"}

BIZ_ICO = {"ITS": "its", "BIS": "bis", "EVS": "evs", "SSZ": "ssz"}


def bizico(code, p=""):
    """사업분야 카드 아이콘 — 벡터(SVG)를 CSS 마스크로 찍어 색은 currentColor 를 따릅니다."""
    k = BIZ_ICO[code]
    # url() 은 인라인 style 에 직접 넣습니다. 커스텀 속성에 담으면 브라우저가
    # 스타일시트 위치(/assets/) 기준으로 경로를 풀어 assets/assets/... 로 깨집니다.
    u = "%sassets/img/ico/%s.svg?v=%s" % (p, k, V)
    m = "url(%s) center/contain no-repeat" % u
    return ('<div class="ic"><i class="ico" aria-hidden="true" '
            'style="-webkit-mask:%s;mask:%s"></i></div>') % (m, m)


def pimg(key, p="", cls="", loading="lazy", alt=None):
    """제품 실사 <picture>. 없으면 빈 문자열."""
    if key not in PROD_IMG:
        return ""
    a, fit = PROD_IMG[key]
    if alt is not None:
        a = alt
    c = (' class="%s"' % cls) if cls else ""
    return ('<picture%s><source srcset="%sassets/img/prod/%s.webp?v=%s" type="image/webp">'
            '<img src="%sassets/img/prod/%s.png?v=%s" alt="%s" loading="%s" data-fit="%s"></picture>'
            % (c, p, key, V, p, key, V, a, loading, fit))


def ptz_show(p, lang="ko", to="product"):
    """PTZ 카메라 — 스크롤에 맞춰 영상이 재생되는 몰입형 소개 (Apple 스타일)."""
    T = dict(
      ko=dict(kicker="PTZ CAMERA",
        h1="부품 하나까지<br><em>직접</em> 설계했습니다",
        p1="렌즈 모듈부터 팬·틸트 구동부, 제어 보드까지. 상림기술이 설계하고 만듭니다.",
        h2="어둠 속에서도<br><em>컬러</em> 그대로",
        p2="1/2.8″ SONY STARVIS 센서와 2D/3D 노이즈 리덕션으로 저조도에서도 선명한 컬러 영상을 얻습니다.",
        h3="<em>360°</em> 끊김 없는 회전",
        p3="제한 없는 팬과 -40°~+55° 틸트. 교차로 전체를 한 대로 담습니다.",
        h4="현장에서 검증된<br>신뢰성",
        p4="KC 적합등록과 TTA 시험인증을 마친 3개 모델을 운영 중입니다.",
        chips=["SL-P223ID5","SL-P230ID5","SL-P510ID5","KC 적합등록","TTA 인증"],
        cta="PTZ 카메라 자세히 보기", cta2="도입 문의하기", replay="다시 보기"),
      en=dict(kicker="PTZ CAMERA",
        h1="Engineered<br><em>part by part</em>",
        p1="From the lens module to the pan-tilt drive and the control board — designed and built by SangLim.",
        h2="Colour that holds<br>in the <em>dark</em>",
        p2="A 1/2.8″ SONY STARVIS sensor with 2D/3D noise reduction keeps images clean and in colour at night.",
        h3="<em>360°</em> endless pan",
        p3="Unlimited pan with -40° to +55° tilt. One camera covers the whole intersection.",
        h4="Proven in<br>the field",
        p4="Three models in service, each with KC conformity registration and TTA test certification.",
        chips=["SL-P223ID5","SL-P230ID5","SL-P510ID5","KC certified","TTA tested"],
        cta="Explore the PTZ camera", cta2="Talk to us", replay="Replay"),
    )[lang]
    chip_html = "".join('<span>%s</span>' % c for c in T["chips"])
    T = dict(T); T.pop("chips")
    # 제품 페이지 안에서는 자기 자신으로 보낼 수 없으니 문의로 연결합니다
    if to == "contact":
        T["cta"] = T["cta2"]; href = "contact.html"
    else:
        href = "product/ptz.html"
    T.pop("cta2")
    arrow = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4">'
             '<path d="M5 12h14M13 6l6 6-6 6"/></svg>')
    return '''<section class="ptz" id="ptzShow">
  <div class="ptz-sticky">
    <video class="ptz-vid" id="ptzVid" playsinline muted preload="auto" disablepictureinpicture
           poster="%(p)sassets/video/ptz-poster.jpg" data-caps="0.4,3.6,6.9,9.2" data-end="10.72">
      <source src="%(p)sassets/video/ptz.webm" type="video/webm">
      <source src="%(p)sassets/video/ptz.mp4" type="video/mp4">
    </video>
    <span class="ptz-vig"></span>
    <div class="ptz-stage">
      <div class="ptz-cap c1"><span class="kick">%(kicker)s</span><h2>%(h1)s</h2><p>%(p1)s</p></div>
      <div class="ptz-cap c2"><h2>%(h2)s</h2><p>%(p2)s</p></div>
      <div class="ptz-cap c3"><h2>%(h3)s</h2><p>%(p3)s</p></div>
      <div class="ptz-cap c4"><h2>%(h4)s</h2><p>%(p4)s</p>
        <div class="ptz-chips">%(chips)s</div>
        <a class="btn btn-primary ptz-cta" href="%(p)s%(ld)s%(href)s">%(cta)s%(arrow)s</a>
      </div>
    </div>
    <div class="ptz-prog" aria-hidden="true"><span id="ptzBar"></span></div>
    <button class="pv-replay" id="ptzReplay" type="button">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round">
        <path d="M3 12a9 9 0 1 0 3-6.7"/><path d="M3 4v5h5"/></svg>%(replay)s</button>
  </div>
</section>''' % dict(p=p, ld=LD(), href=href, arrow=arrow, chips=chip_html, **T)


def ptz_page(p, lang="ko"):
    """PTZ 제품 상세 — 몰입 섹션이 먼저, 그 아래 어두운 스펙 섹션."""
    T = dict(
      ko=dict(eyebrow="MAIN PRODUCT", h2="PTZ 카메라",
        lead="스타비스 센서를 사용하여 저조도 환경에서 강력한 2D/3D 노이즈 리덕션 영상 처리기술을 통해 "
             "고품질의 컬러 영상으로 모니터링이 가능합니다.",
        specs=[("광학·디지털 줌","뛰어난 오토포커싱 능력과 넓은 줌 범위를 제공합니다."),
               ("고신뢰 구동부","이중 타이밍 벨트 구조와 파워 스테핑 모터로 잦은 움직임에 따른 유격과 모터 탈조를 최소화합니다."),
               ("정밀 제어","고분해능 모터 구동 제어로 고정밀·저진동·저소음을 실현하고, 미세 제어를 위한 저속 구동이 가능합니다."),
               ("AI 기능 탑재","딥러닝 기반 AI 스마트 기능을 지원합니다.")],
        note="방진·방수 등급으로 설계되어 외부의 열악한 환경으로부터 카메라를 보호합니다.",
        mh="LINEUP", mt="모델 라인업",
        models=[("SL-P223ID5","2MP · 23배 광학줌"),("SL-P230ID5","2MP · 30배 광학줌"),
                ("SL-P510ID5","5MP · 10배 광학줌")],
        ch="CERTIFICATION", ct="검증된 품질", cl="인증서를 클릭하면 원본 크기로 확인할 수 있습니다.",
        certs=[("KC","방송통신기자재 적합등록"),("TTA","한국정보통신기술협회 시험인증"),
               ("IP","방진·방수 설계")],
        docs=[("kc-cam","KC","적합등록 · 회전형 카메라","SL-P223ID5"),
              ("tta-223","TTA","시험인증서","SL-P223ID5"),
              ("tta-230","TTA","시험인증서","SL-P230ID5"),
              ("tta-510","TTA","시험인증서","SL-P510ID5")]),
      en=dict(eyebrow="MAIN PRODUCT", h2="PTZ Camera",
        lead="A STARVIS sensor combined with powerful 2D/3D noise-reduction processing delivers "
             "high-quality colour monitoring even in low light.",
        specs=[("Optical &amp; digital zoom","Fast, accurate autofocus across a wide zoom range."),
               ("Reliable drive unit","A dual timing-belt structure and power stepping motors minimise backlash and motor step-out under constant movement."),
               ("Precise control","High-resolution motor drive control delivers precision with low vibration and low noise, including slow-speed operation for fine adjustment."),
               ("AI on board","Supports deep-learning based smart functions.")],
        note="Rated for dust and water ingress, protecting the camera in harsh outdoor environments.",
        mh="LINEUP", mt="Model line-up",
        models=[("SL-P223ID5","2MP · 23× optical zoom"),("SL-P230ID5","2MP · 30× optical zoom"),
                ("SL-P510ID5","5MP · 10× optical zoom")],
        ch="CERTIFICATION", ct="Verified quality", cl="Click a certificate to view it full size.",
        certs=[("KC","Broadcasting &amp; communication equipment conformity"),
               ("TTA","Telecommunications Technology Association test certification"),
               ("IP","Dust- and water-resistant design")],
        docs=[("kc-cam","KC","Conformity registration · PTZ camera","SL-P223ID5"),
              ("tta-223","TTA","Test certificate","SL-P223ID5"),
              ("tta-230","TTA","Test certificate","SL-P230ID5"),
              ("tta-510","TTA","Test certificate","SL-P510ID5")]),
    )[lang]

    sp = "".join(
        '<article class="dspec" data-reveal style="--td:%dms"><span class="n">%02d</span>'
        '<h3>%s</h3><p>%s</p></article>' % (i * 110, i + 1, a, b)
        for i, (a, b) in enumerate(T["specs"]))
    md = "".join(
        '<li class="dmodel" data-reveal style="--td:%dms"><b>%s</b><span>%s</span></li>' % (i * 100, a, b)
        for i, (a, b) in enumerate(T["models"]))
    cf = "".join(
        '<li class="dcert" data-reveal style="--td:%dms"><em>%s</em><span>%s</span></li>' % (i * 100, a, b)
        for i, (a, b) in enumerate(T["certs"]))
    dc = "".join(
        '<figure class="cert dcert-card" data-cat="all" data-reveal style="--td:%dms">'
        '<button class="cert-img" type="button" data-full="%sassets/cert/%s.jpg" data-cap="%s — %s">'
        '<img src="%sassets/cert/%s-t.jpg" alt="%s — %s" loading="lazy" width="600" height="800"></button>'
        '<figcaption><span class="dtag">%s</span><h3>%s</h3><p class="model">%s</p></figcaption>'
        '</figure>' % (i * 90, p, key, title, model, p, key, title, model, tag, title, model)
        for i, (key, tag, title, model) in enumerate(T["docs"]))

    T = dict(T)
    for k in ("specs", "models", "certs", "docs"):
        T.pop(k)
    return ptz_show(p, lang, "contact") + '''
<section class="section dark-sec"><div class="area">
  <div class="section-head is-dark" data-reveal><span class="eyebrow">%(eyebrow)s</span><h2>%(h2)s</h2></div>
  <div class="dsol">
    <figure class="dsol-fig" data-reveal data-speed="0.06">
      <span class="dsol-glow"></span>%(img)s
    </figure>
    <div class="dsol-body">
      <p class="dsol-lead" data-reveal>%(lead)s</p>
      <div class="dspec-grid">%(specs)s</div>
      <p class="dsol-note" data-reveal>%(note)s</p>
    </div>
  </div>
</div></section>

<section class="section dark-sec dark-sec2"><div class="area">
  <div class="section-head is-dark" data-reveal><span class="eyebrow">%(mh)s</span><h2>%(mt)s</h2></div>
  <ul class="dmodels">%(models)s</ul>
  <div class="section-head is-dark" data-reveal style="margin-top:clamp(60px,8vw,100px)">
    <span class="eyebrow">%(ch)s</span><h2>%(ct)s</h2><p class="lead">%(cl)s</p></div>
  <ul class="dcerts">%(certs)s</ul>
  <div class="dcert-gal" id="certGrid">%(docs)s</div>
</div></section>

<div class="lb" id="lb">
  <button class="lb-x" type="button" aria-label="close">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M18 6L6 18M6 6l12 12"/></svg></button>
  <button class="lb-nav lb-prev" type="button" aria-label="prev">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M15 18l-6-6 6-6"/></svg></button>
  <button class="lb-nav lb-next" type="button" aria-label="next">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M9 18l6-6-6-6"/></svg></button>
  <img alt="">
  <div class="lb-cap"></div>
</div>''' % dict(img=pimg("ptz", p), specs=sp, models=md, certs=cf, docs=dc, **T)


# ============================================================
# 주요제품 / 상황판(대시보드)
#   출처: 화성ITS 상황판 시나리오 기획 (2025)
# ============================================================
DASH_SC = {
 "ko": [
  ("integrated", "01", "통합운영", "INTEGRATED",
   "교통·안전·신호·버스정보 4개 시나리오의 주요 지표를 한 화면으로 모읍니다.",
   ["교통정보 수집시스템 (스마트교차로 · CCTV · VDS)",
    "교통정보 제공시스템 (VMS · 홈페이지 · 공공데이터 개방)",
    "스마트 안전시스템 (스마트횡단보도 · 스쿨존)",
    "디지털도로 · 신호 · 버스정보 시스템 운영현황"]),
  ("traffic", "02", "소통관리", "TRAFFIC FLOW",
   "실시간 교통량과 속도를 분석해 정체를 미리 읽어냅니다.",
   ["실시간 교통량 · 속도 통계 분석",
    "유출입 교통량의 시간대별 추이와 총계",
    "상습정체구간 첨두/비첨두 · 평일/주말 현황",
    "실시간 지체·정체 구간과 주요교차로 CCTV"]),
  ("safety", "03", "안전관리", "SAFETY",
   "도로 위 위험을 히트맵으로 모아 사고가 나기 전에 보이게 합니다.",
   ["돌발상황 히트맵 · 실시간 돌발현황(사고 · 공사)",
    "횡단보도 위험관리 (무단횡단 · 역주행 · 횡단대기)",
    "스마트 횡단보도 검지 (통행인구 · 차량접근 · 불법주차)",
    "디지털도로 위험물 수집 (포트홀 · 균열 · 노면표시 파손)"]),
  ("signal", "04", "신호운영", "SIGNAL",
   "교차로 서비스 수준을 등급으로 보고, 개선 효과를 숫자로 확인합니다.",
   ["주요교차로 실시간 신호운영 현황",
    "신호개선 효과지표 (대기행렬 · 통행속도)",
    "신호교차로 서비스 수준(LOS) 등급 표출",
    "서비스 수준 상위 4개 교차로 연동 표출"]),
  ("bus", "05", "버스정보", "BUS",
   "시내·마을·광역 버스의 실시간 위치와 안내기 운영상태를 함께 봅니다.",
   ["실시간 버스 이동정보 (시내 · 마을)",
    "실시간 버스 이동정보 (광역)",
    "버스정보안내기(BIT) 운영현황",
    "국토교통부 기준지표 충족 현황"]),
 ],
 "en": [
  ("integrated", "01", "Integrated view", "INTEGRATED",
   "Key indicators from all four scenarios &mdash; traffic, safety, signals and buses &mdash; on one screen.",
   ["Data collection: smart intersections, CCTV, VDS",
    "Data delivery: VMS, public website, open data",
    "Smart safety: smart crosswalks and school zones",
    "Digital road, signal and bus system status"]),
  ("traffic", "02", "Traffic flow", "TRAFFIC FLOW",
   "Live volume and speed analysis that lets operators see congestion before it forms.",
   ["Real-time volume and speed statistics",
    "Inbound / outbound volume by time of day",
    "Recurring congestion by peak / off-peak and weekday / weekend",
    "Live delay sections with major-intersection CCTV"]),
  ("safety", "03", "Safety", "SAFETY",
   "Road hazards gathered into a heat map, so risk is visible before an accident happens.",
   ["Incident heat map and live incident status (crashes, works)",
    "Crosswalk risk: jaywalking, wrong-way, waiting pedestrians",
    "Smart crosswalk detection: footfall, approaching vehicles, illegal parking",
    "Digital-road hazards: potholes, cracks, damaged markings"]),
  ("signal", "04", "Signal operation", "SIGNAL",
   "Intersection level of service at a glance, with the effect of every change measured.",
   ["Live signal operation at major intersections",
    "Improvement metrics: queue length and travel speed",
    "Level of service (LOS) grading per intersection",
    "Top four intersections linked to the LOS ranking"]),
  ("bus", "05", "Bus information", "BUS",
   "Live positions for city, community and intercity buses alongside terminal health.",
   ["Live bus positions (city and community routes)",
    "Live bus positions (intercity routes)",
    "Bus Information Terminal (BIT) operating status",
    "Compliance with Ministry of Land standard indicators"]),
 ],
}

DASH_T = {
 "ko": dict(
   eyebrow="MAIN PRODUCT", h2="상황판 (대시보드)",
   hero_kick="ITS CONTROL WALL",
   hero_h="도시의 교통을<br><em>한 화면</em>에",
   hero_p="흩어져 있던 교통·안전·신호·버스 데이터를 하나의 상황판으로 모읍니다. "
          "관제 요원이 화면을 옮겨 다니지 않아도, 지금 도시에서 무슨 일이 벌어지는지 보입니다.",
   kw2="도시 전체를", kwl2="<em>한 화면</em>에서 봅니다",
   zoom=[("시스템 운영현황", "스마트교차로 · CCTV · VDS부터 전광판 · 버스까지, 운영 중인 모든 장비를 종류별로 집계합니다."),
         ("GIS 통합지도", "지자체 전역의 교통시설물을 지도 위에. 옆의 버튼으로 시나리오를 즉시 전환합니다."),
         ("미니 대시보드", "실시간 신호개방, 협력 데이터 연계, 홈페이지 운영 상태를 상시 표출합니다."),
         ("교통정보 제공현황", "도로안내 전광판이 지금 무엇을 표출하고 있는지, 도로별 소통 상태와 함께 확인합니다.")],
   zfull="한 대의 상황판, 다섯 개의 화면",
   sh="SCENARIOS", st="6가지 시나리오", sl="목적에 맞는 시나리오를 골라 상황판을 전환합니다. 스크롤해 보세요.",
   lh="COMMON LAYOUT", lt="모든 화면의 공통 구성",
   layout=[("GIS 기반 지도", "지자체 전역의 교통시설물을 지도 위에 표현하고, 버튼을 누르면 해당 지역 중심으로 이동합니다."),
           ("미니 대시보드", "화면 오른쪽에 요약 지표를 상시 표출합니다. 시나리오에 따라 강조 항목이 바뀝니다."),
           ("시나리오 이동", "한 번의 클릭으로 통합운영 · 소통 · 안전 · 신호 · 버스정보 화면을 오갑니다.")],
   fh="ONE MORE", ft="장애관리 시나리오",
   fp="운영·유지보수 관점에서 시스템별 장애를 한눈에 관제합니다. "
      "스마트교차로 · CCTV · VDS · VMS 등 장비별 장애현황을 GIS 위에 표시해 위치까지 바로 파악할 수 있습니다.",
   fitems=["시스템별 장애현황 집계", "GIS 기반 장애 위치 파악", "장비 유형별 필터", "실시간 상태 갱신"],
   note="화면 이미지는 화성특례시 ITS 상황판 구축 사례입니다.",
   cta="상황판 도입 문의"),
 "en": dict(
   eyebrow="MAIN PRODUCT", h2="Control Wall Dashboard",
   hero_kick="ITS CONTROL WALL",
   hero_h="A whole city&rsquo;s traffic<br>on <em>one screen</em>",
   hero_p="Traffic, safety, signal and bus data that used to live in separate systems, gathered into a "
          "single control wall. Operators no longer switch between screens to find out what the city is doing.",
   kw2="A whole city,", kwl2="on <em>one screen</em>",
   zoom=[("System status", "Every device in service counted by type &mdash; smart intersections, CCTV, VDS, message signs and buses."),
         ("GIS base map", "All traffic infrastructure drawn on the city map, with scenario buttons alongside it."),
         ("Mini dashboard", "Live signal opening, partner data links and website status, always on screen."),
         ("Information delivery", "What each message sign is showing right now, next to the flow state of every road.")],
   zfull="One wall, five screens",
   sh="SCENARIOS", st="Six scenarios", sl="Switch the wall to the scenario that fits the task. Scroll to explore.",
   lh="COMMON LAYOUT", lt="Shared across every screen",
   layout=[("GIS base map", "Every piece of traffic infrastructure in the city, drawn on the map. One click centres the view on a district."),
           ("Mini dashboard", "A summary panel always on the right. The highlighted figures change with the scenario."),
           ("Scenario switch", "Move between integrated, traffic, safety, signal and bus views in a single click.")],
   fh="ONE MORE", ft="Fault management scenario",
   fp="A sixth view built for operations and maintenance. Faults across smart intersections, CCTV, VDS and VMS "
      "are aggregated by system and plotted on the GIS map, so the location is immediately clear.",
   fitems=["Fault counts by system", "GIS-based fault location", "Filter by equipment type", "Live status refresh"],
   note="Screens shown are from the Hwaseong City ITS control wall project.",
   cta="Talk to us about a control wall"),
}


def dash_page(p, lang="ko"):
    """상황판(대시보드) 제품 페이지 — 스크롤로 시나리오가 전환되는 몰입 구성."""
    T  = dict(DASH_T[lang])
    SC = DASH_SC[lang]
    arrow = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4">'
             '<path d="M5 12h14M13 6l6 6-6 6"/></svg>')

    shots, caps, dots = "", "", ""
    for i, (key, no, name, en, desc, items) in enumerate(SC):
        shots += ('<div class="ds-shot%s" data-i="%d">'
                  '<picture><source srcset="%sassets/img/dash/%s.webp" type="image/webp">'
                  '<img src="%sassets/img/dash/%s.jpg" alt="%s 상황판 화면" loading="lazy"></picture>'
                  '</div>' % (" on" if i == 0 else "", i, p, key, p, key, name))
        li = "".join('<li>%s</li>' % t for t in items)
        caps += ('<div class="ds-cap%s" data-i="%d"><span class="ds-no">%s</span>'
                 '<span class="ds-en">%s</span><h3>%s</h3><p>%s</p><ul>%s</ul></div>'
                 % (" on" if i == 0 else "", i, no, en, name, desc, li))
        dots += ('<button class="ds-dot%s" type="button" data-go="%d">'
                 '<i></i><span>%s</span></button>' % (" on" if i == 0 else "", i, name))

    lay = "".join(
        '<article class="dlay" data-reveal style="--td:%dms"><span class="n">%02d</span>'
        '<h3>%s</h3><p>%s</p></article>' % (i * 120, i + 1, a, b)
        for i, (a, b) in enumerate(T["layout"]))
    fit = "".join('<li class="dfi" data-reveal style="--td:%dms">%s</li>' % (i * 90, t)
                  for i, t in enumerate(T["fitems"]))
    for k in ("layout", "fitems"):
        T.pop(k)

    zcaps = "".join(
        '<div class="dz-cap" data-i="%d"><span class="dz-n">%02d</span><h3>%s</h3><p>%s</p></div>'
        % (i + 1, i + 1, a, b) for i, (a, b) in enumerate(T["zoom"]))
    T = dict(T); T.pop("zoom")

    return '''<section class="dz" id="dashZoom">
  <div class="dz-sticky">
    <!-- 1) 거대한 키워드 -->
    <div class="dz-kw" id="dzKw">
      <span class="dz-kick">%(hero_kick)s</span>
      <h2><span class="l1">%(kw2)s</span><span class="l2">%(kwl2)s</span></h2>
      <p>%(hero_p)s</p>
    </div>
    <!-- 2) 커지는 상황판 -->
    <div class="dz-stage">
      <div class="dz-wall" id="dzWall">
        <picture><source srcset="%(p)sassets/img/dash/integrated-hi.webp" type="image/webp">
        <img src="%(p)sassets/img/dash/integrated-hi.jpg" alt="%(h2)s" id="dzImg"></picture>
        <span class="dz-focus" id="dzFocus"></span>
      </div>
    </div>
    <!-- 3) 패널별 설명 -->
    <div class="dz-caps" id="dzCaps">
      <div class="dz-cap dz-full" data-i="0"><h3>%(zfull)s</h3></div>
      %(zcaps)s
    </div>
    <div class="dz-prog"><span id="dzBar"></span></div>
  </div>
</section>

''' % dict(p=p, zcaps=zcaps, **T) + '''<section class="ds" id="dashShow">
  <div class="ds-sticky">
    <div class="ds-inner">
      <div class="ds-head">
        <span class="eyebrow">%(sh)s</span>
        <h2>%(st)s</h2>
        <p>%(sl)s</p>
      </div>
      <div class="ds-stage">
        <div class="ds-frame" id="dsFrame">%(shots)s<span class="ds-scan"></span></div>
        <div class="ds-caps">%(caps)s</div>
      </div>
      <div class="ds-rail">%(dots)s</div>
      <div class="ds-prog"><span id="dsBar"></span></div>
    </div>
  </div>
</section>

<section class="section dark-sec"><div class="area">
  <div class="section-head is-dark" data-reveal><span class="eyebrow">%(lh)s</span><h2>%(lt)s</h2></div>
  <div class="dlay-grid">%(layout)s</div>
</div></section>

<section class="section dark-sec dark-sec2"><div class="area">
  <div class="dfault">
    <div class="dfault-txt">
      <span class="eyebrow" data-reveal>%(fh)s</span>
      <h2 data-reveal data-d="80">%(ft)s</h2>
      <p data-reveal data-d="160">%(fp)s</p>
      <ul class="dfault-list">%(fitems)s</ul>
      <a class="btn btn-primary" href="%(p)s%(ld)scontact.html" data-reveal data-d="300"
         style="margin-top:30px">%(cta)s%(arrow)s</a>
    </div>
    <div class="dfault-viz" data-reveal data-d="140" data-speed="0.08">
      <span class="dfv-ring r1"></span><span class="dfv-ring r2"></span><span class="dfv-ring r3"></span>
      <span class="dfv-pin p1"></span><span class="dfv-pin p2"></span><span class="dfv-pin p3"></span>
      <span class="dfv-pin p4"></span><span class="dfv-pin p5"></span>
      <span class="dfv-core"></span>
    </div>
  </div>
  <p class="dsol-note" data-reveal style="margin-top:clamp(46px,6vw,72px)">%(note)s</p>
</div></section>''' % dict(p=p, ld=LD(), arrow=arrow, shots=shots, caps=caps, dots=dots,
                           layout=lay, fitems=fit, **T)


# ============================================================
# 주요제품 / 초정밀 모듈(GNSS)
# ============================================================
GNSS_DOTS = [
  (80.70,76.62,'l',0.00), (24.74,91.67,'l',0.38), (69.82,74.91,'l',0.75), (75.68,64.44,'l',0.13),
  (96.20,65.93,'l',0.50), (60.29,86.71,'l',0.88), (29.61,73.15,'l',0.25), (52.21,84.86,'l',0.63),
  (71.88,60.83,'l',0.00), (45.65,54.31,'l',0.38), (35.18,64.31,'l',0.75), (3.98,48.61,'l',0.13),
  (63.80,53.43,'l',0.50), (95.68,85.97,'l',0.88), (98.75,15.97,'l',0.25), (45.70,18.94,'l',0.63),
  (31.33,96.06,'l',0.00), (50.34,60.42,'l',0.38), (65.89,74.17,'l',0.75), (92.37,38.38,'l',0.13),
  (8.46,19.17,'m',0.50), (65.34,46.85,'m',0.88), (68.88,79.21,'m',0.25), (76.20,19.72,'m',0.63),
  (31.82,48.06,'m',0.00), (56.93,34.21,'m',0.38), (27.60,36.99,'m',0.75), (67.63,11.48,'m',0.13),
  (55.94,21.62,'m',0.50), (80.49,30.65,'m',0.88), (81.95,45.74,'m',0.25), (87.63,4.31,'m',0.63),
  (48.96,21.30,'m',0.00), (17.55,38.10,'m',0.38), (52.16,66.85,'m',0.75), (45.91,45.37,'m',0.13),
  (77.45,62.45,'m',0.50), (81.41,57.13,'m',0.88), (63.88,82.50,'m',0.25), (57.53,86.94,'m',0.63),
  (62.27,27.04,'m',0.00), (48.23,88.70,'m',0.38), (87.45,52.04,'m',0.75), (35.05,55.74,'m',0.13),
  (72.14,55.74,'m',0.50), (21.59,59.91,'m',0.88), (47.19,57.27,'m',0.25), (40.83,58.70,'m',0.63),
  (64.48,90.56,'m',0.00), (80.99,96.34,'m',0.38), (52.45,81.30,'m',0.75), (60.26,14.49,'m',0.13),
  (16.48,20.05,'m',0.50), (9.32,48.66,'s',0.88), (68.31,86.30,'s',0.25), (38.36,56.44,'s',0.63),
  (54.56,12.18,'s',0.00), (35.86,31.62,'s',0.38), (77.21,37.96,'s',0.75), (31.43,6.85,'s',0.13),
  (67.21,28.66,'s',0.50), (81.43,39.68,'s',0.88), (59.40,95.19,'s',0.25), (68.62,44.40,'s',0.63),
  (34.24,70.97,'s',0.01), (30.18,38.10,'s',0.38), (16.80,55.60,'s',0.76), (64.90,16.06,'s',0.13),
  (55.47,86.99,'s',0.51), (48.18,60.74,'s',0.88), (52.60,89.95,'s',0.26), (34.04,51.57,'s',0.63),
  (70.83,70.42,'s',0.01), (61.77,90.60,'s',0.38), (39.95,31.16,'s',0.76), (36.51,52.27,'s',0.13),
  (40.94,53.52,'s',0.51), (69.01,36.57,'s',0.88), (38.31,81.30,'s',0.26), (48.23,83.75,'s',0.63),
  (42.89,69.54,'s',0.01), (49.95,92.04,'s',0.38), (22.97,24.72,'s',0.76), (71.54,46.39,'s',0.13),
  (37.81,76.20,'s',0.51), (68.75,92.18,'s',0.88), (28.59,11.11,'s',0.26), (33.02,22.50,'s',0.63),
  (38.78,39.44,'s',0.01), (70.68,82.96,'s',0.38), (62.29,18.43,'s',0.76), (42.73,23.43,'s',0.13),
  (40.83,43.61,'s',0.51), (44.58,58.61,'s',0.88), (61.93,99.31,'s',0.26), (60.49,10.56,'s',0.63),
]


GNSS_T = {
 "ko": dict(
   kick="HIGH-PRECISION BUS POSITIONING",
   caps=[("위치 데이터의 기준이<br><em>10m</em>에서 <em>2cm</em>로",
          "시내버스 운전석 하단의 초정밀 GNSS 모듈. RTK 보정으로 좌표 오차의 기준 자체를 바꿉니다."),
         ("같은 버스,<br><em>다른 정확도</em>",
          "위치 데이터가 정확해질수록 도착 예정시간도 정확해집니다. "
          "버스정보의 품질은 좌표에서 시작합니다."),
         ("일반 GPS <em>약 10m</em><br>초정밀 GNSS <em>약 2cm</em>",
          "같은 버스에서 수집해도 좌표의 정밀도가 다릅니다. "
          "더 정확한 버스정보를 제공하기 위해 기준을 끌어올렸습니다."),
         ("전국 어디서나<br><em>같은 기준</em>",
          "기준국(BASE)이 만든 보정정보를 차량 단말(OBE)이 실시간으로 받습니다. "
          "지역이 달라져도 버스정보의 기준은 같습니다.")],
   mh="LIVE NETWORK", mt="전국이 하나의 망으로",
   ml="기준국과 차량 단말이 주고받는 보정 신호. 점 하나가 하나의 측위 지점입니다.",
   legend=[("기준국 (BASE)","고정 좌표를 기준으로 보정정보를 생성"),
           ("차량 단말 (OBE)","버스에 탑재되어 보정정보를 수신·적용"),
           ("보정 링크","LTE 망을 통한 실시간 보정정보 전송")],
   sh="SPECIFICATION", st="제품 사양",
   note="영상은 초정밀 버스 측위의 동작 개념을 표현한 것입니다. 실제 정확도는 기준국 거리와 수신 환경에 따라 달라질 수 있습니다.",
   replay="다시 보기", cta="도입 문의하기"),
 "en": dict(
   kick="HIGH-PRECISION BUS POSITIONING",
   caps=[("Position data moves from<br><em>10&nbsp;m</em> to <em>2&nbsp;cm</em>",
          "A high-precision GNSS module under the driver's seat. RTK correction changes the baseline "
          "of the coordinate itself."),
         ("Same bus,<br><em>different accuracy</em>",
          "The more accurate the position data, the more accurate the arrival estimate. "
          "The quality of bus information starts at the coordinate."),
         ("Ordinary GPS <em>~10&nbsp;m</em><br>High-precision <em>~2&nbsp;cm</em>",
          "Collected from the same bus, the precision of the coordinate is not the same. "
          "We raised the baseline in order to deliver more accurate bus information."),
         ("The same baseline<br><em>everywhere</em>",
          "On-board units receive correction data from base stations in real time, so bus information "
          "is held to the same standard in every region.")],
   mh="LIVE NETWORK", mt="One network, nationwide",
   ml="Correction signals exchanged between base stations and vehicle units. Each dot is one positioning point.",
   legend=[("Base station","Generates correction data from a fixed known coordinate"),
           ("On-board unit (OBE)","Mounted on the bus, receives and applies the correction"),
           ("Correction link","Real-time correction delivered over the LTE network")],
   sh="SPECIFICATION", st="Specification",
   note="The film illustrates how high-precision bus positioning works. Achieved accuracy varies with baseline distance to the base station and reception conditions.",
   replay="Replay", cta="Talk to us"),
}


ECS_T = {
 "ko": dict(
   kick="EV CHARGING STATION DISPLAY",
   replay="다시 보기",
   caps=[("배터리는 줄어드는데<br><em>자리는 알 수 없다</em>",
          "충전소에 다다를 때까지, 운전자는 몇 대가 비어 있는지 알 방법이 없습니다."),
         ("진입하는 순간<br><em>답이 보입니다</em>",
          "캐노피 위 전광판이 충전기 한 대 한 대의 상태를 실시간으로 표출합니다."),
         ("고휘도 LED,<br><em>멀리서도</em> 선명하게",
          "주광 아래에서도 또렷한 화면. 차를 세우기 전에 판단이 끝납니다."),
         ("충전 가능 여부와 잔량을<br><em>한눈에</em>",
          "충전 중·충전 가능·충전 불가와 잔량, 남은 시간까지 한 줄로 정리해 보여 줍니다.")],
   chips=["고휘도 LED 소자","실시간 상태 표출","충전 잔량·잔여시간","옥외 시인성 확보"],
   cta="도입 문의하기"),
 "en": dict(
   kick="EV CHARGING STATION DISPLAY",
   replay="Replay",
   caps=[("The battery drops,<br><em>the bays stay unknown</em>",
          "Until you arrive, there is no way to know how many chargers are free."),
         ("The moment you pull in,<br><em>you have the answer</em>",
          "A display on the canopy reports the live status of every charger."),
         ("High-brightness LED,<br><em>legible from a distance</em>",
          "Clear in full daylight. The decision is made before you stop the car."),
         ("Availability and charge level<br><em>at a glance</em>",
          "Charging, available or out of service — plus charge level and time remaining, in one line.")],
   chips=["High-brightness LED","Live status output","Charge level & time","Outdoor legibility"],
   cta="Talk to us"),
}


def ecs_show(p, lang="ko"):
    """전기차 충전소 전광판 도입부 — 운전석 1인칭 영상이 자동 재생됩니다."""
    T = ECS_T[lang]
    caps = "".join(
        '<div class="film-cap c%d">%s<h2>%s</h2><p>%s</p>%s</div>' % (
            i + 1,
            ('<span class="kick">%s</span>' % T["kick"]) if i == 0 else "",
            h, d,
            ('<div class="film-chips">%s</div>'
             '<a class="btn btn-primary film-cta" href="%s%scontact.html">%s%s</a>'
             % ("".join('<span>%s</span>' % c for c in T["chips"]),
                p, LD(), T["cta"],
                '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4">'
                '<path d="M5 12h14M13 6l6 6-6 6"/></svg>')) if i == 3 else "")
        for i, (h, d) in enumerate(T["caps"]))
    return '''<section class="film" id="ecsShow">
  <div class="film-sticky">
    <video class="film-vid" id="ecsVid" playsinline muted preload="auto" disablepictureinpicture
           poster="%(p)sassets/video/ecs-poster.jpg" data-caps="0.4,4.0,6.6,9.2" data-end="12.04"
           aria-label="%(kick)s">
      <source src="%(p)sassets/video/ecs.webm" type="video/webm">
      <source src="%(p)sassets/video/ecs.mp4" type="video/mp4">
    </video>
    <span class="film-vig"></span>
    <div class="film-stage">%(caps)s</div>
    <div class="film-prog" aria-hidden="true"><span id="ecsBar"></span></div>
    <button class="pv-replay" id="ecsReplay" type="button">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round">
        <path d="M3 12a9 9 0 1 0 3-6.7"/><path d="M3 4v5h5"/></svg>%(replay)s</button>
  </div>
</section>''' % dict(p=p, caps=caps, kick=T["kick"], replay=T["replay"])


def gnss_show(p, lang="ko"):
    """GNSS 도입부 — 스크롤에 맞춰 영상 프레임이 흐르고 문구가 바뀝니다."""
    T = GNSS_T[lang]
    caps = "".join(
        '<div class="gn-cap%s"><h2>%s</h2><p>%s</p></div>' % (" on" if i == 0 else "", h, d)
        for i, (h, d) in enumerate(T["caps"]))
    dots = "".join(
        '<span class="gd gd-%s" style="left:%.2f%%;top:%.2f%%;--dl:%.2fs"></span>' % (t, x, y, d * 3.4)
        for x, y, t, d in GNSS_DOTS)
    return '''<section class="gn" id="gnssShow">
  <div class="gn-sticky">
    <video class="gn-cv" id="gnVid" playsinline muted preload="auto" disablepictureinpicture
           poster="%(p)sassets/video/gnss-poster.jpg" data-caps="0.4,3.2,6.2,9.2" data-end="12.04"
           data-dots="11.0" aria-label="%(kick)s">
      <source src="%(p)sassets/video/gnss.webm" type="video/webm">
      <source src="%(p)sassets/video/gnss.mp4" type="video/mp4">
    </video>
    <div class="gn-dots gn-live" id="gnDots">%(dots)s</div>
    <span class="gn-vig"></span>
    <div class="gn-stage">
      <span class="gn-kick">%(kick)s</span>
      <div class="gn-caps">%(caps)s</div>
    </div>
    <div class="gn-prog" aria-hidden="true"><span id="gnBar"></span></div>
    <button class="pv-replay" id="gnReplay" type="button">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round">
        <path d="M3 12a9 9 0 1 0 3-6.7"/><path d="M3 4v5h5"/></svg>%(replay)s</button>
  </div>
</section>''' % dict(p=p, caps=caps, dots=dots, kick=T["kick"], replay=T["replay"])


def gnss_map(p, lang="ko"):
    """전국 측위망 설명 — 지도는 위 몰입 섹션의 마지막 장면이 그대로 이어집니다."""
    T = GNSS_T[lang]
    lg = "".join(
        '<li class="gl%d" data-reveal style="--td:%dms"><i></i><b>%s</b><span>%s</span></li>'
        % (i + 1, i * 110, a, b) for i, (a, b) in enumerate(T["legend"]))
    return '''<section class="section dark-sec gn-mapsec"><div class="area">
  <div class="section-head is-dark" data-reveal><span class="eyebrow">%(mh)s</span>
    <h2>%(mt)s</h2><p class="lead">%(ml)s</p></div>
  <ul class="gn-legend">%(legend)s</ul>
  <p class="dsol-note" data-reveal style="margin-top:clamp(34px,4vw,52px)">%(note)s</p>
</div></section>''' % dict(legend=lg, mh=T["mh"], mt=T["mt"], ml=T["ml"], note=T["note"])


def chatbot(p):
    """우측 하단 고정 상담 위젯 — 스크롤과 무관하게 항상 따라옵니다."""
    return '''<!-- 상담 위젯 -->
<div class="cw" id="cw" data-base="%(p)s%(ld)s" data-tel="%(tel)s" data-mail="%(mail)s" data-lang="%(lang)s">
  <button class="cw-fab" id="cwFab" type="button" aria-expanded="false" aria-controls="cwPanel"
          aria-label="%(open)s">
    <svg class="cw-i-chat" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9"
         stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
      <path d="M21 11.5a8.4 8.4 0 0 1-9 8.4 9.5 9.5 0 0 1-2.9-.4L3 21l1.6-4.6A8.3 8.3 0 0 1 3.6 11.5 8.4 8.4 0 0 1 12 3.1a8.4 8.4 0 0 1 9 8.4z"/>
    </svg>
    <svg class="cw-i-x" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3"
         stroke-linecap="round" aria-hidden="true"><path d="M18 6L6 18M6 6l12 12"/></svg>
    <span class="cw-ping" aria-hidden="true"></span>
  </button>

  <div class="cw-tip" id="cwTip" role="note">%(tip)s<i></i></div>

  <section class="cw-panel" id="cwPanel" role="dialog" aria-modal="false" aria-label="%(title)s" hidden>
    <header class="cw-head">
      <span class="cw-ava" aria-hidden="true">
        <img src="%(p)sassets/img/logo-v-white.png" alt="">
      </span>
      <div class="cw-who"><b>%(title)s</b><span><i></i>%(reply)s</span></div>
      <button class="cw-min" id="cwMin" type="button" aria-label="%(close)s">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round"><path d="M6 12h12"/></svg>
      </button>
    </header>

    <div class="cw-log" id="cwLog" role="log" aria-live="polite"></div>

    <div class="cw-foot">
      <div class="cw-chips" id="cwChips"></div>
      <div class="cw-quick">
        <a class="cw-q" href="tel:%(telraw)s"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></svg>%(call)s</a>
        <a class="cw-q" href="mailto:%(mail)s"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16v16H4z"/><path d="M4 6l8 6 8-6"/></svg>%(mailtxt)s</a>
        <a class="cw-q" href="%(p)s%(ld)scontact.html"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/><path d="M14 3v6h6"/></svg>%(form)s</a>
      </div>
    </div>
  </section>
</div>''' % dict(p=p, ld=LD(), lang=LANG, tel=TEL, telraw=TEL.replace("-", ""), mail=MAIL,
            open=U('cw_open'), tip=U('cw_tip'), title=U('cw_title'), reply=U('cw_reply'),
            close=U('cw_close'), call=U('cw_call'), mailtxt=U('cw_mail'), form=U('cw_form'))


def page(url, title, desc, cur, body, *, home=False, extra_head=""):
    """한 페이지 완성"""
    p = rel(url)
    out = LD() + url
    globe = ""   # 히어로가 영상으로 바뀌어 three.js 불필요
    head_cls = "" if home else " class=\"has-sub\""
    top = ""
    if not home:
        top = subvis(title, cur, url, p) + "\n" + subnav(cur, url, p)
    html = f'''<!DOCTYPE html>
<html lang="{U('htmllang')}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{(CO() + ' | ' + title) if home else (title + ' | ' + CO())}</title>
<meta name="description" content="{desc}">
<meta http-equiv="Cache-Control" content="no-cache">
<link rel="icon" href="{p}assets/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="{p}assets/favicon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="{p}assets/favicon.png">
<link rel="apple-touch-icon" href="{p}assets/apple-touch-icon.png">
<meta name="theme-color" content="#1F2A5A">
<script>
/* 배포 감시 — 서버가 캐시 헤더를 안 보내는 환경(python -m http.server 등)에서
   브라우저가 옛 HTML 을 계속 쓰는 일을 막습니다. 빌드 번호가 다르면 한 번만 새로고침. */
window.__BUILD__="{V}";(function(){{try{{
 fetch("{p}version.json?t="+Date.now(),{{cache:"no-store"}}).then(function(r){{return r.json();}})
  .then(function(j){{
    if(!j||!j.build||j.build===window.__BUILD__) return;
    /* 빌드 번호별로 한 번씩만 새로고침 — 예전엔 세션당 한 번뿐이라
       두 번째 수정부터는 옛 화면이 그대로 남았습니다 */
    var k="sl-rl:"+j.build;
    if(sessionStorage.getItem(k)) return;
    sessionStorage.setItem(k,"1");
    location.reload();
  }}).catch(function(){{}});
 }}catch(e){{}}}})();
</script>
<link rel="alternate" hreflang="ko" href="{p}{url}">
<link rel="alternate" hreflang="en" href="{p}en/{url}">
<link rel="stylesheet" href="{p}vendor/swiper-bundle.min.css">
<link rel="stylesheet" href="{p}assets/style.css?v={V}">
<noscript><style>[data-reveal]{{opacity:1!important;translate:none!important}}</style></noscript>
{extra_head}</head>
<body{head_cls}>

{header(cur, p, url)}

<main id="top">
{top}
{body}
{cta(p)}
</main>

{footer(p)}

{chatbot(p)}

<script src="{p}vendor/swiper-bundle.min.js"></script>
<script src="{p}vendor/gsap.min.js"></script>
<script src="{p}vendor/ScrollTrigger.min.js"></script>
<script src="{p}assets/app.js?v={V}"></script>{globe}
</body>
</html>
'''
    full = os.path.join(ROOT, out)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w", encoding="utf-8").write(html)
    return out


# ============================================================
# 본문 조각 헬퍼
# ============================================================
def sec(inner, bg=False, wide=False):
    style = ' style="background:var(--c-bg-soft)"' if bg else ''
    area = "area-box" if wide else "area"
    return '<section class="section"%s>\n<div class="%s">\n%s\n</div></section>' % (style, area, inner)


def head(eyebrow, h2, lead=""):
    l = f'<p class="lead">{lead}</p>' if lead else ""
    return f'<div class="section-head" data-reveal><span class="eyebrow">{eyebrow}</span><h2>{h2}</h2>{l}</div>'


def needs(items):
    d = "".join(f'<div><b>POINT {i+1:02d}</b><p>{t}</p></div>' for i, t in enumerate(items))
    return f'<div class="need" data-reveal>{d}</div>'


ICONS = {
 "vms": '<svg viewBox="0 0 100 100" fill="none" stroke="#5B78E0" stroke-width="2"><rect x="12" y="22" width="76" height="40" rx="3"/><path d="M24 36h30M24 46h44M50 62v14M36 76h28"/></svg>',
 "bit": '<svg viewBox="0 0 100 100" fill="none" stroke="#5B78E0" stroke-width="2"><rect x="14" y="20" width="72" height="34" rx="3"/><path d="M26 32h28M26 42h20M50 54v10M30 64h40"/><circle cx="70" cy="37" r="5"/></svg>',
 "ecs": '<svg viewBox="0 0 100 100" fill="none" stroke="#5B78E0" stroke-width="2"><rect x="20" y="16" width="46" height="52" rx="4"/><path d="M32 34h22M32 46h14M66 30h10v26a6 6 0 01-6 6"/><path d="M46 68v12M34 80h24"/></svg>',
 "gnss": '<svg viewBox="0 0 100 100" fill="none" stroke="#5B78E0" stroke-width="2"><circle cx="50" cy="50" r="7" fill="#5B78E0"/><ellipse cx="50" cy="50" rx="38" ry="15"/><ellipse cx="50" cy="50" rx="38" ry="15" transform="rotate(60 50 50)"/><ellipse cx="50" cy="50" rx="38" ry="15" transform="rotate(120 50 50)"/></svg>',
 "ptz": '<svg viewBox="0 0 100 100" fill="none" stroke="#5B78E0" stroke-width="2"><rect x="18" y="30" width="46" height="28" rx="4"/><path d="M64 38l16-8v28l-16-8z"/><circle cx="34" cy="44" r="7"/><path d="M40 58v14M28 72h24"/></svg>',
 "cam": '<svg viewBox="0 0 100 100" fill="none" stroke="#5B78E0" stroke-width="2"><rect x="16" y="28" width="52" height="32" rx="4"/><circle cx="42" cy="44" r="10"/><path d="M68 40l14-8v24l-14-8z"/></svg>',
 "sw":  '<svg viewBox="0 0 100 100" fill="none" stroke="#5B78E0" stroke-width="2"><rect x="14" y="20" width="72" height="48" rx="4"/><path d="M14 34h72M30 78h40"/><circle cx="26" cy="27" r="2.5" fill="#5B78E0"/></svg>',
 "ctrl":'<svg viewBox="0 0 100 100" fill="none" stroke="#5B78E0" stroke-width="2"><circle cx="50" cy="50" r="26"/><path d="M50 24v12M50 64v12M24 50h12M64 50h12"/><circle cx="50" cy="50" r="7" fill="#5B78E0"/></svg>',
 "sign":'<svg viewBox="0 0 100 100" fill="none" stroke="#5B78E0" stroke-width="2"><path d="M50 14l30 14v20c0 18-13 28-30 34-17-6-30-16-30-34V28z"/><path d="M38 48l8 8 16-16"/></svg>',
}


_ARROW = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4">'
          '<path d="M5 12h14M13 6l6 6-6 6"/></svg>')

# 솔루션 카드에 실사를 쓸 수 있는 이미지 목록.
#   key: (확장자 뺀 경로, 확장자, object-fit, 국문 alt, 영문 alt)
SOL_PHOTO = {
  "p_vms":  ("assets/img/prod/vms", "png", "contain",
             "도형식 도로교통 전광판(VMS)", "Graphic variable message sign (VMS)"),
  "p_cam":  ("assets/img/prod/ptz", "png", "contain",
             "PTZ 회전형 지능형 카메라", "PTZ intelligent camera"),
  "p_dash": ("assets/img/dash/traffic", "jpg", "cover",
             "교통 관제 상황판 화면", "Traffic control wall dashboard"),
  "p_evsled": ("assets/img/prod/evsled", "jpg", "cover",
             "교차로에 설치된 긴급차량 출동안내 전광판 — '긴급차량 출동중' 표출",
             "Emergency dispatch advisory display in service at an intersection"),
  "p_ctrl": ("assets/img/prod/ctrl", "png", "tall",
             "교통관리시스템 현장 제어기 함체", "Roadside traffic-management controller cabinet"),
  "p_ssz2": ("assets/img/prod/ssz2", "png", "cover",
             "어린이보호구역 스마트 스쿨존 전광판", "School-zone LED display"),
  "p_bit":  ("assets/img/prod/bit", "png", "contain",
             "버스정보안내 전광판(BIT)", "Bus information terminal (BIT)"),
  "p_gnss": ("assets/img/prod/gnss", "png", "contain",
             "초정밀 GNSS 모듈", "High-precision GNSS module"),
  "p_bus":  ("assets/img/dash/bus", "jpg", "cover",
             "버스정보 운영 상황판 화면", "Bus information operations dashboard", "14% center"),
  # 같은 상황판이지만 오른쪽 지표 패널(정확도·운영현황) 쪽을 잘라 씁니다
  "p_proc": ("assets/img/dash/bus", "jpg", "cover",
             "도착예정시간 정확도 · 운영지표 산출 화면",
             "Arrival-accuracy and operating-indicator panels", "73% center"),
}


def solphoto(key, p=""):
    """SOL_PHOTO 항목: (경로, 확장자, fit, 국문 alt, 영문 alt[, object-position])
    상황판처럼 아주 가로로 긴 화면은 가운데만 잘리면 다 비슷해 보여서,
    카드마다 보여줄 위치를 따로 지정할 수 있게 했습니다."""
    it = SOL_PHOTO[key]
    base, ext, fit, ko, en = it[:5]
    pos = it[5] if len(it) > 5 else None
    alt = ko if LANG == "ko" else en
    st = ' style="object-position:%s"' % pos if pos else ""
    return ('<picture><source srcset="%s%s.webp?v=%s" type="image/webp">'
            '<img src="%s%s.%s?v=%s" alt="%s" loading="lazy" class="fit-%s"%s></picture>'
            % (p, base, V, p, base, ext, V, alt, fit, st))


def solgrid(items, p=""):
    """솔루션 카드.
    · 네 번째 값(SOL_PHOTO 키)이 있으면 아이콘 대신 실사를 씁니다.
    · 다섯 번째 값(주소)이 있으면 카드 전체가 해당 주요제품 페이지로 가는 링크가 됩니다.
      제품 페이지가 없는 소프트웨어 항목은 링크 없이 그대로 둡니다."""
    out = ""
    for it in items:
        name, icon, desc = it[0], it[1], it[2]
        ph = it[3] if len(it) > 3 else None
        href = it[4] if len(it) > 4 else None
        fig = solphoto(ph, p) if ph else ICONS[icon]
        cls = "sol-item" + (" has-photo" if ph else "") + (" is-link" if href else "")
        op = ('<a class="%s" href="%s" data-cursor="%s" data-reveal>'
              % (cls, href, "제품 보기" if LANG == "ko" else "View product")) if href \
             else '<article class="%s" data-reveal>' % cls
        go = '<span class="sol-go">%s</span>' % _ARROW if href else ""
        out += (f'{op}<div class="fig">{fig}{go}</div>'
                f'<div class="txt"><h3>{name}</h3><p>{desc}</p></div>'
                f'{"</a>" if href else "</article>"}')
    one = " is-one" if len(items) == 1 else ""
    return f'<div class="sol-grid{one}" data-reveal-stagger="110">{out}</div>'


def spec(items):
    d = "".join(f'<div><h4>{t}</h4><p>{b}</p></div>' for t, b in items)
    return f'<div class="spec" data-reveal>{d}</div>'


def dspec(items):
    d = "".join('<article class="dspec" data-reveal style="--td:%dms"><span class="n">%02d</span>'
                '<h3>%s</h3><p>%s</p></article>' % (i * 110, i + 1, a, b)
                for i, (a, b) in enumerate(items))
    return '<div class="dspec-grid">%s</div>' % d


def dl(rows):
    r = "".join(f'<div class="row"><dt>{k}</dt><dd>{v}</dd></div>' for k, v in rows)
    return f'<dl class="dl" data-reveal>{r}</dl>'


# ============================================================
# 페이지별 본문
# ============================================================
PAGES = []

# ---------- 메인 ----------
HOME_BODY = open(os.path.join(ROOT, "_home_body.html"), encoding="utf-8").read() \
    if os.path.exists(os.path.join(ROOT, "_home_body.html")) else ""

# ---------- 회사소개 / 인사말 ----------
greeting = f'''<section class="section"><div class="area-box">
{head("GREETING", "CEO 인사말", "상림기술을 찾아주신 여러분을 환영합니다.")}
<div class="ceo">
  <figure class="ceo-photo" data-reveal>
    <picture>
      <source srcset="../assets/img/ceo.webp" type="image/webp">
      <img src="../assets/img/ceo.png" alt="(주)상림기술 대표이사 임상일" width="666" height="760">
    </picture>
    <figcaption class="ceo-badge">대표이사 <b>임상일</b></figcaption>
  </figure>
  <div class="greet-card" data-reveal data-d="140">
    <p class="q">무한한 책임감과 도전정신으로<br>지속적인 신뢰를 받는 기업이 되겠습니다</p>
    <p>주식회사 상림기술은 지난 2021년 04월 창립 이래 신뢰와 기술력, 도전정신을 바탕으로
    첨단 교통 시스템 구축을 위한 다양한 사업을 영위하는 기업으로서 국가 교통 산업 발전에 기여해 왔습니다.</p>
    <p>급변하는 국제정세와 경제블록화 등 여러 불확실성 속에서도 <strong>누적매출액 210억</strong>,
    <strong>기업신용평가등급 BBB+</strong>를 달성하는 쾌거를 이루었습니다.
    이는 창업기업으로서 높은 신뢰도와 경쟁력을 갖추었다는 점에서 매우 값진 성과였습니다.</p>
    <p>한편, 상림기술은 점차 높아지는 시장장벽을 넘어서고 잠재적 리스크를 사전에 식별·완화하기 위해
    다각적인 노력을 기울이고 있습니다. 이제 국내 교통분야뿐만 아니라 해외 교통부문 시장에 도전하는 등
    사업 영역을 넓히고 지속가능한 경영을 실현하는 새로운 기업으로 변화해 가고 있습니다.</p>
    <div class="greet-sign" data-reveal>
      <div class="gs-txt"><span class="role">(주)상림기술 대표이사</span><span class="name">임상일</span></div>
    </div>
  </div>
</div>
</div></section>

<section class="section band"><div class="area-box">
<div class="section-head" data-reveal><span class="eyebrow" style="color:var(--c-accent-bright)">AT A GLANCE</span>
<h2>숫자로 보는 상림기술</h2></div>
<div class="stat-grid">
  <div class="stat" data-reveal><b><span class="num" data-count="210">0</span><span class="u">억</span></b><span>누적 매출액</span><i></i></div>
  <div class="stat" data-reveal data-d="100"><b><span class="num">BBB+</span></b><span>기업신용평가등급</span><i></i></div>
  <div class="stat" data-reveal data-d="200"><b><span class="num">2021</span><span class="u">년</span></b><span>설립</span><i></i></div>
</div>
</div></section>

<section class="section"><div class="area">
{head("COMPANY PROFILE", "회사 개요")}
{dl([
  ("회사명", COMPANY),
  ("대표이사", "임상일"),
  ("설립일", FOUNDED),
  ("사업자등록번호", BIZNO),
  ("해당부문 사업기간", "2021년 04월 ~ 현재"),
  ("등록 사업분야", BIZ_FIELDS),
  ("주요사업", "지능형 도로교통체계(ITS) 솔루션 / 버스정보안내시스템(BIS) / 긴급차량 우선신호 솔루션 / 스마트 스쿨존 솔루션<br>"
              "버스정보안내기기(BIT) / 도로전광표지판(VMS) / 보안용카메라 / 행선지안내판 / 초정밀 GNSS<br>"
              "ITS·BIS 센터 유지보수 / 교통시설물 현장장비 유지보수"),
  ("4차 산업 R&amp;D", "자율주행 / 스마트시티 / 스마트팩토리 / IoT"),
  ("본사", ADDR_HQ),
  ("공장", ADDR_FT),
  ("연락처", f'T. <a href="tel:0220831333">{TEL}</a> &nbsp;·&nbsp; E. <a href="mailto:{MAIL}">{MAIL}</a>'),
])}
<div class="lead-box" data-reveal style="margin-top:48px;margin-bottom:0">
<p>주식회사 상림기술은 2021년 창업하여 화성시 교통정보시스템(ITS) 사업 참여를 시작으로,
전국 주요 지자체와 민간기업에 교통솔루션과 전문기기를 제공하는 정보통신분야의 전문 업체로 자리잡아 가고 있습니다.</p></div>
</div></section>'''
PAGES.append(("company/greeting.html", "인사말", "상림기술 대표이사 인사말과 회사 개요입니다.", "company", greeting))

# ---------- 회사소개 / 구축사례 ----------
REC = [
 ("도로교통 전광판 (VMS)", [
   ("대전지방국토관리청 (VMS)","충청북도 충북권"),("영천시 도로교통정보표지판","경상북도 영천시"),
   ("원적산 터널 전광판","인천광역시 원적산"),("원적산터널 VMS 요금표시기","인천광역시 원적산터널"),
   ("안동시 ITS 도로교통정보표지판","경상북도 안동시"),("성남시 ITS 도로교통정보표지판","경기도 성남시"),
   ("춘천시 ITS 도로교통정보표지판","강원도 춘천시")]),
 ("버스정보안내 단말기 (BIT)", [
   ("화성시 버스정보안내단말기","경기도 화성시"),("수원시 버스정보안내단말기","경기도 수원시"),
   ("용인시 버스정보안내단말기","경기도 용인시"),("안양시 버스정보안내단말기","경기도 안양시"),
   ("광명시 버스정보안내단말기","경기도 광명시"),("광명시 스마트 버스정류장","경기도 광명시")]),
 ("긴급차량 우선신호 시스템", [
   ("서울시 긴급차량 우선신호 시스템","서울특별시"),("영천시 긴급차량 출동안내 전광판","경상북도 영천시"),
   ("수원시 긴급차량 출동안내 전광판","경기도 수원시"),("광명시 긴급차량 출동안내 전광판","경기도 광명시"),
   ("용인시 긴급차량 출동안내 전광판","경기도 용인시")]),
 ("보행자 안전 · 스마트 스쿨존", [
   ("광명시 어린이보호구역 보행자안전시스템","경기도 광명시"),("광명시 보행신호 자동연장 시스템","경기도 광명시"),
   ("안양시 어린이보호구역 계도전광판","경기도 안양시"),("화성시 스마트 보행자안전시스템","경기도 화성시")]),
 ("전기차 충전소 · 기타", [
   ("칼텍스 전기차 충전소 전광판","서울특별시 내곡동"),("이지차저 전기차 충전소 전광판","경부고속도로 김천휴게소"),
   ("안동시 신시장 직진금지 안내 시스템","경상북도 안동시")]),
]
_cats = ""
REC_IMG = ["vms", "bit", "evs2", "ssz2", "ecs"]   # 카테고리 순서와 1:1
for _ci, (cname, rows) in enumerate(REC):
    lis = "".join(f'<li><b>{a}</b><span>{b}</span></li>' for a, b in rows)
    _thumb = ('<span class="rec-thumb">%s</span>' % pimg(REC_IMG[_ci], "../")) if _ci < len(REC_IMG) else ""
    _cats += (f'<div class="rec-cat" data-reveal>'
              f'<h3>{_thumb}<span class="rec-t">{cname}</span>'
              f'<span class="cnt">{len(rows)}건</span></h3>'
              f'<ul class="rec-list">{lis}</ul></div>')
_total = sum(len(r) for _, r in REC)
record = f'''<section class="section band"><div class="area-box">
<div class="section-head" data-reveal><span class="eyebrow" style="color:var(--c-accent-bright)">TRACK RECORD</span>
<h2>구축사례</h2><p class="lead">전국 지자체와 기관에 상림기술의 시스템이 설치·운영되고 있습니다. (총 {_total}건)</p></div>
{_cats}
</div></section>'''
HIST_TPL = """<section class="section tl-sec"><div class="area-box">
<div class="section-head" data-reveal><span class="eyebrow">HISTORY</span>
<h2>회사 연혁</h2><p class="lead">2021년 창업 이후 6년, %(n)d건의 발자취입니다.</p></div>

<div class="tl-wrap">
  <aside class="tl-rail" aria-label="연도 바로가기">
    <div class="tl-bar"><span class="tl-fill" id="tlFill"></span></div>
    <div class="tl-jumps">%(jumps)s</div>
  </aside>
  <div class="tl" id="tl">%(items)s</div>
</div>

<div class="lead-box" data-reveal style="margin-top:60px;margin-bottom:0">
<p>2021년 화성시 ITS 고도화 사업을 시작으로 매년 사업 영역과 구축 지역을 넓혀 왔습니다.
2022년 기업부설연구소·벤처기업 등록으로 연구개발 기반을 갖추었고, 2024년 전국 고속도로 59개소
전기차 충전소 전광판 사업으로 민간 부문에, 2025년 부산광역시 BIMS 사업으로 광역시 시장에 진입했습니다.</p></div>
</div></section>"""


# ---------- 회사소개 / 연혁 ----------
# 출처: 일반현황 상림.pptx (주요연혁) + 회사소개서 25ver
#   k = 구분 | b:사업수주  c:인증·등록  s:창업
HISTORY = [
 ("2026", "클라우드 전환기", [
   ("b", "2026년 평택시 ITS 통합 유지관리 용역", "수행중", 1),
   ("b", "버스정보시스템(BIS) 확장 구축 사업 · 안동시", "수행중", 1),
 ]),
 ("2025", "광역시 진출", [
   ("b", "2025년 부산광역시 버스정보관리시스템(BIMS) 추가 및 개선사업", "", 1),
   ("b", "버스정보시스템 클라우드 적용 SW 개발사업", "", 1),
   ("b", "화성시 지능형교통체계(ITS) 고도화 사업 시행", "", 0),
   ("b", "24년 부산청 국도 감응신호 구축사업", "", 0),
   ("b", "목포시 버스정보시스템 기능개선 고도화", "", 0),
 ]),
 ("2024", "민간 부문 확장", [
   ("b", "전기차 충전소 전광판 제작 및 설치", "전국 고속도로 59개소 · GS칼텍스", 1),
   ("b", "서울시 긴급차량 우선신호시스템 시범사업 용역", "", 1),
   ("b", "안동시 버스정보시스템(BIS) 확장 및 개선사업", "", 0),
   ("b", "2024년 제천시 버스정보안내시스템(BIS) 고도화 구축 사업", "", 0),
   ("b", "2024년~2025년 광명시 지능형교통정보시스템 통합유지보수용역", "", 0),
   ("b", "안동시 신시장 신호등 전광판 운영소프트웨어 구축용역", "", 0),
   ("b", "기흥구 수위안내 LED 전광판 제작·설치공사", "", 0),
   ("c", "직접생산확인증명서 2건 등록", "소프트웨어 유지 및 지원 서비스", 0),
 ]),
 ("2023", "안전 분야 진입", [
   ("b", "광명 긴급차량 우선신호 시스템 구축 사업", "", 1),
   ("b", "어린이보호구역 보행자안전시스템 구축사업", "", 1),
   ("b", "2023년 광명 지능형교통정보시스템 통합 유지보수 용역", "", 0),
   ("b", "교통신호제어시스템 소프트웨어 업그레이드 고도화 용역", "", 0),
   ("b", "안동 ITS 자재 납품 (설치 포함)", "", 0),
   ("c", "직접생산확인증명서 3건 등록", "영상정보디스플레이 장치 · 버스및차량안내장치 · 안내전광판", 0),
 ]),
 ("2022", "연구개발 기반 구축", [
   ("c", "기업부설연구소 등록", "", 1),
   ("c", "벤처기업 등록", "혁신성장유형", 1),
   ("b", "광명시 지능형교통정보시스템 구축 및 성능개선 사업", "", 1),
   ("b", "버스정류장 안내단말기 이전설치 공사", "", 0),
   ("c", "직접생산확인증명서 6건 등록", "빅데이터분석 서비스 · 정보인프라 구축 · 정보시스템 개발 서비스 · 패키지소프트웨어 개발 및 도입 · 운영위탁 서비스 · 인터넷 지원개발 서비스", 0),
   ("c", "직접생산확인증명서 2건 등록", "보안용 카메라 · 영상감시장치", 0),
 ]),
 ("2021", "창업", [
   ("s", "주식회사 상림기술 창업", "2021. 04. 07", 1),
   ("b", "2021년 화성시 지능형교통체계(ITS) 고도화 구축 사업", "첫 수주", 1),
   ("c", "정보통신공사업 등록", "", 0),
   ("c", "소프트웨어 사업자 신고", "", 0),
 ]),
]
_KIND = {"b": ("사업", "k-b"), "c": ("인증·등록", "k-c"), "s": ("창업", "k-s")}

_ty = ""
for _y, _cap, _items in HISTORY:
    _li = ""
    for _k, _t, _sub, _hi in _items:
        _label, _cls = _KIND[_k]
        _sh = '<span class="tl-sub">%s</span>' % _sub if _sub else ""
        _li += ('<li class="%s%s"><span class="tl-dot"></span>'
                '<span class="tl-tag">%s</span>'
                '<span class="tl-txt"><b>%s</b>%s</span></li>'
                % (_cls, " hi" if _hi else "", _label, _t, _sh))
    _ty += ('<section class="tl-year" id="y%s" data-year="%s">'
            '<div class="tl-head"><div class="tl-y"><span>%s</span></div>'
            '<p class="tl-cap">%s</p><span class="tl-cnt">%d건</span></div>'
            '<ul class="tl-list">%s</ul></section>'
            % (_y, _y, _y, _cap, len(_items), _li))

_jumps = "".join('<button class="tl-jump" type="button" data-go="y%s"><i></i><span>%s</span></button>'
                 % (y, y) for y, _, _ in HISTORY)
_nitem = sum(len(i) for _, _, i in HISTORY)

history = HIST_TPL % dict(items=_ty, jumps=_jumps, n=_nitem)
PAGES.append(("company/history.html", "연혁",
              "2021년 창업 이후 상림기술이 걸어온 6년간의 주요 사업·인증 이력입니다.", "company", history))


PAGES.append(("company/rnd.html", "기업부설연구소", "2022년 출범한 상림기술 기업부설연구소와 R&D 비전.", "company", '<section class="section"><div class="area">\n<div class="section-head" data-reveal><span class="eyebrow">R&amp;D CENTER</span><h2>기업부설연구소</h2><p class="lead">2022년 출범 · 첨단 교통정보 시스템 개발</p></div>\n<div class="lead-box" data-reveal><p>상림기술 연구소는 2022년 기업부설연구소로 출범하여 첨단 교통정보 시스템 개발에 앞장서 왔습니다.\n우수한 연구인력을 통해 전국 주요 지자체의 지능형교통체계(ITS), 버스정보시스템(BIS),\n긴급차량 우선신호 서비스, 스마트 스쿨존 서비스를 성공적으로 구축하는 등 경쟁력을 갖춘 연구소로 거듭나고 있으며,\n지속적인 고도화를 통해 그 기술력을 인정받고 있습니다.</p></div>\n</div></section>\n\n<section class="section" style="background:var(--c-bg-soft)"><div class="area-box">\n<div class="section-head" data-reveal><span class="eyebrow">R&amp;D VISION</span><h2>연구 비전</h2></div>\n<div class="rnd-grid" data-reveal-stagger="120">\n  <article class="rnd-card" data-reveal>\n    <span class="n">CORE</span><h3>솔루션 구축</h3>\n    <p>핵심 성장 동력은 교통부문 솔루션 제공입니다. 상림기술의 솔루션은 높은 안정성과 데이터 정합성을 보장하며,\n    사용자의 편의성 개선을 위해 공인기관에서 객관적인 평가를 받아 개선하는 등 교통시스템 분야에서 활발히 연구하고 있습니다.</p>\n  </article>\n  <article class="rnd-card" data-reveal>\n    <span class="n">MID-LONG TERM</span><h3>시스템 고도화</h3>\n    <p>솔루션 연구와 구축을 통해 축적한 내부역량을 바탕으로 기존 시스템에 대한 고도화 기능을 제공하는 것을 목표로 합니다.\n    이를 통해 해외 시장에 진출 가능한 첨단 솔루션을 개발하고자 합니다.</p>\n  </article>\n  <article class="rnd-card" data-reveal>\n    <span class="n">NEW GROWTH</span><h3>신규 시스템 개발</h3>\n    <p>기존 교통 시스템의 규격과 한계를 극복하고자 합니다. 기 구축 시스템과 AI 분야의 융합,\n    클라우드화에 대한 연구를 진행하며 이를 구현하기 위한 다양한 연구를 활발히 수행하고 있습니다.</p>\n  </article>\n</div>\n</div></section>'))
PAGES.append(("company/partners.html", "파트너사", "상림기술과 함께한 공공기관·민간기업 파트너.", "company", '<section class="section"><div class="area-box">\n<div class="section-head" data-reveal><span class="eyebrow">PARTNERS</span><h2>파트너사</h2><p class="lead">상림기술과 함께한 기관과 기업입니다.</p></div>\n<div class="pt-tabs" data-reveal>\n  <button class="on" data-cat="all">전체 30</button>\n  <button data-cat="pub">공공부문 21</button>\n  <button data-cat="pri">민간부문 9</button>\n</div>\n<div class="pt-grid" id="ptGrid" data-reveal-stagger="45"><figure class="pt" data-cat="pub" data-reveal><img src="../assets/img/partner/pub-01.png" alt="화성시" loading="lazy"><figcaption class="pt-name">화성시</figcaption></figure><figure class="pt" data-cat="pub" data-reveal><img src="../assets/img/partner/pub-02.png" alt="광명시" loading="lazy"><figcaption class="pt-name">광명시</figcaption></figure><figure class="pt" data-cat="pub" data-reveal><img src="../assets/img/partner/pub-03.png" alt="용인시" loading="lazy"><figcaption class="pt-name">용인시</figcaption></figure><figure class="pt" data-cat="pub" data-reveal><img src="../assets/img/partner/pub-04.png" alt="서울특별시" loading="lazy"><figcaption class="pt-name">서울특별시</figcaption></figure><figure class="pt" data-cat="pub" data-reveal><img src="../assets/img/partner/pub-05.png" alt="안양시" loading="lazy"><figcaption class="pt-name">안양시</figcaption></figure><figure class="pt" data-cat="pub" data-reveal><img src="../assets/img/partner/pub-06.png" alt="안동시" loading="lazy"><figcaption class="pt-name">안동시</figcaption></figure><figure class="pt" data-cat="pub" data-reveal><img src="../assets/img/partner/pub-07.png" alt="파주시" loading="lazy"><figcaption class="pt-name">파주시</figcaption></figure><figure class="pt" data-cat="pub" data-reveal><img src="../assets/img/partner/pub-08.png" alt="수원시" loading="lazy"><figcaption class="pt-name">수원시</figcaption></figure><figure class="pt" data-cat="pub" data-reveal><img src="../assets/img/partner/pub-09.png" alt="광양시" loading="lazy"><figcaption class="pt-name">광양시</figcaption></figure><figure class="pt" data-cat="pub" data-reveal><img src="../assets/img/partner/pub-10.png" alt="김포시" loading="lazy"><figcaption class="pt-name">김포시</figcaption></figure><figure class="pt" data-cat="pub" data-reveal><img src="../assets/img/partner/pub-11.png" alt="성남시" loading="lazy"><figcaption class="pt-name">성남시</figcaption></figure><figure class="pt" data-cat="pub" data-reveal><img src="../assets/img/partner/pub-12.png" alt="대전광역시" loading="lazy"><figcaption class="pt-name">대전광역시</figcaption></figure><figure class="pt" data-cat="pub" data-reveal><img src="../assets/img/partner/pub-13.png" alt="세종특별자치시" loading="lazy"><figcaption class="pt-name">세종특별자치시</figcaption></figure><figure class="pt" data-cat="pub" data-reveal><img src="../assets/img/partner/pub-14.png" alt="춘천시" loading="lazy"><figcaption class="pt-name">춘천시</figcaption></figure><figure class="pt" data-cat="pub" data-reveal><img src="../assets/img/partner/pub-15.png" alt="경주시" loading="lazy"><figcaption class="pt-name">경주시</figcaption></figure><figure class="pt" data-cat="pub" data-reveal><img src="../assets/img/partner/pub-16.png" alt="충청남도" loading="lazy"><figcaption class="pt-name">충청남도</figcaption></figure><figure class="pt" data-cat="pub" data-reveal><img src="../assets/img/partner/pub-17.png" alt="청주시" loading="lazy"><figcaption class="pt-name">청주시</figcaption></figure><figure class="pt" data-cat="pub" data-reveal><img src="../assets/img/partner/pub-18.png" alt="고양특례시" loading="lazy"><figcaption class="pt-name">고양특례시</figcaption></figure><figure class="pt" data-cat="pub" data-reveal><img src="../assets/img/partner/pub-19.png" alt="영천시" loading="lazy"><figcaption class="pt-name">영천시</figcaption></figure><figure class="pt" data-cat="pub" data-reveal><img src="../assets/img/partner/pub-20.png" alt="제천시" loading="lazy"><figcaption class="pt-name">제천시</figcaption></figure><figure class="pt" data-cat="pub" data-reveal><img src="../assets/img/partner/pub-21.png" alt="제주특별자치도" loading="lazy"><figcaption class="pt-name">제주특별자치도</figcaption></figure><figure class="pt" data-cat="pri" data-reveal><img src="../assets/img/partner/pri-01.png" alt="GS칼텍스" loading="lazy"><figcaption class="pt-name">GS칼텍스</figcaption></figure><figure class="pt" data-cat="pri" data-reveal><img src="../assets/img/partner/pri-02.png" alt="EASY CHARGER" loading="lazy"><figcaption class="pt-name">EASY CHARGER</figcaption></figure><figure class="pt" data-cat="pri" data-reveal><img src="../assets/img/partner/pri-03.png" alt="SONGAM" loading="lazy"><figcaption class="pt-name">SONGAM</figcaption></figure><figure class="pt" data-cat="pri" data-reveal><img src="../assets/img/partner/pri-04.png" alt="KT" loading="lazy"><figcaption class="pt-name">KT</figcaption></figure><figure class="pt" data-cat="pri" data-reveal><img src="../assets/img/partner/pri-05.png" alt="SK telecom" loading="lazy"><figcaption class="pt-name">SK telecom</figcaption></figure><figure class="pt" data-cat="pri" data-reveal><img src="../assets/img/partner/pri-06.png" alt="한국정보기술" loading="lazy"><figcaption class="pt-name">한국정보기술</figcaption></figure><figure class="pt" data-cat="pri" data-reveal><img src="../assets/img/partner/pri-07.png" alt="대보정보통신" loading="lazy"><figcaption class="pt-name">대보정보통신</figcaption></figure><figure class="pt" data-cat="pri" data-reveal><img src="../assets/img/partner/pri-08.png" alt="TRACOM" loading="lazy"><figcaption class="pt-name">TRACOM</figcaption></figure><figure class="pt" data-cat="pri" data-reveal><img src="../assets/img/partner/pri-09.png" alt="대흥정보" loading="lazy"><figcaption class="pt-name">대흥정보</figcaption></figure></div>\n<div class="lead-box" data-reveal style="margin-top:52px;margin-bottom:0">\n<p>전국 지자체와 공공기관, 그리고 민간 기업과 함께 교통 인프라를 구축하고 있습니다.\n로고에 마우스를 올리면 원래 색상으로 크게 확대됩니다.</p></div>\n</div></section>'))

PAGES.append(("company/record.html", "구축사례", f"상림기술이 전국 지자체·기관에 구축한 {_total}건의 사례입니다.", "company", record))

ORG_TPL = """<section class="section"><div class="area-box">
<div class="section-head" data-reveal><span class="eyebrow">ORGANIZATION</span>
<h2>조직도</h2><p class="lead">기술영업 · 제안 · 수행 · 연구개발 전 과정을 자체 조직으로 수행합니다.</p></div>

<div class="og" id="og">
  <div class="og-l0"><div class="og-node og-ceo" data-og>대표이사</div></div>
  <div class="og-line og-line-v"><span></span></div>
  <div class="og-l1">
    <div class="og-col" data-og>
      <div class="og-node og-dept">기술영업부</div>
      <div class="og-kids"><span class="og-kid">기술영업 1팀</span><span class="og-kid">기술영업 2팀</span></div>
    </div>
    <div class="og-col" data-og>
      <div class="og-node og-dept">제안기획팀</div>
      <div class="og-kids"><span class="og-kid">제안팀</span><span class="og-kid">디자인팀</span></div>
    </div>
    <div class="og-col" data-og>
      <div class="og-node og-dept">시스템 수행팀</div>
      <div class="og-kids"><span class="og-kid">수행팀</span><span class="og-kid">장비제작팀</span></div>
    </div>
    <div class="og-col" data-og>
      <div class="og-node og-dept og-rnd">기업부설연구소</div>
      <div class="og-kids"><span class="og-kid">IoT 개발팀</span><span class="og-kid">S/W 개발팀</span></div>
    </div>
  </div>
  <div class="og-support" data-og><span>근무지원</span></div>
</div>
</div></section>"""


# ---------- 회사소개 / 조직도 ----------
# 출처: 일반현황 상림.pptx — 제안사 조직 및 인원(주사업자)
organization = ORG_TPL
PAGES.append(("company/organization.html", "조직도",
              "상림기술 조직 구성입니다.", "company", organization))


# ---------- 회사소개 / 인증현황 ----------
cert = '<section class="section"><div class="area-box">\n<div class="section-head" data-reveal><span class="eyebrow">CERTIFICATION</span>\n<h2>인증현황</h2>\n<p class="lead">상림기술은 국제 경영시스템 인증과 제품별 KC 적합등록, TTA 시험인증, 환경표지 인증을 보유하고 있습니다.</p></div>\n\n<div class="cert-stats" data-reveal>\n  <div><b>4</b><span>ISO 경영시스템</span></div>\n  <div><b>9</b><span>KC 적합등록</span></div>\n  <div><b>3</b><span>TTA 시험인증</span></div>\n  <div><b>3</b><span>환경표지 · 시험성적</span></div>\n</div>\n\n<div class="cert-filter" data-reveal>\n  <button class="on" data-cat="all">전체 19</button>\n  <button data-cat="iso">ISO 경영시스템</button>\n  <button data-cat="kc">KC 적합등록</button>\n  <button data-cat="tta">TTA 시험인증</button>\n  <button data-cat="eco">환경표지</button>\n  <button data-cat="rel">시험성적서</button>\n</div>\n\n<div class="cert-grid" id="certGrid" data-reveal-stagger="70"><figure class="cert" data-cat="iso" data-reveal><button class="cert-img" type="button" data-full="../assets/cert/iso9001.jpg" data-cap="품질경영시스템 ISO 9001 — ISO 9001:2015"><img src="../assets/cert/iso9001-t.jpg" alt="품질경영시스템 ISO 9001 — ISO 9001:2015" loading="lazy" width="600" height="800"></button><figcaption><span class="tag tag-iso">ISO</span><h3>품질경영시스템 ISO 9001</h3><p class="model">ISO 9001:2015</p><dl><div><dt>인증범위</dt><dd>교통시스템 설계·개발·구축</dd></div><div><dt>구분</dt><dd>국문 인증서</dd></div></dl></figcaption></figure><figure class="cert" data-cat="iso" data-reveal><button class="cert-img" type="button" data-full="../assets/cert/iso14001.jpg" data-cap="환경경영시스템 ISO 14001 — ISO 14001:2015"><img src="../assets/cert/iso14001-t.jpg" alt="환경경영시스템 ISO 14001 — ISO 14001:2015" loading="lazy" width="600" height="800"></button><figcaption><span class="tag tag-iso">ISO</span><h3>환경경영시스템 ISO 14001</h3><p class="model">ISO 14001:2015</p><dl><div><dt>인증범위</dt><dd>교통시스템 설계·개발·구축</dd></div><div><dt>구분</dt><dd>국문 인증서</dd></div></dl></figcaption></figure><figure class="cert" data-cat="iso" data-reveal><button class="cert-img" type="button" data-full="../assets/cert/iso9001-en.jpg" data-cap="품질경영시스템 ISO 9001 — ISO 9001:2015"><img src="../assets/cert/iso9001-en-t.jpg" alt="품질경영시스템 ISO 9001 — ISO 9001:2015" loading="lazy" width="600" height="800"></button><figcaption><span class="tag tag-iso">ISO</span><h3>품질경영시스템 ISO 9001</h3><p class="model">ISO 9001:2015</p><dl><div><dt>인증범위</dt><dd>Quality Management</dd></div><div><dt>구분</dt><dd>영문 인증서</dd></div></dl></figcaption></figure><figure class="cert" data-cat="iso" data-reveal><button class="cert-img" type="button" data-full="../assets/cert/iso14001-en.jpg" data-cap="환경경영시스템 ISO 14001 — ISO 14001:2015"><img src="../assets/cert/iso14001-en-t.jpg" alt="환경경영시스템 ISO 14001 — ISO 14001:2015" loading="lazy" width="600" height="800"></button><figcaption><span class="tag tag-iso">ISO</span><h3>환경경영시스템 ISO 14001</h3><p class="model">ISO 14001:2015</p><dl><div><dt>인증범위</dt><dd>Environmental Management</dd></div><div><dt>구분</dt><dd>영문 인증서</dd></div></dl></figcaption></figure><figure class="cert" data-cat="kc" data-reveal><button class="cert-img" type="button" data-full="../assets/cert/kc-gnss.jpg" data-cap="초정밀 GNSS RTK 모듈 — SLv-001"><img src="../assets/cert/kc-gnss-t.jpg" alt="초정밀 GNSS RTK 모듈 — SLv-001" loading="lazy" width="600" height="800"></button><figcaption><span class="tag tag-kc">KC</span><h3>초정밀 GNSS RTK 모듈</h3><p class="model">SLv-001</p><dl><div><dt>등록번호</dt><dd>R-R-SLv-SLGRO-001</dd></div><div><dt>등록일</dt><dd>2023-02-22</dd></div><div><dt>기기부호</dt><dd>MOB31 / LTE9, IMT9</dd></div></dl></figcaption></figure><figure class="cert" data-cat="kc" data-reveal><button class="cert-img" type="button" data-full="../assets/cert/kc-bit.jpg" data-cap="버스정보안내기 SL-BIT — SL-BIT-TRI"><img src="../assets/cert/kc-bit-t.jpg" alt="버스정보안내기 SL-BIT — SL-BIT-TRI" loading="lazy" width="600" height="800"></button><figcaption><span class="tag tag-kc">KC</span><h3>버스정보안내기 SL-BIT</h3><p class="model">SL-BIT-TRI</p><dl><div><dt>등록번호</dt><dd>R-R-SLv-SL-BIT-TRI</dd></div><div><dt>등록일</dt><dd>2023-10-11</dd></div><div><dt>파생모델</dt><dd>3D8Y · 4D12Y</dd></div></dl></figcaption></figure><figure class="cert" data-cat="kc" data-reveal><button class="cert-img" type="button" data-full="../assets/cert/kc-led.jpg" data-cap="LED 모듈 — SL240M111"><img src="../assets/cert/kc-led-t.jpg" alt="LED 모듈 — SL240M111" loading="lazy" width="600" height="800"></button><figcaption><span class="tag tag-kc">KC</span><h3>LED 모듈</h3><p class="model">SL240M111</p><dl><div><dt>등록번호</dt><dd>R-R-SLv-SL240M111</dd></div><div><dt>등록일</dt><dd>2023-09-14</dd></div><div><dt>기기부호</dt><dd>VDO11</dd></div></dl></figcaption></figure><figure class="cert" data-cat="kc" data-reveal><button class="cert-img" type="button" data-full="../assets/cert/kc-rtu.jpg" data-cap="상태제어보드 CONTROLLER — SL_RTU"><img src="../assets/cert/kc-rtu-t.jpg" alt="상태제어보드 CONTROLLER — SL_RTU" loading="lazy" width="600" height="800"></button><figcaption><span class="tag tag-kc">KC</span><h3>상태제어보드 CONTROLLER</h3><p class="model">SL_RTU</p><dl><div><dt>등록번호</dt><dd>R-R-SLv-SL_RTU</dd></div><div><dt>등록일</dt><dd>2023-11-10</dd></div><div><dt>파생모델</dt><dd>Ver.1.00</dd></div></dl></figcaption></figure><figure class="cert" data-cat="kc" data-reveal><button class="cert-img" type="button" data-full="../assets/cert/kc-ps01.jpg" data-cap="PoE 스플리터 PS01 — SL-PS01"><img src="../assets/cert/kc-ps01-t.jpg" alt="PoE 스플리터 PS01 — SL-PS01" loading="lazy" width="600" height="800"></button><figcaption><span class="tag tag-kc">KC</span><h3>PoE 스플리터 PS01</h3><p class="model">SL-PS01</p><dl><div><dt>등록번호</dt><dd>R-R-SLv-SL-PS01</dd></div><div><dt>등록일</dt><dd>2024-01-23</dd></div><div><dt>기기부호</dt><dd>IMI61</dd></div></dl></figcaption></figure><figure class="cert" data-cat="kc" data-reveal><button class="cert-img" type="button" data-full="../assets/cert/kc-vcu.jpg" data-cap="MCU-VCU 제어유닛 — SL-VCU_12CH"><img src="../assets/cert/kc-vcu-t.jpg" alt="MCU-VCU 제어유닛 — SL-VCU_12CH" loading="lazy" width="600" height="800"></button><figcaption><span class="tag tag-kc">KC</span><h3>MCU-VCU 제어유닛</h3><p class="model">SL-VCU_12CH</p><dl><div><dt>등록번호</dt><dd>R-R-SLv-SL-VCU_12CH</dd></div><div><dt>등록일</dt><dd>2024-05-09</dd></div><div><dt>파생모델</dt><dd>10CH · 8CH</dd></div></dl></figcaption></figure><figure class="cert" data-cat="kc" data-reveal><button class="cert-img" type="button" data-full="../assets/cert/kc-mcu.jpg" data-cap="표준형제어기 MCU — SL_MCU"><img src="../assets/cert/kc-mcu-t.jpg" alt="표준형제어기 MCU — SL_MCU" loading="lazy" width="600" height="800"></button><figcaption><span class="tag tag-kc">KC</span><h3>표준형제어기 MCU</h3><p class="model">SL_MCU</p><dl><div><dt>등록번호</dt><dd>R-R-SLv-SL_MCU</dd></div><div><dt>등록일</dt><dd>2024-08-14</dd></div><div><dt>기기부호</dt><dd>IMC31</dd></div></dl></figcaption></figure><figure class="cert" data-cat="kc" data-reveal><button class="cert-img" type="button" data-full="../assets/cert/kc-ssz.jpg" data-cap="스쿨존 안내전광판 — SL-SMART-16D32Y"><img src="../assets/cert/kc-ssz-t.jpg" alt="스쿨존 안내전광판 — SL-SMART-16D32Y" loading="lazy" width="600" height="800"></button><figcaption><span class="tag tag-kc">KC</span><h3>스쿨존 안내전광판</h3><p class="model">SL-SMART-16D32Y</p><dl><div><dt>인증구분</dt><dd>KC 인증</dd></div><div><dt>비고</dt><dd>인증서 원본 참조</dd></div></dl></figcaption></figure><figure class="cert" data-cat="kc" data-reveal><button class="cert-img" type="button" data-full="../assets/cert/kc-cam.jpg" data-cap="회전형 카메라 — SL-P223ID5"><img src="../assets/cert/kc-cam-t.jpg" alt="회전형 카메라 — SL-P223ID5" loading="lazy" width="600" height="800"></button><figcaption><span class="tag tag-kc">KC</span><h3>회전형 카메라</h3><p class="model">SL-P223ID5</p><dl><div><dt>인증구분</dt><dd>KC 인증</dd></div><div><dt>비고</dt><dd>인증서 원본 참조</dd></div></dl></figcaption></figure><figure class="cert" data-cat="tta" data-reveal><button class="cert-img" type="button" data-full="../assets/cert/tta-223.jpg" data-cap="TTA 시험인증 · 회전형 카메라 — SL-P223ID5"><img src="../assets/cert/tta-223-t.jpg" alt="TTA 시험인증 · 회전형 카메라 — SL-P223ID5" loading="lazy" width="600" height="800"></button><figcaption><span class="tag tag-tta">TTA</span><h3>TTA 시험인증 · 회전형 카메라</h3><p class="model">SL-P223ID5</p><dl><div><dt>인증기관</dt><dd>한국정보통신기술협회</dd></div><div><dt>구분</dt><dd>TTA 인증서</dd></div></dl></figcaption></figure><figure class="cert" data-cat="tta" data-reveal><button class="cert-img" type="button" data-full="../assets/cert/tta-230.jpg" data-cap="TTA 시험인증 · 회전형 카메라 — SL-P230ID5"><img src="../assets/cert/tta-230-t.jpg" alt="TTA 시험인증 · 회전형 카메라 — SL-P230ID5" loading="lazy" width="600" height="800"></button><figcaption><span class="tag tag-tta">TTA</span><h3>TTA 시험인증 · 회전형 카메라</h3><p class="model">SL-P230ID5</p><dl><div><dt>인증기관</dt><dd>한국정보통신기술협회</dd></div><div><dt>구분</dt><dd>TTA 인증서</dd></div></dl></figcaption></figure><figure class="cert" data-cat="tta" data-reveal><button class="cert-img" type="button" data-full="../assets/cert/tta-510.jpg" data-cap="TTA 시험인증 · 회전형 카메라 — SL-P510ID5"><img src="../assets/cert/tta-510-t.jpg" alt="TTA 시험인증 · 회전형 카메라 — SL-P510ID5" loading="lazy" width="600" height="800"></button><figcaption><span class="tag tag-tta">TTA</span><h3>TTA 시험인증 · 회전형 카메라</h3><p class="model">SL-P510ID5</p><dl><div><dt>인증기관</dt><dd>한국정보통신기술협회</dd></div><div><dt>구분</dt><dd>TTA 인증서</dd></div></dl></figcaption></figure><figure class="cert" data-cat="eco" data-reveal><button class="cert-img" type="button" data-full="../assets/cert/eco.jpg" data-cap="환경표지 인증 · LED 전광판 — EL265"><img src="../assets/cert/eco-t.jpg" alt="환경표지 인증 · LED 전광판 — EL265" loading="lazy" width="600" height="800"></button><figcaption><span class="tag tag-eco">환경표지</span><h3>환경표지 인증 · LED 전광판</h3><p class="model">EL265</p><dl><div><dt>인증번호</dt><dd>제 31489 호</dd></div><div><dt>인증기간</dt><dd>2024.08.29 ~ 2027.05.26</dd></div><div><dt>인증기관</dt><dd>한국환경산업기술원</dd></div></dl></figcaption></figure><figure class="cert" data-cat="rel" data-reveal><button class="cert-img" type="button" data-full="../assets/cert/rel-bit.jpg" data-cap="BIT 신뢰성 시험성적서 — SL-BIT-BS"><img src="../assets/cert/rel-bit-t.jpg" alt="BIT 신뢰성 시험성적서 — SL-BIT-BS" loading="lazy" width="600" height="800"></button><figcaption><span class="tag tag-rel">시험성적</span><h3>BIT 신뢰성 시험성적서</h3><p class="model">SL-BIT-BS</p><dl><div><dt>성적서번호</dt><dd>KR0140-2024-11_3842</dd></div><div><dt>구분</dt><dd>신뢰성 TRF</dd></div></dl></figcaption></figure><figure class="cert" data-cat="rel" data-reveal><button class="cert-img" type="button" data-full="../assets/cert/pwr-evs.jpg" data-cap="긴급차량 전광판 소비전력 성적서 — EVS 전광판"><img src="../assets/cert/pwr-evs-t.jpg" alt="긴급차량 전광판 소비전력 성적서 — EVS 전광판" loading="lazy" width="600" height="800"></button><figcaption><span class="tag tag-rel">시험성적</span><h3>긴급차량 전광판 소비전력 성적서</h3><p class="model">EVS 전광판</p><dl><div><dt>구분</dt><dd>소비전력 시험성적서</dd></div></dl></figcaption></figure></div>\n\n<div class="lead-box" data-reveal style="margin-top:56px;margin-bottom:0">\n<p><strong>KC 적합등록</strong>은 「전파법」 제58조의2 제3항에 따라 국립전파연구원에 등록된 것으로,\n방송통신기자재의 전자파적합성을 인증받았음을 의미합니다.\n인증서 이미지를 클릭하면 원본 크기로 확인할 수 있습니다.</p></div>\n</div></section>\n\n<div class="lb" id="lb">\n  <button class="lb-x" type="button" aria-label="닫기">\n    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M18 6L6 18M6 6l12 12"/></svg></button>\n  <button class="lb-nav lb-prev" type="button" aria-label="이전">\n    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M15 18l-6-6 6-6"/></svg></button>\n  <button class="lb-nav lb-next" type="button" aria-label="다음">\n    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M9 18l6-6-6-6"/></svg></button>\n  <img alt="">\n  <div class="lb-cap"></div>\n</div>'
DIRECT_TPL = """

<section class="section band"><div class="area-box">
<div class="section-head" data-reveal><span class="eyebrow" style="color:var(--c-accent-bright)">DIRECT PRODUCTION</span>
<h2>직접생산확인증명서</h2>
<p class="lead">중소벤처기업부 직접생산 확인 품목 %(n)d개 분야 — 자체 생산·개발 역량을 공인받았습니다.</p></div>
<ul class="dp-grid" id="dpGrid">%(items)s</ul>
</div></section>

<section class="section"><div class="area">
<div class="section-head" data-reveal><span class="eyebrow">CREDENTIALS</span><h2>제안사 신인도</h2></div>
<div class="cred" data-reveal-stagger="90">
  <div class="cred-i" data-reveal><b data-count="4">0</b><span>특허증</span></div>
  <div class="cred-i" data-reveal><b data-count="2">0</b><span>ISO 인증</span></div>
  <div class="cred-i" data-reveal><b>보유</b><span>기업부설연구소</span></div>
  <div class="cred-i" data-reveal><b>보유</b><span>TTA 인증서</span></div>
  <div class="cred-i" data-reveal><b>보유</b><span>벤처기업 확인서</span></div>
  <div class="cred-i" data-reveal><b>외 14</b><span>기타 인증</span></div>
</div>
</div></section>"""


# ---------- 직접생산확인증명서 (인증현황 하단에 추가) ----------
# 출처: 일반현황 상림.pptx — 기술능력(주사업자) / 직접생산확인증명서
DIRECT = [
 ("시스템 관리",            "운영위탁 서비스 · 정보시스템 유지관리 서비스"),
 ("컴퓨터",                 "버스 및 차량정보 안내장치"),
 ("표식 장비",              "안내 전광판 · 교통정보 전광판 · 기상 전광판"),
 ("소프트웨어 엔지니어링",  "패키지 소프트웨어 개발 및 도입 서비스 · 정보시스템 개발 서비스"),
 ("소프트웨어 유지 및 지원", "소프트웨어 유지 및 지원 서비스"),
 ("복합영상장비 · 콘트롤러", "영상정보 디스플레이 장치"),
 ("인터넷 서비스",          "인터넷 지원 개발 서비스"),
 ("데이터 서비스",          "빅데이터 분석 서비스"),
 ("경영정보 시스템",        "정보 인프라 구축 서비스"),
]
_dp = "".join(
    '<li class="dp" data-reveal style="--td:%dms"><b>%s</b><span>%s</span></li>' % (i * 60, a, b)
    for i, (a, b) in enumerate(DIRECT))

cert += DIRECT_TPL % dict(items=_dp, n=len(DIRECT))


PAGES.append(("company/certification.html", "인증현황", "상림기술 보유 인증 현황입니다.", "company", cert))

LOC_TPL = """<section class="section"><div class="area">
%(head)s

<div class="map-wrap" data-reveal>
  <iframe class="map-frame" title="(주)상림기술 위치 지도"
          src="https://www.google.com/maps?q=%(q)s&hl=ko&z=17&output=embed"
          loading="lazy" referrerpolicy="no-referrer-when-downgrade"
          allowfullscreen></iframe>
  <div class="map-card">
    <span class="map-eyebrow">HEAD OFFICE</span>
    <b>%(company)s</b>
    <p>%(addr)s</p>
    <div class="map-links">
      <a href="https://map.kakao.com/?q=%(q)s" target="_blank" rel="noopener">카카오맵</a>
      <a href="https://map.naver.com/p/search/%(q)s" target="_blank" rel="noopener">네이버지도</a>
      <a href="https://www.google.com/maps/search/?api=1&query=%(q)s" target="_blank" rel="noopener">구글지도</a>
    </div>
  </div>
</div>

%(dl)s

<div class="way" data-reveal-stagger="110">
  <article class="way-i" data-reveal>
    <span class="way-ic way-sub">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round">
        <rect x="5" y="3" width="14" height="14" rx="4"/><path d="M5 10h14M8 20l-1.5 2M16 20l1.5 2"/>
        <circle cx="8.5" cy="13.5" r="1"/><circle cx="15.5" cy="13.5" r="1"/></svg></span>
    <h3>지하철</h3>
    <p><b>1호선 석수역</b> 하차 후 마을버스 환승<br>
    <b>7호선 철산역</b> 에서 버스 환승</p>
  </article>
  <article class="way-i" data-reveal>
    <span class="way-ic way-bus">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round">
        <rect x="3" y="4" width="18" height="13" rx="3"/><path d="M3 11h18M7 21v-2M17 21v-2"/>
        <circle cx="7" cy="14.5" r="1"/><circle cx="17" cy="14.5" r="1"/></svg></span>
    <h3>버스</h3>
    <p><b>광명 SK테크노파크</b> 정류장 하차<br>
    소하동·하안로 경유 노선 이용</p>
  </article>
  <article class="way-i" data-reveal>
    <span class="way-ic way-car">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round">
        <path d="M4 15l1.4-5A3 3 0 0 1 8.3 8h7.4a3 3 0 0 1 2.9 2l1.4 5"/>
        <rect x="3" y="15" width="18" height="5" rx="2"/><circle cx="7.5" cy="17.5" r="1"/><circle cx="16.5" cy="17.5" r="1"/></svg></span>
    <h3>자가용</h3>
    <p><b>서해안고속도로 소하 IC</b> 인근<br>
    내비게이션에 <b>광명 SK테크노파크</b> 입력</p>
  </article>
</div>
</div></section>"""


# ---------- 회사소개 / 오시는 길 ----------
from urllib.parse import quote as _q
loc = LOC_TPL % dict(
    head=head("LOCATION", "오시는 길", "본사와 공장이 광명 SK테크노파크 같은 건물에 위치합니다."),
    q=_q("경기도 광명시 하안로 60 광명 SK테크노파크"),
    company=COMPANY, addr=ADDR_HQ,
    dl=dl([
      ("본사", ADDR_HQ),
      ("공장", ADDR_FT),
      ("대표전화", '<a href="tel:0220831333">%s</a>' % TEL),
      ("이메일", '<a href="mailto:%s">%s</a>' % (MAIL, MAIL)),
    ]))
PAGES.append(("company/location.html", "오시는 길",
              "%s 본사·공장 위치 및 교통편 안내." % COMPANY, "company", loc))

# ---------- 사업분야 ----------
# 지능형교통체계(ITS) 페이지 전용 데이터·컴포넌트.
#  자료 근거: 국토교통부 ITS 정책자료 / 지능형교통체계 기본계획 2030(국토교통부, 2021)
#  이미지는 외부에서 가져오지 않고 전부 인라인 SVG 로 직접 그렸습니다.
import io

FLOW = [
  ("01", "수집", "COLLECT",
   "도로 위 장비가 차량의 존재·속도·번호·영상을 초 단위로 읽어들입니다.",
   ["VDS 차량검지기", "AVI 차량번호인식", "CCTV 영상검지", "GNSS 프로브"]),
  ("02", "가공", "PROCESS",
   "센터로 모인 원시 데이터를 AI 딥러닝으로 정제해 소통상태·돌발상황·예측 통행시간으로 바꿉니다.",
   ["교통량·점유율 산출", "돌발상황 자동판정", "구간 통행시간 예측", "이력 데이터 축적"]),
  ("03", "제공", "PROVIDE",
   "가공된 정보를 운전자와 시민이 바로 쓸 수 있는 형태로 현장과 단말에 내보냅니다.",
   ["VMS 도로전광판", "BIT 버스정보안내", "신호제어 연동", "개방 API·앱"]),
]

SERVICES7 = [
  ("교통관리", "신호·돌발·단속을 하나의 체계로 운영"),
  ("대중교통", "버스 위치와 도착시간을 시민에게 전달"),
  ("전자지불", "정차 없이 통행료·요금을 처리"),
  ("교통정보 유통", "수집한 정보를 기관·민간과 나눠 씀"),
  ("부가정보 제공", "주차·기상·관광 등 생활정보 연계"),
  ("지능형 차량·도로", "차량과 도로가 통신으로 협력"),
  ("화물운송", "화물·위험물 차량의 안전과 효율 관리"),
]

CITS_CMP = [
  ("정보의 흐름", "센터가 모아서 내려주는 <b>단방향</b>", "차량·인프라가 주고받는 <b>양방향</b>"),
  ("정보의 출처", "노변 검지기·CCTV 등 기반시설", "기반시설 + <b>주행 중인 차량 자체</b>"),
  ("전달 시점", "수집·가공을 거친 뒤 (지연 존재)", "발생 즉시 (수백 ms 단위)"),
  ("대표 수단", "VMS · BIT · 신호제어",
   'V2V · V2I · V2P · V2N <span class="nw">(WAVE / LTE-V2X)</span>'),
]

POLICY = [
  ("미래 신교통수단의 도입 인프라 구축", "자율주행차·UAM 등 새로운 이동수단이 달릴 수 있는 도로 기반을 먼저 깝니다."),
  ("첨단기술로 교통안전 사각지대 해소", "AI 영상분석으로 보행자·이륜차 등 그동안 잡히지 않던 위험을 검지합니다."),
  ("이용자 맞춤형 서비스 제공 기반 마련", "수집한 교통 데이터를 개방해 민간 서비스로 확장되도록 합니다."),
  ("국내 지능형교통체계의 해외진출 지원", "국내에서 검증된 ITS 기술을 수출 산업으로 키웁니다."),
]


# ── 버스정보 안내시스템(BIS) 페이지 데이터 ────────────────────────────
BIS_TV = [
  ("Live Tracking", "실시간 위치 파악", "hub",
   "운행 중인 버스의 위치를 GPS로 초 단위로 읽고 LTE로 센터에 올립니다. "
   "정류장 통과와 노선 이탈까지 자동으로 판정합니다."),
  ("Arrival Prediction", "도착시간 예측", "eye",
   "현재 위치만으로는 부족합니다. 구간 소통상태와 과거 운행 이력을 함께 계산해 "
   "'몇 분 뒤 도착'을 산출하고, 상황이 바뀌면 다시 계산합니다."),
  ("Multi-channel", "문자와 음성 동시 안내", "panel",
   "정류장 전광판, 차내 안내기, 음성 안내로 동시에 내보냅니다. "
   "눈으로 보든 귀로 듣든 같은 정보가 닿게 만듭니다."),
  ("Operation Data", "운행 데이터 관리", "shield",
   "배차 간격과 노선 준수율이 데이터로 남습니다. 결행과 지연을 사후에 확인하는 대신 "
   "운행 중에 잡아낼 수 있습니다."),
]

BIS_FLOW = [
  ("01", "수집", "ON BOARD",
   "버스에 실린 단말기가 자기 위치를 초 단위로 읽어 센터로 올립니다.",
   ["GPS 측위", "LTE 전송", "정류장 통과 판정", "노선 매칭"]),
  ("02", "예측", "CENTER",
   "위치·구간 소통상태·과거 운행 이력을 합쳐 도착 예정시간을 계산합니다.",
   ["구간 소요시간", "이력 데이터", "혼잡 반영", "주기적 재계산"]),
  ("03", "안내", "AT THE STOP",
   "정류장과 차내, 앱으로 같은 정보를 동시에 내보냅니다.",
   ["BIT 전광판", "차내 안내기", "TTS 음성", "개방 API"]),
]

BIS_SPEC = [
  ("고휘도 LED 표출", "야외 직사광선 아래에서도 읽히도록 고휘도 LED를 씁니다. "
   "노선번호·도착예정시간·현재통과위치를 한 화면에 담습니다."),
  ("문자와 음성 동시 안내", "표출과 함께 음성으로도 안내해, 시각에 의존하지 않고도 "
   "버스 정보를 받을 수 있습니다."),
  ("정류장 규모별 라인업", "SL-BIT-TRI · 3D8Y · 4D12Y 등 노선 수와 정류장 규모에 맞춰 "
   "표출 단수와 크기를 고를 수 있습니다."),
  ("옥외 환경 전제 설계", "혹서·혹한과 진동, 낙뢰가 있는 옥외를 전제로 설계하고 "
   "설치 이후 점검과 유지보수까지 제조사가 직접 대응합니다."),
]


# ── TECH VISION — 좌측 다크 스테이트먼트 패널 + 우측 2x2 번호 카드 ─────
#    (레이아웃 구성 방식만 참고했고, 문구·아이콘·그래픽은 전부 새로 만들었습니다)
TV_CARDS = [
  ("AI Detection", "AI 영상 검지", "eye",
   "딥러닝 영상분석으로 차량은 물론 보행자·이륜차까지 검지하고, "
   "교통량·속도·점유율을 초 단위로 산출해 도로의 상태를 숫자로 바꿉니다."),
  ("Unified Display", "통합 표출", "panel",
   "VMS 도로전광판부터 BIT 버스정보안내기, 충전소 전광판까지 표출 장비를 "
   "직접 설계·제조합니다. 현장 조건에 맞춰 크기와 표출 방식을 바꿀 수 있습니다."),
  ("Center Integration", "센터 연동", "hub",
   "수집한 정보를 관제 상황판과 기관 시스템에 연계합니다. 한 화면에서 "
   "전 구간을 감시하고, 돌발상황이 잡히면 곧바로 대응 절차로 이어집니다."),
  ("Field Reliability", "현장 신뢰성", "shield",
   "혹서·혹한과 진동, 낙뢰가 있는 옥외 환경을 전제로 설계합니다. "
   "설치 이후의 점검과 유지보수까지 제조사가 직접 대응합니다."),
]

TV_ICON = {
 # 옅은 면(뒤) + 진한 면(앞) 두 겹으로 입체감을 냅니다. 색은 타일의 color 를 따릅니다.
 "eye": '<path d="M3 9.1V6.4A3.4 3.4 0 016.4 3h2.7" fill="none" stroke="currentColor" '
        'stroke-width="1.9" stroke-linecap="round" opacity=".45"/>'
        '<path d="M14.9 3h2.7A3.4 3.4 0 0121 6.4v2.7" fill="none" stroke="currentColor" '
        'stroke-width="1.9" stroke-linecap="round" opacity=".45"/>'
        '<path d="M21 14.9v2.7a3.4 3.4 0 01-3.4 3.4h-2.7" fill="none" stroke="currentColor" '
        'stroke-width="1.9" stroke-linecap="round" opacity=".45"/>'
        '<path d="M9.1 21H6.4A3.4 3.4 0 013 17.6v-2.7" fill="none" stroke="currentColor" '
        'stroke-width="1.9" stroke-linecap="round" opacity=".45"/>'
        '<circle cx="12" cy="12" r="5.3" opacity=".3"/><circle cx="12" cy="12" r="2.6"/>',
 "panel": '<rect x="2.4" y="4" width="19.2" height="12.4" rx="2.4" opacity=".3"/>'
          '<rect x="5.2" y="6.6" width="13.6" height="4.6" rx="1.2"/>'
          '<rect x="5.2" y="12.6" width="7.6" height="1.7" rx=".85" opacity=".75"/>'
          '<path d="M11.1 16.4h1.8v3.1h-1.8z"/><rect x="7.6" y="19.2" width="8.8" height="1.8" rx=".9"/>',
 "hub": '<circle cx="12" cy="12" r="3.2"/>'
        '<circle cx="4.4" cy="5.4" r="2.2" opacity=".38"/><circle cx="19.6" cy="5.4" r="2.2" opacity=".38"/>'
        '<circle cx="4.4" cy="18.6" r="2.2" opacity=".38"/><circle cx="19.6" cy="18.6" r="2.2" opacity=".38"/>'
        '<path d="M6.2 6.9l3.4 3M17.8 6.9l-3.4 3M6.2 17.1l3.4-3M17.8 17.1l-3.4-3" fill="none" '
        'stroke="currentColor" stroke-width="1.7" stroke-linecap="round" opacity=".5"/>',
 "siren": '<path d="M3.6 20.4h16.8a1.3 1.3 0 011.3 1.3H2.3a1.3 1.3 0 011.3-1.3z"/>'
          '<path d="M5.4 19.1v-6.3a6.6 6.6 0 1113.2 0v6.3z" opacity=".3"/>'
          '<path d="M12 6.2a6.6 6.6 0 00-6.6 6.6v2.1h13.2v-2.1A6.6 6.6 0 0012 6.2z"/>'
          '<path d="M12 1.3v2.3M4.1 4.4l1.6 1.6M19.9 4.4l-1.6 1.6" fill="none" stroke="currentColor" '
          'stroke-width="1.9" stroke-linecap="round" opacity=".5"/>',
 "shield": '<path d="M12 2.3l8.4 3.5v5.9c0 5.3-3.7 8.5-8.4 10.3-4.7-1.8-8.4-5-8.4-10.3V5.8z" opacity=".3"/>'
           '<path d="M7.9 12.1l2.9 2.9 5.3-5.6" fill="none" stroke="currentColor" stroke-width="2.2" '
           'stroke-linecap="round" stroke-linejoin="round"/>',
}


TV_ART = '''<span class="tv-art" aria-hidden="true">
<svg viewBox="0 0 420 520" preserveAspectRatio="xMaxYMax slice">
 <defs>
  <linearGradient id="tvSheet" x1=".08" y1="1" x2=".92" y2=".05">
   <stop offset="0" stop-color="#0A1233"/><stop offset=".38" stop-color="#1E39B4"/>
   <stop offset=".72" stop-color="#4E7CF8"/><stop offset="1" stop-color="#AECBFF"/>
  </linearGradient>
  <linearGradient id="tvEdge" x1="0" y1="1" x2=".7" y2="0">
   <stop offset="0" stop-color="#5C87FF" stop-opacity="0"/>
   <stop offset=".55" stop-color="#B9D2FF" stop-opacity=".95"/>
   <stop offset="1" stop-color="#F2F7FF"/>
  </linearGradient>
  <linearGradient id="tvFacet" x1="0" y1="0" x2="1" y2="1">
   <stop offset="0" stop-color="#E8F1FF" stop-opacity=".92"/>
   <stop offset="1" stop-color="#3C63E8" stop-opacity="0"/>
  </linearGradient>
  <linearGradient id="tvBack" x1="0" y1="0" x2="1" y2="1">
   <stop offset="0" stop-color="#16246B" stop-opacity=".0"/>
   <stop offset="1" stop-color="#2A4BD8" stop-opacity=".85"/>
  </linearGradient>
  <filter id="tvSoft" x="-40%" y="-40%" width="180%" height="180%">
   <feGaussianBlur stdDeviation="34"/></filter>
  <filter id="tvSoft2" x="-30%" y="-30%" width="160%" height="160%">
   <feGaussianBlur stdDeviation="9"/></filter>
 </defs>
 <ellipse cx="330" cy="372" rx="205" ry="215" fill="#2B4CDC" opacity=".62" filter="url(#tvSoft)"/>
 <path d="M64 520 L286 128 L420 196 L420 520 Z" fill="url(#tvSheet)"/>
 <path d="M286 128 L420 196 L420 96 Z" fill="url(#tvBack)"/>
 <path d="M64 520 L286 128 L306 139 L92 520 Z" fill="url(#tvEdge)" filter="url(#tvSoft2)" opacity=".9"/>
 <path d="M286 128 L306 139 L420 205 L420 196 Z" fill="url(#tvFacet)" opacity=".8"/>
 <path d="M188 520 L338 254 L420 296 L420 520 Z" fill="#7FA6FF" opacity=".16"/>
</svg></span>'''


def techvision(eyebrow, title_lines, body_paras, cards=None):
    cards = cards or TV_CARDS
    h = "".join('<span>%s</span>' % t for t in title_lines)
    b = "".join('<p>%s</p>' % t for t in body_paras)
    out = []
    for i, c in enumerate(cards):
        en, ko, ic, desc = c[0], c[1], c[2], c[3]
        href = c[4] if len(c) > 4 else None      # 있으면 카드 전체가 링크가 됩니다
        tag = ('a class="tv-card is-link" href="%s" data-cursor="%s"' % (href, "자세히" if LANG == "ko" else "More")
               if href else 'article class="tv-card"')
        out.append(
          '<%s data-reveal style="--td:%dms">'
          '<span class="tv-n">%02d</span>'
          '<span class="tv-ico"><svg viewBox="0 0 24 24" fill="currentColor">%s</svg></span>'
          '<h3>%s</h3><b>%s</b><p>%s</p>%s</%s>'
          % (tag, i * 110, i + 1, TV_ICON[ic], en, ko, desc,
             '<span class="tv-go">' + _ARROW + '</span>' if href else '',
             'a' if href else 'article'))
    # TV_ART 안에 %(퍼센트) 문자가 있어 %-포맷과 섞으면 깨집니다. 포맷을 먼저 끝내고 붙입니다.
    txt = ('<span class="tv-eyebrow">%s</span><h2 class="tv-title">%s</h2>'
           '<div class="tv-body">%s</div>') % (eyebrow, h, b)
    return ('<div class="tv"><aside class="tv-panel" data-reveal>' + TV_ART + txt +
            '</aside><div class="tv-grid">' + "".join(out) + '</div></div>')


def its_flow(rows=None):
    """수집 → 가공 → 제공. 사이 연결선 위로 데이터 패킷이 흐릅니다."""
    ico = {
      "01": '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round">'
            '<path d="M6 34V20a4 4 0 014-4h6l3-5h10l3 5h6a4 4 0 014 4v14"/>'
            '<circle cx="24" cy="26" r="7"/><path d="M6 34h36"/></svg>',
      "02": '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round">'
            '<rect x="16" y="16" width="16" height="16" rx="3"/>'
            '<path d="M24 6v10M24 32v10M6 24h10M32 24h10M11 11l7 7M30 30l7 7M37 11l-7 7M18 30l-7 7"/></svg>',
      "03": '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round">'
            '<rect x="7" y="12" width="34" height="20" rx="3"/><path d="M14 20h12M14 26h20M24 32v8M16 40h16"/></svg>',
    }
    out = []
    for i, (no, ko, en, desc, tags) in enumerate(rows or FLOW):
        if i:
            out.append('<div class="flow-link" aria-hidden="true"><i></i><i></i><i></i></div>')
        li = "".join('<li>%s</li>' % t for t in tags)
        out.append(
          '<article class="flow-step" data-reveal style="--td:%dms">'
          '<span class="fs-no">%s</span>'
          '<span class="fs-ico">%s</span>'
          '<span class="fs-en">%s</span><h3>%s</h3><p>%s</p>'
          '<ul class="fs-tags">%s</ul></article>' % (i * 140, no, ico[no], en, ko, desc, li))
    return '<div class="flow">%s</div>' % "".join(out)


def its_services(rows=None):
    out = "".join(
      '<article class="svc7" data-reveal style="--td:%dms"><span class="n">%02d</span>'
      '<h3>%s</h3><p>%s</p></article>' % (i * 80, i + 1, a, b)
      for i, (a, b) in enumerate(rows or SERVICES7))
    return '<div class="svc7-grid">%s</div>' % out


# 보행자 픽토그램.
#   상림기술에서 제공한 보행자.svg 에서 배경 흰 사각형을 빼고 형상만 가져왔습니다.
#   원본 캔버스 3500×3500, 형상 바운딩박스 중심 (1750.7, 1750.2), 형상 높이 2936.3.
#   따라서 원하는 높이 h 로 쓰려면 배율 = h / 2936.3 입니다.
PED_BODY = ('<path d="M1924.29,1406.23c0,143.57.25,287.13-.28,430.7-.08,20.62,5.23,37.68,17.37,54.49,211.61,293.03,422.96,586.24,633.67,879.91,12.61,17.57,19.83,19.81,38.05,6.46,46.49-34.07,99.68-24.2,124.23,20.1,17.07,30.82,10.73,59.47-18.69,78.95-67.65,44.77-135.31,89.56-203.58,133.38-52.81,33.89-100.91,26.63-139.1-23.87-76.34-100.95-150.74-203.37-225.86-305.25-197.25-267.52-396.55-533.51-604.43-792.89-34.96-43.62-50.78-88.86-49.87-145.04,2.52-155.72.86-311.5.32-467.26-.05-13.5,3.1-21.8,15.56-28.99,75.61-43.6,150.65-88.16,225.89-132.4.58-.34,1.15-.72,1.74-1.05,28.55-16,38.15-36.77,26.36-57.03-12.11-20.81-33.28-21.88-62.08-4.9-125.87,74.2-251.86,148.21-378.15,221.69-12.64,7.35-20.17,15.88-24.17,30.01-37.55,132.54-76.05,264.8-113.42,397.38-14.64,51.94-42.05,90.9-97.55,102.77-85.24,18.24-161.44-59.44-139.15-143.86,25.37-96.08,54.05-191.3,81.64-286.79,17.26-59.75,35.21-119.3,52.79-178.95,15.09-51.23,46.56-89.35,92.32-116.28,145.22-85.43,290.53-170.71,435.49-256.57,55.51-32.88,113.5-46.21,176.84-28.08,78.73,22.55,135.03,98.71,135.02,182.7-.02,143.57,0,287.13,0,430.7-.31,0-.62,0-.94,0Z"/><path d="M1746.23,3217.77c-394.82,0-789.64-.47-1184.46.54-55.2.14-94.32-50.99-77.19-97.15,9.28-25.01,25.85-42.81,53.86-46.29,12.72-1.58,25.58-2.81,38.38-2.81,629.81-.12,1259.62-.09,1889.43-.08,155.76,0,311.52.08,467.28-.12,26.87-.03,51.64,5.53,69.41,26.94,18.15,21.89,23.65,46.98,11.14,73.81-13.21,28.33-36.4,43.87-67.15,44.69-48.05,1.29-96.15.45-144.23.45-352.15.01-704.31,0-1056.46,0Z"/><path d="M1453.32,1884.31c72.61,93.38,142.92,184.37,214.1,274.68,9.79,12.42,1.96,18.64-3.43,27.48-51.39,84.26-102.11,169.19-161.88,247.7-79.03,103.81-162.13,204.53-242.93,307-61.54,78.05-122.5,156.57-183.16,235.31-20.09,26.08-42.59,47.25-77.22,50.24-24.69,2.13-45.04-7.71-62.21-24.41-31.52-30.67-62.97-61.43-93.8-92.79-33.32-33.9-39.44-78.12-11.06-116.24,35.9-48.24,75.86-93.46,114.23-139.85,83.67-101.16,165.44-204,251.91-302.71,54.26-61.94,84.59-136.19,121.7-207.13,44.47-85,85.9-171.59,133.76-259.28Z"/><path d="M1997.41,1057.09c10.4,19.3,20.99,38.5,31.18,57.92,39.93,76.08,80.4,151.88,119.08,228.58,9.17,18.18,23.01,21.76,39.93,25.14,120.58,24.11,241.15,48.31,361.55,73.3,49.56,10.29,81.68,41.67,95.14,89.87,12.15,43.51-.91,82.13-32.98,112.9-29.06,27.88-65.12,38.68-104.88,30.76-127.24-25.34-254.31-51.52-381.45-77.33-37.06-7.52-73.96-16.29-111.33-21.69-17.39-2.51-20.18-10.09-20.12-24.95.51-120.54.52-241.09.65-361.63.05-43.83,0-87.66,0-131.5,1.08-.46,2.15-.91,3.23-1.37Z"/><path d="M1577.6,504.74c.24-123.87,96.03-220.66,216.33-222.66,135.87-2.26,227.37,104.58,228.93,221.41,1.62,121.62-102.75,223.39-226.59,222.69-119.33-.67-218.9-101.5-218.67-221.44Z"/>')


def pedfig(h):
    """다이어그램 좌표계 원점에 중심을 맞춘 보행자 픽토그램."""
    return ('<g class="pedfig" transform="scale(%.6f) translate(-1750.7,-1750.2)">%s</g>'
            % (h / 2936.3, PED_BODY))


def cits_viz(L=None):
    """C-ITS V2X 개념도 — 차량·노변장치·보행자·센터가 서로 신호를 주고받습니다.

    아이콘은 Lucide 아이콘 세트(ISC 라이선스, 상업적 이용·수정 자유)의 도형을
    가져와 다이어그램 좌표계에 맞게 배치했습니다. 저작권 문제가 없는 소스입니다.
      · 보행자     person-standing
      · 차량       car
      · 노변기지국  radio-tower
      · 관제센터    monitor + 대시보드 패널(직접 구성)
    선 굵기는 확대 배율(--s)로 나눠 어느 아이콘이든 같은 두께로 보이게 합니다.
    """
    L = L or dict(alt="C-ITS V2X 통신 개념도 — 차량 간, 차량과 노변장치, 보행자, 관제센터가 "
                      "서로 정보를 주고받습니다",
                  center="관제센터", rsu="노변기지국 RSU", carA="차량 A", carB="차량 B", ped="보행자",
                  cap="차량·도로·보행자·센터가 서로 정보를 주고받는 <b>C-ITS</b> 구조. "
                      "기존 ITS가 센터에서 내려주는 단방향이라면, C-ITS는 위험을 <b>발생 즉시</b> 서로에게 알립니다.")
    return '''<figure class="v2x" data-reveal>
<svg viewBox="0 0 720 344" role="img" aria-label="%(alt)s">
  <defs>
    <linearGradient id="v2xRoad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#1b2550"/><stop offset="1" stop-color="#0b1024"/>
    </linearGradient>
    <radialGradient id="v2xGlow"><stop offset="0" stop-color="#5B78E0" stop-opacity=".55"/>
      <stop offset="1" stop-color="#5B78E0" stop-opacity="0"/></radialGradient>
  </defs>

  <rect x="0" y="196" width="720" height="148" fill="url(#v2xRoad)"/>
  <line class="v2x-lane" x1="0" y1="256" x2="720" y2="256"/>

  <!-- 관제센터 -->
  <g class="v2x-node" transform="translate(600,46)">
    <circle class="v2x-halo" r="36"/>
    <g class="v2x-ico" style="--s:2.15" transform="scale(2.15) translate(-12,-12)">
      <rect x="2" y="3" width="20" height="14" rx="2"/>
      <path d="M12 17v4"/><path d="M8 21h8"/>
      <rect x="5" y="6" width="6.2" height="4.4" rx="1"/>
      <rect x="12.8" y="6" width="6.2" height="2.2" rx="1"/>
      <rect x="12.8" y="9.8" width="6.2" height="4.6" rx="1"/>
      <rect x="5" y="12.2" width="6.2" height="2.2" rx="1"/>
    </g>
    <text y="52">%(center)s</text>
  </g>

  <!-- 노변기지국(RSU) : 안테나 호가 순서대로 밝아지며 전파를 표현합니다 -->
  <g class="v2x-node" transform="translate(300,88)">
    <circle class="v2x-halo" r="34"/>
    <g class="v2x-ico" style="--s:2.1" transform="scale(2.1) translate(-12,-12)">
      <path class="v2x-sig s2" d="M4.9 16.1C1 12.2 1 5.8 4.9 1.9"/>
      <path class="v2x-sig s1" d="M7.8 4.7a6.14 6.14 0 0 0-.8 7.5"/>
      <circle cx="12" cy="9" r="2"/>
      <path class="v2x-sig s1" d="M16.2 4.8c2 2 2.26 5.11.8 7.47"/>
      <path class="v2x-sig s2" d="M19.1 1.9a9.96 9.96 0 0 1 0 14.1"/>
      <path d="M9.5 18h5"/><path d="m8 22 4-11 4 11"/>
    </g>
    <text y="48">%(rsu)s</text>
  </g>

  <!-- 차량 A -->
  <g class="v2x-node v2x-car" transform="translate(150,272)">
    <circle class="v2x-halo" r="34"/>
    <g class="v2x-ico" style="--s:2.4" transform="scale(2.4) translate(-12,-12)">
      <path d="M19 17h2c.6 0 1-.4 1-1v-3c0-.9-.7-1.7-1.5-1.9C18.7 10.6 16 10 16 10s-1.3-1.4-2.2-2.3c-.5-.4-1.1-.7-1.8-.7H5c-.6 0-1.1.4-1.4.9l-1.4 2.9A3.7 3.7 0 0 0 2 12v4c0 .6.4 1 1 1h2"/>
      <circle cx="7" cy="17" r="2"/><path d="M9 17h6"/><circle cx="17" cy="17" r="2"/>
    </g>
    <text y="40">%(carA)s</text>
  </g>

  <!-- 차량 B -->
  <g class="v2x-node v2x-car" transform="translate(470,272)">
    <circle class="v2x-halo" r="34"/>
    <g class="v2x-ico" style="--s:2.4" transform="scale(2.4) translate(-12,-12)">
      <path d="M19 17h2c.6 0 1-.4 1-1v-3c0-.9-.7-1.7-1.5-1.9C18.7 10.6 16 10 16 10s-1.3-1.4-2.2-2.3c-.5-.4-1.1-.7-1.8-.7H5c-.6 0-1.1.4-1.4.9l-1.4 2.9A3.7 3.7 0 0 0 2 12v4c0 .6.4 1 1 1h2"/>
      <circle cx="7" cy="17" r="2"/><path d="M9 17h6"/><circle cx="17" cy="17" r="2"/>
    </g>
    <text y="40">%(carB)s</text>
  </g>

  <!-- 보행자 -->
  <g class="v2x-node" transform="translate(80,112)">
    <circle class="v2x-halo" r="28"/>
    {PEDFIG44}
    <text y="38">%(ped)s</text>
  </g>

  <g class="v2x-links">
    <path class="v2x-link l1" d="M162 254 C 205 200 250 145 286 104"/>
    <path class="v2x-link l2" d="M316 106 C 380 152 420 210 460 252"/>
    <path class="v2x-link l3" d="M180 286 C 250 312 380 312 440 286"/>
    <path class="v2x-link l4" d="M322 70 C 420 38 520 34 570 44"/>
    <path class="v2x-link l5" d="M102 124 C 156 156 232 130 282 100"/>
  </g>

  <g class="v2x-tag">
    <text x="198" y="180">V2I</text>
    <text x="368" y="192">V2I</text>
    <text x="310" y="334">V2V</text>
    <text x="464" y="26">V2N</text>
    <text x="174" y="118">V2P</text>
  </g>
</svg>
<figcaption>%(cap)s</figcaption>
</figure>'''.replace('{PEDFIG44}', pedfig(44)) % L


def cits_table(rows=None, ha="기존 ITS", hb="C-ITS", tag="차세대"):
    rows = "".join(
      '<div class="cmp-row" data-reveal style="--td:%dms"><span class="k">%s</span>'
      '<span class="a">%s</span><span class="b">%s</span></div>' % (i * 90, k, a, b)
      for i, (k, a, b) in enumerate(rows or CITS_CMP))
    # 좁은 화면에서는 표가 카드로 접히면서 각 값 앞에 열 이름을 붙입니다.
    # 그 이름을 CSS 변수로 넘겨, 페이지마다 다른 머리글을 그대로 쓰게 합니다.
    return ('<div class="cmp" style="--ha:\'%s · \';--hb:\'%s · \'">'
            '<div class="cmp-head" data-reveal>'
            '<span class="k"></span><span class="a">%s</span>'
            '<span class="b">%s <em>%s</em></span></div>%s</div>'
            % (ha, hb, ha, hb, tag, rows))


# ── 긴급차량 우선신호 개념도 ──────────────────────────────────────────
#    출동 → GPS 위치전송 → 통합센터 → 교차로 신호제어기 → 녹색 → 병원
#    아이콘은 Lucide(ISC 라이선스) 도형을 좌표계에 맞춰 배치했습니다.
def evs_viz(L=None):
    L = L or dict(
      alt="긴급차량 우선신호 개념도 — 출동한 긴급차량의 GPS 위치를 통합센터가 추적해 "
          "진입할 교차로의 신호를 미리 녹색으로 바꿉니다",
      car="긴급차량 출동", sat="GPS 위치전송", ctr="도시안전 통합센터",
      s1="교차로 ①", s2="교차로 ②", hos="병원 도착",
      t1="위치 수신", t2="신호 제어", t3="접근 안내",
      cap="출동한 순간부터 병원 도착까지, 통과할 교차로의 신호가 <b>차량보다 먼저</b> 준비됩니다. "
          "일반 차량에는 전광판으로 접근을 알려 길을 열어 줍니다.")
    return '''<figure class="evsv" data-reveal>
<svg viewBox="0 0 720 404" role="img" aria-label="%(alt)s">
  <defs>
    <linearGradient id="evsRoad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#1b2550"/><stop offset="1" stop-color="#0b1024"/>
    </linearGradient>
    <radialGradient id="evsGlow"><stop offset="0" stop-color="#5B78E0" stop-opacity=".5"/>
      <stop offset="1" stop-color="#5B78E0" stop-opacity="0"/></radialGradient>
    <radialGradient id="evsRed"><stop offset="0" stop-color="#FF5A5A" stop-opacity=".6"/>
      <stop offset="1" stop-color="#FF5A5A" stop-opacity="0"/></radialGradient>
  </defs>

  <!-- 도로 · 교차로 -->
  <rect x="0" y="236" width="720" height="168" fill="url(#evsRoad)"/>
  <line class="evsv-lane" x1="0" y1="304" x2="720" y2="304"/>
  <g class="evsv-stop">
    <path d="M272 236v168M324 236v168M472 236v168M524 236v168"/>
  </g>
  <!-- 차량이 지나갈 길이 앞서 열리는 진행선 — 주행 차로(중앙선 아래) 안에 둡니다 -->
  <path class="evsv-run" d="M156 340H608"/>

  <!-- 통과한 교차로가 순서대로 녹색으로 열립니다 -->
  <rect class="evsv-open o1" x="272" y="236" width="52" height="168"/>
  <rect class="evsv-open o2" x="472" y="236" width="52" height="168"/>

  <!-- 긴급차량 -->
  <g class="evsv-node evsv-car" transform="translate(112,344)">
    <circle class="evsv-halo is-red" r="40"/>
    <g class="evsv-ico" style="--s:2.3" transform="scale(2.3) translate(-12,-12)">
      <path d="M10 10H6"/>
      <path d="M14 18V6a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v11a1 1 0 0 0 1 1h2"/>
      <path d="M19 18h2a1 1 0 0 0 1-1v-3.28a1 1 0 0 0-.684-.948l-1.923-.641a1 1 0 0 1-.578-.502l-1.539-3.076A1 1 0 0 0 16.382 8H14"/>
      <path d="M8 8v4"/><path d="M9 18h6"/>
      <circle cx="17" cy="18" r="2"/><circle cx="7" cy="18" r="2"/>
    </g>
    <text y="46">%(car)s</text>
  </g>

  <!-- GPS 위성 -->
  <g class="evsv-node" transform="translate(214,74)">
    <circle class="evsv-halo" r="34"/>
    <g class="evsv-ico" style="--s:2" transform="scale(2) translate(-12,-12)">
      <path d="m13.5 6.5-3.148-3.148a1.205 1.205 0 0 0-1.704 0L6.352 5.648a1.205 1.205 0 0 0 0 1.704L9.5 10.5"/>
      <path d="M16.5 7.5 19 5"/>
      <path d="m17.5 10.5 3.148 3.148a1.205 1.205 0 0 1 0 1.704l-2.296 2.296a1.205 1.205 0 0 1-1.704 0L13.5 14.5"/>
      <path class="evsv-sig" d="M9 21a6 6 0 0 0-6-6"/>
      <path d="M9.352 10.648a1.205 1.205 0 0 0 0 1.704l2.296 2.296a1.205 1.205 0 0 0 1.704 0l4.296-4.296a1.205 1.205 0 0 0 0-1.704l-2.296-2.296a1.205 1.205 0 0 0-1.704 0z"/>
    </g>
    <text y="44">%(sat)s</text>
  </g>

  <!-- 통합센터 -->
  <g class="evsv-node" transform="translate(468,68)">
    <circle class="evsv-halo" r="36"/>
    <g class="evsv-ico" style="--s:2.15" transform="scale(2.15) translate(-12,-12)">
      <rect x="2" y="3" width="20" height="14" rx="2"/>
      <path d="M12 17v4"/><path d="M8 21h8"/>
      <rect x="5" y="6" width="6.2" height="4.4" rx="1"/>
      <rect x="12.8" y="6" width="6.2" height="2.2" rx="1"/>
      <rect x="12.8" y="9.8" width="6.2" height="4.6" rx="1"/>
      <rect x="5" y="12.2" width="6.2" height="2.2" rx="1"/>
    </g>
    <text y="-44">%(ctr)s</text>
  </g>

  <!-- 신호등 ① · ② : 빨강이 꺼지고 녹색이 켜집니다 -->
  <g class="evsv-sgl" transform="translate(298,186)">
    <rect class="evsv-box" x="-13" y="-34" width="26" height="60" rx="7"/>
    <path class="evsv-pole" d="M0 26v22"/>
    <circle class="evsv-lamp red r1" cx="0" cy="-21" r="6.6"/>
    <circle class="evsv-lamp amb" cx="0" cy="-4" r="6.6"/>
    <circle class="evsv-lamp grn g1" cx="0" cy="13" r="6.6"/>
    <text y="-46">%(s1)s</text>
  </g>
  <g class="evsv-sgl" transform="translate(498,186)">
    <rect class="evsv-box" x="-13" y="-34" width="26" height="60" rx="7"/>
    <path class="evsv-pole" d="M0 26v22"/>
    <circle class="evsv-lamp red r2" cx="0" cy="-21" r="6.6"/>
    <circle class="evsv-lamp amb" cx="0" cy="-4" r="6.6"/>
    <circle class="evsv-lamp grn g2" cx="0" cy="13" r="6.6"/>
    <text y="-46">%(s2)s</text>
  </g>

  <!-- 병원 -->
  <g class="evsv-node" transform="translate(652,344)">
    <circle class="evsv-halo" r="36"/>
    <g class="evsv-ico" style="--s:2.3" transform="scale(2.3) translate(-12,-12)">
      <path d="M12 7v4"/><path d="M14 9h-4"/>
      <path d="M14 21v-3a2 2 0 0 0-4 0v3"/>
      <path d="M18 11h2a2 2 0 0 1 2 2v6a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2v-9a2 2 0 0 1 2-2h2"/>
      <path d="M18 21V5a2 2 0 0 0-2-2H8a2 2 0 0 0-2 2v16"/>
    </g>
    <text y="46">%(hos)s</text>
  </g>

  <!-- 통신 경로 -->
  <g class="evsv-links">
    <path class="evsv-link l1" d="M138 312 C 162 224 178 142 196 102"/>
    <path class="evsv-link l2" d="M244 66 C 310 44 390 44 434 60"/>
    <path class="evsv-link l3" d="M440 100 C 400 126 342 146 314 158"/>
    <path class="evsv-link l4" d="M496 102 C 500 120 500 140 500 156"/>
  </g>
  <g class="evsv-tag">
    <text x="120" y="186">%(t1)s</text>
    <text x="392" y="164">%(t2)s</text>
    <text x="576" y="124">%(t3)s</text>
  </g>

</svg>
<figcaption>%(cap)s</figcaption>
</figure>''' % L


# ── 스마트 스쿨존 개념도 ────────────────────────────────────────────
#    AI 카메라가 보행자를 잡으면 → 전광판이 즉시 경고 → 운전자가 미리 감속
#    아이콘은 Lucide(ISC 라이선스) 도형을 좌표계에 맞춰 배치했습니다.
def ssz_viz(L=None):
    L = L or dict(
      alt="스마트 스쿨존 개념도 — AI 카메라가 횡단보도의 보행자를 감지하면 "
          "전광판이 즉시 경고를 표출해 운전자가 미리 감속합니다",
      sign="스마트 전광판", cam="AI 영상 검지", ped="보행자 감지",
      spd="제한속도 30", car="접근 차량",
      t1="즉시 표출", warn="보행자<tspan x='0' dy='18'>주의</tspan>",
      cap="카메라가 보행자를 잡는 순간 전광판이 켜집니다. 운전자가 아이를 <b>보기 전에</b> "
          "먼저 알게 만드는 것이 스마트 스쿨존의 핵심입니다.")
    return '''<figure class="sszv" data-reveal>
<svg viewBox="0 0 720 420" role="img" aria-label="%(alt)s">
  <defs>
    <linearGradient id="sszRoad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#1b2550"/><stop offset="1" stop-color="#0b1024"/>
    </linearGradient>
    <radialGradient id="sszGlow"><stop offset="0" stop-color="#5B78E0" stop-opacity=".5"/>
      <stop offset="1" stop-color="#5B78E0" stop-opacity="0"/></radialGradient>
    <radialGradient id="sszWarm"><stop offset="0" stop-color="#FFC24B" stop-opacity=".55"/>
      <stop offset="1" stop-color="#FFC24B" stop-opacity="0"/></radialGradient>
    <linearGradient id="sszBeam" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#8FA4F0" stop-opacity=".34"/>
      <stop offset="1" stop-color="#8FA4F0" stop-opacity="0"/>
    </linearGradient>
  </defs>

  <!-- 도로 · 중앙선 (우측통행 : 왼쪽→오른쪽 주행은 중앙선 아래 차로) -->
  <rect x="0" y="244" width="720" height="176" fill="url(#sszRoad)"/>
  <line class="sszv-lane" x1="0" y1="316" x2="720" y2="316"/>

  <!-- 스쿨존 노면 표시 -->
  <rect class="sszv-zone" x="96" y="244" width="560" height="176"/>

  <!-- 횡단보도 -->
  <g class="sszv-cw">
    <rect x="404" y="248" width="13" height="168"/>
    <rect x="422" y="248" width="13" height="168"/>
    <rect x="440" y="248" width="13" height="168"/>
    <rect x="458" y="248" width="13" height="168"/>
  </g>

  <!-- AI 카메라 검지 영역 -->
  <path class="sszv-beam" d="M300 176 L488 244 L376 244 Z"/>

  <!-- 스마트 전광판 -->
  <g class="sszv-node" transform="translate(120,160)">
    <circle class="sszv-halo is-warm" r="46"/>
    <rect class="sszv-panel" x="-52" y="-34" width="104" height="60" rx="8"/>
    <text class="sszv-warn" y="-11">%(warn)s</text>
    <path class="sszv-pole" d="M0 26v58"/>
    <text y="58">%(sign)s</text>
  </g>

  <!-- AI 카메라 -->
  <g class="sszv-node" transform="translate(300,150)">
    <circle class="sszv-halo" r="34"/>
    <g class="sszv-ico" style="--s:2.1" transform="scale(2.1) translate(-12,-12)">
      <path d="M16.75 12h3.632a1 1 0 0 1 .894 1.447l-2.034 4.069a1 1 0 0 1-1.708.134l-2.124-2.97"/>
      <path d="M17.106 9.053a1 1 0 0 1 .447 1.341l-3.106 6.211a1 1 0 0 1-1.342.447L3.61 12.3a2.92 2.92 0 0 1-1.3-3.91L3.69 5.6a2.92 2.92 0 0 1 3.92-1.3z"/>
      <path d="M2 19h3.76a2 2 0 0 0 1.8-1.1L9 15"/><path d="M2 21v-4"/>
      <circle class="sszv-lens" cx="7" cy="9" r="1.1"/>
    </g>
    <path class="sszv-pole" d="M0 30v64"/>
    <text y="58">%(cam)s</text>
  </g>

  <!-- 제한속도 30 -->
  <g class="sszv-node" transform="translate(602,158)">
    <circle class="sszv-halo" r="34"/>
    <circle class="sszv-spd" cx="0" cy="-6" r="26"/>
    <text class="sszv-spdn" y="4">30</text>
    <path class="sszv-pole" d="M0 22v64"/>
    <text y="52">%(spd)s</text>
  </g>

  <!-- 횡단보도를 건너는 보행자 -->
  <g class="sszv-node sszv-ped" transform="translate(436,282)">
    <circle class="sszv-halo is-warm" r="30"/>
    {PEDFIG40}
    <rect class="sszv-box" x="-26" y="-30" width="52" height="60" rx="4"/>
    <text y="-44">%(ped)s</text>
  </g>

  <!-- 접근 차량 -->
  <g class="sszv-node" transform="translate(152,362)">
    <circle class="sszv-halo" r="34"/>
    <g class="sszv-ico" style="--s:2.3" transform="scale(2.3) translate(-12,-12)">
      <path d="M19 17h2c.6 0 1-.4 1-1v-3c0-.9-.7-1.7-1.5-1.9C18.7 10.6 16 10 16 10s-1.3-1.4-2.2-2.3c-.5-.4-1.1-.7-1.8-.7H5c-.6 0-1.1.4-1.4.9l-1.4 2.9A3.7 3.7 0 0 0 2 12v4c0 .6.4 1 1 1h2"/>
      <circle cx="7" cy="17" r="2"/><path d="M9 17h6"/><circle cx="17" cy="17" r="2"/>
    </g>
    <text y="46">%(car)s</text>
  </g>

  <!-- 카메라 → 전광판 -->
  <g class="sszv-links">
    <path class="sszv-link l1" d="M272 132 C 232 100 176 100 138 124"/>
  </g>
  <g class="sszv-tag">
    <text x="204" y="92">%(t1)s</text>
  </g>
</svg>
<figcaption>%(cap)s</figcaption>
</figure>'''.replace('{PEDFIG40}', pedfig(40)) % L


def policy_grid(rows=None, label="전략"):
    out = "".join(
      '<article class="pol" data-reveal style="--td:%dms"><span class="n">%s %02d</span>'
      '<h3>%s</h3><p>%s</p></article>' % (i * 100, label, i + 1, a, b)
      for i, (a, b) in enumerate(rows or POLICY))
    return '<div class="pol-grid">%s</div>' % out


its = f'''<section class="section"><div class="area">
{head("INTELLIGENT TRANSPORT SYSTEMS", "지능형 교통체계")}
<div class="lead-box" data-reveal><p>지능형교통체계(ITS, Intelligent Transport Systems)란 교통수단 및 교통시설에 대하여
전자·제어 및 통신 등 첨단 교통기술과 교통정보를 개발·활용함으로써 교통 체계의 운영 및 관리를
과학화·자동화하고, 교통의 효율성과 안전성을 향상시키는 교통 체계를 의미합니다.</p></div>
</div></section>

<section class="section" style="padding-top:0"><div class="area">
{techvision("SangLim Tech Vision",
  ["상림기술은 도로 위 검지부터",
   "AI 교통정보 운영까지,",
   "하나의 흐름으로 만듭니다"],
  ["교통 인프라 시장은 장비를 납품하는 단계를 넘어, 수집한 데이터를 "
   "어떻게 가공하고 운영하느냐로 무게중심이 옮겨가고 있습니다.",
   "상림기술은 이 변화에 맞춰 검지 장비부터 표출 장비, 관제 소프트웨어까지 "
   "하나의 체계로 연결한 지능형 교통체계를 제공합니다."])}
</div></section>

<section class="section" style="background:var(--c-bg-soft)"><div class="area">
{head("HOW IT WORKS", "도로 위 데이터가 정보가 되기까지", "센서가 읽은 신호는 세 단계를 거쳐 운전자가 읽을 수 있는 문장이 됩니다.")}
{its_flow()}
</div></section>

<section class="section"><div class="area">
{head("SERVICE DOMAINS", "7대 서비스 분야")}
{its_services()}
</div></section>

<section class="section dark-sec dark-sec2"><div class="area">
  <div class="section-head is-dark" data-reveal><span class="eyebrow">C-ITS</span>
  <h2>차세대 지능형교통체계</h2>
  <p class="lead">기존 ITS가 센터에서 정보를 <em>내려주는</em> 구조라면,
  C-ITS는 차량과 도로, 보행자가 <em>서로 주고받는</em> 구조입니다. 자율주행이 달릴 수 있는 도로의 전제 조건입니다.</p></div>
{cits_viz()}
{cits_table()}
</div></section>

<section class="section"><div class="area">
{head("NECESSITY", "도입 필요성")}
{needs(["사고 다발 지역에 대한 안전성 향상","차량인식 시스템의 정확도 개선","지·정체 구간 등 교통문제에 대한 개선","보행자·이륜차 등 검지 사각지대 해소"])}
</div></section>

<section class="section" style="background:var(--c-bg-soft)"><div class="area-box">
{head("SOLUTION", "주요 솔루션")}
{solgrid([("도로전광판 (VMS)","sign","실시간 교통정보를 운전자에게 전달하는 가변정보 표출 장비","p_vms","../product/vms.html"),
          ("지능형 카메라","cam","AI 영상분석으로 차량을 인식하고 교통량 데이터를 수집","p_cam","../product/ptz.html"),
          ("교통 관제 상황판","sw","수집된 정보를 한 화면에서 감시하고 대응하는 관제 소프트웨어","p_dash","../product/dashboard.html"),
          ("현장 제어기","ctrl","검지·표출 장비를 묶어 센터와 통신하는 현장 제어 장치","p_ctrl")], "../")}
</div></section>

<section class="section"><div class="area">
{head("POLICY", "정책 방향 — ITS 기본계획 2030",
      "국토교통부는 <em>“친환경적이고 안전하면서 단절 없는 사람 중심의 교통서비스 제공”</em>을 비전으로 네 갈래 전략을 제시했습니다.")}
{policy_grid()}
<p class="src" data-reveal>자료: 국토교통부 「지능형교통체계 기본계획 2030」(2021) · 국토교통부 ITS 정책자료</p>
</div></section>'''
PAGES.append(("business/its.html","지능형 교통체계","AI 딥러닝 기반 실시간 교통정보 수집·가공 시스템.","business",its))

bis = f'''<section class="section"><div class="area">
{head("BUS INFORMATION SYSTEM", "버스정보 안내시스템")}
<div class="lead-box" data-reveal><p>버스정보 안내시스템(BIS, Bus Information System)은 위성항법장치(GPS)로 현재 운행 중인
버스의 위치를 파악하고, 이를 무선이동통신(LTE)을 통해 각 정류장과 버스 내 단말기에
도착 예정시간·운행노선 등의 정보를 문자와 음성으로 알려주는 첨단 버스 정보 안내 시스템입니다.</p></div>
</div></section>

<section class="section" style="padding-top:0"><div class="area">
{techvision("SangLim Tech Vision",
  ["상림기술은 버스의 위치부터",
   "정류장 안내까지,",
   "끊기지 않게 잇습니다"],
  ["버스를 기다리는 시간의 대부분은 '언제 오는지 모른다'는 불확실성입니다. "
   "정확한 도착 정보 하나가 체감 대기시간을 눈에 띄게 줄입니다.",
   "상림기술은 정류장에 서는 BIT 단말기를 직접 설계·제조하고, "
   "위치 수집부터 예측, 표출까지의 전 구간을 하나로 잇습니다."],
  BIS_TV)}
</div></section>

<section class="section" style="background:var(--c-bg-soft)"><div class="area">
{head("HOW IT WORKS", "버스가 어디쯤 오는지 어떻게 알까요", "버스에서 출발한 좌표 하나가 정류장 전광판의 '3분'이 되기까지.")}
{its_flow(BIS_FLOW)}
</div></section>

<section class="section dark-sec dark-sec2"><div class="area">
  <div class="section-head is-dark" data-reveal><span class="eyebrow">BIT TERMINAL</span>
  <h2>정류장에 서는 장비</h2>
  <p class="lead">BIT(Bus Information Terminal)는 이용자가 실제로 마주하는 유일한 장비입니다.
  읽히지 않으면 시스템 전체가 무의미해집니다.</p></div>
  <div class="dsol">
    <figure class="dsol-fig" data-reveal data-speed="0.06">
      <span class="dsol-glow"></span>{pimg("bit", "../")}
    </figure>
    <div class="dsol-body">
      <p class="dsol-lead" data-reveal>노선번호 · 도착예정시간 · 현재통과위치를 한 화면에 담아,
      정류장에 선 사람이 고개를 들자마자 판단할 수 있게 만듭니다.</p>
      {dspec(BIS_SPEC)}
    </div>
  </div>
</div></section>

<section class="section"><div class="area">
{head("NECESSITY", "도입 필요성")}
{needs(["버스 대기 시간의 불확실성 해소","정류장·차내 안내로 이용 편의 향상",
        "배차·노선 운영 데이터 확보","음성 안내로 교통약자 접근성 확보"])}
</div></section>

<section class="section" style="background:var(--c-bg-soft)"><div class="area-box">
{head("SOLUTION", "주요 솔루션")}
{solgrid([("버스정보 안내 단말기 (BIT)","bit","정류장에 설치되어 도착 예정시간과 노선 정보를 표출","p_bit","../product/bit.html"),
          ("차량 탑재 단말기 (OBE)","gnss","GPS로 위치를 측정하고 무선망으로 센터에 전송","p_gnss","../product/gnss.html"),
          ("운영단말 S/W","sw","정류장 단말기 상태를 관리하고 안내 정보를 배포","p_bus"),
          ("가공 및 제어 S/W","ctrl","수집된 위치 데이터를 가공해 도착 예정시간을 산출","p_proc")], "../")}
</div></section>'''
PAGES.append(("business/bis.html","버스정보 안내시스템","GPS·LTE 기반 버스 위치 파악 및 도착정보 안내 통합 솔루션.","business",bis))

EVS_FLOW = [
  ("01", "출동", "DISPATCH",
   "출동 지령과 동시에 차량 단말기가 위치·방향·목적지를 센터로 올립니다.",
   ["출동 지령 연동", "GPS 측위", "진행 방향 판정", "이송 경로 설정"]),
  ("02", "판단", "CENTER",
   "경로상의 교차로를 추려 도착 예정 시각을 계산하고, 우선신호가 필요한 곳을 정합니다.",
   ["경로 교차로 추출", "도착 시각 예측", "우선신호 요청", "중복 요청 조정"]),
  ("03", "제어", "INTERSECTION",
   "신호제어기가 녹색을 확보하고, 전광판이 주변 차량에 접근을 알립니다. 통과 후 즉시 복귀합니다.",
   ["녹색 시간 확보", "전광판 경고 표출", "통과 감지", "신호 주기 복귀"]),
]

EVS_CMP = [
  ("제어 위치", "교차로 현장의 신호제어기가 직접 판단", "센터가 경로 전체를 보고 판단"),
  ("적용 범위", "차량이 접근한 <b>그 교차로 하나</b>", "이송 경로상 <b>여러 교차로를 연속</b>으로"),
  ("연동 방식", "차량 단말기 ↔ 현장 제어기 근거리 통신", "차량 → 센터 → 각 신호제어기"),
  ("확장성", "교차로를 늘릴수록 개별 설치·조정 필요",
   '경로·우선순위를 <span class="nw">센터에서 일괄 관리</span>'),
]

EVS_SPEC = [
  ("출동 상황을 먼저 알립니다", "사이렌은 가까워져야 들립니다. 교차로 진입 전 전광판에 "
   "긴급차량 접근을 표출해, 운전자가 미리 진로를 비켜 줄 수 있게 합니다."),
  ("고휘도 LED · 옥외 설계", "직사광선 아래에서도 읽히는 고휘도 LED를 쓰고, 혹서·혹한과 "
   "진동, 낙뢰가 있는 옥외를 전제로 설계합니다."),
  ("신호제어기와 함께 동작", "전광판 표출과 우선신호 부여가 같은 신호로 묶여 있어, "
   "녹색 확보와 경고 표출이 어긋나지 않습니다."),
  ("통과 후 자동 복귀", "긴급차량이 지나가면 표출이 꺼지고 신호도 원래 주기로 돌아갑니다. "
   "일반 교통 흐름에 남기는 영향을 최소로 줄입니다."),
]

evs = f'''<section class="section dark-sec"><div class="area">
  <div class="section-head is-dark" data-reveal><span class="eyebrow">EMERGENCY VEHICLE PRIORITY</span>
  <h2>이송 경로를 앞서 여는 방식</h2>
  <p class="lead">구급차 등 긴급차량이 응급환자를 이송할 때, 도시안전 통합센터가 차량 위치를
  GPS로 추적해 교차로 진입 시 자동으로 녹색 신호를 줍니다. 한 교차로만 여는 것이 아니라,
  이송 경로 위의 교차로들이 차량보다 먼저 순서대로 준비됩니다.</p></div>
  {evs_viz()}
</div></section>

<section class="section dark-sec dark-sec2"><div class="area">
  <div class="section-head is-dark" data-reveal><span class="eyebrow">ON THE ROAD</span>
  <h2>사이렌보다 먼저 도착하는 신호</h2>
  <p class="lead">긴급차량 출동안내 전광판은 교차로 진입 전에 일반 차량 운전자가
  상황을 알아차리도록 만드는 장비입니다.</p></div>
  <div class="dsol">
    <figure class="dsol-fig" data-reveal data-speed="0.06">
      <span class="dsol-glow"></span>{pimg("evs2", "../")}
    </figure>
    <div class="dsol-body">
      <p class="dsol-lead" data-reveal>소방차·구급차가 지나갈 길을, 도로 위의 장비가 미리 만들어 둡니다.</p>
      {dspec(EVS_SPEC)}
    </div>
  </div>
</div></section>

<section class="section" style="background:var(--c-bg-soft)"><div class="area">
{head("HOW IT WORKS", "신호는 어떻게 미리 열리나", "출동 지령이 떨어진 순간부터 교차로의 녹색이 준비되기까지.")}
{its_flow(EVS_FLOW)}
</div></section>

<section class="section dark-sec dark-sec2"><div class="area">
  <div class="section-head is-dark" data-reveal><span class="eyebrow">CONTROL MODE</span>
  <h2>현장제어에서 중앙제어로</h2>
  <p class="lead">초기에는 교차로 단위의 <em>현장제어</em>로 시작했고, 지금은 이송 경로 전체를
  관리하는 <em>중앙제어</em> 방식으로 확대되고 있습니다.</p></div>
{cits_table(EVS_CMP, "현장제어 방식", "중앙제어 방식", "확대 적용")}
</div></section>

<section class="section"><div class="area">
{head("NECESSITY", "도입 필요성")}
{needs(["상습 교통정체로 인한 출동지연","긴급차량 교통사고 증가",
        "긴급차량 골든타임 확보","교차로 통과 대기시간 단축"])}
</div></section>

<section class="section" style="background:var(--c-bg-soft)"><div class="area-box">
{head("SOLUTION", "주요 솔루션")}
{solgrid([("긴급차량 출동안내 전광판","sign",
           "교차로 진입 전 일반 차량에 긴급차량 접근을 안내","p_evsled")], "../")}
</div></section>'''
PAGES.append(("business/evs.html","긴급차량 우선신호 시스템","GPS 추적 기반 긴급차량 우선신호 부여로 골든타임을 확보합니다.","business",evs))

SSZ_FLOW = [
  ("01", "검지", "AT THE CROSSING",
   "보호구역 카메라가 횡단보도와 그 주변을 상시 봅니다. 사람과 차를 구분해 읽습니다.",
   ["AI 영상분석", "보행자 검지", "차량 인식", "주야간 대응"]),
  ("02", "판단", "ON SITE",
   "보행 의도와 차량 접근을 함께 보고, 경고를 낼지 단속 자료로 남길지 판단합니다.",
   ["보행 의도 판정", "접근 차량 속도", "위험 상황 분류", "이벤트 기록"]),
  ("03", "표출", "TO THE DRIVER",
   "전광판이 즉시 경고를 띄우고, 위반은 자료로 남아 단속 시스템으로 넘어갑니다.",
   ["LED 경고 표출", "음성 안내", "불법 주정차", "정지선 위반"]),
]

SSZ_CMP = [
  ("감지 방식", "지정된 지점을 지날 때만 반응", "화면 전체를 계속 보고 <b>사람과 차를 구분</b>"),
  ("알리는 시점", "이미 도로에 들어선 뒤", "보행 의도를 읽어 <b>진입 전에</b>"),
  ("남는 자료", "통과 여부 정도", "영상·시각·유형이 함께 남아 단속 연계"),
  ("확장", "기능마다 장비를 따로 설치",
   '한 대로 <span class="nw">감지 · 경고 · 단속</span>을 함께'),
]

SSZ_SPEC = [
  ("보행자를 보면 바로 켜집니다", "평소에는 보호구역 안내를 표출하다가, 카메라가 보행자를 "
   "잡는 순간 경고 화면으로 바뀝니다. 운전자가 아이를 보기 전에 먼저 알게 됩니다."),
  ("고휘도 LED · 옥외 설계", "직사광선 아래에서도 읽히는 고휘도 LED를 쓰고, 혹서·혹한과 "
   "진동, 낙뢰가 있는 옥외를 전제로 설계합니다."),
  ("문자와 음성 동시 안내", "표출과 함께 음성으로도 안내해, 운전자와 보행자 양쪽에 "
   "같은 정보가 닿게 만듭니다."),
  ("단속 시스템과 연계", "불법 주정차와 정지선 위반이 같은 장비에서 자료로 남아, "
   "안내에서 끝나지 않고 실제 개선으로 이어집니다."),
]

ssz = f'''<section class="section dark-sec"><div class="area">
  <div class="section-head is-dark" data-reveal><span class="eyebrow">SMART SCHOOL ZONE</span>
  <h2>아이를 보기 전에 먼저 알립니다</h2>
  <p class="lead">어린이 보호구역 내 위험한 상황을 LED전광판으로 알려 충돌과 사고를 예방하는
  안전 보행 서비스입니다. 운전자가 아이를 발견했을 때는 이미 늦습니다 &mdash;
  카메라가 먼저 보고, 전광판이 먼저 알리는 구조입니다.</p></div>
  {ssz_viz()}
</div></section>

<section class="section dark-sec dark-sec2"><div class="area">
  <div class="section-head is-dark" data-reveal><span class="eyebrow">ON THE ROAD</span>
  <h2>보호구역에 서는 전광판</h2>
  <p class="lead">스마트 스쿨존 전광판은 아이와 운전자가 실제로 마주하는 유일한 장비입니다.
  읽히지 않으면 시스템 전체가 무의미해집니다.</p></div>
  <div class="dsol">
    <figure class="dsol-fig" data-reveal data-speed="0.06">
      <span class="dsol-glow"></span>{pimg("ssz2", "../")}
    </figure>
    <div class="dsol-body">
      <p class="dsol-lead" data-reveal>평소에는 보호구역임을 알리고, 위험한 순간에는 경고로 바뀝니다.</p>
      {dspec(SSZ_SPEC)}
    </div>
  </div>
</div></section>

<section class="section" style="background:var(--c-bg-soft)"><div class="area">
{head("HOW IT WORKS", "카메라가 본 것이 경고가 되기까지", "보호구역 안의 한 장면이 운전자의 눈앞 문장으로 바뀌는 세 단계.")}
{its_flow(SSZ_FLOW)}
</div></section>

<section class="section dark-sec dark-sec2"><div class="area">
  <div class="section-head is-dark" data-reveal><span class="eyebrow">WHY AI</span>
  <h2>지나가는 것을 세는 것과, 보고 있는 것의 차이</h2>
  <p class="lead">같은 자리에 장비를 두어도, <em>지나갔는지</em>를 세는 것과
  <em>무엇이 있는지</em>를 보는 것은 전혀 다른 결과를 만듭니다.</p></div>
{cits_table(SSZ_CMP, "기존 검지 방식", "AI 영상분석", "적용 확대")}
</div></section>

<section class="section"><div class="area">
{head("NECESSITY", "도입 필요성")}
{needs(["사고 다발 지역에 대한 안정성 향상","차량인식 시스템의 정확도 개선",
        "지·정체 구간 등 교통문제에 대한 개선","안내에서 끝나지 않는 위반 단속 연계"])}
</div></section>

<section class="section" style="background:var(--c-bg-soft)"><div class="area-box">
{head("SOLUTION", "주요 솔루션")}
{solgrid([("스마트스쿨존 전광판","sign","보행자 감지 시 운전자에게 즉시 경고를 표출","p_ssz2"),
          ("지능형 카메라","cam","보호구역 전체를 상시 감시하는 AI 영상 검지 장비","p_cam","../product/ptz.html")], "../")}
</div></section>'''
PAGES.append(("business/ssz.html","스마트 스쿨존 시스템","AI 영상분석 기반 어린이보호구역 보행자 안전 시스템.","business",ssz))

# ---------- 주요제품 ----------
def product_page(url, title, desc, lead, specs, icon, extra="", after="", before=""):
    body = f'''{before}<section class="section{" dark-sec" if before else ""}"><div class="area">
{head("MAIN PRODUCT", title) if not before else '<div class="section-head is-dark" data-reveal><span class="eyebrow">MAIN PRODUCT</span><h2>' + title + '</h2></div>'}
<div class="sol" data-reveal>
  <div class="sol-media{" sol-photo" if icon in PROD_IMG else ""}{" sol-dark" if before else ""}">{pimg(icon, "../") or ICONS[icon]}</div>
  <div class="sol-body">
    <p class="{"dsol-lead" if before else ""}" style="font-size:var(--fs-lead);{"" if before else "color:var(--c-ink);"}font-weight:var(--w-read);letter-spacing:-.012em;line-height:1.8">{lead}</p>
    {dspec(specs) if before else spec(specs)}
    {extra}
  </div>
</div>
</div></section>{after}'''
    PAGES.append((url, title, desc, "product", body))

product_page("product/vms.html","도로교통 전광판(VMS)",
  "실시간 교통정보를 표출하는 도로교통 전광판입니다.",
  "시인성을 고려한 Full-Color 초고휘도 LED를 적용한 도로교통 정보 표출 장비입니다.",
  [("초고휘도 LED","시인성을 고려한 Full-Color 초고휘도 LED 적용"),
   ("열방출 용이 설계","모듈 일체형 패키징 구성으로 유지보수 및 관리에 용이한 시스템 구현"),
   ("안정성 극대화 함체","방수·방진·방열을 대비하여 비늘창 제작 및 냉각 FAN 기능으로 장비 수명 단축 방지"),
   ("자체 감시 기능","모듈부 전원 및 표출부 자체 감시 기능으로 원격 모듈 점검 기능 구현")], "vms")

product_page("product/bit.html","버스정보안내 전광판(BIT)",
  "정류장 버스 도착정보를 안내하는 전광판입니다.",
  "정류장에 설치되어 버스 도착 예정시간과 노선 정보를 표출하는 안내 전광판입니다.",
  [("Full Color 초고휘도 LED","시인성을 고려한 Full-Color 초고휘도 LED 적용"),
   ("LED 사출방식 도입","모듈 베젤크기를 줄여 하나의 디스플레이로 보이도록 설계하여 시인성을 향상, 촘촘한 LED 모듈 간격으로 글자가 선명하게 표출"),
   ("Smart Cooling System","상태 감시 보드와 연동된 내부 FAN을 통한 쿨링으로 열에 의한 장비 수명 단축 방지"),
   ("Remote Reboot","원격 재부팅 기능으로 장애 발생 시 현장에 가지 않고 센터에서 처리, 함체 보안을 위한 원격 개폐(암호화 잠금장치) 지원")], "bit")

product_page("product/ecs.html","전기차 충전소 전광판",
  "전기차 충전소 이용 정보를 표출하는 전광판입니다.",
  "고휘도 LED 소자를 바탕으로 밝고 선명한 화면을 통해 충전 가능 여부 및 충전 잔량을 표출합니다.",
  [("설치 목적","전기차 충전소 이용 고객에게 충전 가능 여부와 잔량을 시각적으로 전달"),
   ("기대 효과","전기차 충전 편의성을 높이고 국내 전기차 보급 활성화에 기여")], "ecs",
  before=ecs_show("../", "ko"))

product_page("product/gnss.html","초정밀 모듈(GNSS)",
  "좌표 기준을 약 10m에서 약 2cm로 끌어올린 초정밀 버스 측위 모듈입니다.",
  "더 정확한 버스정보를 제공하기 위해, RTK 보정으로 위치 데이터의 기준을 약 10m에서 약 2cm 수준으로 끌어올렸습니다. "
  "전세계 초소형 초정밀 GPS 업계 1위(u-blox) 모듈을 사용해 정확도와 신뢰성을 확보했습니다.",
  [("2cm 수준 측위","기준국 보정을 적용한 RTK 방식으로, 약 10m 오차의 일반 GPS 대비 좌표 정밀도를 크게 높였습니다."),
   ("GPS 모듈","전세계 초소형 초정밀 GPS 업계 1위(u-blox) 모듈을 사용해 정확도와 신뢰성을 확보했습니다."),
   ("RTK 보정","기준국(BASE)과 차량 단말(OBE)이 짝을 이루는 SANGLIM_GNSS_RTK 구성으로 등록되어 있습니다."),
   ("전자파적합성","KC 전자파적합성 시험을 통과해 버스 내 운전자와 승객의 안전성을 확보했습니다."),
   ("LED 상태표시기","상태표시를 통해 시스템 업그레이드 진행과 동작 상태를 현장에서 바로 확인할 수 있습니다.")],
  "gnss",
  before=gnss_show("../", "ko"),
  after="\n" + gnss_map("../", "ko"))

PAGES.append(("product/dashboard.html","상황판(대시보드)",
  "교통·안전·신호·버스 데이터를 한 화면에 모으는 ITS 관제 상황판입니다.",
  "product", dash_page("../", "ko")))
PAGES.append(("product/ptz.html","PTZ 카메라",
  "저조도 환경에서도 고품질 영상을 제공하는 회전형 보안 카메라입니다.",
  "product", ptz_page("../", "ko")))

# ---------- 문의하기 ----------
contact = f'''<section class="section"><div class="area">
{head("CONTACT", "문의하기", "사업 요구사항을 남겨주시면 담당자가 확인 후 연락드리겠습니다.")}
<div class="split" style="align-items:start">
  <div data-reveal>
    {dl([("대표전화", f'<a href="tel:0220831333">{TEL}</a>'),
         ("이메일", f'<a href="mailto:{MAIL}">{MAIL}</a>'),
         ("본사", ADDR_HQ),
         ("공장", ADDR_FT)])}
  </div>
  <form class="cform" id="cform" data-reveal data-d="120" novalidate
        data-mail="{MAIL}" data-endpoint="">
    <div class="form-grid">
      <div class="field"><label for="f-name">담당자명 <b class="req">*</b></label>
        <input id="f-name" name="name" type="text" placeholder="홍길동" required autocomplete="name"></div>
      <div class="field"><label for="f-org">기관 / 회사명</label>
        <input id="f-org" name="org" type="text" placeholder="○○시청" autocomplete="organization"></div>
      <div class="field"><label for="f-tel">연락처</label>
        <input id="f-tel" name="tel" type="tel" placeholder="010-0000-0000" autocomplete="tel"></div>
      <div class="field"><label for="f-mail">이메일 <b class="req">*</b></label>
        <input id="f-mail" name="email" type="email" placeholder="name@example.com" required autocomplete="email"></div>
      <div class="field full"><label for="f-msg">문의 내용 <b class="req">*</b></label>
        <textarea id="f-msg" name="message" required placeholder="도입 검토 중인 시스템과 일정, 예산 범위 등을 알려주시면 더 정확한 제안이 가능합니다."></textarea></div>
    </div>
    <div class="form-act">
      <button type="submit" class="btn btn-primary">문의 보내기
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M5 12h14M13 6l6 6-6 6"/></svg></button>
      <button type="button" class="btn btn-line cf-copy">내용 복사</button>
    </div>
    <p class="form-msg" role="status" aria-live="polite" hidden></p>
    <p class="form-note">※ <b>문의 보내기</b>를 누르면 작성하신 내용이 그대로 담긴 메일이
    <a href="mailto:{MAIL}" style="color:var(--c-brand);font-weight:var(--w-mid)">{MAIL}</a> 앞으로 열립니다.
    보내기만 누르시면 됩니다.<br>
    메일 앱이 열리지 않는 환경이라면 <b>내용 복사</b>를 눌러 붙여넣어 보내주세요.</p>
  </form>
</div>
</div></section>'''
PAGES.append(("contact.html","문의하기",f"{COMPANY} 문의 안내. 대표전화 {TEL}.","contact",contact))

# ---------- 메인 페이지 ----------
_hero = '<!-- ============ HERO (영상 배경) ============ -->\n<section class="hero" id="hero">\n  <div class="hero-media">\n    <!-- 기본 720p. 넓은 화면에서는 app.js 가 1080p 로 교체한다.\n         (video 안의 source media 속성은 브라우저가 무시하므로 JS 로 선택) -->\n    <video id="heroVid" playsinline muted loop autoplay preload="metadata"\n           poster="assets/video/hero-poster.jpg" data-hd="assets/video/hero">\n      <source src="assets/video/hero-720.webm" type="video/webm">\n      <source src="assets/video/hero-720.mp4" type="video/mp4">\n    </video>\n  </div>\n  <div class="hero-scrim"></div>\n  <div class="hero-grid"></div>\n  <div class="hero-inner">\n    <h1 class="hero-h">\n      <span class="reveal-line"><span class="thin">축적된 기술력으로</span></span>\n      <span class="reveal-line"><span><span class="hl"><em class="accent">더 안전한 길</em></span>을 만들고</span></span>\n      <span class="reveal-line"><span>더 나은 교통시스템을 세웁니다</span></span>\n    </h1>\n    <p class="hero-sub">119 구급차의 골든타임 확보부터 어린이보호구역 보행 안전까지,\n      상림기술은 <b>사람의 안전</b>을 가장 앞에 두고 교통 인프라를 만듭니다.</p>\n    <div class="hero-cta">\n      <a href="#business" class="btn btn-primary">사업분야 보기\n        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>\n      <a href="company/record.html" class="btn btn-ghost">구축사례</a>\n    </div>\n    </div>\n  <div class="scroll-cue"></div>\n  <div class="hero-fade"></div>\n</section>\n\n\n'

# 홈 · 사업 분야 — 좌측 스테이트먼트 패널 + 우측 번호 카드(각 카드가 링크)
BIZ_TV = [
  ("Intelligent Transport", "지능형 교통체계", "hub",
   "교통수단과 시설에 첨단 교통기술을 접목해 운영·관리를 자동화합니다. "
   "AI 딥러닝 기반으로 실시간 교통정보를 수집·가공해 교통혼잡을 방지합니다.",
   "business/its.html"),
  ("Bus Information", "버스정보 안내시스템", "panel",
   "위성항법장치로 운행 중인 버스 위치를 파악하고, 정류장과 차내 단말기에 "
   "도착 예정시간·운행노선을 문자와 음성으로 안내합니다.",
   "business/bis.html"),
  ("Emergency Priority", "긴급차량 우선신호", "siren",
   "긴급차량이 응급환자를 이송할 때 GPS로 위치를 추적해, 교차로 진입 시 "
   "자동으로 녹색 신호를 부여합니다.",
   "business/evs.html"),
  ("Smart School Zone", "스마트 스쿨존", "shield",
   "어린이 보호구역 내 위험 상황을 LED전광판으로 알려 사고를 예방합니다. "
   "AI 영상분석으로 보행자를 감지합니다.",
   "business/ssz.html"),
]

_PRODS = [
  ("VMS Series",  "도로교통 전광판", "product/vms.html", "vms",
   "시인성을 고려한 Full-Color 초고휘도 LED를 적용한 도로교통 정보 표출 장비입니다.",
   ["SL240M111"]),
  ("BIT Series",  "버스정보안내 전광판", "product/bit.html", "bit",
   "정류장에 설치되어 버스 도착 예정시간과 노선 정보를 표출하는 안내 전광판입니다.",
   ["SL-BIT-TRI", "3D8Y", "4D12Y"]),
  ("ECS Series",  "전기차 충전소 전광판", "product/ecs.html", "ecs",
   "고휘도 LED로 충전 가능 여부와 충전 잔량을 표출해 이용 편의성을 높입니다.",
   ["EL265"]),
  ("GNSS Module", "초정밀 모듈", "product/gnss.html", "gnss",
   "u-blox 기반 초정밀 GNSS RTK 모듈로 정확도와 신뢰성을 확보했습니다.",
   ["SLv-001", "OBE", "BASE"]),
  ("PTZ Camera",  "회전형 보안 카메라", "product/ptz.html", "ptz",
   "저조도 환경에서도 2D/3D 노이즈 리덕션으로 고품질 컬러 영상을 제공합니다.",
   ["SL-P223ID5", "P230ID5", "P510ID5"]),
]

_PLUS = ('<svg class="acc-plus" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
         'stroke-width="1.6"><path d="M12 5v14M5 12h14"/></svg>')

def _png_size(key):
    """PNG IHDR 에서 가로·세로를 읽습니다(표준 라이브러리만 사용)."""
    import struct
    f = os.path.join(ROOT, "assets/img/prod", key + ".png")
    with open(f, "rb") as fp:
        head = fp.read(24)
    return struct.unpack(">II", head[16:24])


# 높이 보정 계수.
#   높이만 똑같이 맞추면, 정사각형에 가까운 제품(초정밀 모듈 1.02:1)은
#   면적이 작아 눈에는 훨씬 작아 보입니다. 그래서 '보이는 면적'이 같아지도록
#   비율의 제곱근만큼 높이를 보정합니다.
#     k = sqrt(1.531 / ar)          1.531 = 버스정보안내 전광판 = 기준 1.0
#   결과: 초정밀 모듈 +22.3%, 도로교통 전광판 +13.3%, PTZ +6.1%, 전기차 충전소 +1.0%
_HK_REF = 1.5311


def _hk(ar):
    return max(0.90, min(1.30, (_HK_REF / ar) ** 0.5))


def accfig(icon, p=""):
    """아코디언 제품 이미지.

    크기는 '폭'이 아니라 '높이' 로 잡습니다(CSS 쪽 height + aspect-ratio).
    그래야 제품마다 가로세로비가 달라도 카드 안에서 세로 존재감이 같아지고,
    폭은 비율대로 따라오면서 오른쪽으로 자연스럽게 잘려 나갑니다.
    PROD_ALT 에 짝이 있으면 마우스를 올렸을 때 분해도로 교차 전환됩니다.
    """
    if icon not in PROD_IMG:
        return '<div class="acc-fig">%s</div>' % ICONS[icon]
    aw, ah = _png_size(icon)
    ar_a = aw / float(ah)
    st = "--ar-a:%.4f;--hk-a:%.4f" % (ar_a, _hk(ar_a))
    alt = PROD_ALT.get(icon)
    if not alt:
        return ('<div class="acc-fig acc-photo" style="%s">'
                '<span class="ph-a">%s</span></div>') % (st, pimg(icon, p))
    bw, bh = _png_size(alt)
    ar_b = bw / float(bh)
    st += ";--ar-b:%.4f;--hk-b:%.4f" % (ar_b, _hk(ar_b))
    return ('<div class="acc-fig acc-photo has-alt" style="%s">'
            '<span class="ph-a">%s</span>'
            '<span class="ph-b">%s</span>'
            '</div>') % (st, pimg(icon, p), pimg(alt, p))


_acc = ""
for i, (ser, name, url, icon, desc, models) in enumerate(_PRODS):
    chips = "".join('<span>%s</span>' % m for m in models)
    _acc += (
      '<article class="acc-item%s" data-cursor="VIEW">'
      '%s'
      '<div class="acc-mini"><h3>%s</h3><p>#%s</p></div>%s'
      '<div class="acc-full">'
      '<span class="ser">%s</span><h3>%s</h3>'
      '<p class="desc">%s</p>'
      '<div class="acc-models">%s</div>'
      '<a class="acc-go" href="%s">자세히 보기 %s</a>'
      '</div></article>'
    ) % (" is-open" if i == 0 else "", accfig(icon), name, models[0], _PLUS,
         ser, name, desc, chips, url, _ARROW)

home_body = f'''{_hero}
<section class="section" style="background:var(--c-bg-soft)"><div class="area">
{techvision("BUSINESS AREA",
  ["지능형 교통체계부터",
   "스마트 스쿨존까지,",
   "교통 인프라 전 영역"],
  ["도로 위의 검지 장비, 정류장과 교차로에 서는 표출 장비, 그리고 이 둘을 잇는 "
   "관제 소프트웨어. 상림기술의 네 사업 분야는 모두 같은 기술 기반 위에 있습니다.",
   "장비를 납품하는 데서 끝내지 않고, 수집한 데이터가 현장에서 어떻게 쓰이는지까지 "
   "책임집니다. 카드를 눌러 각 분야를 확인해 보세요."],
  BIZ_TV)}
</div></section>

<section class="section"><div class="area-box">
{head("MAIN PRODUCT", "주요 제품", "마우스를 올리면 제품 정보가 펼쳐집니다.")}
<div class="acc" id="prodAcc" data-reveal>{_acc}</div>
</div></section>

<section class="section" style="padding-block:clamp(46px,6vw,80px)"><div class="area-wrap"><div class="section-head" data-reveal style="margin-bottom:34px;text-align:center;max-width:none"><span class="eyebrow">PARTNERS</span><h2 style="font-size:clamp(1.4rem,2.2vw,2rem)">전국 지자체·공공기관과 함께합니다</h2></div><div class="pt-strip" data-reveal><div class="pt-track" id="ptTrack"><img src="assets/img/partner/pub-01.png" alt="화성시" loading="lazy"><img src="assets/img/partner/pub-02.png" alt="광명시" loading="lazy"><img src="assets/img/partner/pub-03.png" alt="용인시" loading="lazy"><img src="assets/img/partner/pub-04.png" alt="서울특별시" loading="lazy"><img src="assets/img/partner/pub-05.png" alt="안양시" loading="lazy"><img src="assets/img/partner/pub-06.png" alt="안동시" loading="lazy"><img src="assets/img/partner/pub-07.png" alt="파주시" loading="lazy"><img src="assets/img/partner/pub-08.png" alt="수원시" loading="lazy"><img src="assets/img/partner/pub-09.png" alt="광양시" loading="lazy"><img src="assets/img/partner/pub-10.png" alt="김포시" loading="lazy"><img src="assets/img/partner/pub-11.png" alt="성남시" loading="lazy"><img src="assets/img/partner/pub-12.png" alt="대전광역시" loading="lazy"><img src="assets/img/partner/pub-13.png" alt="세종특별자치시" loading="lazy"><img src="assets/img/partner/pub-14.png" alt="춘천시" loading="lazy"><img src="assets/img/partner/pub-15.png" alt="경주시" loading="lazy"><img src="assets/img/partner/pub-16.png" alt="충청남도" loading="lazy"><img src="assets/img/partner/pub-17.png" alt="청주시" loading="lazy"><img src="assets/img/partner/pub-18.png" alt="고양특례시" loading="lazy"><img src="assets/img/partner/pub-19.png" alt="영천시" loading="lazy"><img src="assets/img/partner/pub-20.png" alt="제천시" loading="lazy"><img src="assets/img/partner/pub-21.png" alt="제주특별자치도" loading="lazy"></div></div><div class="pt-more"><a href="company/partners.html" class="btn btn-primary">파트너사 전체 보기<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a></div></div></section>

<section class="section band"><div class="area-box">
<div class="section-head" data-reveal><span class="eyebrow" style="color:var(--c-accent-bright)">TRACK RECORD</span>
<h2>구축사례</h2><p class="lead">전국 지자체와 기관에 상림기술의 시스템이 설치·운영되고 있습니다.</p></div>
<div style="margin-top:44px" data-reveal>
  <a href="company/record.html" class="btn btn-ghost" style="border-color:rgba(255,255,255,.35);color:#fff">구축사례 전체 보기
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
</div>
</div></section>'''

# ============================================================
# 실행
# ============================================================
def build_ko():
    made = [page("index.html", "지능형 교통시스템 전문기업",
                 TAGLINE, "", home_body, home=True)]
    for url, title, desc, cur, body in PAGES:
        made.append(page(url, title, desc, cur, body))
    return made


def build_en():
    """content_en.py 에 이 모듈의 헬퍼를 주입한 뒤 영문 페이지를 생성합니다."""
    import content_en
    g = globals()
    for k in ("head", "dl", "spec", "sec", "needs", "solgrid", "pimg", "rel", "dspec",
              "ptz_show", "ptz_page", "dash_page", "gnss_show", "gnss_map", "ecs_show", "bizico", "accfig", "PROD_ALT",
              "its_flow", "its_services", "cits_viz", "cits_table", "policy_grid", "techvision", "evs_viz", "ssz_viz", "solphoto", "SOL_PHOTO", "ICONS", "PROD_IMG", "TEL", "MAIL", "BIZNO", "COMPANY_EN",
              "ADDR_HQ_EN", "ADDR_FT_EN"):
        setattr(content_en, k, g[k])
    made = []
    for item in content_en.pages():
        url, title, desc, cur, body = item[:5]
        is_home = len(item) > 5 and item[5]
        made.append(page(url, title, desc, cur, body, home=is_home))
    return made


if __name__ == "__main__":
    LANG = "ko"
    made = build_ko()
    LANG = "en"
    made += build_en()
    LANG = "ko"
    # 배포 감시용 빌드 번호 — 페이지 head 의 스크립트가 이 파일과 자기 번호를 비교합니다
    with open(os.path.join(ROOT, "version.json"), "w", encoding="utf-8") as f:
        f.write('{"build":"%s"}' % V)
    made.append("version.json")
    print(f"생성 완료: {len(made)}개 페이지")
    for m in made:
        print("  ", m)
