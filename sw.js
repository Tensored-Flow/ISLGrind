/* ISLGrind no longer uses a service worker.
   Older versions cached the app shell, which could keep showing a stale page
   (e.g. the old sign-in screen) after updates. This self-destructing worker
   unregisters any previously-installed worker, clears its caches, and reloads
   open tabs so everyone ends up on the current local files. */
self.addEventListener("install", () => self.skipWaiting());
self.addEventListener("activate", (e) => {
  e.waitUntil((async () => {
    try { await self.registration.unregister(); } catch (_) {}
    try { for (const k of await caches.keys()) await caches.delete(k); } catch (_) {}
    try { for (const c of await self.clients.matchAll()) c.navigate(c.url); } catch (_) {}
  })());
});
