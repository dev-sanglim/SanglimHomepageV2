# -*- coding: utf-8 -*-
"""
English content for the SangLim Technologies site.

build.py injects its helpers (head, dl, spec, pimg, rel, ICONS, …) into this
module's namespace before calling pages(), so everything below can use them
directly. Only the copy lives here; all layout/CSS is shared with the Korean
build.
"""

# ------------------------------------------------------------------ history
HISTORY_EN = [
 ("2026", "Nationwide operations", [
   ("b", "Busan Metropolitan City Bus Information Management System (BIMS) construction", "", 1),
   ("b", "Seoul bus information terminal manufacture, supply and replacement", "", 1),
   ("b", "KTX Gwangmyeong Station bus information system upgrade", "", 1),
   ("b", "Seosan parking information sharing service", "", 0),
   ("b", "Sangju emergency-vehicle priority signal integration upgrade", "", 0),
   ("b", "Hwaseong Intelligent Transport System integrated maintenance", "", 0),
   ("b", "Pyeongtaek Intelligent Transport System integrated maintenance", "in progress", 0),
   ("b", "Namyangju traffic information system integrated maintenance", "", 0),
   ("b", "Gwangmyeong ITS &amp; BIS integrated maintenance", "", 0),
   ("b", "Gwangmyeong smart CCTV integrated maintenance", "", 0),
   ("b", "Andong Intelligent Transport System maintenance", "", 0),
   ("b", "Bus Information System expansion &middot; Andong", "in progress", 0),
 ]),
 ("2025", "Entry into metropolitan cities", [
   ("b", "Busan Metropolitan City BIMS expansion &amp; improvement", "", 1),
   ("b", "Cloud-based Bus Information System software development", "", 1),
   ("b", "Hwaseong Intelligent Transport System upgrade", "", 0),
   ("b", "Busan Regional Office national-road adaptive signal project", "", 0),
   ("b", "Mokpo Bus Information System enhancement", "", 0),
 ]),
 ("2024", "Expansion into the private sector", [
   ("b", "EV charging station displays", "59 expressway sites · GS Caltex", 1),
   ("b", "Seoul emergency-vehicle priority signal pilot project", "", 1),
   ("b", "Andong Bus Information System expansion &amp; improvement", "", 0),
   ("b", "Jecheon Bus Information System upgrade", "", 0),
   ("b", "Gwangmyeong ITS integrated maintenance (2024–2025)", "", 0),
   ("b", "Andong Sinsijang signal display operating software", "", 0),
   ("b", "Giheung water-level LED display manufacture &amp; installation", "", 0),
   ("c", "Direct Production Certificate — 2 items", "Software maintenance &amp; support services", 0),
 ]),
 ("2023", "Moving into road safety", [
   ("b", "Gwangmyeong emergency-vehicle priority signal system", "", 1),
   ("b", "School-zone pedestrian safety system", "", 1),
   ("b", "Gwangmyeong ITS integrated maintenance service", "", 0),
   ("b", "Traffic signal controller software upgrade", "", 0),
   ("b", "Andong ITS equipment supply and installation", "", 0),
   ("c", "Direct Production Certificate — 3 items",
        "Video display units · Bus and vehicle information terminals · Guide signs", 0),
 ]),
 ("2022", "Building the R&amp;D foundation", [
   ("c", "Corporate R&amp;D centre registered", "", 1),
   ("c", "Venture company certification", "Innovation-growth type", 1),
   ("b", "Gwangmyeong ITS construction and performance improvement", "", 1),
   ("b", "Bus stop terminal relocation works", "", 0),
   ("c", "Direct Production Certificate — 6 items",
        "Big-data analysis · IT infrastructure · Information system development · "
        "Packaged software · Operation outsourcing · Internet development services", 0),
   ("c", "Direct Production Certificate — 2 items", "Security cameras · Video surveillance units", 0),
 ]),
 ("2021", "Founded", [
   ("s", "SangLim Technologies Co., Ltd. founded", "7 April 2021", 1),
   ("b", "Hwaseong Intelligent Transport System upgrade", "first contract", 1),
   ("c", "Information &amp; Communication Works licence", "", 0),
   ("c", "Software business registration", "", 0),
 ]),
]
KIND_EN = {"b": ("Project", "k-b"), "c": ("Certification", "k-c"), "s": ("Milestone", "k-s")}

# ------------------------------------------------------------- track record
REC_EN = [
 ("Variable Message Signs (VMS)", [
   ("Daejeon Regional Construction Management Administration", "Chungcheongbuk-do"),
   ("Yeongcheon traffic information sign", "Yeongcheon-si, Gyeongsangbuk-do"),
   ("Wonjeoksan Tunnel display", "Incheon"),
   ("Wonjeoksan Tunnel toll display", "Incheon"),
   ("Andong ITS traffic information sign", "Andong-si, Gyeongsangbuk-do"),
   ("Seongnam ITS traffic information sign", "Seongnam-si, Gyeonggi-do"),
   ("Chuncheon ITS traffic information sign", "Chuncheon-si, Gangwon-do"),
   ("Pohang variable message signs", "Pohang-si, Gyeongsangbuk-do"),
   ("Daegu variable message signs", "Daegu")]),
 ("Bus Information Terminals (BIT)", [
   ("Hwaseong bus information terminals", "Hwaseong-si, Gyeonggi-do"),
   ("Suwon bus information terminals", "Suwon-si, Gyeonggi-do"),
   ("Yongin bus information terminals", "Yongin-si, Gyeonggi-do"),
   ("Anyang bus information terminals", "Anyang-si, Gyeonggi-do"),
   ("Gwangmyeong bus information terminals", "Gwangmyeong-si, Gyeonggi-do"),
   ("Seongnam bus information terminals", "Seongnam-si, Gyeonggi-do"),
   ("Andong bus information terminals", "Andong-si, Gyeongsangbuk-do")]),
 ("Smart Bus Shelters", [
   ("Busan smart shelters (bus information terminals included)", "Busan"),
   ("Gwangmyeong smart shelters (bus information terminals included)", "Gwangmyeong-si, Gyeonggi-do"),
   ("Seongnam smart shelter maintenance", "Seongnam-si, Gyeonggi-do")]),
 ("Emergency Vehicle Priority Signal", [
   ("Seoul emergency-vehicle priority signal system", "Seoul"),
   ("Yeongcheon emergency dispatch display", "Yeongcheon-si, Gyeongsangbuk-do"),
   ("Suwon emergency dispatch display", "Suwon-si, Gyeonggi-do"),
   ("Gwangmyeong emergency dispatch display", "Gwangmyeong-si, Gyeonggi-do"),
   ("Yongin emergency dispatch display", "Yongin-si, Gyeonggi-do")]),
 ("Pedestrian Safety · Smart School Zone", [
   ("Gwangmyeong school-zone pedestrian safety system", "Gwangmyeong-si, Gyeonggi-do"),
   ("Gwangmyeong automatic crossing-time extension system", "Gwangmyeong-si, Gyeonggi-do"),
   ("Anyang school-zone advisory display", "Anyang-si, Gyeonggi-do"),
   ("Hwaseong smart pedestrian safety system", "Hwaseong-si, Gyeonggi-do")]),
 ("EV Charging Displays · Other", [
   ("GS Caltex EV charging station displays", "Naegok-dong, Seoul"),
   ("Easy Charger EV charging station displays", "Gimcheon Service Area, Gyeongbu Expressway"),
   ("Andong Sinsijang no-straight-ahead advisory system", "Andong-si, Gyeongsangbuk-do")]),
]
REC_IMG_EN = {
  "Variable Message Signs (VMS)": "vms",
  "Bus Information Terminals (BIT)": "bit",
  "Smart Bus Shelters": "bitx",
  "Emergency Vehicle Priority Signal": "evs2",
  "Pedestrian Safety \u00b7 Smart School Zone": "ssz2",
  "EV Charging Displays \u00b7 Other": "ecs",
}

# ------------------------------------------------------------- certificates
CERTS_EN = [
 ("iso", "ISO", "Quality Management System ISO 9001", "ISO 9001:2015", "iso9001",
  [("Scope", "Design, development and construction of traffic systems"), ("Issue", "Korean certificate")]),
 ("iso", "ISO", "Environmental Management System ISO 14001", "ISO 14001:2015", "iso14001",
  [("Scope", "Design, development and construction of traffic systems"), ("Issue", "Korean certificate")]),
 ("iso", "ISO", "Quality Management System ISO 9001", "ISO 9001:2015", "iso9001-en",
  [("Scope", "Quality Management"), ("Issue", "English certificate")]),
 ("iso", "ISO", "Environmental Management System ISO 14001", "ISO 14001:2015", "iso14001-en",
  [("Scope", "Environmental Management"), ("Issue", "English certificate")]),
 ("kc", "KC", "High-precision GNSS RTK module", "SLv-001", "kc-gnss",
  [("Reg. no.", "R-R-SLv-SLGRO-001"), ("Registered", "22 Feb 2023"), ("Device code", "MOB31 / LTE9, IMT9")]),
 ("kc", "KC", "Bus information terminal SL-BIT", "SL-BIT-TRI", "kc-bit",
  [("Reg. no.", "R-R-SLv-SL-BIT-TRI"), ("Registered", "11 Oct 2023"), ("Variants", "3D8Y · 4D12Y")]),
 ("kc", "KC", "LED module", "SL240M111", "kc-led",
  [("Reg. no.", "R-R-SLv-SL240M111"), ("Registered", "14 Sep 2023"), ("Device code", "VDO11")]),
 ("kc", "KC", "Status control board / controller", "SL_RTU", "kc-rtu",
  [("Reg. no.", "R-R-SLv-SL_RTU"), ("Registered", "10 Nov 2023"), ("Variant", "Ver. 1.00")]),
 ("kc", "KC", "PoE splitter PS01", "SL-PS01", "kc-ps01",
  [("Reg. no.", "R-R-SLv-SL-PS01"), ("Registered", "23 Jan 2024"), ("Device code", "IMI61")]),
 ("kc", "KC", "MCU-VCU control unit", "SL-VCU_12CH", "kc-vcu",
  [("Reg. no.", "R-R-SLv-SL-VCU_12CH"), ("Registered", "9 May 2024"), ("Variants", "10CH · 8CH")]),
 ("kc", "KC", "Standard controller MCU", "SL_MCU", "kc-mcu",
  [("Reg. no.", "R-R-SLv-SL_MCU"), ("Registered", "14 Aug 2024"), ("Device code", "IMC31")]),
 ("kc", "KC", "School-zone advisory display", "SL-SMART-16D32Y", "kc-ssz",
  [("Type", "KC certification"), ("Note", "See original certificate")]),
 ("kc", "KC", "PTZ camera", "SL-P223ID5", "kc-cam",
  [("Type", "KC certification"), ("Note", "See original certificate")]),
 ("tta", "TTA", "TTA test certification · PTZ camera", "SL-P223ID5", "tta-223",
  [("Body", "Telecommunications Technology Association"), ("Issue", "TTA certificate")]),
 ("tta", "TTA", "TTA test certification · PTZ camera", "SL-P230ID5", "tta-230",
  [("Body", "Telecommunications Technology Association"), ("Issue", "TTA certificate")]),
 ("tta", "TTA", "TTA test certification · PTZ camera", "SL-P510ID5", "tta-510",
  [("Body", "Telecommunications Technology Association"), ("Issue", "TTA certificate")]),
 ("eco", "Eco-Label", "Korea Eco-Label · LED display", "EL265", "eco",
  [("Cert. no.", "No. 31489"), ("Valid", "29 Aug 2024 – 26 May 2027"),
   ("Body", "Korea Environmental Industry &amp; Technology Institute")]),
 ("rel", "Test report", "BIT reliability test report", "SL-BIT-BS", "rel-bit",
  [("Report no.", "KR0140-2024-11_3842"), ("Type", "Reliability TRF")]),
 ("rel", "Test report", "Emergency-vehicle display power consumption report", "EVS display", "pwr-evs",
  [("Type", "Power consumption test report")]),
]

# ----------------------------------------------------------------- partners
PUB_EN = ["Hwaseong-si","Gwangmyeong-si","Yongin-si","Seoul Metropolitan Gov.","Anyang-si",
          "Andong-si","Paju-si","Suwon-si","Gwangyang-si","Gimpo-si","Seongnam-si",
          "Daejeon Metropolitan City","Sejong City","Chuncheon-si","Gyeongju-si",
          "Chungcheongnam-do","Cheongju-si","Goyang-si","Yeongcheon-si","Jecheon-si","Jeju Province"]
PRI_EN = [(1, "GS Caltex"), (2, "EASY CHARGER"), (4, "KT"), (5, "SK telecom")]

# ------------------------------------------------- direct production scopes
DIRECT_EN = [
 ("System management",            "Operation outsourcing · Information system maintenance"),
 ("Computers",                    "Bus and vehicle information terminals"),
 ("Signage equipment",            "Guide displays · Traffic information displays · Weather displays"),
 ("Software engineering",         "Packaged software development · Information system development"),
 ("Software maintenance",         "Software maintenance and support services"),
 ("Video equipment · controllers","Video information display units"),
 ("Internet services",            "Internet application development services"),
 ("Data services",                "Big-data analysis services"),
 ("Management information",       "IT infrastructure implementation services"),
]

# ----------------------------------------------------------------- products
PRODS_EN = [
  ("VMS Series",  "Variable Message Sign", "product/vms.html", "vms",
   "Full-colour, ultra-high-brightness LED displays engineered for road-side legibility.",
   ["SL240M111"]),
  ("BIT Series",  "Bus Information Terminal", "product/bit.html", "bit",
   "Stop-side displays showing bus arrival times and route information in real time.",
   ["SL-BIT-TRI", "3D8Y", "4D12Y"]),
  ("ECS Series",  "EV Charging Station Display", "product/ecs.html", "ecs",
   "High-brightness LED panels showing charger availability and state of charge at a glance.",
   ["EL265"]),
  ("GNSS Module", "High-Precision Module", "product/gnss.html", "gnss",
   "u-blox based high-precision GNSS RTK module delivering reliable positioning accuracy.",
   ["SLv-001", "OBE", "BASE"]),
  ("PTZ Camera",  "Pan-Tilt-Zoom Camera", "product/ptz.html", "ptz",
   "Colour imaging in low light with 2D/3D noise reduction and powerful optical zoom.",
   ["SL-P223ID5", "P230ID5", "P510ID5"]),
]

BIZ_EN = [
 ("ITS", "Intelligent Transport System", "business/its.html", "ctrl",
  "Applies advanced technology to road infrastructure so that operation and management are "
  "automated. AI deep-learning models collect and process live traffic data to prevent congestion."),
 ("BIS", "Bus Information System", "business/bis.html", "bit",
  "Tracks buses in service by satellite positioning and announces arrival times and routes "
  "on stop displays and on-board terminals, in text and by voice."),
 ("EVS", "Emergency Vehicle Priority Signal", "business/evs.html", "sign",
  "Tracks emergency vehicles carrying patients by GPS and grants a green signal automatically "
  "as they approach an intersection."),
 ("SSZ", "Smart School Zone", "business/ssz.html", "cam",
  "Warns drivers of hazards inside school zones on LED displays. AI video analysis detects "
  "pedestrians before they step into the road."),
]

ARROW = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4">'
         '<path d="M5 12h14M13 6l6 6-6 6"/></svg>')
PLUS  = ('<svg class="acc-plus" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
         'stroke-width="1.6"><path d="M12 5v14M5 12h14"/></svg>')


# ==================================================================
#  페이지 생성 — build.py 가 헬퍼를 주입한 뒤 pages() 를 호출합니다
# ==================================================================
def pages():
    P = []                                   # (url, title, desc, section, body)
    p2 = "../../"                            # en/company/*, en/business/*, en/product/*
    p1 = "../"                               # en/index.html, en/contact.html

    # ---------------------------------------------------------- CEO message
    greeting = f'''<section class="section"><div class="area-box">
{head("GREETING", "CEO Message", "Welcome to SangLim Technologies.")}
<div class="ceo">
  <figure class="ceo-photo" data-reveal>
    <picture>
      <source srcset="{p2}assets/img/ceo.webp" type="image/webp">
      <img src="{p2}assets/img/ceo.png" alt="Lim Sang-il, CEO of SangLim Technologies" width="666" height="760">
    </picture>
    <figcaption class="ceo-badge">CEO <b>Lim Sang-il</b></figcaption>
  </figure>
  <div class="greet-card" data-reveal data-d="140">
    <p class="q">Boundless responsibility and a pioneering spirit,<br>earning trust that lasts</p>
    <p>Since our founding in April 2021, SangLim Technologies has built advanced traffic systems
    on a foundation of trust, engineering capability and a willingness to take on hard problems,
    contributing to the growth of Korea&rsquo;s transport industry.</p>
    <p>Even against shifting global conditions and the fragmentation of trade, we have reached
    <strong>cumulative revenue of KRW 55 billion</strong> and a
    <strong>corporate credit rating of BBB0</strong> &mdash; an achievement we value all the more
    as a young company, because it reflects the confidence our clients place in us.</p>
    <p>We continue to work on clearing higher market barriers and on identifying and mitigating risk
    early. Today we are extending beyond the domestic market into overseas transport projects,
    growing into a company built for the long term.</p>
    <div class="greet-sign" data-reveal>
      <div class="gs-txt"><span class="role">SangLim Technologies Co., Ltd. &nbsp;CEO</span><span class="name">Lim Sang-il</span></div>
    </div>
  </div>
</div>
</div></section>

<section class="section band"><div class="area-box">
<div class="section-head" data-reveal><span class="eyebrow" style="color:var(--c-accent-bright)">AT A GLANCE</span>
<h2>SangLim in numbers</h2></div>
<div class="stat-grid">
  <div class="stat" data-reveal><b><span class="num" data-count="55">0</span><span class="u">bn KRW</span></b><span>Cumulative revenue</span><i></i></div>
  <div class="stat" data-reveal data-d="100"><b><span class="num">BBB0</span></b><span>Corporate credit rating</span><i></i></div>
  <div class="stat" data-reveal data-d="200"><b><span class="num">2021</span></b><span>Founded</span><i></i></div>
</div>
</div></section>

<section class="section"><div class="area">
{head("COMPANY PROFILE", "Company profile")}
{dl([
  ("Company", COMPANY_EN),
  ("CEO", "Lim Sang-il"),
  ("Founded", "7 April 2021"),
  ("Business reg. no.", BIZNO),
  ("Years in this field", "April 2021 – present"),
  ("Registered fields", "Information &amp; communication works · Software · Engineering<br>"
                        "Intelligent Transport Systems (ITS) · Emergency traffic signal control · "
                        "Smart intersections · Integrated control centres"),
  ("Main business", "ITS solutions / Bus Information Systems (BIS) / Emergency vehicle priority signals / "
                    "Smart school zone solutions<br>"
                    "Bus Information Terminals (BIT) / Variable Message Signs (VMS) / Security cameras / "
                    "Destination signs / High-precision GNSS<br>"
                    "ITS and BIS control-centre maintenance / Field equipment maintenance"),
  ("R&amp;D focus", "Autonomous driving / Smart city / Smart factory / IoT"),
  ("Head office", ADDR_HQ_EN),
  ("Factory", ADDR_FT_EN),
  ("Contact", f'T. <a href="tel:0220831333">{TEL}</a> &nbsp;·&nbsp; E. <a href="mailto:{MAIL}">{MAIL}</a>'),
])}
<div class="lead-box" data-reveal style="margin-top:48px;margin-bottom:0">
<p>Founded in 2021 and starting with the Hwaseong Intelligent Transport System project,
SangLim Technologies has grown into a specialist supplier of traffic solutions and equipment
to major local governments and private companies across Korea.</p></div>
</div></section>'''
    P.append(("company/greeting.html", "CEO Message",
              "A message from the CEO of SangLim Technologies, and our company profile.",
              "company", greeting))

    # --------------------------------------------------------------- history
    ty = ""
    for y, cap, items in HISTORY_EN:
        li = ""
        for k, t, sub, hi in items:
            label, cls = KIND_EN[k]
            sh = f'<span class="tl-sub">{sub}</span>' if sub else ""
            li += (f'<li class="{cls}{" hi" if hi else ""}"><span class="tl-dot"></span>'
                   f'<span class="tl-tag">{label}</span>'
                   f'<span class="tl-txt"><b>{t}</b>{sh}</span></li>')
        ty += (f'<section class="tl-year" id="y{y}" data-year="{y}">'
               f'<div class="tl-head"><div class="tl-y"><span>{y}</span></div>'
               f'<p class="tl-cap">{cap}</p><span class="tl-cnt">{len(items)}</span></div>'
               f'<ul class="tl-list">{li}</ul></section>')
    jumps = "".join(f'<button class="tl-jump" type="button" data-go="y{y}"><i></i><span>{y}</span></button>'
                    for y, _, _ in HISTORY_EN)
    n = sum(len(i) for _, _, i in HISTORY_EN)
    history = f'''<section class="section tl-sec"><div class="area-box">
<div class="section-head" data-reveal><span class="eyebrow">HISTORY</span>
<h2>Our history</h2><p class="lead">Six years since 2021 &mdash; {n} milestones.</p></div>
<div class="tl-wrap">
  <aside class="tl-rail" aria-label="Jump to year">
    <div class="tl-bar"><span class="tl-fill" id="tlFill"></span></div>
    <div class="tl-jumps">{jumps}</div>
  </aside>
  <div class="tl" id="tl">{ty}</div>
</div>
<div class="lead-box" data-reveal style="margin-top:60px;margin-bottom:0">
<p>Beginning with the Hwaseong ITS upgrade in 2021, we have widened both our scope of work and
our geographic reach every year. Registering a corporate R&amp;D centre and gaining venture
certification in 2022 gave us an engineering base; the 59-site expressway EV charging display
programme took us into the private sector in 2024; and the Busan BIMS project opened the
metropolitan market in 2025.</p></div>
</div></section>'''
    P.append(("company/history.html", "History",
              "Six years of projects and certifications since SangLim Technologies was founded in 2021.",
              "company", history))

    # ---------------------------------------------------------- organisation
    org = f'''<section class="section"><div class="area-box">
<div class="section-head" data-reveal><span class="eyebrow">ORGANIZATION</span>
<h2>Organisation</h2><p class="lead">Sales, proposal, delivery and R&amp;D are all carried out in house.</p></div>
<div class="og" id="og">
  <div class="og-l0"><div class="og-node og-ceo" data-og>CEO</div></div>
  <div class="og-line og-line-v"><span></span></div>
  <div class="og-l1">
    <div class="og-col" data-og>
      <div class="og-node og-dept">Technical Sales</div>
      <div class="og-kids"><span class="og-kid">Sales Team 1</span><span class="og-kid">Sales Team 2</span></div>
    </div>
    <div class="og-col" data-og>
      <div class="og-node og-dept">Proposal Planning</div>
      <div class="og-kids"><span class="og-kid">Proposal Team</span><span class="og-kid">Design Team</span></div>
    </div>
    <div class="og-col" data-og>
      <div class="og-node og-dept">Delivery</div>
      <div class="og-kids"><span class="og-kid">Implementation</span><span class="og-kid">Equipment Manufacture</span></div>
    </div>
    <div class="og-col" data-og>
      <div class="og-node og-dept og-rnd">R&amp;D Centre</div>
      <div class="og-kids"><span class="og-kid">IoT Development</span><span class="og-kid">Software Development</span></div>
    </div>
  </div>
  <div class="og-support" data-og><span>Corporate Support</span></div>
</div>
</div></section>'''
    P.append(("company/organization.html", "Organization",
              "How SangLim Technologies is organised.", "company", org))

    # ---------------------------------------------------------- track record
    cats = ""
    for ci, (cname, rows) in enumerate(REC_EN):
        lis = "".join(f'<li><b>{a}</b><span>{b}</span></li>' for a, b in rows)
        _k = REC_IMG_EN.get(cname)
        thumb = f'<span class="rec-thumb">{pimg(_k, p2)}</span>' if _k else ""
        cats += (f'<div class="rec-cat" data-reveal><h3>{thumb}<span class="rec-t">{cname}</span>'
                 f'<span class="cnt">{len(rows)}</span></h3><ul class="rec-list">{lis}</ul></div>')
    total = sum(len(r) for _, r in REC_EN)
    record = f'''<section class="section band"><div class="area-box">
<div class="section-head" data-reveal><span class="eyebrow" style="color:var(--c-accent-bright)">TRACK RECORD</span>
<h2>Track record</h2><p class="lead">SangLim systems are installed and running for local governments
and public bodies across Korea. ({total} installations)</p></div>
{cats}
</div></section>'''
    P.append(("company/record.html", "Track Record",
              f"{total} installations delivered by SangLim Technologies across Korea.",
              "company", record))

    # ---------------------------------------------------------- certificates
    grid = ""
    for cat, tag, title, model, key, rows in CERTS_EN:
        dls = "".join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in rows)
        grid += (f'<figure class="cert" data-cat="{cat}" data-reveal>'
                 f'<button class="cert-img" type="button" data-full="{p2}assets/cert/{key}.jpg" '
                 f'data-cap="{title} — {model}">'
                 f'<img src="{p2}assets/cert/{key}-t.jpg" alt="{title} — {model}" loading="lazy" '
                 f'width="600" height="800"></button>'
                 f'<figcaption><span class="tag tag-{cat}">{tag}</span><h3>{title}</h3>'
                 f'<p class="model">{model}</p><dl>{dls}</dl></figcaption></figure>')
    dp = "".join(f'<li class="dp" data-reveal style="--td:{i*60}ms"><b>{a}</b><span>{b}</span></li>'
                 for i, (a, b) in enumerate(DIRECT_EN))
    cert = f'''<section class="section"><div class="area-box">
<div class="section-head" data-reveal><span class="eyebrow">CERTIFICATION</span>
<h2>Certifications</h2>
<p class="lead">SangLim holds international management-system certifications, KC conformity
registrations for each product, TTA test certifications and the Korea Eco-Label.</p></div>

<div class="cert-stats" data-reveal>
  <div><b>4</b><span>ISO management systems</span></div>
  <div><b>9</b><span>KC conformity registrations</span></div>
  <div><b>3</b><span>TTA test certifications</span></div>
  <div><b>3</b><span>Eco-Label · test reports</span></div>
</div>

<div class="cert-filter" data-reveal>
  <button class="on" data-cat="all">All {len(CERTS_EN)}</button>
  <button data-cat="iso">ISO</button>
  <button data-cat="kc">KC</button>
  <button data-cat="tta">TTA</button>
  <button data-cat="eco">Eco-Label</button>
  <button data-cat="rel">Test reports</button>
</div>

<div class="cert-grid" id="certGrid" data-reveal-stagger="70">{grid}</div>

<div class="lead-box" data-reveal style="margin-top:56px;margin-bottom:0">
<p><strong>KC conformity registration</strong> is granted by the National Radio Research Agency under
Article 58-2(3) of the Radio Waves Act, confirming the electromagnetic compatibility of broadcasting
and communication equipment. Click any certificate to view it full size.</p></div>
</div></section>

<section class="section band"><div class="area-box">
<div class="section-head" data-reveal><span class="eyebrow" style="color:var(--c-accent-bright)">DIRECT PRODUCTION</span>
<h2>Direct Production Certificates</h2>
<p class="lead">{len(DIRECT_EN)} certified categories from the Ministry of SMEs and Startups &mdash;
independent verification that we manufacture and develop in house.</p></div>
<ul class="dp-grid" id="dpGrid">{dp}</ul>
</div></section>

<section class="section"><div class="area">
<div class="section-head" data-reveal><span class="eyebrow">CREDENTIALS</span><h2>Credentials</h2></div>
<div class="cred" data-reveal-stagger="90">
  <div class="cred-i" data-reveal><b data-count="4">0</b><span>Patents</span></div>
  <div class="cred-i" data-reveal><b data-count="2">0</b><span>ISO certifications</span></div>
  <div class="cred-i" data-reveal><b>Yes</b><span>Corporate R&amp;D centre</span></div>
  <div class="cred-i" data-reveal><b>Yes</b><span>TTA certification</span></div>
  <div class="cred-i" data-reveal><b>Yes</b><span>Venture certification</span></div>
  <div class="cred-i" data-reveal><b>+14</b><span>Other credentials</span></div>
</div>
</div></section>

<div class="lb" id="lb">
  <button class="lb-x" type="button" aria-label="Close">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M18 6L6 18M6 6l12 12"/></svg></button>
  <button class="lb-nav lb-prev" type="button" aria-label="Previous">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M15 18l-6-6 6-6"/></svg></button>
  <button class="lb-nav lb-next" type="button" aria-label="Next">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M9 18l6-6-6-6"/></svg></button>
  <img alt="">
  <div class="lb-cap"></div>
</div>'''
    P.append(("company/certification.html", "Certifications",
              "Certifications held by SangLim Technologies.", "company", cert))

    # -------------------------------------------------------------- partners
    pg = ""
    for i, nm in enumerate(PUB_EN, 1):
        pg += (f'<figure class="pt" data-cat="pub" data-reveal>'
               f'<img src="{p2}assets/img/partner/pub-{i:02d}.png" alt="{nm}" loading="lazy">'
               f'<figcaption class="pt-name">{nm}</figcaption></figure>')
    for i, nm in PRI_EN:
        pg += (f'<figure class="pt" data-cat="pri" data-reveal>'
               f'<img src="{p2}assets/img/partner/pri-{i:02d}.png" alt="{nm}" loading="lazy">'
               f'<figcaption class="pt-name">{nm}</figcaption></figure>')
    partners = f'''<section class="section"><div class="area-box">
<div class="section-head" data-reveal><span class="eyebrow">CLIENTS</span><h2>Clients</h2>
<p class="lead">Public bodies and private companies we have worked with.</p></div>
<div class="pt-tabs" data-reveal>
  <button class="on" data-cat="all">All {len(PUB_EN)+len(PRI_EN)}</button>
  <button data-cat="pub">Public sector {len(PUB_EN)}</button>
  <button data-cat="pri">Private sector {len(PRI_EN)}</button>
</div>
<div class="pt-grid" id="ptGrid" data-reveal-stagger="45">{pg}</div>
<div class="lead-box" data-reveal style="margin-top:52px;margin-bottom:0">
<p>We build traffic infrastructure together with local governments, public agencies and private
companies nationwide. Hover a logo to see it in full colour.</p></div>
</div></section>'''
    P.append(("company/partners.html", "Clients",
              "Public and private partners of SangLim Technologies.", "company", partners))

    # ------------------------------------------------------------ directions
    from urllib.parse import quote as _q
    q = _q("60 Haan-ro Gwangmyeong-si Gyeonggi-do SK Techno Park")
    loc = f'''<section class="section"><div class="area">
{head("LOCATION", "Directions", "Our head office and factory are in the same building at Gwangmyeong SK Techno Park.")}

<div class="map-wrap" data-reveal>
  <iframe class="map-frame" title="SangLim Technologies location"
          src="https://www.google.com/maps?q={q}&amp;hl=en&amp;z=17&amp;output=embed"
          loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
  <div class="map-card">
    <span class="map-eyebrow">HEAD OFFICE</span>
    <b>{COMPANY_EN}</b>
    <p>{ADDR_HQ_EN}</p>
    <div class="map-links">
      <a href="https://map.kakao.com/?q={q}" target="_blank" rel="noopener">Kakao Map</a>
      <a href="https://map.naver.com/p/search/{q}" target="_blank" rel="noopener">Naver Map</a>
      <a href="https://www.google.com/maps/search/?api=1&amp;query={q}" target="_blank" rel="noopener">Google Maps</a>
    </div>
  </div>
</div>

{dl([("Head office", ADDR_HQ_EN),
     ("Factory", ADDR_FT_EN),
     ("Phone", f'<a href="tel:0220831333">+82 2-2083-1333</a>'),
     ("Email", f'<a href="mailto:{MAIL}">{MAIL}</a>')])}

<div class="way" data-reveal-stagger="110">
  <article class="way-i" data-reveal>
    <span class="way-ic way-sub"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="3" width="14" height="14" rx="4"/><path d="M5 10h14M8 20l-1.5 2M16 20l1.5 2"/><circle cx="8.5" cy="13.5" r="1"/><circle cx="15.5" cy="13.5" r="1"/></svg></span>
    <h3>Metro</h3>
    <p><b>Seoksu Station</b> (Line 1), then a local bus<br>
    <b>Cheolsan Station</b> (Line 7), then a bus</p>
  </article>
  <article class="way-i" data-reveal>
    <span class="way-ic way-bus"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="13" rx="3"/><path d="M3 11h18M7 21v-2M17 21v-2"/><circle cx="7" cy="14.5" r="1"/><circle cx="17" cy="14.5" r="1"/></svg></span>
    <h3>Bus</h3>
    <p>Alight at <b>Gwangmyeong SK Techno Park</b><br>
    Routes via Soha-dong and Haan-ro</p>
  </article>
  <article class="way-i" data-reveal>
    <span class="way-ic way-car"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M4 15l1.4-5A3 3 0 0 1 8.3 8h7.4a3 3 0 0 1 2.9 2l1.4 5"/><rect x="3" y="15" width="18" height="5" rx="2"/><circle cx="7.5" cy="17.5" r="1"/><circle cx="16.5" cy="17.5" r="1"/></svg></span>
    <h3>By car</h3>
    <p>Near <b>Soha IC</b>, West Coast Expressway<br>
    Enter <b>Gwangmyeong SK Techno Park</b> in your navigation</p>
  </article>
</div>
</div></section>'''
    P.append(("company/location.html", "Directions",
              f"Location and directions for {COMPANY_EN}.", "company", loc))

    # -------------------------------------------------------------- business
    def biz(url, title, eyebrow, lead, body_p, needs_list, sols, desc):
        b = f"""<section class="section"><div class="area">
{head(eyebrow, title)}
<div class="lead-box" data-reveal><p>{lead}</p></div>
<div class="prose" data-reveal><p>{body_p}</p></div>
</div></section>

<section class="section" style="background:var(--c-bg-soft)"><div class="area">
{head("NECESSITY", "Why it matters")}
{needs(needs_list)}
</div></section>

<section class="section"><div class="area-box">
{head("SOLUTION", "Key solutions")}
{solgrid(sols, p2)}
</div></section>"""
        P.append((url, title, desc, "business", b))

    # ── ITS 페이지는 내용이 많아 biz() 대신 직접 구성합니다 ──────────────
    EN_TV = [
      ("AI Detection", "Deep-learning video analytics", "eye",
       "Detects vehicles, pedestrians and two-wheelers alike, and turns the road into numbers &mdash; "
       "volume, speed and occupancy, recalculated second by second."),
      ("Unified Display", "Built in-house, end to end", "panel",
       "VMS roadside signs, BIT bus terminals and charging-station displays are all designed and "
       "manufactured by SangLim, so size and format follow the site rather than the catalogue."),
      ("Center Integration", "One screen for the whole corridor", "hub",
       "Collected information is fed into control-room dashboards and agency systems, so an incident "
       "picked up in the field flows straight into the response procedure."),
      ("Field Reliability", "Designed for the outdoors", "shield",
       "Heat, cold, vibration and lightning are assumed from the start &mdash; and inspection and "
       "maintenance after installation are handled by the manufacturer directly."),
    ]

    EN_FLOW = [
      ("01", "Collect", "ROADSIDE",
       "Detectors and cameras on the road read every vehicle&rsquo;s presence, speed, plate and image, second by second.",
       ["VDS loop / radar detectors", "AVI plate recognition", "CCTV video detection", "GNSS probe data"]),
      ("02", "Process", "CENTRE",
       "AI deep-learning models turn the raw feed into flow states, incident alerts and predicted travel times.",
       ["Volume &amp; occupancy", "Automatic incident detection", "Travel-time prediction", "Historical archive"]),
      ("03", "Deliver", "FIELD",
       "The processed information goes straight back to the road and to the traveller&rsquo;s screen.",
       ["VMS roadside displays", "BIT bus information", "Signal control link", "Open API &amp; apps"]),
    ]
    EN_SVC7 = [
      ("Traffic management", "Signals, incidents and enforcement run as one system"),
      ("Public transport", "Bus position and arrival times delivered to riders"),
      ("Electronic payment", "Tolls and fares settled without stopping"),
      ("Data distribution", "Collected information shared with agencies and industry"),
      ("Value-added services", "Parking, weather and tourism data linked in"),
      ("Intelligent vehicle &amp; road", "Vehicles and roads cooperating over radio"),
      ("Freight operations", "Safety and efficiency for goods vehicles"),
    ]
    EN_CMP = [
      ("Direction", "<b>One way</b> &mdash; the centre pushes information down",
       "<b>Two way</b> &mdash; vehicles and infrastructure exchange it"),
      ("Source", "Roadside detectors and CCTV",
       "Infrastructure <b>plus the moving vehicles themselves</b>"),
      ("Latency", "After collection and processing", "The moment it happens (hundreds of ms)"),
      ("Carriers", "VMS &middot; BIT &middot; signal control",
       'V2V &middot; V2I &middot; V2P &middot; V2N <span class="nw">(WAVE / LTE-V2X)</span>'),
    ]
    EN_POLICY = [
      ("Infrastructure for new modes of mobility",
       "Laying the road foundation that automated vehicles and UAM will need before they arrive."),
      ("Closing the safety blind spots with AI",
       "Video analytics detects pedestrians and two-wheelers that conventional detectors miss."),
      ("A base for user-tailored services",
       "Opening the collected traffic data so private services can build on top of it."),
      ("Support for exporting Korean ITS",
       "Turning technology proven at home into an export industry."),
    ]
    EN_V2X = dict(
      alt="C-ITS V2X concept diagram — vehicles, roadside unit, pedestrian and control centre exchanging information",
      center="Control centre", rsu="Roadside unit", carA="Vehicle A", carB="Vehicle B", ped="Pedestrian",
      cap="In <b>C-ITS</b>, vehicles, the road, pedestrians and the centre all exchange information. "
          "Where classic ITS pushes data one way from a control centre, C-ITS warns everyone "
          "<b>the moment</b> a hazard appears.")

    its_en = f"""<section class="section"><div class="area">
{head("INTELLIGENT TRANSPORT SYSTEMS", "Intelligent Transport System")}
<div class="lead-box" data-reveal><p>An Intelligent Transport System (ITS) applies electronics, control and
communication technology to roads and vehicles, so that traffic operations are managed scientifically and
automatically &mdash; making the network both more efficient and safer.</p></div>
<div class="prose" data-reveal><p>There is a limit to how many lanes you can add. ITS is about
<b>using the road you already have more intelligently</b> &mdash; reading how each vehicle moves, retiming
signals, warning of a queue before it forms, and noticing an incident within seconds.</p>
<p>SangLim builds the whole chain: AI deep-learning detection that <b>collects</b> live traffic data,
the processing that turns it into usable information, and the roadside displays, bus terminals and control
room dashboards that <b>deliver</b> it.</p></div>
</div></section>

<section class="section" style="padding-top:0"><div class="area">
{techvision("SangLim Tech Vision",
  ["From detection on the road",
   "to AI traffic operations,",
   "we build it as one flow"],
  ["The transport infrastructure market has moved past supplying equipment. What matters now is "
   "how the data that equipment collects is processed and operated.",
   "SangLim answers that shift with a single chain &mdash; detection hardware, display hardware and "
   "control-room software, connected as one intelligent transport system."],
  EN_TV)}
</div></section>

<section class="section" style="background:var(--c-bg-soft)"><div class="area">
{head("HOW IT WORKS", "From road data to something a driver can read",
      "A sensor reading passes through three stages before it becomes a sentence on a sign.")}
{its_flow(EN_FLOW)}
</div></section>

<section class="section"><div class="area">
{head("SERVICE DOMAINS", "Seven service domains")}
{its_services(EN_SVC7)}
</div></section>

<section class="section dark-sec dark-sec2"><div class="area">
  <div class="section-head is-dark" data-reveal><span class="eyebrow">C-ITS</span>
  <h2>Cooperative ITS</h2>
  <p class="lead">Classic ITS <em>sends information down</em> from a control centre.
  C-ITS lets vehicles, roads and pedestrians <em>exchange it directly</em> &mdash; the precondition for
  automated driving.</p></div>
{cits_viz(EN_V2X)}
{cits_table(EN_CMP, "Classic ITS", "C-ITS", "next generation")}
</div></section>

<section class="section"><div class="area">
{head("NECESSITY", "Why it matters")}
{needs(["Improved safety at accident-prone locations",
        "Higher accuracy in vehicle recognition",
        "Relief for chronically congested sections",
        "Detection of pedestrians and two-wheelers that sensors miss"])}
</div></section>

<section class="section" style="background:var(--c-bg-soft)"><div class="area-box">
{head("SOLUTION", "Key solutions")}
{solgrid([("Variable Message Sign (VMS)", "sign",
           "Roadside displays that deliver live traffic information to drivers", "p_vms",
           "../product/vms.html"),
          ("Intelligent camera", "cam",
           "AI video analysis that recognises vehicles and collects volume data", "p_cam",
           "../product/ptz.html"),
          ("Control room dashboard", "sw",
           "Software that monitors the whole network on one screen and drives the response", "p_dash",
           "../product/dashboard.html"),
          ("Field controller", "ctrl",
           "On-site unit that ties detection and display equipment back to the centre", "p_ctrl")], p2)}
</div></section>

<section class="section"><div class="area">
{head("POLICY", "Policy direction &mdash; ITS Master Plan 2030",
      "Korea&rsquo;s Ministry of Land, Infrastructure and Transport set out four strategies under the vision of "
      "<em>&ldquo;green, safe and seamless people-centred transport services&rdquo;</em>.")}
{policy_grid(EN_POLICY, "STRATEGY")}
<p class="src" data-reveal>Source: Ministry of Land, Infrastructure and Transport,
&ldquo;Intelligent Transport Systems Master Plan 2030&rdquo; (2021) &middot; MOLIT ITS policy materials</p>
</div></section>"""
    P.append(("business/its.html", "Intelligent Transport System",
              "Real-time traffic data collection and processing built on AI deep learning.",
              "business", its_en))

    # ── BIS 페이지도 국문과 동일한 구성으로 직접 작성합니다 ────────────────
    EN_BIS_TV = [
      ("Live Tracking", "Second-by-second position", "hub",
       "Every bus in service reports its GPS position over LTE. Stop arrivals and route deviations "
       "are judged automatically from that stream."),
      ("Arrival Prediction", "Not just where &mdash; when", "eye",
       "Position alone is not an answer. Link travel times and historical running data are combined "
       "into a &ldquo;minutes away&rdquo; figure, and recalculated whenever conditions change."),
      ("Multi-channel", "Text and voice together", "panel",
       "The same information goes out to the stop-side display, the on-board unit and voice "
       "announcement at once &mdash; whether the passenger reads it or hears it."),
      ("Operation Data", "Operations you can audit", "shield",
       "Headway and route compliance are left behind as data. Missed and delayed runs can be caught "
       "during service rather than reconstructed afterwards."),
    ]

    EN_BIS_FLOW = [
      ("01", "Collect", "ON BOARD",
       "The terminal on the bus reads its own position second by second and sends it to the centre.",
       ["GPS positioning", "LTE uplink", "Stop-arrival detection", "Route matching"]),
      ("02", "Predict", "CENTRE",
       "Position, link travel state and historical running data are combined into an expected arrival time.",
       ["Link travel time", "Historical data", "Congestion applied", "Continuous recalculation"]),
      ("03", "Inform", "AT THE STOP",
       "The same information is published to the stop, the vehicle and the app simultaneously.",
       ["BIT displays", "On-board unit", "TTS voice", "Open API"]),
    ]

    EN_BIS_SPEC = [
      ("High-brightness LED", "High-brightness LEDs keep the display readable in direct sunlight. Route number, "
       "expected arrival time and current position sit on one screen."),
      ("Text and voice together", "Information is announced by voice alongside the display, so passengers who "
       "cannot rely on sight still receive it."),
      ("A line-up per stop size", "SL-BIT-TRI, 3D8Y, 4D12Y and others &mdash; the number of display lines and the "
       "cabinet size are chosen to match the route count and the stop."),
      ("Built for the outdoors", "Designed on the assumption of heat, cold, vibration and lightning, with "
       "inspection and maintenance after installation handled by the manufacturer directly."),
    ]

    bis_en = f"""<section class="section"><div class="area">
{head("BUS INFORMATION SYSTEM", "Bus Information System")}
<div class="lead-box" data-reveal><p>A Bus Information System (BIS) locates buses in service by GPS and sends
arrival times and route details over LTE to stop-side displays and on-board terminals, presented both as
text and as voice announcements.</p></div>
</div></section>

<section class="section" style="padding-top:0"><div class="area">
{techvision("SangLim Tech Vision",
  ["From the position of the bus",
   "to the sign at the stop,",
   "we keep the line unbroken"],
  ["Most of the time spent waiting for a bus is really spent not knowing when it will come. "
   "One accurate arrival figure noticeably shortens how long the wait feels.",
   "SangLim designs and manufactures the BIT terminals that stand at the stop, and connects the whole "
   "span &mdash; position collection, prediction and display &mdash; as a single system."],
  EN_BIS_TV)}
</div></section>

<section class="section" style="background:var(--c-bg-soft)"><div class="area">
{head("HOW IT WORKS", "How do we know where the bus is",
      "What it takes for one coordinate leaving the bus to become &ldquo;3 min&rdquo; on the sign at the stop.")}
{its_flow(EN_BIS_FLOW)}
</div></section>

<section class="section dark-sec dark-sec2"><div class="area">
  <div class="section-head is-dark" data-reveal><span class="eyebrow">BIT TERMINAL</span>
  <h2>The unit that stands at the stop</h2>
  <p class="lead">The BIT (Bus Information Terminal) is the only part of the system a passenger actually
  meets. If it cannot be read, the rest of the system means nothing.</p></div>
  <div class="dsol">
    <figure class="dsol-fig" data-reveal data-speed="0.06">
      <span class="dsol-glow"></span>{pimg("bit", p2)}
    </figure>
    <div class="dsol-body">
      <p class="dsol-lead" data-reveal>Route number, expected arrival time and current position on a single
      screen &mdash; so someone standing at the stop can decide the moment they look up.</p>
      {dspec(EN_BIS_SPEC)}
    </div>
  </div>
</div></section>

<section class="section"><div class="area">
{head("NECESSITY", "Why it is needed")}
{needs(["Removing the uncertainty from waiting for a bus",
        "Better passenger experience at the stop and on board",
        "Operating data for headway and route management",
        "Voice announcement for passengers with reduced mobility"])}
</div></section>

<section class="section" style="background:var(--c-bg-soft)"><div class="area-box">
{head("SOLUTION", "Key solutions")}
{solgrid([("Bus Information Terminal (BIT)", "bit",
           "Stop-side display showing arrival times and route information", "p_bit",
           "../product/bit.html"),
          ("On-board equipment (OBE)", "gnss",
           "Measures position by GPS and reports it to the centre over the wireless network", "p_gnss",
           "../product/gnss.html"),
          ("Operations software", "sw",
           "Monitors terminal health and distributes passenger information", "p_bus"),
          ("Processing and control software", "ctrl",
           "Turns raw position data into accurate arrival predictions", "p_proc")], p2)}
</div></section>"""
    P.append(("business/bis.html", "Bus Information System",
              "An integrated GPS and LTE solution for bus tracking and passenger information.",
              "business", bis_en))


    biz("business/evs.html", "Emergency Vehicle Priority Signal", "EMERGENCY VEHICLE PRIORITY",
        "When an ambulance is carrying a patient to hospital, the urban safety control centre "
        "tracks it by GPS and grants a green signal automatically as the vehicle approaches "
        "each intersection.",
        "The system began as a locally controlled deployment and is now being rolled out with "
        "central control.",
        ["Dispatch delays caused by chronic congestion",
         "Rising number of collisions involving emergency vehicles",
         "Protecting the golden hour for patients"],
        [("Emergency dispatch advisory display", "sign",
          "Warns other drivers of an approaching emergency vehicle before the intersection",
          "p_evsled")],
        "GPS-based signal priority that protects the golden hour for emergency patients.")

    biz("business/ssz.html", "Smart School Zone", "SMART SCHOOL ZONE",
        "The Smart School Zone system warns drivers and pedestrians of hazards inside a "
        "children&rsquo;s protection zone on LED displays, preventing collisions before they happen.",
        "AI camera analysis detects pedestrians and links to enforcement of illegal parking and "
        "stop-line violations &mdash; an approach now being adopted by a growing number of local "
        "governments.",
        ["Improved safety at accident-prone locations",
         "Higher accuracy in pedestrian detection",
         "Active prevention rather than after-the-fact enforcement"],
        [("Smart school-zone display", "sign",
          "Warns the driver the moment a pedestrian is detected"),
         ("Intelligent camera", "cam",
          "AI video detection that watches the whole protection zone")],
        "Pedestrian safety in school zones, built on AI video analysis.")

    # -------------------------------------------------------------- products
    def prod(url, title, desc, lead, specs, icon, after="", before=""):
        headline = (f'<div class="section-head is-dark" data-reveal><span class="eyebrow">MAIN PRODUCT</span>'
                    f'<h2>{title}</h2></div>') if before else head("MAIN PRODUCT", title)
        b = f"""{before}<section class="section{" dark-sec" if before else ""}"><div class="area">
{headline}
<div class="sol" data-reveal>
  <div class="sol-media{" sol-photo" if icon in PROD_IMG else ""}{" sol-dark" if before else ""}">{pimg(icon, p2) or ICONS[icon]}</div>
  <div class="sol-body">
    <p class="{"dsol-lead" if before else ""}" style="font-size:var(--fs-lead);{"" if before else "color:var(--c-ink);"}font-weight:var(--w-read);letter-spacing:-.012em;line-height:1.8">{lead}</p>
    {dspec(specs) if before else spec(specs)}
  </div>
</div>
</div></section>""" + after
        P.append((url, title, desc, "product", b))

    prod("product/vms.html", "Variable Message Sign (VMS)",
         "Roadside displays presenting live traffic information.",
         "Full-colour, ultra-high-brightness LED equipment engineered for legibility on the road.",
         [("Ultra-high-brightness LED", "Full-colour ultra-high-brightness LEDs chosen for road-side legibility"),
          ("Thermally efficient design", "Module-integrated packaging that simplifies maintenance and service"),
          ("Robust enclosure", "Waterproof, dust-proof and heat-managed housing with louvres and cooling fans to protect equipment life"),
          ("Self-diagnostics", "Module power and display self-monitoring enables remote inspection")], "vms")

    prod("product/bit.html", "Bus Information Terminal (BIT)",
         "Stop-side displays for bus arrival information.",
         "Installed at bus stops to present arrival times and route information to waiting passengers.",
         [("Full-colour ultra-high-brightness LED", "Full-colour ultra-high-brightness LEDs chosen for legibility"),
          ("Injection-moulded LED assembly", "Reduced module bezels make the panel read as a single display, and tight LED pitch keeps text crisp"),
          ("Smart cooling system", "Internal fans linked to the monitoring board prevent heat from shortening equipment life"),
          ("Remote reboot", "Faults can be cleared from the control centre without a site visit; an encrypted lock supports remote enclosure access")], "bit")

    prod("product/ecs.html", "EV Charging Station Display",
         "Displays presenting EV charging status to drivers.",
         "High-brightness LEDs present charger availability and state of charge on a bright, legible screen.",
         [("Purpose", "Tells drivers at a glance whether a charger is free and how far a charge has progressed"),
          ("Expected benefit", "Improves the charging experience and supports wider EV adoption in Korea")], "ecs",
         before=ecs_show(p2, "en"))

    prod("product/gnss.html", "High-Precision GNSS Module",
         "Bus positioning module that moves the coordinate baseline from about 10&nbsp;m to about 2&nbsp;cm.",
         "Built to deliver more accurate bus information: RTK correction raises the baseline of the position "
         "data from roughly 10&nbsp;m to roughly 2&nbsp;cm, on modules from u-blox, the global leader in "
         "compact high-precision GNSS.",
         [("2&nbsp;cm-level positioning", "RTK correction from a base station lifts coordinate precision far above ordinary GPS, which is accurate to around 10&nbsp;m."),
          ("GPS module", "Uses modules from u-blox, the worldwide leader in compact high-precision GNSS, for accuracy and reliability."),
          ("RTK correction", "Registered as SANGLIM_GNSS_RTK (OBE, BASE) &mdash; on-board equipment paired with a base station."),
          ("KC electromagnetic compatibility", "Passed KC EMC testing, protecting the safety of drivers and passengers on board."),
          ("LED status indicator", "Status LEDs show upgrade progress and operating state right there on site.")], "gnss",
         before=gnss_show(p2, "en"),
         after="\n" + gnss_map(p2, "en"))

    P.append(("product/dashboard.html", "Control Wall Dashboard",
              "An ITS control wall that brings traffic, safety, signal and bus data onto one screen.",
              "product", dash_page(p2, "en")))
    P.append(("product/ptz.html", "PTZ Camera",
              "Pan-tilt-zoom camera for traffic and security monitoring.",
              "product", ptz_page(p2, "en")))

    # ------------------------------------------------------------ R&D centre
    rnd = f"""<section class="section"><div class="area">
{head("R&amp;D CENTER", "Corporate R&amp;D Centre", "Established 2022 &middot; developing advanced traffic information systems")}
<div class="lead-box" data-reveal><p>Registered as a corporate R&amp;D centre in 2022, the SangLim
research team has led our work on advanced traffic information systems. Our researchers have
delivered Intelligent Transport Systems, Bus Information Systems, emergency-vehicle priority
services and smart school-zone services for major local governments across Korea, and the centre
continues to earn recognition for its engineering work.</p></div>
</div></section>

<section class="section" style="background:var(--c-bg-soft)"><div class="area-box">
{head("R&amp;D VISION", "Research vision")}
<div class="rnd-grid" data-reveal-stagger="120">
  <article class="rnd-card" data-reveal>
    <span class="n">CORE</span><h3>Solution delivery</h3>
    <p>Traffic-sector solutions are our core growth engine. Our solutions are built for high
    availability and data integrity, and we submit them for independent evaluation by accredited
    bodies so that usability keeps improving.</p>
  </article>
  <article class="rnd-card" data-reveal>
    <span class="n">MID-LONG TERM</span><h3>System enhancement</h3>
    <p>Using the capability built through research and delivery, we aim to offer enhancement
    programmes for systems already in service &mdash; and from there to develop solutions strong
    enough for overseas markets.</p>
  </article>
  <article class="rnd-card" data-reveal>
    <span class="n">NEW GROWTH</span><h3>New system development</h3>
    <p>We want to move past the limits of existing traffic system specifications. Our current work
    covers the convergence of deployed systems with AI, and the migration of those systems to the
    cloud.</p>
  </article>
</div>
</div></section>"""
    P.append(("company/rnd.html", "Corporate R&D Centre",
              "The SangLim Technologies corporate R&D centre and our research vision.",
              "company", rnd))

    # --------------------------------------------------------------- contact
    contact = f"""<section class="section"><div class="area">
{head("CONTACT", "Contact us", "Leave your requirements and a member of our team will get back to you.")}
<div class="split" style="align-items:start">
  <div data-reveal>
    {dl([("Phone", '<a href="tel:0220831333">+82 2-2083-1333</a>'),
         ("Email", f'<a href="mailto:{MAIL}">{MAIL}</a>'),
         ("Head office", ADDR_HQ_EN),
         ("Factory", ADDR_FT_EN)])}
  </div>
  <form class="cform" id="cform" data-reveal data-d="120" novalidate
        data-mail="{MAIL}" data-endpoint="" data-lang="en">
    <div class="form-grid">
      <div class="field"><label for="f-name">Name <b class="req">*</b></label>
        <input id="f-name" name="name" type="text" placeholder="Jane Doe" required autocomplete="name"></div>
      <div class="field"><label for="f-org">Organisation</label>
        <input id="f-org" name="org" type="text" placeholder="City of ..." autocomplete="organization"></div>
      <div class="field"><label for="f-tel">Phone</label>
        <input id="f-tel" name="tel" type="tel" placeholder="+82 10-0000-0000" autocomplete="tel"></div>
      <div class="field"><label for="f-mail">Email <b class="req">*</b></label>
        <input id="f-mail" name="email" type="email" placeholder="name@example.com" required autocomplete="email"></div>
      <div class="field full"><label for="f-msg">Message <b class="req">*</b></label>
        <textarea id="f-msg" name="message" required placeholder="Tell us which system you are considering, along with timeline and budget range, and we can be more specific in our reply."></textarea></div>
    </div>
    <div class="form-act">
      <button type="submit" class="btn btn-primary">Send enquiry
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M5 12h14M13 6l6 6-6 6"/></svg></button>
      <button type="button" class="btn btn-line cf-copy">Copy text</button>
    </div>
    <p class="form-msg" role="status" aria-live="polite" hidden></p>
    <p class="form-note">&#8251; <b>Send enquiry</b> opens a message to
    <a href="mailto:{MAIL}" style="color:var(--c-brand);font-weight:var(--w-mid)">{MAIL}</a>
    with everything you wrote already filled in &mdash; just press send.<br>
    If no mail app opens, use <b>Copy text</b> and paste it into your own mail.</p>
  </form>
</div>
</div></section>"""
    P.append(("contact.html", "Contact Us",
              f"Contact {COMPANY_EN}. Phone +82 2-2083-1333.", "contact", contact))

    # ------------------------------------------------------------------ home
    hero = f"""<section class="hero" id="hero">
  <div class="hero-media">
    <video id="heroVid" playsinline muted loop autoplay preload="metadata"
           poster="{p1}assets/video/hero-poster.jpg" data-hd="{p1}assets/video/hero">
      <source src="{p1}assets/video/hero-720.webm" type="video/webm">
      <source src="{p1}assets/video/hero-720.mp4" type="video/mp4">
    </video>
  </div>
  <div class="hero-scrim"></div>
  <div class="hero-grid"></div>
  <div class="hero-inner">
    <h1 class="hero-h">
      <span class="reveal-line"><span class="thin">Proven engineering,</span></span>
      <span class="reveal-line"><span><span class="hl"><em class="accent">safer roads</em></span> for everyone</span></span>
      <span class="reveal-line"><span>and better traffic systems</span></span>
    </h1>
    <p class="hero-sub">From protecting the golden hour for ambulances to keeping children safe on
      the way to school, SangLim Technologies builds traffic infrastructure that puts
      <b>people&rsquo;s safety</b> first.</p>
    <div class="hero-cta">
      <a href="#business" class="btn btn-primary">Our business{ARROW}</a>
      <a href="company/record.html" class="btn btn-ghost">Track record</a>
    </div>
  </div>
  <div class="scroll-cue"></div>
  <div class="hero-fade"></div>
</section>"""

    BIZ_TV_EN = [
      ("Intelligent Transport", "ITS", "hub",
       "Applies advanced technology to road infrastructure so that operation and management are "
       "automated. AI deep-learning models collect and process live traffic data to prevent congestion.",
       "business/its.html"),
      ("Bus Information", "BIS", "panel",
       "Tracks buses in service by satellite positioning and announces arrival times and routes "
       "on stop displays and on-board terminals, in text and by voice.",
       "business/bis.html"),
      ("Emergency Priority", "EVS", "siren",
       "Tracks emergency vehicles carrying patients by GPS and grants a green signal automatically "
       "as they approach an intersection.",
       "business/evs.html"),
      ("Smart School Zone", "SSZ", "shield",
       "Warns drivers of hazards inside school zones on LED displays. AI video analysis detects "
       "pedestrians before they step into the road.",
       "business/ssz.html"),
    ]

    acc = ""
    for i, (ser, name, url, icon, desc, models) in enumerate(PRODS_EN):
        chips = "".join(f'<span>{m}</span>' for m in models)
        acc += (f'<article class="acc-item{" is-open" if i==0 else ""}" data-cursor="VIEW">' +
                accfig(icon, p1) +
                f'<div class="acc-mini"><h3>{name}</h3><p>#{models[0]}</p></div>{PLUS}'
                f'<div class="acc-full"><span class="ser">{ser}</span><h3>{name}</h3>'
                f'<p class="desc">{desc}</p><div class="acc-models">{chips}</div>'
                f'<a class="acc-go" href="{url}">View details {ARROW}</a></div></article>')

    strip = "".join(f'<img src="{p1}assets/img/partner/pub-{i:02d}.png" alt="{nm}" loading="lazy">'
                    for i, nm in enumerate(PUB_EN, 1))

    home_body = f"""{hero}
<section class="section" style="background:var(--c-bg-soft)" id="business"><div class="area">
{techvision("BUSINESS AREA",
  ["From intelligent transport",
   "to smart school zones,",
   "the whole of the road"],
  ["Detection equipment out on the road, display equipment standing at stops and intersections, "
   "and the control software that ties the two together. All four of SangLim&rsquo;s business "
   "areas rest on the same technical base.",
   "We do not stop at supplying the equipment &mdash; we stay responsible for how the collected "
   "data is actually used in the field. Open a card to see each area."],
  BIZ_TV_EN)}
</div></section>

<section class="section"><div class="area-box">
{head("MAIN PRODUCT", "Our products", "Hover a card to open the product details.")}
<div class="acc" id="prodAcc" data-reveal>{acc}</div>
</div></section>

<section class="section" style="padding-block:clamp(46px,6vw,80px)"><div class="area-wrap">
<div class="section-head" data-reveal style="margin-bottom:34px;text-align:center;max-width:none">
<span class="eyebrow">PARTNERS</span>
<h2 style="font-size:clamp(1.4rem,2.2vw,2rem)">Working with local governments across Korea</h2></div>
<div class="pt-strip" data-reveal><div class="pt-track" id="ptTrack">{strip}</div></div>
<div class="pt-more"><a href="company/partners.html" class="btn btn-primary">See all clients{ARROW}</a></div>
</div></section>

<section class="section band"><div class="area-box">
<div class="section-head" data-reveal><span class="eyebrow" style="color:var(--c-accent-bright)">TRACK RECORD</span>
<h2>Track record</h2><p class="lead">SangLim systems are installed and running for local governments
and public bodies across Korea.</p></div>
<div style="margin-top:8px" data-reveal>
  <a href="company/record.html" class="btn btn-ghost" style="border-color:rgba(255,255,255,.35);color:#fff">See all installations{ARROW}</a>
</div>
</div></section>"""
    P.append(("index.html", "Intelligent Transport Systems",
              "SangLim Technologies builds intelligent transport systems, bus information systems, "
              "emergency vehicle priority signals and smart school zones across Korea.",
              "", home_body, True))

    return P
