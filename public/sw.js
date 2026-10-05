/* Faqat ilova qobig‘ini keshlaydi. Do‘kon ma’lumotlari brauzer xotirasida (localStorage),
   service worker ularni ko‘rmaydi va saqlamaydi. Yangi versiyada VERSION ni oshiring. */
const VERSION='milliy-apple-v2.3.0';
const SHELL=['./','index.html','manifest.webmanifest','icons/icon-192.png','icons/icon-512.png'];
self.addEventListener('install',e=>{e.waitUntil(caches.open(VERSION).then(c=>c.addAll(SHELL)).then(()=>self.skipWaiting()))});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==VERSION).map(k=>caches.delete(k)))).then(()=>self.clients.claim()))});
self.addEventListener('fetch',e=>{const u=new URL(e.request.url);if(e.request.method!=='GET'||u.origin!==location.origin)return;
  /* Avval tarmoq — yangi versiya darhol keladi; internet bo‘lmasa keshdagi qobiq ochiladi */
  e.respondWith(fetch(e.request).then(r=>{if(r.ok){const c=r.clone();caches.open(VERSION).then(x=>x.put(e.request,c))}return r}).catch(()=>caches.match(e.request).then(r=>r||caches.match('index.html'))))});
