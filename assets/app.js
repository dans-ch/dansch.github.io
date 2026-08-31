/* ============================================================
   DanSch — dans.ch
   No framework. Vanilla ES2020, ~one file.
   Optional external: three.js + vanta.net (background only).
   ============================================================ */
(function () {
  'use strict';

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var clamp = function (v, lo, hi) { return v < lo ? lo : v > hi ? hi : v; };

  /* ---------- Header ---------------------------------------- */
  function initHeader() {
    var header = document.querySelector('.site-header');
    var nav = document.querySelector('.nav');
    var toggle = document.querySelector('.nav-toggle');

    if (header) {
      var sync = function () { header.classList.toggle('is-stuck', window.scrollY > 8); };
      sync();
      window.addEventListener('scroll', sync, { passive: true });
    }

    if (toggle && nav) {
      toggle.addEventListener('click', function () {
        var open = nav.classList.toggle('is-open');
        toggle.setAttribute('aria-expanded', String(open));
        document.body.style.overflow = open ? 'hidden' : '';
      });
      nav.addEventListener('click', function (e) {
        if (e.target.closest('a') && nav.classList.contains('is-open')) {
          nav.classList.remove('is-open');
          toggle.setAttribute('aria-expanded', 'false');
          document.body.style.overflow = '';
        }
      });
    }
  }

  /* ---------- Reveal on scroll ------------------------------- */
  function initReveal() {
    var targets = document.querySelectorAll('[data-reveal]');
    if (!targets.length) return;

    if (reduceMotion || !('IntersectionObserver' in window)) {
      targets.forEach(function (el) { el.classList.add('in-view'); });
      return;
    }

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('in-view');
        io.unobserve(entry.target);
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });

    // Stagger siblings that share a parent
    var seen = new Map();
    targets.forEach(function (el) {
      var p = el.parentNode;
      var i = seen.get(p) || 0;
      if (!el.style.getPropertyValue('--i')) el.style.setProperty('--i', String(Math.min(i, 6)));
      seen.set(p, i + 1);
      io.observe(el);
    });
  }

  /* ---------- Terminal typewriter ---------------------------- */
  function initTypewriter() {
    document.querySelectorAll('[data-typewriter]').forEach(function (el) {
      var lines;
      try { lines = JSON.parse(el.getAttribute('data-typewriter')); } catch (e) { return; }
      if (!Array.isArray(lines) || !lines.length) return;

      if (reduceMotion) { el.textContent = lines[0]; return; }

      var hold = parseInt(el.getAttribute('data-period'), 10) || 1900;
      var idx = 0, len = 0, erasing = false;

      (function tick() {
        var full = lines[idx % lines.length];
        len += erasing ? -1 : 1;
        el.textContent = full.slice(0, len);

        var wait = erasing ? 34 : 62 + Math.random() * 46;
        if (!erasing && len === full.length) { erasing = true; wait = hold; }
        else if (erasing && len === 0) { erasing = false; idx++; wait = 320; }

        setTimeout(tick, wait);
      })();
    });
  }

  /* ---------- The walker -------------------------------------
     A small bot sticks at 46% of the viewport and descends the
     rail as the page scrolls. Section nodes light up as it
     passes them; the rail behind it energises. */
  function initWalker() {
    var rail = document.querySelector('.rail');
    var walker = document.querySelector('.walker');
    var progress = document.querySelector('.rail-progress');
    if (!rail || !walker || !progress) return;
    if (!window.matchMedia('(min-width: 1181px)').matches) return;

    var nodes = Array.prototype.map.call(
      document.querySelectorAll('[data-node]'),
      function (section) { return { section: section, marker: section.querySelector('.node') }; }
    ).filter(function (n) { return n.marker; });

    var walking = false, idleTimer = null, scanTimer = null, queued = false;

    var stopWalking = function () {
      walking = false;
      walker.classList.remove('is-walking');
    };

    var scan = function () {
      walker.classList.add('is-scanning');
      clearTimeout(scanTimer);
      scanTimer = setTimeout(function () { walker.classList.remove('is-scanning'); }, 780);
    };

    var update = function () {
      queued = false;
      var railBox = rail.getBoundingClientRect();
      var botY = window.innerHeight * 0.46;

      var travelled = clamp(botY - railBox.top, 0, railBox.height);
      progress.style.height = travelled + 'px';
      walker.classList.toggle('is-live', travelled > 24);

      nodes.forEach(function (n) {
        var lit = n.marker.getBoundingClientRect().top <= botY + 4;
        if (lit === n.section.classList.contains('is-lit')) return;
        n.section.classList.toggle('is-lit', lit);
        if (lit) scan();
      });
    };

    var onScroll = function () {
      if (!walking) { walking = true; walker.classList.add('is-walking'); }
      clearTimeout(idleTimer);
      idleTimer = setTimeout(stopWalking, 170);
      if (!queued) { queued = true; requestAnimationFrame(update); }
    };

    update();
    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', function () {
      if (!queued) { queued = true; requestAnimationFrame(update); }
    }, { passive: true });
  }

  /* ---------- Reactive background ----------------------------
     three.js + Vanta NET, loaded only after first paint so it
     never blocks rendering. Skipped for reduced motion. */
  function initBackground() {
    var host = document.getElementById('bg-net');
    if (!host || reduceMotion) return;
    if (window.matchMedia('(max-width: 640px)').matches) return;

    var load = function (src) {
      return new Promise(function (resolve, reject) {
        var s = document.createElement('script');
        s.src = src;
        s.async = true;
        s.onload = resolve;
        s.onerror = reject;
        document.head.appendChild(s);
      });
    };

    load('https://cdnjs.cloudflare.com/ajax/libs/three.js/r134/three.min.js')
      .then(function () { return load('https://cdn.jsdelivr.net/npm/vanta@0.5.24/dist/vanta.net.min.js'); })
      .then(function () {
        if (!window.VANTA || !window.VANTA.NET) return;
        window.VANTA.NET({
          el: host,
          mouseControls: true,
          touchControls: false,
          gyroControls: false,
          minHeight: 200,
          minWidth: 200,
          scale: 1,
          scaleMobile: 1,
          color: 0x22d3ee,
          backgroundColor: 0x08090b,
          backgroundAlpha: 0,
          points: 9,
          maxDistance: 21,
          spacing: 19,
          showDots: true
        });
        host.classList.add('is-ready');
        setTimeout(function () { host.classList.add('is-live'); }, 1400);
        fadeOnScroll();
      })
      .catch(function () { /* background is decorative — ignore */ });
  }

  /* The network belongs to the hero. Past it, it recedes to a
     texture so body copy always wins. */
  function fadeOnScroll() {
    var root = document.documentElement;
    var queued = false;

    var apply = function () {
      queued = false;
      var span = window.innerHeight * 1.1;
      var t = Math.min(1, window.scrollY / span);
      root.style.setProperty('--net-opacity', (0.5 - 0.34 * t).toFixed(3));
    };

    apply();
    window.addEventListener('scroll', function () {
      if (!queued) { queued = true; requestAnimationFrame(apply); }
    }, { passive: true });
  }

  /* ---------- Contact form ----------------------------------- */
  function initForm() {
    var form = document.getElementById('contactForm');
    if (!form) return;
    var status = form.querySelector('.form-status');

    var setStatus = function (msg, kind) {
      if (!status) return;
      status.textContent = msg;
      status.className = 'form-status' + (kind ? ' is-' + kind : '');
    };

    var validate = function () {
      var ok = true;
      form.querySelectorAll('input[required], textarea[required]').forEach(function (input) {
        var field = input.closest('.field');
        var valid = input.type === 'email'
          ? /^\S+@\S+\.\S+$/.test(input.value.trim())
          : input.value.trim().length > 0;
        if (field) field.classList.toggle('is-invalid', !valid);
        if (!valid) ok = false;
      });
      return ok;
    };

    form.addEventListener('input', function (e) {
      var field = e.target.closest('.field.is-invalid');
      if (field) field.classList.remove('is-invalid');
    });

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!validate()) { setStatus('Please complete the highlighted fields.', 'error'); return; }

      var button = form.querySelector('button[type="submit"]');
      if (button) button.disabled = true;
      setStatus('Sending…');

      fetch(form.action, {
        method: form.method || 'POST',
        body: new FormData(form),
        headers: { Accept: 'application/json' }
      })
        .then(function (res) {
          if (!res.ok) return res.json().then(function (d) { throw new Error((d.errors || []).map(function (x) { return x.message; }).join(', ')); });
          setStatus('Thanks — your message is on its way.', 'ok');
          form.reset();
          setTimeout(function () { window.location.href = 'thanks.html'; }, 1200);
        })
        .catch(function (err) {
          setStatus(err.message || 'Something went wrong. Email hello at dans ch instead.', 'error');
          if (button) button.disabled = false;
        });
    });
  }

  /* ---------- Service worker --------------------------------- */
  function initServiceWorker() {
    if (location.protocol !== 'https:' || !('serviceWorker' in navigator)) return;
    navigator.serviceWorker.register('/sw.js').catch(function () {});
  }

  /* ---------- Boot ------------------------------------------- */
  function boot() {
    initHeader();
    initReveal();
    initTypewriter();
    initWalker();
    initForm();
    requestAnimationFrame(function () { setTimeout(initBackground, 120); });
    initServiceWorker();
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot);
  else boot();
})();
