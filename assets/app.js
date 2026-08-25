/* ==================================================================
   상림기술 GNSS 메인 — 인터랙션
   ================================================================== */
const reduce = matchMedia('(prefers-reduced-motion:reduce)').matches;

/* ---------- 1) 헤더 고정 + 히어로 등장 ---------- */
const header = document.getElementById('header');
const onScroll = () => header.classList.toggle('stuck', scrollY > 40);
addEventListener('scroll', onScroll, {passive:true}); onScroll();
const heroEl = document.getElementById('hero');   // 서브페이지엔 없음
if (heroEl) {
  addEventListener('load', () => heroEl.classList.add('in'));
  setTimeout(() => heroEl.classList.add('in'), 350);
}

/* ---------- 2) 모바일 드로어 (GNB 복제) ---------- */
(function(){
  const gnb=document.querySelector('.gnb'), drawer=document.getElementById('drawer');
  const tog=document.getElementById('navtog'), dim=document.getElementById('dim');
  gnb.querySelectorAll(':scope>li').forEach(li=>{
    const link=li.querySelector(':scope>a'), sub=li.querySelector(':scope>.gnb-2dep ul');
    const item=document.createElement('div'); item.className='drawer-item';
    const btn=document.createElement('button'); btn.type='button'; btn.textContent=link.textContent.trim();
    item.appendChild(btn);
    if(sub){
      const wrap=document.createElement('div'); wrap.className='drawer-sub';
      wrap.appendChild(sub.cloneNode(true)); item.appendChild(wrap);
      btn.addEventListener('click',()=>item.classList.toggle('on'));
    } else { btn.addEventListener('click',()=>{location.hash=link.getAttribute('href');close();}); }
    drawer.querySelectorAll('.drawer-sub a, .drawer-item>button').forEach; drawer.appendChild(item);
  });
  drawer.querySelectorAll('a').forEach(a=>a.addEventListener('click',close));
  const lock=b=>{if(b){const w=innerWidth-document.documentElement.clientWidth;
    document.documentElement.style.setProperty('--scrollbar-w',w+'px');document.body.classList.add('is-locked');}
    else{document.body.classList.remove('is-locked');document.documentElement.style.setProperty('--scrollbar-w','0px');}};
  function open(){tog.classList.add('on');drawer.classList.add('on');dim.classList.add('on');tog.setAttribute('aria-expanded','true');lock(true);}
  function close(){tog.classList.remove('on');drawer.classList.remove('on');dim.classList.remove('on');tog.setAttribute('aria-expanded','false');lock(false);}
  tog.addEventListener('click',()=>drawer.classList.contains('on')?close():open());
  dim.addEventListener('click',close);
  addEventListener('keydown',e=>{if(e.key==='Escape')close();});
})();

/* ---------- 3) reveal (IntersectionObserver) ---------- */
(function(){
  document.querySelectorAll('[data-reveal-stagger]').forEach(p=>{
    const step=+p.dataset.revealStagger||110;
    p.querySelectorAll('[data-reveal]').forEach((c,i)=>c.style.setProperty('--d',(i*step)+'ms'));
  });
  document.querySelectorAll('[data-reveal][data-d]').forEach(el=>el.style.setProperty('--d',el.dataset.d+'ms'));
  const io=new IntersectionObserver((es)=>{es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});},
    {threshold:.01,rootMargin:'0px 0px -6% 0px'});
  document.querySelectorAll('[data-reveal]').forEach(el=>io.observe(el));

  /* 백스톱 — End 키·빠른 휠 등으로 화면을 건너뛰면 IntersectionObserver 가
     중간 요소를 놓칠 수 있습니다. 이미 지나간 요소는 강제로 노출시킵니다. */
  let tick=false;
  const sweep=()=>{
    document.querySelectorAll('[data-reveal]:not(.in)').forEach(el=>{
      if(el.getBoundingClientRect().top < innerHeight*0.94){
        el.classList.add('in'); io.unobserve(el);
      }
    });
  };
  addEventListener('scroll',()=>{
    if(tick) return; tick=true;
    requestAnimationFrame(()=>{ sweep(); tick=false; });
  },{passive:true});
  addEventListener('load',sweep);
  addEventListener('resize',sweep,{passive:true});
})();

/* ---------- 4) 숫자 카운터 ---------- */
(function(){
  const run=el=>{
    const end=+el.dataset.count, dec=+el.dataset.dec||0, pre=el.dataset.pre||'', dur=1400, t0=performance.now();
    const step=t=>{let k=Math.min(1,(t-t0)/dur); k=1-Math.pow(1-k,3);
      let v=end*k; el.textContent=pre+ (dec?v.toFixed(dec):Math.round(v).toLocaleString());
      if(k<1)requestAnimationFrame(step); else el.textContent=pre+(dec?end.toFixed(dec):end.toLocaleString());};
    requestAnimationFrame(step);
  };
  const io=new IntersectionObserver((es)=>{es.forEach(e=>{if(e.isIntersecting){run(e.target);io.unobserve(e.target);}});},{threshold:.6});
  document.querySelectorAll('[data-count]').forEach(el=>io.observe(el));
})();

/* ---------- 5) 탭 ---------- */
(function(){
  const btns=[...document.querySelectorAll('#tablist .tab-btn')];
  const panels=[...document.querySelectorAll('#tabpanels .tab-panel')];
  btns.forEach((b,i)=>{
    b.setAttribute('role','tab');
    b.addEventListener('click',()=>{btns.forEach(x=>x.classList.remove('on'));panels.forEach(x=>x.classList.remove('on'));
      b.classList.add('on');panels[i].classList.add('on');ScrollTrigger&&ScrollTrigger.refresh&&ScrollTrigger.refresh();});
    b.addEventListener('keydown',e=>{if(e.key==='ArrowRight'||e.key==='ArrowLeft'){e.preventDefault();
      const n=e.key==='ArrowRight'?(i+1)%btns.length:(i-1+btns.length)%btns.length;btns[n].focus();btns[n].click();}});
  });
})();

/* ---------- 6) GSAP 패럴랙스 (data-speed) ---------- */
(function(){
  if(!window.gsap||!window.ScrollTrigger||reduce)return;
  gsap.registerPlugin(ScrollTrigger);
  ScrollTrigger.matchMedia({'(min-width:801px)':()=>{
    document.querySelectorAll('[data-speed]').forEach(el=>{
      const sp=parseFloat(el.dataset.speed)||0, dist=(el.offsetHeight||300)*sp;
      gsap.fromTo(el,{y:0},{y:dist,ease:'none',
        scrollTrigger:{trigger:el,start:'top bottom',end:'bottom top',scrub:1,invalidateOnRefresh:true}});
    });
  }});
  addEventListener('load',()=>ScrollTrigger.refresh());
})();

/* ---------- 7) to-top ---------- */
(function(){
  const b=document.getElementById('totop');
  addEventListener('scroll',()=>b.classList.toggle('on',scrollY>innerHeight*.7),{passive:true});
  b.addEventListener('click',()=>scrollTo({top:0,behavior:'smooth'}));
})();

/* ---------- 9) 인증현황 — 필터 + 라이트박스 ---------- */
(function(){
  const grid = document.getElementById('certGrid');
  if(!grid) return;
  const cards = [...grid.querySelectorAll('.cert')];

  /* 카테고리 필터 */
  document.querySelectorAll('.cert-filter button').forEach(btn=>{
    btn.addEventListener('click',()=>{
      document.querySelectorAll('.cert-filter button').forEach(b=>b.classList.remove('on'));
      btn.classList.add('on');
      const c = btn.dataset.cat;
      cards.forEach(el=>el.classList.toggle('hide', c!=='all' && el.dataset.cat!==c));
    });
  });

  /* 라이트박스 */
  const lb = document.getElementById('lb');
  const img = lb.querySelector('img');
  const cap = lb.querySelector('.lb-cap');
  let list = [], idx = 0;

  const show = i => {
    list = cards.filter(c=>!c.classList.contains('hide'));
    idx = (i + list.length) % list.length;
    const b = list[idx].querySelector('.cert-img');
    img.src = b.dataset.full;
    img.alt = b.dataset.cap || '';
    cap.textContent = `${b.dataset.cap}  (${idx+1}/${list.length})`;
  };
  const open = el => {
    list = cards.filter(c=>!c.classList.contains('hide'));
    show(list.indexOf(el));
    lb.classList.add('on');
    if(window.SL && SL.lockScroll) SL.lockScroll(true); else document.body.classList.add('is-locked');
  };
  const close = () => {
    lb.classList.remove('on'); img.removeAttribute('src');
    if(window.SL && SL.lockScroll) SL.lockScroll(false); else document.body.classList.remove('is-locked');
  };

  cards.forEach(c=>c.querySelector('.cert-img').addEventListener('click',()=>open(c)));
  lb.querySelector('.lb-x').addEventListener('click',close);
  lb.querySelector('.lb-prev').addEventListener('click',e=>{e.stopPropagation();show(idx-1);});
  lb.querySelector('.lb-next').addEventListener('click',e=>{e.stopPropagation();show(idx+1);});
  lb.addEventListener('click',e=>{ if(e.target===lb||e.target===img) close(); });
  addEventListener('keydown',e=>{
    if(!lb.classList.contains('on')) return;
    if(e.key==='Escape') close();
    if(e.key==='ArrowRight') show(idx+1);
    if(e.key==='ArrowLeft') show(idx-1);
  });
})();

/* ---------- 10) 스크롤 텍스트 필 ---------- */
(function(){
  const lines = [...document.querySelectorAll('.fill-line')];
  if(!lines.length) return;

  // 모션 최소화 설정이면 즉시 채움
  if(reduce){ lines.forEach(l=>l.classList.add('is-done')); return; }

  if(window.gsap && window.ScrollTrigger){
    gsap.registerPlugin(ScrollTrigger);
    ScrollTrigger.matchMedia({
      /* PC — 스크롤에 물려 한 줄씩 차오름 */
      '(min-width:801px)':()=>{
        lines.forEach((el,i)=>{
          gsap.fromTo(el,{backgroundSize:'0% 100%'},{
            backgroundSize:'100% 100%', ease:'none',
            scrollTrigger:{
              trigger: el,
              start: `top bottom-=${180 + i*40}`,   // 줄마다 시작을 밀어 순차 진행
              end:   `top center-=${i*30}`,
              scrub: 0.6,
              invalidateOnRefresh: true,
            }
          });
        });
      },
      /* 모바일 — 효과 해제, 바로 표시 */
      '(max-width:800px)':()=>{ lines.forEach(l=>l.classList.add('is-done')); }
    });
  } else {
    lines.forEach(l=>l.classList.add('is-done'));   // GSAP 없으면 그냥 표시
  }
})();

/* ---------- 11) 커스텀 마우스 포인터 ---------- */
(function(){
  if(matchMedia('(hover:none)').matches || innerWidth<=800 || reduce) return;

  const dot  = document.createElement('div'); dot.className='cursor';
  const lbl  = document.createElement('span'); dot.appendChild(lbl);
  const ring = document.createElement('div'); ring.className='cursor-ring';
  document.body.append(ring, dot);

  let mx=innerWidth/2, my=innerHeight/2, rx=mx, ry=my, shown=false;

  addEventListener('mousemove', e=>{
    mx=e.clientX; my=e.clientY;
    if(!shown){ shown=true; dot.classList.add('on'); ring.classList.add('on'); }
  }, {passive:true});
  addEventListener('mouseleave', ()=>{ dot.classList.remove('on'); ring.classList.remove('on'); shown=false; });

  (function loop(){
    dot.style.transform = `translate(${mx}px,${my}px)`;
    rx += (mx-rx)*0.16; ry += (my-ry)*0.16;      // 링은 지연 추종
    ring.style.transform = `translate(${rx}px,${ry}px)`;
    requestAnimationFrame(loop);
  })();

  // data-cursor 가 붙은 요소 위에서 라벨 표시
  const bind = el => {
    el.addEventListener('mouseenter',()=>{
      lbl.textContent = el.dataset.cursor || 'VIEW';
      dot.classList.add('hot'); ring.classList.add('hot');
    });
    el.addEventListener('mouseleave',()=>{
      dot.classList.remove('hot'); ring.classList.remove('hot');
    });
  };
  document.querySelectorAll('[data-cursor]').forEach(bind);
})();

/* ---------- 12) 아코디언 확장 카드 ---------- */
(function(){
  const acc = document.getElementById('prodAcc');
  if(!acc) return;
  const items = [...acc.querySelectorAll('.acc-item')];
  if(!items.length) return;

  /* 카드가 열리는 순간 바로 확대 상태로 넘어갑니다.
     (예전에는 카드 열기 -> 이미지에 다시 호버, 두 단계였습니다)
     분해도가 있으면 분해도로 교차 전환되고, 없으면 원래 이미지가 그대로 커집니다. */
  const canZoom = matchMedia('(hover:hover)').matches && innerWidth > 800;
  const zoomable = el => !!(el && el.querySelector('.acc-photo'));

  let openEl = items.find(i=>i.classList.contains('is-open')) || null;
  const open = el => {
    if(el === openEl) return;              /* 같은 카드면 아무것도 하지 않습니다 */
    openEl = el;
    items.forEach(i=>{
      i.classList.toggle('is-open', i===el);
      if(i !== el) i.classList.remove('is-zoom');   /* 닫히면 확대도 해제 */
    });
  };
  /* 카드를 '고르는' 모든 경로(호버/클릭/포커스)에서 확대까지 함께 켭니다.
     첫 화면은 확대되지 않은 상태로 두고, 사용자가 올렸을 때만 전환합니다. */
  const activate = el => {
    open(el);
    if(canZoom && zoomable(el)) el.classList.add('is-zoom');
  };

  /* 마우스가 스쳐 지나갈 때 카드가 연달아 열리지 않도록 잠깐 기다립니다 */
  let hoverT = 0;
  const intent = el => { clearTimeout(hoverT); hoverT = setTimeout(()=>activate(el), 150); };
  const cancel = ()   => clearTimeout(hoverT);

  // 포인터가 있는 기기(PC)는 hover, 터치 기기는 탭으로 전환
  const canHover = matchMedia('(hover:hover)').matches && innerWidth > 1100;

  items.forEach(el=>{
    if(canHover){
      el.addEventListener('mouseenter',()=>intent(el));
      el.addEventListener('mouseleave',cancel);
    }
    el.addEventListener('click', e=>{
      // 접힌 카드를 처음 누르면 펼치기만 하고 이동은 막는다
      if(!el.classList.contains('is-open')){ e.preventDefault(); cancel(); activate(el); }
    });
    // 키보드 접근성
    el.setAttribute('tabindex','0');
    el.addEventListener('focus',()=>activate(el));
    el.addEventListener('keydown',e=>{
      if(e.key==='Enter'||e.key===' '){
        const link = el.querySelector('a[href]');
        if(el.classList.contains('is-open') && link){ location.href = link.href; }
        else { e.preventDefault(); activate(el); }
      }
    });
  });

  /* 폭 전환이 끝난 뒤에만 스크롤 위치를 다시 계산합니다.
     예전에는 카드를 열 때마다 즉시 refresh 를 불러 전환이 끊겼습니다. */
  let refreshT = 0;
  acc.addEventListener('transitionend', e=>{
    if(e.propertyName !== 'flex-grow') return;
    clearTimeout(refreshT);
    refreshT = setTimeout(()=>{
      window.ScrollTrigger && ScrollTrigger.refresh && ScrollTrigger.refresh();
    }, 120);
  });

  // 화면 크기가 바뀌면 hover/tap 모드 재판단이 필요하므로 첫 항목으로 리셋
  let last = innerWidth > 1100;
  addEventListener('resize', debounceAcc(()=>{
    const now = innerWidth > 1100;
    if(now !== last){ last = now; open(items[0]); }
  },200), {passive:true});

  function debounceAcc(fn,ms){let t;return(...a)=>{clearTimeout(t);t=setTimeout(()=>fn(...a),ms);};}
})();

/* ---------- 13) 히어로 배경 영상 ---------- */
(function(){
  const v = document.getElementById('heroVid');
  if(!v) return;

  // 모션 최소화 설정이면 영상 대신 포스터만
  if(reduce){ v.remove(); return; }

  /* 넓은 화면에서만 1080p 로 교체.
     video 내부 <source media> 는 브라우저가 무시하므로 JS 로 고른다. */
  const conn = navigator.connection || {};
  const light = conn.saveData || /2g/.test(conn.effectiveType || '');
  const base = v.dataset.hd;
  if(base && innerWidth >= 1100 && !light){
    v.innerHTML =
      `<source src="${base}.webm" type="video/webm">` +
      `<source src="${base}.mp4" type="video/mp4">`;
    v.load();
  }

  // 자동재생이 막히면 조용히 포스터로 남긴다
  const tryPlay = () => { const p = v.play(); if(p && p.catch) p.catch(()=>{}); };
  v.addEventListener('loadeddata', tryPlay, {once:true});
  tryPlay();

  // 화면 밖으로 나가면 정지 — 배터리·CPU 절약
  if('IntersectionObserver' in window){
    new IntersectionObserver(es=>es.forEach(e=>{
      if(e.isIntersecting) tryPlay(); else v.pause();
    }),{threshold:0.05}).observe(v);
  }
})();

/* ---------- 14) 연혁 타임라인 — 스크롤 연동 (진행바 + 연도 활성 + 항목 순차) ---------- */
(function(){
  const tl = document.getElementById('tl');
  const years = [...document.querySelectorAll('.tl-year')];
  if(!years.length) return;

  /* 항목 순차 지연 */
  years.forEach(y=>y.querySelectorAll('.tl-list li')
    .forEach((li,i)=>li.style.setProperty('--td',(i*85)+'ms')));

  if(reduce){ years.forEach(y=>y.classList.add('in')); return; }

  /* 연도 블록 등장 */
  const io=new IntersectionObserver(es=>es.forEach(e=>{
    if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); }
  }),{threshold:.1,rootMargin:'0px 0px -8% 0px'});
  years.forEach(y=>io.observe(y));

  const fill  = document.getElementById('tlFill');
  const jumps = [...document.querySelectorAll('.tl-jump')];

  /* 연도 바로가기 */
  jumps.forEach(btn=>btn.addEventListener('click',()=>{
    const t=document.getElementById(btn.dataset.go);
    if(!t) return;
    const off=(document.querySelector('.subnav')?.getBoundingClientRect().bottom||0)+18;
    scrollTo({top:t.getBoundingClientRect().top+scrollY-off,behavior:'smooth'});
  }));

  let tick=false;
  const sync=()=>{
    /* 백스톱 — 빠른 스크롤로 건너뛴 연도 보정 */
    years.forEach(y=>{ if(!y.classList.contains('in') &&
      y.getBoundingClientRect().top < innerHeight*0.92) y.classList.add('in'); });

    if(tl && fill){
      const r=tl.getBoundingClientRect(), mid=innerHeight*0.42;
      const k=Math.min(1,Math.max(0,(mid-r.top)/Math.max(1,r.height)));
      fill.style.height=(k*100).toFixed(2)+'%';
    }
    /* 현재 연도 */
    let cur=years[0];
    for(const y of years){ if(y.getBoundingClientRect().top <= innerHeight*0.46) cur=y; }
    const id=cur && cur.id;
    jumps.forEach(b=>b.classList.toggle('on', b.dataset.go===id));
  };
  addEventListener('scroll',()=>{ if(tick)return; tick=true;
    requestAnimationFrame(()=>{ sync(); tick=false; }); },{passive:true});
  addEventListener('resize',sync,{passive:true});
  addEventListener('load',sync);
  sync();
})();

/* ---------- 17) 카드 순차 등장 (직접생산확인 · 제품 상세) ---------- */
(function(){
  const els=[...document.querySelectorAll('.dp, .dspec, .dmodel, .dcert, .dcert-card, .dsol-lead, .dsol-note, .dlay, .dfi, .gn-legend li')];
  if(!els.length) return;
  if(reduce){ els.forEach(e=>e.classList.add('in')); return; }
  const io=new IntersectionObserver(es=>es.forEach(e=>{
    if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); }
  }),{threshold:.25,rootMargin:'0px 0px -6% 0px'});
  els.forEach(e=>io.observe(e));
  let tick=false;
  addEventListener('scroll',()=>{ if(tick)return; tick=true;
    requestAnimationFrame(()=>{
      els.forEach(e=>{ if(!e.classList.contains('in') &&
        e.getBoundingClientRect().top < innerHeight*0.9) e.classList.add('in'); });
      tick=false;
    });
  },{passive:true});
  addEventListener('load',()=>els.forEach(e=>{
    if(e.getBoundingClientRect().top < innerHeight*0.9) e.classList.add('in');
  }));
})();

/* ---------- 18) 조직도 등장 ---------- */
(function(){
  const og=document.getElementById('og');
  if(!og) return;
  og.querySelectorAll('.og-col').forEach((c,i)=>c.style.setProperty('--td',(180+i*110)+'ms'));
  if(reduce){ og.classList.add('in'); return; }
  const io=new IntersectionObserver(es=>es.forEach(e=>{
    if(e.isIntersecting){ og.classList.add('in'); io.disconnect(); }
  }),{threshold:.2});
  io.observe(og);
  addEventListener('load',()=>{ if(og.getBoundingClientRect().top<innerHeight*0.9) og.classList.add('in'); });
})();

/* ---------- 15) 파트너사 — 공공/민간 전환 ---------- */
(function(){
  const wrap = document.getElementById('ptGrid');
  if(!wrap) return;
  const cards = [...wrap.querySelectorAll('.pt')];
  document.querySelectorAll('.pt-tabs button').forEach(btn=>{
    btn.addEventListener('click',()=>{
      document.querySelectorAll('.pt-tabs button').forEach(b=>b.classList.remove('on'));
      btn.classList.add('on');
      const c=btn.dataset.cat;
      cards.forEach(el=>{
        const show = (c==='all' || el.dataset.cat===c);
        el.style.display = show ? '' : 'none';
      });
      window.ScrollTrigger && ScrollTrigger.refresh && ScrollTrigger.refresh();
    });
  });
})();

/* ---------- 16) 홈 파트너 띠 — 무한 흐름 ---------- */
(function(){
  const track = document.getElementById('ptTrack');
  if(!track) return;
  // 원본을 한 벌 복제해 이어붙여야 -50% 이동이 매끄럽게 순환한다
  track.innerHTML += track.innerHTML;
})();

/* ---------- 19) 우측 하단 상담 위젯 ---------- */
(function(){
  const cw = document.getElementById('cw');
  if(!cw) return;
  const fab   = document.getElementById('cwFab'),
        panel = document.getElementById('cwPanel'),
        log   = document.getElementById('cwLog'),
        chips = document.getElementById('cwChips'),
        tip   = document.getElementById('cwTip'),
        min   = document.getElementById('cwMin');
  const BASE = cw.dataset.base || '', TEL = cw.dataset.tel, MAIL = cw.dataset.mail;
  const EN = cw.dataset.lang === 'en';
  const esc = t => String(t).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));

  /* ---- 시나리오 ---- */
  const MENU = ['biz','prod','quote','maint','visit'];
  const LINK = (href,label)=>`<a class="cw-link" href="${BASE}${href}">${label} →</a>`;

  const ANSWER_KO = {
    biz: {html:`상림기술은 <b>4개 사업분야</b>를 수행합니다.
        <ul><li>지능형 교통체계(ITS)</li><li>버스정보 안내시스템(BIS)</li>
        <li>긴급차량 우선신호 시스템</li><li>스마트 스쿨존 시스템</li></ul>
        ${LINK('business/its.html','사업분야 자세히 보기')}`, next:['quote','prod','ask']},
    prod: {html:`직접 설계·생산하는 <b>5개 제품군</b>이 있습니다.
        <ul><li>도로교통 전광판(VMS)</li><li>버스정보안내 전광판(BIT)</li>
        <li>전기차 충전소 전광판</li><li>초정밀 GNSS 모듈</li><li>PTZ 카메라</li></ul>
        ${LINK('product/vms.html','주요제품 자세히 보기')}`, next:['quote','cert','ask']},
    quote: {html:`구축·견적은 사업 규모와 현장 조건에 따라 달라집니다.
        아래 <b>문의 남기기</b>로 개요를 남겨주시면 담당자가 확인 후 연락드립니다.`, next:['ask','call']},
    maint: {html:`ITS·BIS 센터 유지보수와 교통시설물 현장장비 유지보수를 수행하고 있습니다.
        운영 중인 시스템이 있으시면 기관명과 증상을 남겨주세요.`, next:['ask','call']},
    visit: {html:`<b>본사</b> 경기도 광명시 하안로 60, 광명 SK테크노파크 D동 1507호<br>
        <b>공장</b> 같은 건물 D동 1508호<br><b>대표전화</b> ${TEL}
        ${LINK('company/location.html','오시는 길 보기')}`, next:['ask','call']},
    cert: {html:`ISO 9001·14001, KC 적합등록 9건, TTA 시험인증, 환경표지 인증을 보유하고 있습니다.
        ${LINK('company/certification.html','인증현황 보기')}`, next:['quote','ask']}
  };
  const ANSWER_EN = {
    biz: {html:`We work across <b>four business areas</b>.
        <ul><li>Intelligent Transport System (ITS)</li><li>Bus Information System (BIS)</li>
        <li>Emergency Vehicle Priority Signal</li><li>Smart School Zone</li></ul>
        ${LINK('business/its.html','See our business areas')}`, next:['quote','prod','ask']},
    prod: {html:`We design and manufacture <b>five product families</b>.
        <ul><li>Variable Message Sign (VMS)</li><li>Bus Information Terminal (BIT)</li>
        <li>EV charging station display</li><li>High-precision GNSS module</li><li>PTZ camera</li></ul>
        ${LINK('product/vms.html','See our products')}`, next:['quote','cert','ask']},
    quote: {html:`Pricing depends on project scale and site conditions.
        Leave an outline through <b>Send an enquiry</b> below and our team will get back to you.`, next:['ask','call']},
    maint: {html:`We maintain ITS and BIS control centres as well as field equipment.
        If you already operate a system, tell us the organisation and the symptoms.`, next:['ask','call']},
    visit: {html:`<b>Head office</b> SK Techno Park D-1507, 60 Haan-ro, Gwangmyeong-si, Gyeonggi-do<br>
        <b>Factory</b> D-1508, same building<br><b>Phone</b> +82 2-2083-1333
        ${LINK('company/location.html','View directions')}`, next:['ask','call']},
    cert: {html:`We hold ISO 9001 and 14001, nine KC conformity registrations, TTA test
        certifications and the Korea Eco-Label.
        ${LINK('company/certification.html','View certifications')}`, next:['quote','ask']}
  };
  const ANSWER = EN ? ANSWER_EN : ANSWER_KO;
  const LABEL_KO = {biz:'사업분야가 궁금해요', prod:'제품이 궁금해요', quote:'구축·견적 문의',
    maint:'유지보수 문의', visit:'오시는 길', cert:'인증현황', ask:'문의 남기기',
    call:'전화로 상담', menu:'처음으로'};
  const LABEL_EN = {biz:'About your business', prod:'About your products', quote:'Project & pricing',
    maint:'Maintenance', visit:'Directions', cert:'Certifications', ask:'Send an enquiry',
    call:'Talk by phone', menu:'Start over'};
  const LABEL = EN ? LABEL_EN : LABEL_KO;
  const T = EN ? {
    greet1:'Hello, this is <b>SangLim Technologies</b>. 👋',
    greet2:'Ask us anything about deploying, building or maintaining a traffic system.<br>Pick a topic below and we will answer right away.',
    again:'Anything else we can help with? Pick a topic below.',
    callTxt:'Connecting you to <b>+82 2-2083-1333</b>.<br>Our team is available 09:00–18:00 on weekdays.',
    callBtn:'Call now',
    askIntro:'Fill in the details below and our team will get back to you.',
    lOrg:'Organisation', lName:'Name', lTel:'Phone', lMail:'Email', lMsg:'Message',
    phOrg:'e.g. City of Gwangmyeong', phName:'Jane Doe', phTel:'+82 10-0000-0000',
    phMail:'name@company.com',
    phMsg:'Tell us which system you are considering, the target area and the timeline.',
    send:'Send by email', missing:' are required.',
    subject:'[Website enquiry] ', tidy:'has been summarised.',
    mailOpen:'Your mail app will open. Just press <b>Send</b>.<br>If it does not open, copy the text below and email it to <b>'+MAIL+'</b>.',
    copy:'Copy text', copied:'Copied',
    fOrg:'Organisation : ', fName:'Name : ', fTel:'Phone : ', fMail:'Email : ',
    fMsg:'Message', fFrom:'Sent from : '
  } : {
    greet1:'안녕하세요, <b>(주)상림기술</b>입니다. 👋',
    greet2:'교통 시스템 도입·구축·유지보수 무엇이든 물어보세요.<br>아래에서 궁금한 항목을 선택하시면 바로 안내해 드립니다.',
    again:'다른 도움이 필요하시면 아래에서 골라주세요.',
    callTxt:'대표전화 <b>'+TEL+'</b> 로 연결합니다.<br>평일 09:00 – 18:00에 상담 가능합니다.',
    callBtn:'지금 전화 걸기',
    askIntro:'아래 항목을 남겨주시면 담당자가 확인 후 연락드립니다.',
    lOrg:'회사 · 기관명', lName:'성함', lTel:'연락처', lMail:'이메일', lMsg:'문의 내용',
    phOrg:'예) ○○시청 교통과', phName:'홍길동', phTel:'010-0000-0000',
    phMail:'name@company.com',
    phMsg:'도입을 검토 중인 시스템, 대상 지역, 일정 등을 적어주세요.',
    send:'메일로 문의 보내기', missing:'을(를) 입력해 주세요.',
    subject:'[홈페이지 문의] ', tidy:'님 문의를 정리했습니다.',
    mailOpen:'메일 앱이 열립니다. 그대로 <b>보내기</b>만 눌러주세요.<br>메일 앱이 열리지 않으면 아래 내용을 복사해 <b>'+MAIL+'</b> 로 보내주셔도 됩니다.',
    copy:'내용 복사하기', copied:'복사했습니다',
    fOrg:'회사·기관명 : ', fName:'성함 : ', fTel:'연락처 : ', fMail:'이메일 : ',
    fMsg:'문의 내용', fFrom:'보낸 페이지 : '
  };

  /* ---- 출력 도우미 ---- */
  const scroll = ()=>{ log.scrollTop = log.scrollHeight; };
  const push = (cls, html)=>{
    const d=document.createElement('div');
    d.className='cw-msg '+cls; d.innerHTML=html; log.appendChild(d); scroll(); return d;
  };
  const typing = ()=>{
    const d=document.createElement('div');
    d.className='cw-typing'; d.innerHTML='<span></span><span></span><span></span>';
    log.appendChild(d); scroll(); return d;
  };
  const bot = (html, delay)=> new Promise(res=>{
    if(reduce){ push('cw-bot',html); return res(); }
    const t=typing();
    setTimeout(()=>{ t.remove(); push('cw-bot',html); res(); }, delay||620);
  });

  const setChips = keys=>{
    chips.innerHTML='';
    keys.forEach(k=>{
      const b=document.createElement('button');
      b.type='button';
      b.className='cw-chip'+(k==='menu'?' alt':'');
      b.textContent=LABEL[k]||k;
      b.addEventListener('click',()=>choose(k));
      chips.appendChild(b);
    });
    requestAnimationFrame(scroll);
  };

  /* ---- 문의 폼 ---- */
  function askForm(){
    chips.innerHTML='';
    const f=document.createElement('form');
    f.className='cw-form'; f.noValidate=true;
    f.innerHTML=
      '<label for="cwOrg">'+T.lOrg+'</label><input id="cwOrg" name="org" autocomplete="organization" placeholder="'+T.phOrg+'">'+
      '<label for="cwName">'+T.lName+' <span style="color:#C2410C">*</span></label><input id="cwName" name="name" autocomplete="name" placeholder="'+T.phName+'">'+
      '<label for="cwTel">'+T.lTel+' <span style="color:#C2410C">*</span></label><input id="cwTel" name="tel" inputmode="tel" autocomplete="tel" placeholder="'+T.phTel+'">'+
      '<label for="cwMail">'+T.lMail+'</label><input id="cwMail" name="mail" type="email" autocomplete="email" placeholder="'+T.phMail+'">'+
      '<label for="cwMsg">'+T.lMsg+' <span style="color:#C2410C">*</span></label><textarea id="cwMsg" name="msg" placeholder="'+T.phMsg+'"></textarea>'+
      '<button class="cw-send" type="submit">'+T.send+'</button>';
    log.appendChild(f); scroll();
    setTimeout(()=>f.querySelector('#cwName').focus(),260);

    f.addEventListener('submit',e=>{
      e.preventDefault();
      f.querySelectorAll('.cw-err').forEach(n=>n.remove());
      const v=n=>f.querySelector('#'+n).value.trim();
      const org=v('cwOrg'), name=v('cwName'), tel=v('cwTel'), mail=v('cwMail'), msg=v('cwMsg');
      const miss=[];
      if(!name) miss.push(T.lName); if(!tel) miss.push(T.lTel); if(!msg) miss.push(T.lMsg);
      if(miss.length){
        const p=document.createElement('p');
        p.className='cw-err'; p.textContent=miss.join(' · ')+T.missing;
        f.insertBefore(p, f.querySelector('.cw-send')); scroll(); return;
      }
      const subject=T.subject+(org?org+' · ':'')+name;
      const body=[T.fOrg+(org||'-'),T.fName+name,T.fTel+tel,
                  T.fMail+(mail||'-'),'',T.fMsg,'────────────',msg,'',
                  T.fFrom+location.href].join('\n');
      f.remove();
      push('cw-me','<b>'+esc(name)+'</b> — '+T.tidy);
      bot(T.mailOpen)
        .then(()=>{
          const box=push('cw-bot','<div style="white-space:pre-wrap;font-size:.83rem;'+
            'background:#f4f6fb;border-radius:9px;padding:11px 12px;margin-top:2px">'+
            esc(body)+'</div>');
          const cp=document.createElement('button');
          cp.type='button'; cp.className='cw-chip'; cp.textContent=T.copy;
          cp.style.marginTop='10px';
          cp.addEventListener('click',()=>{
            const done=()=>{ cp.textContent=T.copied; setTimeout(()=>cp.textContent=T.copy,1800); };
            if(navigator.clipboard && navigator.clipboard.writeText){
              navigator.clipboard.writeText(body).then(done,()=>{});
            }else{
              const ta=document.createElement('textarea'); ta.value=body;
              ta.style.position='fixed'; ta.style.opacity='0';
              document.body.appendChild(ta); ta.select();
              try{ document.execCommand('copy'); done(); }catch(_){}
              ta.remove();
            }
          });
          box.appendChild(cp); scroll();
          setChips(['menu','call']);
          location.href='mailto:'+MAIL+'?subject='+encodeURIComponent(subject)+
                        '&body='+encodeURIComponent(body);
        });
    });
  }

  /* ---- 분기 ---- */
  function choose(k){
    if(k==='menu'){ push('cw-me',LABEL.menu); return greet(true); }
    if(k==='call'){
      push('cw-me',LABEL.call);
      bot(T.callTxt+'<a class="cw-link" href="tel:'+TEL.replace(/-/g,'')+'">'+T.callBtn+' →</a>')
        .then(()=>setChips(['ask','menu']));
      return;
    }
    if(k==='ask'){
      push('cw-me',LABEL.ask);
      bot(T.askIntro).then(askForm);
      return;
    }
    const a=ANSWER[k];
    if(!a) return;
    push('cw-me',LABEL[k]);
    chips.innerHTML='';
    bot(a.html, 720).then(()=>setChips(a.next.concat('menu')));
  }

  /* ---- 시작 ---- */
  let started=false;
  function greet(again){
    if(again){
      bot(T.again,420)
        .then(()=>setChips(MENU));
      return;
    }
    bot(T.greet1,420).then(()=>bot(T.greet2,700))
      .then(()=>setChips(MENU));
  }

  /* ---- 열고 닫기 ---- */
  function open(){
    cw.classList.add('on','seen');
    panel.hidden=false;
    fab.setAttribute('aria-expanded','true');
    fab.setAttribute('aria-label','온라인 상담 닫기');
    if(!started){ started=true; greet(false); }
    scroll();
  }
  function close(){
    cw.classList.remove('on');
    fab.setAttribute('aria-expanded','false');
    fab.setAttribute('aria-label','온라인 상담 열기');
    setTimeout(()=>{ if(!cw.classList.contains('on')) panel.hidden=true; }, 340);
  }
  fab.addEventListener('click',()=>cw.classList.contains('on')?close():open());
  min.addEventListener('click',close);
  addEventListener('keydown',e=>{ if(e.key==='Escape' && cw.classList.contains('on')){ close(); fab.focus(); } });

  /* 힌트 말풍선 — 한 번만, 조용히 */
  if(!reduce && innerWidth>520){
    setTimeout(()=>{
      if(cw.classList.contains('seen')) return;
      tip.classList.add('on');
      setTimeout(()=>tip.classList.remove('on'),6500);
    },4200);
  }
})();

/* ---------- 19b) 자동 재생 필름 섹션 공통 엔진 ---------- */
window.SL = window.SL || {};
SL.filmSection = function(o){
  const sec = o.sec, v = o.video, bar = o.bar, caps = o.caps || [],
        dots = o.dots || null, replay = o.replay || null;
  if(!sec || !v) return;

  const CAPS  = (v.dataset.caps || '').split(',').map(Number).filter(n=>!isNaN(n));
  let   TOTAL = parseFloat(v.dataset.end) || 12;
  const DOTAT = parseFloat(v.dataset.dots);

  /* 안전장치 — data-end 가 실제 영상 길이보다 길면 영상이 멈춘 채로 몇 초를 더
     기다리게 됩니다. 메타데이터가 오면 실제 길이에 맞춰 자동으로 줄입니다. */
  function syncTotal(){
    const d = v.duration;
    if(isFinite(d) && d > 0.5 && TOTAL > d) TOTAL = d;
  }
  if(v.readyState >= 1) syncTotal();
  v.addEventListener('loadedmetadata', syncTotal);
  let t0 = 0, elapsed = 0, running = false, done = false, raf = 0, capNow = -1;

  /* 캔버스가 아니라 <video> 이므로 끝나면 마지막 프레임이 그대로 남습니다 (loop 없음) */
  v.loop = false;

  function show(i){
    if(i === capNow) return;
    capNow = i;
    caps.forEach((c,k)=>c.classList.toggle('on', k === i));
  }
  function frame(now){
    raf = 0;
    if(running){
      elapsed += (now - t0) / 1000;
      t0 = now;
    }
    let i = -1;
    for(let k=0;k<CAPS.length;k++){ if(elapsed >= CAPS[k]) i = k; }
    show(i);
    if(bar) bar.style.width = Math.min(100, elapsed / TOTAL * 100).toFixed(2) + '%';
    if(dots && !isNaN(DOTAT)){
      const a = Math.max(0, Math.min(1, (elapsed - DOTAT) / 0.9));
      dots.style.opacity = a.toFixed(3);
      dots.classList.toggle('on', a > 0.02);
    }
    if(elapsed >= TOTAL){
      running = false; done = true;
      /* 마지막 상태를 확실히 채워 둡니다 — 진행바 100%, 점 완전히 켜짐, 마지막 문구 */
      if(bar) bar.style.width = '100%';
      if(dots && !isNaN(DOTAT)){ dots.style.opacity = '1'; dots.classList.add('on'); }
      if(CAPS.length) show(CAPS.length - 1);
      sec.classList.add('is-done');
      return;
    }
    if(running) raf = requestAnimationFrame(frame);
  }
  function start(){
    if(running || done) return;
    running = true; t0 = performance.now();
    sec.classList.add('is-playing');
    v.play().catch(()=>{});
    if(!raf) raf = requestAnimationFrame(frame);
  }
  function pause(){
    if(!running) return;
    running = false; v.pause();
    if(raf){ cancelAnimationFrame(raf); raf = 0; }
  }
  function resume(){
    if(done || running) return;
    running = true; t0 = performance.now();
    if(v.currentTime < v.duration - 0.05) v.play().catch(()=>{});
    if(!raf) raf = requestAnimationFrame(frame);
  }
  function restart(){
    done = false; elapsed = 0; capNow = -1;
    sec.classList.remove('is-done');
    try{ v.currentTime = 0; }catch(_){}
    running = false; start();
  }

  if(reduce){
    /* 모션 최소화 — 마지막 장면과 모든 문구를 그대로 보여줍니다 */
    caps.forEach(c=>c.classList.add('on'));
    if(dots){ dots.style.opacity = '1'; dots.classList.add('on'); }
    sec.classList.add('is-done');
    v.addEventListener('loadedmetadata', ()=>{ try{ v.currentTime = v.duration - 0.05; }catch(_){} });
    return;
  }

  /* 화면을 얼마나 덮고 있는지로 판단합니다. 단순 threshold 는 위쪽 요소 높이가
     조금만 달라져도(예: 영문 페이지의 긴 제목) 기준을 못 넘어 재생이 아예
     시작되지 않는 문제가 있었습니다. */
  const io = new IntersectionObserver(es=>es.forEach(e=>{
    const vh = window.innerHeight || document.documentElement.clientHeight;
    const ref = Math.min(vh, e.boundingClientRect.height || vh);
    const cover = ref > 0 ? e.intersectionRect.height / ref : 0;
    if(cover >= 0.5){ elapsed > 0 ? resume() : start(); }
    else if(cover < 0.25) pause();
  }), {threshold:[0, .1, .2, .3, .4, .5, .6, .75, .9, 1]});
  io.observe(sec);

  if(replay) replay.addEventListener('click', restart);
  /* loop 를 끄면 브라우저가 마지막 프레임을 그대로 남깁니다 — 되감지 않습니다 */
  v.addEventListener('ended', ()=>{ v.pause(); sec.classList.add('vid-ended'); });
};

/* ---------- 20) PTZ 카메라 — 화면에 들어오면 자동 재생, 끝나면 마지막 장면 유지 ---------- */
(function(){
  const sec = document.getElementById('ptzShow');
  if(!sec) return;
  SL.filmSection({
    sec  : sec,
    video: document.getElementById('ptzVid'),
    bar  : document.getElementById('ptzBar'),
    caps : [...sec.querySelectorAll('.ptz-cap')],
    replay: document.getElementById('ptzReplay')
  });
})();

/* ---------- 20b) 전기차 충전소 전광판 — 화면에 들어오면 자동 재생, 끝나면 마지막 장면 유지 ---------- */
(function(){
  const sec = document.getElementById('ecsShow');
  if(!sec) return;
  SL.filmSection({
    sec  : sec,
    video: document.getElementById('ecsVid'),
    bar  : document.getElementById('ecsBar'),
    caps : [...sec.querySelectorAll('.film-cap')],
    replay: document.getElementById('ecsReplay')
  });
})();

/* ---------- 21) 상황판 시나리오 — 스크롤로 화면이 전환되고 가로로 흐릅니다 ---------- */
(function(){
  const sec = document.getElementById('dashShow');
  if(!sec) return;
  const frame = document.getElementById('dsFrame'),
        bar   = document.getElementById('dsBar'),
        shots = [...sec.querySelectorAll('.ds-shot')],
        caps  = [...sec.querySelectorAll('.ds-cap')],
        dots  = [...sec.querySelectorAll('.ds-dot')];
  const N = shots.length;
  if(!N) return;

  if(reduce){
    shots.forEach(s=>s.classList.add('on'));
    caps.forEach(c=>c.classList.add('on'));
    return;
  }

  /* 시나리오 바로가기 */
  dots.forEach(btn=>btn.addEventListener('click',()=>{
    const i = +btn.dataset.go;
    const span = sec.offsetHeight - innerHeight;
    const y = sec.offsetTop + span * ((i + 0.42) / N);
    scrollTo({top:y, behavior:'smooth'});
  }));

  let target = 0, cur = 0, raf = 0, active = -1;

  function paint(){
    raf = 0;
    cur += (target - cur) * 0.16;
    if(Math.abs(target - cur) < 0.0006) cur = target;

    const seg = Math.min(N - 0.0001, Math.max(0, cur * N));
    const i   = Math.floor(seg);
    const t   = seg - i;                       // 현재 시나리오 안에서의 진행도

    if(i !== active){
      active = i;
      shots.forEach((s,k)=>s.classList.toggle('on', k === i));
      caps.forEach((c,k)=>c.classList.toggle('on', k === i));
      dots.forEach((d,k)=>d.classList.toggle('on', k === i));
    }

    /* 초광각 화면을 좌 → 우로 훑습니다 */
    const fw = frame.clientWidth;
    const img = shots[i] && shots[i].querySelector('img');
    if(img && img.naturalWidth){
      const iw = frame.clientHeight * (img.naturalWidth / img.naturalHeight);
      const max = Math.max(0, iw - fw);
      /* 양끝에 여유를 주어 처음/끝에서 멈춘 느낌이 나도록 */
      const e = Math.min(1, Math.max(0, (t - 0.08) / 0.84));
      img.style.transform = 'translateX(' + (-e * max).toFixed(1) + 'px)';
    }

    if(bar) bar.style.width = (cur * 100).toFixed(2) + '%';
    if(cur !== target) raf = requestAnimationFrame(paint);
  }

  function sync(){
    const r = sec.getBoundingClientRect();
    const span = Math.max(1, sec.offsetHeight - innerHeight);
    target = Math.max(0, Math.min(1, -r.top / span));
    if(!raf) raf = requestAnimationFrame(paint);
  }

  addEventListener('scroll', sync, {passive:true});
  addEventListener('resize', ()=>{ active = -1; sync(); }, {passive:true});
  addEventListener('load', ()=>{ active = -1; sync(); });
  /* 이미지가 늦게 오면 다시 계산 */
  shots.forEach(s=>{ const im = s.querySelector('img'); if(im) im.addEventListener('load', ()=>{ active=-1; sync(); }); });
  sync();
})();

/* ---------- 22) 초정밀 GNSS — 자동 재생 + 마지막 장면에서 점이 반짝입니다 ---------- */
(function(){
  const sec = document.getElementById('gnssShow');
  if(!sec) return;
  SL.filmSection({
    sec  : sec,
    video: document.getElementById('gnVid'),
    bar  : document.getElementById('gnBar'),
    caps : [...sec.querySelectorAll('.gn-cap')],
    dots : document.getElementById('gnDots'),
    replay: document.getElementById('gnReplay')
  });
})();

/* ---------- 23) 상황판 인트로 — 키워드 → 확대 → 패널 단위 강조 ---------- */
(function(){
  const sec = document.getElementById('dashZoom');
  if(!sec) return;
  const kw    = document.getElementById('dzKw'),
        wall  = document.getElementById('dzWall'),
        img   = document.getElementById('dzImg'),
        bar   = document.getElementById('dzBar'),
        caps  = [...sec.querySelectorAll('.dz-cap')];
  if(!wall || !img) return;

  /* 패널 구간 [시작, 끝] — 이미지 가로 비율 */
  const FULL  = [0, 1];
  const PANEL = [[0.004,0.288],[0.292,0.622],[0.600,0.668],[0.663,0.998]];
  /* 진행도별 목표 구간 */
  const KF = [
    {at:0.00, r:FULL},      {at:0.30, r:FULL},
    {at:0.40, r:PANEL[0]},  {at:0.49, r:PANEL[0]},
    {at:0.57, r:PANEL[1]},  {at:0.66, r:PANEL[1]},
    {at:0.73, r:PANEL[2]},  {at:0.80, r:PANEL[2]},
    {at:0.88, r:PANEL[3]},  {at:1.00, r:PANEL[3]},
  ];
  const CAP  = [[0.215,0.335],[0.375,0.510],[0.545,0.680],[0.715,0.820],[0.865,1.01]];
  const ease = t => t<.5 ? 4*t*t*t : 1-Math.pow(-2*t+2,3)/2;
  const MINW = 0.17;                       /* 너무 좁은 패널은 최소 폭으로 넓혀서 보여줍니다 */

  if(reduce){ caps.forEach(c=>c.classList.add('on')); return; }

  let target = 0, cur = 0, raf = 0, capNow = -1, W0 = 0, H0 = 0, AR = 5.24;

  function measure(){
    AR = (img.naturalWidth && img.naturalHeight) ? img.naturalWidth/img.naturalHeight : 5.24;
    W0 = Math.min(innerWidth * 0.92, 1500);
    H0 = W0 / AR;
  }

  function rangeAt(p){
    if(p <= KF[0].at) return KF[0].r;
    for(let i=0;i<KF.length-1;i++){
      const a=KF[i], b=KF[i+1];
      if(p>=a.at && p<=b.at){
        const t = ease((p-a.at)/Math.max(1e-6,(b.at-a.at)));
        return [a.r[0]+(b.r[0]-a.r[0])*t, a.r[1]+(b.r[1]-a.r[1])*t];
      }
    }
    return KF[KF.length-1].r;
  }

  function paint(){
    raf = 0;
    cur += (target - cur) * 0.15;
    if(Math.abs(target-cur) < 0.0005) cur = target;
    const p = cur;

    /* 1) 키워드가 물러나고 상황판이 나타납니다 */
    const g  = Math.min(1, p / 0.19), ge = ease(g);
    kw.style.opacity   = String(Math.max(0, 1 - g*1.45));
    kw.style.transform = 'translateY(' + (-ge*70).toFixed(1) + 'px) scale(' + (1-ge*0.14).toFixed(4) + ')';
    wall.style.opacity = String(Math.min(1, 0.04 + ge*1.6));
    const grow = 0.32 + ge*0.68;

    /* 2) 프레임이 패널 모양으로 변형되며 파고듭니다 */
    let [s0,s1] = rangeAt(p);
    let pw = Math.max(0.02, s1-s0), cx = (s0+s1)/2;
    if(pw < MINW){ pw = MINW; }                       /* 좁은 패널은 주변까지 함께 */
    const maxH = Math.max(180, innerHeight - 430);
    const z    = Math.max(1, Math.min(maxH/H0, 1/pw));
    const fw   = Math.min(W0, pw * W0 * z);
    const fh   = Math.min(maxH, H0 * z);

    wall.style.width  = (fw * grow).toFixed(1) + 'px';
    wall.style.height = (fh * grow).toFixed(1) + 'px';
    img.style.width   = (W0 * z * grow).toFixed(1) + 'px';
    img.style.left    = (-(cx * W0 * z * grow) + (fw * grow)/2).toFixed(1) + 'px';

    /* 3) 자막 */
    let ci = -1;
    for(let i=0;i<CAP.length;i++){ if(p>=CAP[i][0] && p<CAP[i][1]) ci = i; }
    if(ci !== capNow){
      capNow = ci;
      caps.forEach((c,i)=>c.classList.toggle('on', i === ci));
      wall.classList.toggle('zoomed', ci > 0);
    }

    if(bar) bar.style.width = (p*100).toFixed(2) + '%';
    if(cur !== target) raf = requestAnimationFrame(paint);
  }

  function sync(){
    const r = sec.getBoundingClientRect();
    const span = Math.max(1, sec.offsetHeight - innerHeight);
    target = Math.max(0, Math.min(1, -r.top / span));
    if(!raf) raf = requestAnimationFrame(paint);
  }
  function reset(){ measure(); capNow = -1; sync(); }
  addEventListener('scroll', sync, {passive:true});
  addEventListener('resize', reset, {passive:true});
  addEventListener('load', reset);
  img.addEventListener('load', reset);
  reset();
})();

/* ---------- 24) 메인 인덱스 인터랙션 강화 ---------- */
(function(){
  const reduceMo = matchMedia('(prefers-reduced-motion:reduce)').matches;
  const fine     = matchMedia('(hover:hover) and (pointer:fine)').matches;

  /* --- 24-1) 상단 스크롤 진행 바 (모든 페이지) --- */
  if(!reduceMo){
    const bar = document.createElement('div');
    bar.className = 'sprog';
    document.body.appendChild(bar);
    let raf = 0;
    const draw = ()=>{
      raf = 0;
      const h = document.documentElement.scrollHeight - innerHeight;
      const t = h > 0 ? Math.min(1, Math.max(0, scrollY / h)) : 0;
      bar.style.transform = 'scaleX(' + t.toFixed(4) + ')';
    };
    addEventListener('scroll', ()=>{ if(!raf) raf = requestAnimationFrame(draw); }, {passive:true});
    addEventListener('resize', draw, {passive:true});
    draw();
  }

  /* --- 24-2) 섹션 제목 줄 단위 마스크 등장 --- */
  document.querySelectorAll('.section-head h2').forEach(h2=>{
    if(h2.querySelector('.ln')) return;
    const parts = h2.innerHTML.split(/<br\s*\/?>/i);
    h2.innerHTML = parts.map(s=>'<span class="ln"><i>'+s+'</i></span>').join('');
    h2.classList.add('splt');
  });

  /* --- 24-3) 히어로 — 스크롤에 따라 밀려나며 사라짐 --- */
  const hero = document.getElementById('hero');
  if(hero && !reduceMo){
    const inner = hero.querySelector('.hero-inner');
    const media = hero.querySelector('.hero-media');
    const cue   = hero.querySelector('.scroll-cue');
    let raf = 0;
    const draw = ()=>{
      raf = 0;
      const h = hero.offsetHeight || innerHeight;
      const t = Math.min(1, Math.max(0, scrollY / h));
      if(inner){
        inner.style.transform = 'translate3d(0,' + (-t * 96).toFixed(1) + 'px,0)';
        inner.style.opacity   = Math.max(0, 1 - t * 1.35).toFixed(3);
      }
      if(media) media.style.transform = 'scale(' + (1 + t * 0.14).toFixed(4) + ')';
      if(cue)   cue.style.opacity = Math.max(0, 1 - t * 4).toFixed(3);
    };
    addEventListener('scroll', ()=>{ if(!raf) raf = requestAnimationFrame(draw); }, {passive:true});
    addEventListener('resize', draw, {passive:true});
    draw();
  }

  /* --- 24-4) 카드 3D 틸트 + 커서 위치 발광 --- */
  if(fine && !reduceMo){
    document.querySelectorAll('.feat-grid .card').forEach(card=>{
      card.classList.add('tilt');
      if(!card.querySelector('.cglow')){
        const g = document.createElement('span');
        g.className = 'cglow';
        card.prepend(g);
      }
      let raf = 0, mx = 0, my = 0;
      const apply = ()=>{
        raf = 0;
        const r = card.getBoundingClientRect();
        const px = (mx - r.left) / r.width;
        const py = (my - r.top) / r.height;
        card.style.setProperty('--ry', ((px - .5) *  9).toFixed(2) + 'deg');
        card.style.setProperty('--rx', ((py - .5) * -7).toFixed(2) + 'deg');
        card.style.setProperty('--mx', (px * 100).toFixed(1) + '%');
        card.style.setProperty('--my', (py * 100).toFixed(1) + '%');
      };
      card.addEventListener('pointerenter', ()=>card.classList.add('act'));
      card.addEventListener('pointermove', e=>{
        mx = e.clientX; my = e.clientY;
        if(!raf) raf = requestAnimationFrame(apply);
      });
      card.addEventListener('pointerleave', ()=>{
        card.classList.remove('act');
        card.style.setProperty('--rx','0deg');
        card.style.setProperty('--ry','0deg');
      });
    });
  }

  /* --- 24-5) 마그네틱 버튼 --- */
  if(fine && !reduceMo){
    document.querySelectorAll('.btn-primary, .btn-ghost').forEach(btn=>{
      btn.classList.add('mag');
      let raf = 0, tx = 0, ty = 0;
      const apply = ()=>{ raf = 0; btn.style.transform = 'translate3d('+tx.toFixed(1)+'px,'+ty.toFixed(1)+'px,0)'; };
      btn.addEventListener('pointermove', e=>{
        const r = btn.getBoundingClientRect();
        tx = (e.clientX - (r.left + r.width /2)) * 0.22;
        /* CSS 의 hover 살짝 뜨는 값(-3px)을 그대로 살려 둡니다 */
        ty = (e.clientY - (r.top  + r.height/2)) * 0.30 - 3;
        if(!raf) raf = requestAnimationFrame(apply);
      });
      btn.addEventListener('pointerleave', ()=>{
        if(raf){ cancelAnimationFrame(raf); raf = 0; }
        btn.style.transform = '';           /* CSS 규칙으로 되돌립니다 */
      });
    });
  }

  /* --- 24-6) WHO WE ARE 이미지 — 포인터 따라 미세하게 떠다님 --- */
  const viz = document.querySelector('.about-viz');
  if(viz && fine && !reduceMo){
    const one  = viz.querySelector('.av-one');      /* 합성 이미지 한 장 버전 */
    const main = viz.querySelector('.av-main');
    const subs = [...viz.querySelectorAll('.av-sub')];
    let raf = 0, nx = 0, ny = 0;
    const apply = ()=>{
      raf = 0;
      if(one){  one.style.setProperty('--px',(nx* 12).toFixed(1)+'px');
                one.style.setProperty('--py',(ny*  9).toFixed(1)+'px'); }
      if(main){ main.style.setProperty('--px',(nx* 10).toFixed(1)+'px');
                main.style.setProperty('--py',(ny*  8).toFixed(1)+'px'); }
      subs.forEach((el,i)=>{
        const k = i === 0 ? -1 : 1;           /* 두 장이 서로 반대로 움직입니다 */
        el.style.setProperty('--px',(nx * 19 * k).toFixed(1)+'px');
        el.style.setProperty('--py',(ny * 15 * k).toFixed(1)+'px');
      });
    };
    viz.addEventListener('pointerenter', ()=>viz.classList.add('pp'));
    viz.addEventListener('pointermove', e=>{
      const r = viz.getBoundingClientRect();
      nx = (e.clientX - (r.left + r.width /2)) / (r.width /2);
      ny = (e.clientY - (r.top  + r.height/2)) / (r.height/2);
      if(!raf) raf = requestAnimationFrame(apply);
    });
    viz.addEventListener('pointerleave', ()=>{
      viz.classList.remove('pp'); nx = ny = 0;
      if(!raf) raf = requestAnimationFrame(apply);
    });
  }

  /* --- 24-6) 파트너 띠 — 스크롤 중에는 잠깐 빨라짐 --- */
  const track = document.querySelector('.pt-track');
  if(track && !reduceMo){
    let t = 0;
    addEventListener('scroll', ()=>{
      track.style.animationDuration = '18s';
      clearTimeout(t);
      t = setTimeout(()=>{ track.style.animationDuration = ''; }, 420);
    }, {passive:true});
  }

  /* --- 25) 문의 폼 ------------------------------------------------
     별도 서버 없이 동작합니다.
       · data-endpoint 가 비어 있으면  → 작성한 내용을 담아 메일 앱을 엽니다
       · data-endpoint 에 주소를 넣으면 → 그 주소로 바로 전송합니다
         (Formspree / Web3Forms / FormSubmit 같은 폼 중계 서비스 주소를
          contact.html 의 form 태그 data-endpoint 에 붙여 넣기만 하면 됩니다)
  ------------------------------------------------------------------ */
  const cf = document.getElementById('cform');
  if(cf){
    const EN   = cf.dataset.lang === 'en';
    const MAIL = cf.dataset.mail || '';
    const box  = cf.querySelector('.form-msg');
    const T = EN ? {
      need:'Please fill in the required fields.',
      mail:'Please check the email address.',
      open:'Your mail app should be opening. If nothing happens, use “Copy text”.',
      sent:'Thank you — your enquiry has been sent. We will be in touch shortly.',
      fail:'Sending failed. Please use “Copy text” and mail us directly.',
      copied:'Copied. Paste it into a mail to ' + MAIL + '.',
      nocopy:'Could not copy — please select the text manually.',
      subj:'[Website enquiry]'
    } : {
      need:'필수 항목을 입력해 주세요.',
      mail:'이메일 주소를 확인해 주세요.',
      open:'메일 앱이 열립니다. 열리지 않으면 “내용 복사”를 눌러 주세요.',
      sent:'문의가 전송되었습니다. 확인 후 연락드리겠습니다.',
      fail:'전송에 실패했습니다. “내용 복사”를 눌러 메일로 보내 주세요.',
      copied:'복사했습니다. ' + MAIL + ' 로 붙여넣어 보내주세요.',
      nocopy:'복사하지 못했습니다. 내용을 직접 선택해 복사해 주세요.',
      subj:'[홈페이지 문의]'
    };
    const say = (t, kind) => {
      box.textContent = t;
      box.className = 'form-msg' + (kind ? ' is-' + kind : '');
      box.hidden = false;
    };
    const val = n => (cf.elements[n] ? cf.elements[n].value.trim() : '');
    const mark = (el, bad) => {
      el.closest('.field').classList.toggle('is-bad', bad);
      el.setAttribute('aria-invalid', bad ? 'true' : 'false');
    };

    const check = () => {
      let first = null;
      cf.querySelectorAll('[required]').forEach(el => {
        const bad = !el.value.trim();
        mark(el, bad);
        if(bad && !first) first = el;
      });
      if(first){ say(T.need, 'bad'); first.focus(); return false; }
      const m = cf.elements['email'];
      if(!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(m.value.trim())){
        mark(m, true); say(T.mail, 'bad'); m.focus(); return false;
      }
      return true;
    };

    /* 메일 본문 — 라벨과 값을 그대로 옮겨 담습니다 */
    const compose = () => {
      const L = EN
        ? [['Name','name'],['Organisation','org'],['Phone','tel'],['Email','email']]
        : [['담당자명','name'],['기관 / 회사명','org'],['연락처','tel'],['이메일','email']];
      const lines = L.filter(([,n]) => val(n)).map(([k,n]) => k + ': ' + val(n));
      lines.push('', (EN ? 'Message' : '문의 내용') + '\n' + val('message'));
      const who = val('org') || val('name');
      return { subject: T.subj + ' ' + who, body: lines.join('\n') };
    };

    cf.addEventListener('input', e => {
      if(e.target.closest('.field')) mark(e.target, false);
    });

    cf.addEventListener('submit', async e => {
      e.preventDefault();
      if(!check()) return;
      const { subject, body } = compose();
      const url = cf.dataset.endpoint;

      if(!url){                                   /* 메일 앱으로 열기 */
        say(T.open, 'ok');
        const href = 'mailto:' + MAIL +
          '?subject=' + encodeURIComponent(subject) +
          '&body='    + encodeURIComponent(body);
        window.__mailto = href;          /* 점검용 */
        location.href = href;
        return;
      }

      const btn = cf.querySelector('button[type=submit]');
      btn.disabled = true;
      try{
        const r = await fetch(url, {
          method:'POST',
          headers:{'Content-Type':'application/json', 'Accept':'application/json'},
          body: JSON.stringify({
            name:val('name'), org:val('org'), tel:val('tel'),
            email:val('email'), message:val('message'),
            _subject: subject
          })
        });
        if(!r.ok) throw 0;
        cf.reset(); say(T.sent, 'ok');
      }catch(_){ say(T.fail, 'bad'); }
      btn.disabled = false;
    });

    /* 내용 복사 — 메일 앱이 없는 환경의 대비책 */
    cf.querySelector('.cf-copy').addEventListener('click', async () => {
      if(!check()) return;
      const { subject, body } = compose();
      const text = subject + '\n\n' + body;
      /* 최신 API 를 먼저 쓰되, 막히면 예전 방식으로 한 번 더 시도합니다
         (file:// 로 직접 연 경우처럼 보안 컨텍스트가 아닐 때가 있습니다) */
      let done = false;
      try{
        if(navigator.clipboard && isSecureContext){
          await navigator.clipboard.writeText(text); done = true;
        }
      }catch(_){}
      if(!done){
        try{
          const ta = document.createElement('textarea');
          ta.value = text;
          ta.style.cssText = 'position:fixed;top:0;left:0;opacity:0';
          document.body.appendChild(ta);
          ta.focus(); ta.select();
          done = document.execCommand('copy');
          ta.remove();
        }catch(_){}
      }
      say(done ? T.copied : T.nocopy, done ? 'ok' : 'bad');
    });
  }

})();
