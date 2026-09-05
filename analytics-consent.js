(() => {
  'use strict';

  const MEASUREMENT_ID = 'G-WL5X8JNFFL';
  const STORAGE_KEY = 'cfl_analytics_consent_v1';
  let analyticsLoaded = false;

  // Keep gtag calls local until the Google library is explicitly loaded.
  window.dataLayer = window.dataLayer || [];
  window.gtag = window.gtag || function gtag() { window.dataLayer.push(arguments); };

  const copy = {
    ro: {
      title: 'Preferințe analytics',
      text: 'Folosim analytics opțional ca să înțelegem ce pagini funcționează. Google Analytics se încarcă numai dacă accepți.',
      accept: 'Accept analytics',
      reject: 'Doar necesare',
      privacy: 'Confidențialitate'
    },
    en: {
      title: 'Analytics preferences',
      text: 'Optional analytics help us understand which pages work. Google Analytics loads only if you accept.',
      accept: 'Accept analytics',
      reject: 'Necessary only',
      privacy: 'Privacy'
    },
    de: {
      title: 'Analytics-Einstellungen',
      text: 'Optionale Analytics helfen uns zu verstehen, welche Seiten funktionieren. Google Analytics wird nur nach deiner Zustimmung geladen.',
      accept: 'Analytics akzeptieren',
      reject: 'Nur notwendige',
      privacy: 'Datenschutz'
    }
  };

  function language() {
    const lang = (document.documentElement.lang || 'ro').toLowerCase().slice(0, 2);
    return copy[lang] ? lang : 'ro';
  }

  function getChoice() {
    try { return localStorage.getItem(STORAGE_KEY); } catch (_) { return null; }
  }

  function setChoice(value) {
    try { localStorage.setItem(STORAGE_KEY, value); } catch (_) {}
  }

  function loadAnalytics() {
    if (analyticsLoaded) return;
    analyticsLoaded = true;

    const script = document.createElement('script');
    script.async = true;
    script.src = `https://www.googletagmanager.com/gtag/js?id=${encodeURIComponent(MEASUREMENT_ID)}`;
    document.head.appendChild(script);

    window.gtag('js', new Date());
    window.gtag('config', MEASUREMENT_ID);
  }

  function hideBanner() {
    document.getElementById('cfl-consent')?.remove();
  }

  function renderBanner(force = false) {
    if (!force && getChoice()) return;
    hideBanner();

    const t = copy[language()];
    const wrap = document.createElement('div');
    wrap.id = 'cfl-consent';
    wrap.setAttribute('role', 'dialog');
    wrap.setAttribute('aria-live', 'polite');
    wrap.setAttribute('aria-label', t.title);
    wrap.innerHTML = `
      <div class="cfl-consent__panel">
        <div class="cfl-consent__copy">
          <strong>${t.title}</strong>
          <span>${t.text} <a href="/privacy.html">${t.privacy}</a></span>
        </div>
        <div class="cfl-consent__actions">
          <button type="button" data-cfl-consent="necessary">${t.reject}</button>
          <button type="button" data-cfl-consent="analytics" class="primary">${t.accept}</button>
        </div>
      </div>`;

    const style = document.createElement('style');
    style.id = 'cfl-consent-style';
    style.textContent = `
      #cfl-consent{position:fixed;z-index:9999;left:16px;right:16px;bottom:16px;display:flex;justify-content:center;font-family:Inter,system-ui,sans-serif}
      .cfl-consent__panel{width:min(920px,100%);display:flex;gap:20px;align-items:center;justify-content:space-between;padding:18px 20px;border-radius:18px;border:1px solid rgba(255,255,255,.14);background:rgba(11,11,16,.96);box-shadow:0 18px 60px rgba(0,0,0,.5);backdrop-filter:blur(16px);color:#EBECF0}
      .cfl-consent__copy{display:grid;gap:5px;line-height:1.45;font-size:14px}.cfl-consent__copy strong{font-size:15px}.cfl-consent__copy span{color:#C8CBD2}.cfl-consent__copy a{color:#ffd166;text-decoration:underline}
      .cfl-consent__actions{display:flex;gap:10px;flex-wrap:wrap;flex:0 0 auto}.cfl-consent__actions button{border:1px solid rgba(255,255,255,.18);border-radius:999px;background:#17171f;color:#EBECF0;padding:11px 16px;font:inherit;font-weight:700;cursor:pointer}.cfl-consent__actions button.primary{border:0;background:linear-gradient(135deg,#ffd166,#8A5FFF);color:#0b0b10}
      @media(max-width:720px){.cfl-consent__panel{align-items:stretch;flex-direction:column}.cfl-consent__actions{display:grid;grid-template-columns:1fr 1fr}.cfl-consent__actions button{width:100%}}
    `;
    if (!document.getElementById(style.id)) document.head.appendChild(style);
    document.body.appendChild(wrap);

    wrap.addEventListener('click', (event) => {
      const button = event.target.closest('[data-cfl-consent]');
      if (!button) return;
      const value = button.getAttribute('data-cfl-consent');
      setChoice(value);
      hideBanner();
      if (value === 'analytics') loadAnalytics();
    });
  }

  function init() {
    const choice = getChoice();
    if (choice === 'analytics') loadAnalytics();
    if (!choice) renderBanner();
  }

  window.CashFlowLabPrivacy = {
    openAnalyticsSettings() {
      try { localStorage.removeItem(STORAGE_KEY); } catch (_) {}
      renderBanner(true);
    }
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init, { once: true });
  } else {
    init();
  }
})();
