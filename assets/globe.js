/* ==================================================================
   8) GNSS 3D 지구본  (three.js r128)
   ================================================================== */
(function(){
  const canvas=document.getElementById('globe');
  if(!window.THREE){canvas.style.display='none';return;}
  const scene=new THREE.Scene();
  const cam=new THREE.PerspectiveCamera(45,1,0.1,100);
  cam.position.set(0,0.6,15.2);
  const renderer=new THREE.WebGLRenderer({canvas,antialias:true,alpha:true});
  renderer.setClearColor(0x000000,0);

  const R=4.9;
  const world=new THREE.Group();
  world.rotation.z=0.32;                 // 지축 기울기
  scene.add(world);

  /* 라운드 도트 텍스처 */
  const dotTex=(()=>{ const c=document.createElement('canvas');c.width=c.height=64;const x=c.getContext('2d');
    const g=x.createRadialGradient(32,32,0,32,32,32);g.addColorStop(0,'#fff');g.addColorStop(.5,'#fff');
    g.addColorStop(1,'rgba(255,255,255,0)');x.fillStyle=g;x.beginPath();x.arc(32,32,32,0,7);x.fill();
    const t=new THREE.CanvasTexture(c);return t;})();

  /* (a0) 어두운 본체 구 — 뒷면 점을 가려 진짜 지구처럼 보이게 */
  (function(){
    const g=new THREE.SphereGeometry(R*0.985,64,64);
    const m=new THREE.MeshBasicMaterial({color:0x0d1330});
    world.add(new THREE.Mesh(g,m));
  })();

  /* (a) 점으로 이뤄진 지구 — fibonacci sphere */
  (function(){
    const N=2600, pos=[], col=[];
    const cA=new THREE.Color(0x5C6DBC), cB=new THREE.Color(0x16C0CE);
    for(let i=0;i<N;i++){
      const y=1-(i/(N-1))*2, r=Math.sqrt(1-y*y), th=i*2.399963;
      const x=Math.cos(th)*r, z=Math.sin(th)*r;
      pos.push(x*R,y*R,z*R);
      const c=Math.random()<0.14?cB:cA; col.push(c.r,c.g,c.b);
    }
    const g=new THREE.BufferGeometry();
    g.setAttribute('position',new THREE.Float32BufferAttribute(pos,3));
    g.setAttribute('color',new THREE.Float32BufferAttribute(col,3));
    const m=new THREE.PointsMaterial({size:0.075,map:dotTex,vertexColors:true,transparent:true,
      depthWrite:false,opacity:0.95});
    world.add(new THREE.Points(g,m));
  })();

  /* (b) 위도/경도 와이어 */
  (function(){
    const mat=new THREE.LineBasicMaterial({color:0x4a5ab0,transparent:true,opacity:0.32});
    for(let la=-60;la<=60;la+=30){
      const p=[],rr=R*Math.cos(la*Math.PI/180),yy=R*Math.sin(la*Math.PI/180);
      for(let a=0;a<=360;a+=6)p.push(new THREE.Vector3(rr*Math.cos(a*Math.PI/180),yy,rr*Math.sin(a*Math.PI/180)));
      world.add(new THREE.Line(new THREE.BufferGeometry().setFromPoints(p),mat));
    }
    for(let lo=0;lo<180;lo+=30){
      const p=[];for(let a=0;a<=360;a+=6){const rad=a*Math.PI/180;
        p.push(new THREE.Vector3(R*Math.sin(rad)*Math.cos(lo*Math.PI/180),R*Math.cos(rad),R*Math.sin(rad)*Math.sin(lo*Math.PI/180)));}
      world.add(new THREE.Line(new THREE.BufferGeometry().setFromPoints(p),mat));
    }
  })();

  /* (c) 대기 글로우 (뒷면 렌더 구) */
  (function(){
    const g=new THREE.SphereGeometry(R*1.09,48,48);
    const m=new THREE.ShaderMaterial({transparent:true,side:THREE.BackSide,depthWrite:false,blending:THREE.AdditiveBlending,
      uniforms:{c:{value:new THREE.Color(0x2a6fd0)}},
      vertexShader:'varying vec3 n;void main(){n=normalize(normalMatrix*normal);gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.0);}',
      fragmentShader:'varying vec3 n;uniform vec3 c;void main(){float i=pow(max(0.0,0.62-dot(n,vec3(0.,0.,1.))),3.1)*1.6;gl_FragColor=vec4(c,1.0)*i;}'});
    scene.add(new THREE.Mesh(g,m));
  })();

  /* 지표 위 좌표 → 벡터 */
  const surf=(la,lo,rad)=>{const p=(90-la)*Math.PI/180,t=(lo+180)*Math.PI/180;
    return new THREE.Vector3(-rad*Math.sin(p)*Math.cos(t),rad*Math.cos(p),rad*Math.sin(p)*Math.sin(t));};

  /* (d) 기준국(스테이션) 발광 점 */
  const stations=[[37.5,127],[35,139],[1.3,103],[ -33,151],[51,0],[40,-74],[19,-99],[ -23,-46]];
  const stPts=[];
  stations.forEach(([la,lo])=>{
    const v=surf(la,lo,R*1.01); stPts.push(v);
    const s=new THREE.Mesh(new THREE.SphereGeometry(0.06,10,10),
      new THREE.MeshBasicMaterial({color:0x16C0CE}));
    s.position.copy(v); world.add(s);
    const ring=new THREE.Mesh(new THREE.RingGeometry(0.09,0.13,20),
      new THREE.MeshBasicMaterial({color:0x16C0CE,transparent:true,opacity:0.5,side:THREE.DoubleSide}));
    ring.position.copy(v); ring.lookAt(v.clone().multiplyScalar(2)); world.add(ring);
  });

  /* (e) 대권 아크 + 이동 점 */
  const arcs=[];
  function greatArc(a,b,lift){
    const pts=[],steps=60;
    for(let i=0;i<=steps;i++){const t=i/steps;
      const v=a.clone().lerp(b,t).normalize().multiplyScalar(R*(1+lift*Math.sin(Math.PI*t)));pts.push(v);}
    const g=new THREE.BufferGeometry().setFromPoints(pts);
    world.add(new THREE.Line(g,new THREE.LineBasicMaterial({color:0x16C0CE,transparent:true,opacity:0.34})));
    const head=new THREE.Mesh(new THREE.SphereGeometry(0.05,8,8),new THREE.MeshBasicMaterial({color:0xffffff}));
    world.add(head); arcs.push({pts,head,t:Math.random(),sp:0.0018+Math.random()*0.0016});
  }
  for(let i=0;i<6;i++){const a=stPts[i%stPts.length],b=stPts[(i*3+2)%stPts.length];if(a!==b)greatArc(a,b,0.28+Math.random()*0.16);}

  /* (f) 위성 궤도 + 위성 + 신호 빔 */
  const sats=[];
  const orbInfo=[[R*1.9,20],[R*2.15,72],[R*2.05,-46]];
  orbInfo.forEach(([rad,inc],k)=>{
    const p=[];for(let a=0;a<=360;a+=4)p.push(new THREE.Vector3(rad*Math.cos(a*Math.PI/180),0,rad*Math.sin(a*Math.PI/180)));
    const orbit=new THREE.Line(new THREE.BufferGeometry().setFromPoints(p),
      new THREE.LineBasicMaterial({color:0x7A86BE,transparent:true,opacity:0.32}));
    orbit.rotation.x=inc*Math.PI/180; world.add(orbit);
    const cnt=k===1?2:1;
    for(let s=0;s<cnt;s++){
      const sat=new THREE.Group();
      const body=new THREE.Mesh(new THREE.SphereGeometry(0.11,10,10),new THREE.MeshBasicMaterial({color:0xffffff}));
      const halo=new THREE.Sprite(new THREE.SpriteMaterial({map:dotTex,color:0x16C0CE,transparent:true,opacity:0.7,blending:THREE.AdditiveBlending}));
      halo.scale.set(0.6,0.6,0.6); sat.add(body,halo); world.add(sat);
      const beamG=new THREE.BufferGeometry().setFromPoints([new THREE.Vector3(),new THREE.Vector3()]);
      const beam=new THREE.Line(beamG,new THREE.LineBasicMaterial({color:0x16C0CE,transparent:true,opacity:0.4}));
      world.add(beam);
      sats.push({sat,beam,rad,inc:inc*Math.PI/180,a:Math.random()*Math.PI*2,sp:0.0034+Math.random()*0.0022,
        target:stPts[Math.floor(Math.random()*stPts.length)]});
    }
  });

  /* 마우스 패럴랙스 */
  let mx=0,my=0,tx=0,ty=0;
  if(!('ontouchstart' in window)){
    addEventListener('mousemove',e=>{tx=(e.clientX/innerWidth-0.5);ty=(e.clientY/innerHeight-0.5);});
  }

  function resize(){const w=canvas.clientWidth,h=canvas.clientHeight;
    if(canvas.width!==w||canvas.height!==h){renderer.setPixelRatio(Math.min(devicePixelRatio,2));renderer.setSize(w,h,false);
      cam.aspect=w/h;cam.updateProjectionMatrix();}}
  new ResizeObserver(resize).observe(canvas); resize();

  let running=true;
  document.addEventListener('visibilitychange',()=>{running=!document.hidden;if(running)tick();});

  const _v=new THREE.Vector3();
  function tick(){
    if(!running)return;
    world.rotation.y+=reduce?0:0.0016;
    mx+=(tx-mx)*0.04; my+=(ty-my)*0.04;
    world.rotation.x=0.12+my*0.25; world.position.x=mx*0.7;
    // 아크 이동 점
    arcs.forEach(o=>{o.t+=o.sp;if(o.t>1)o.t=0;const idx=Math.min(o.pts.length-1,Math.floor(o.t*(o.pts.length-1)));o.head.position.copy(o.pts[idx]);});
    // 위성
    sats.forEach(o=>{o.a+=o.sp;
      _v.set(o.rad*Math.cos(o.a),0,o.rad*Math.sin(o.a));_v.applyAxisAngle(new THREE.Vector3(1,0,0),o.inc);
      o.sat.position.copy(_v);
      const arr=o.beam.geometry.attributes.position.array;
      arr[0]=_v.x;arr[1]=_v.y;arr[2]=_v.z;arr[3]=o.target.x;arr[4]=o.target.y;arr[5]=o.target.z;
      o.beam.geometry.attributes.position.needsUpdate=true;});
    renderer.render(scene,cam);
    requestAnimationFrame(tick);
  }
  tick();
})();
