/* ISLGrind service worker — app shell offline + fast static assets */
const CACHE = "islgrind-v1";
const CORE = ["./","./index.html","./bank.js","./manifest.json","./icon-192.png","./icon-512.png"];
self.addEventListener("install", e=>{ e.waitUntil(caches.open(CACHE).then(c=>c.addAll(CORE)).then(()=>self.skipWaiting())); });
self.addEventListener("activate", e=>{ e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==CACHE).map(k=>caches.delete(k)))).then(()=>self.clients.claim())); });
self.addEventListener("fetch", e=>{
  const req=e.request; if(req.method!=="GET") return;
  const url=new URL(req.url);
  const netFirst = req.mode==="navigate" || url.pathname.endsWith("/bank.js") || url.pathname.endsWith("/index.html");
  if(netFirst){
    e.respondWith(fetch(req).then(res=>{ const c=res.clone(); caches.open(CACHE).then(ca=>ca.put(req,c)); return res; })
      .catch(()=>caches.match(req).then(h=>h||caches.match("./index.html"))));
  } else {
    e.respondWith(caches.match(req).then(hit=> hit || fetch(req).then(res=>{ const c=res.clone();
      caches.open(CACHE).then(ca=>{ try{ca.put(req,c);}catch(_){} }); return res; }).catch(()=>hit)));
  }
});
