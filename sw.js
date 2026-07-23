// Bump this version whenever an existing image is replaced at the same URL.
var IMAGE_CACHE = 'mos-images-v1';

function isSiteImage(request) {
  if (request.method !== 'GET') return false;

  var url = new URL(request.url);
  return url.origin === self.location.origin && url.pathname.indexOf('/images/') === 0;
}

function updateCachedImage(cache, request) {
  return fetch(request).then(function (response) {
    if (response.ok) {
      cache.put(request, response.clone());
    }
    return response;
  });
}

self.addEventListener('install', function () {
  self.skipWaiting();
});

self.addEventListener('activate', function (event) {
  event.waitUntil(
    caches.keys().then(function (keys) {
      return Promise.all(keys.map(function (key) {
        if (key.indexOf('mos-images-') === 0 && key !== IMAGE_CACHE) {
          return caches.delete(key);
        }
      }));
    }).then(function () {
      return self.clients.claim();
    })
  );
});

self.addEventListener('fetch', function (event) {
  if (!isSiteImage(event.request)) return;

  event.respondWith(
    caches.open(IMAGE_CACHE).then(function (cache) {
      return cache.match(event.request).then(function (cached) {
        return cached || updateCachedImage(cache, event.request);
      });
    })
  );
});

self.addEventListener('message', function (event) {
  if (!event.data || event.data.type !== 'CACHE_IMAGES' || !Array.isArray(event.data.urls)) return;

  event.waitUntil(
    caches.open(IMAGE_CACHE).then(function (cache) {
      return Promise.all(event.data.urls.map(function (url) {
        var request = new Request(url, { credentials: 'same-origin' });
        if (!isSiteImage(request)) return;

        return cache.match(request).then(function (cached) {
          if (cached) return;
          return updateCachedImage(cache, request);
        }).catch(function () {});
      }));
    })
  );
});
