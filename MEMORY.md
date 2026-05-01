# MEMORY.md - CashFlowLab Project

## Proiect: CashFlowLab AI Website
**URL:** https://cashflowlabai.com  
**Ultima activitate:** 28 Aprilie 2026  
**Status:** Impecabil — pregătit pentru lansare 🚀

### Fișiere active (Workspace curățat)
- **index.html** ← Versiunea RO principală (live)
- **en/index.html** ← Versiunea engleză (live, link-uri legale activate)
- **de/index.html** ← Versiunea germană (live, link-uri legale activate)
- **privacy.html** ← Politica de Confidențialitate (GDPR complet, 7756 bytes)
- **terms.html** ← Termeni și Condiții (complet, 6420 bytes)
- **imprint.html** ← Imprint (EU compliant, 6630 bytes)
- **kit/index.html** ← Pagina kit-uri produse
- **kit/privacy.html** ← Backup legal (identic cu root)
- **kit/terms.html** ← Backup legal (identic cu root)
- **kit/imprint.html** ← Backup legal (identic cu root)

### Archive (backup)
- `cashflowlab_index.html` (vechi, feb 2025)
- `cashflowlab_index_FIXED.html` (variantă intermediară)
- `cashflowlab_combined.html`
- `cashflowlab_index_EN.html` / `cashflowlab_index_DE.html` (vechi, înainte de restructurare)

---

## 🎯 LISTĂ PRIORITARĂ - CASHFLOWLAB

### FAZA 1: FUNDAMENT (Corecții critice)
**Prioritate: MAXIMĂ — ✅ COMPLETAT**

1. **CTA-uri și butoane** ✅
   - [x] FREE Kit - link corectat la `/l/jktsac`
   - [x] MINI Kit - `/l/bpsbou` ✅ verificat
   - [x] MEDIUM Kit - `/l/divha` ✅ verificat  
   - [x] PRO Kit - `/l/udxody` ✅ verificat
   - [x] **Formular MailerLite fixat** — ID `176693602287617412`
   - [x] **Redirect corectat** — `/free-kit.html`

2. **Pagini legale** ✅ *Completat 28.04.2026*
   - [x] **Privacy Policy** — GDPR complet (7.7KB), tabel retenție date, drepturi utilizator
   - [x] **Terms of Service** — complet (6.4KB), limite răspundere, proprietate intelectuală
   - [x] **Imprint** — EU compliant (6.6KB), date companie, responsabilitate
   - [x] **Footer activat** — RO/EN/DE toate au link-uri funcționale către legal pages
   - [x] **Script suspect eliminat** — script kimi.com injectat, eliminat din head

3. **Analytics** ✅ *Completat 28.04.2026*
   - [x] **TikTok Pixel** — activ (ID: D6339KJC77U6FREANB80)
   - [x] **Cookie consent banner** — gata, gestionează analytics_storage
   - [x] **Google Analytics 4** — placeholder adăugat, TODO: înlocuiește `G-PLACEHOLDER` cu Measurement ID real
   - [x] **Preconnect** la GTM, Facebook, Hotjar, GA region

### FAZA 2: MULTILINGV (Extindere)
**Prioritate: RIDICATĂ**

4. **Switcher limbă (UI)** ✅
   - [x] Dropdown sau flag-uri în header — activ în toate 3 limbile

5. **Traducere EN** ✅
   - [x] Traducere completă — verificat, body complet în engleză

6. **Traducere DE** ✅
   - [x] Traducere completă — verificat, body complet în germană

### FAZA 3: PRODUSE (Conversie)
**Prioritate: RIDICATĂ**

7. **Pagini produs individuale** — Free Kit ✅
   - [x] Pagină dedicată Free Kit — creată `free-kit.html`
   - [ ] Pagină dedicată Mini Kit  
   - [ ] Pagină dedicată Medium Kit
   - [ ] Pagină dedicată PRO Kit

8. **Redesign showcase produse** — ⏳ Nefinalizat
   - [ ] Card-uri mai informative
   - [ ] Prețuri vizibile
   - [ ] Feature comparison table
   - [ ] "Best value" badge pe Medium/PRO

9. **Checkout flow** ✅
   - [x] Link-uri directe Gumroad verificate (manual — toate 4 funcționale)
   - [ ] Upsell/downsell logic (opțional)

### FAZA 4: IMPLEMENTĂRI TEHNICE (Polish)
**Prioritate: MEDIE**

10. **Performance**
    - [ ] Lazy loading imagini
    - [ ] Optimizare fonturi (subset)
    - [ ] Minificare CSS/JS

11. **Analytics și tracking**
    - [x] Google Analytics 4 — placeholder gata, așteaptă Measurement ID
    - [ ] Facebook Pixel (dacă e cazul)
    - [ ] Event tracking butoane CTA (data-evt deja există, trebuie conectat la GA4)

12. **Notion Template**
    - [ ] Creare efectivă template în Notion (Florin)
    - [ ] Structură salvată în `notion-template-structure.md` ✅

---

## 📋 STATUS ACTIV

**Lucrăm la:** Faza 4 — Polish final înainte de lansare  
**Ultimele modificări (28.04.2026):**
1. ✅ Pagini legale sincronizate din `kit/` în root (privacy, terms, imprint)
2. ✅ Canonical URLs actualizate pentru root
3. ✅ Footer RO — link-uri legale activate (nu mai sunt "în curând")
4. ✅ Footer EN — link-uri legale activate (Terms, Privacy, Imprint)
5. ✅ Footer DE — link-uri legale activate (AGB, Datenschutz, Impressum)
6. ✅ Script suspect kimi.com eliminat din `index.html`
7. ✅ Google Analytics 4 placeholder adăugat în head
8. ✅ Cookie consent management compatibil cu GA4

**TODO înainte de lansare:**
- [ ] Înlocuiește `G-PLACEHOLDER` în index.html cu Measurement ID real GA4
- [ ] Verificare manuală link-uri Gumroad (deschide-le în browser de pe telefon)
- [ ] Testare mobil pe Fold 6 (ambele moduri: cover display + inner display)
- [ ] Creare pagină Free Kit (`free-kit.html` lipsește din root)
- [ ] Traducere completă EN/DE (sau ascundere până sunt gata)
- [ ] Deploy pe Netlify și verificare live

---

### Note personale
Floare = Florin, prietenii îi zic așa. E în Germania, pasionat de știință și tech. Vrea ca site-ul să arate profesionist și să convertească bine.

**Stil de lucru preferat:** Pas cu pas, verificăm de două ori înainte de deploy, păstrăm backup-uri.

### Echipament
- **Telefon:** Samsung Galaxy Z Fold 6 (cu S Pen — esențial pentru lucru, degetele sunt "crenvuști" pentru touch precis 😂)
- **NU Z Fold 7** — a pierdut suportul S Pen, deci e inutil pentru workflow-ul lui Florin
