# MEMORY.md - CashFlowLab Project

## Proiect: CashFlowLab AI Website
**URL:** https://cashflowlabai.com  
**Ultima activitate:** Iunie 2025  
**Status:** Reactivat - în lucru activ

### Fișiere active (Workspace curățat)
- **index.html** ← Versiunea RO principală (fost `cashflowlab_index_FIXED_CLEAN.html`)
- **cashflowlab_index_EN.html** ← Versiunea engleză
- **cashflowlab_index_DE.html** ← Versiunea germană

### Archive (backup)
- `cashflowlab_index.html` (vechi, feb 2025)
- `cashflowlab_index_FIXED.html` (variantă intermediară)
- `cashflowlab_combined.html`
- SEO complet: Open Graph, Twitter Cards, JSON-LD Schema
- Suport multilingv pregătit (RO/EN/DE) - hreflang tags + data-i18n attributes
- Fonturi: Inter + Playfair Display
- Produse: Free Kit, Mini Kit, Medium Kit, PRO Kit (în HTML)
- Schema.org Product pentru PRO Kit $39
- Formular captură email în hero

---

## 🎯 LISTĂ PRIORITARĂ - CASHFLOWLAB

### FAZA 1: FUNDAMENT (Corecții critice)
**Prioritate: MAXIMĂ**

1. **CTA-uri și butoane** ✅ *Completat*
   - [x] FREE Kit - link corectat la `/l/jktsac` (era `/l/linjxk` - 404)
   - [x] MINI Kit - `/l/bpsbou` ✅ verificat
   - [x] MEDIUM Kit - `/l/divha` ✅ verificat  
   - [x] PRO Kit - `/l/udxody` ✅ verificat
   - [x] **Formular MailerLite fixat** — schimbat de la form ID `35810117` la `176693602287617412` (cel legat de automation)
   - [x] **Fix ID container și callback** — corectat `mlb2-35810117` → `mlb2-176693602287617412` și funcția success
   - [x] **Redirect corectat** — formularul duce acum la `/free-kit.html` (pagină proprie)
   - [x] **Creată pagina Free Kit** — `/free-kit.html` cu design modern, preview Notion, CTA (actualizat pentru structură hibridă)
   - [x] **Structură Notion hibrid gata** — salvată în `notion-template-structure.md`
     - 20 slide-uri vizuale (ghid prezentare)
     - 4 pagini de lucru (Claritate, Ofertă, Funnel, Acțiuni)
     - Database pentru task-uri
   - [ ] Creare efectivă template în Notion (Florin)
   - [x] Ascuns link-urile EN/DE până avem pagini traduse
   - [x] Ascuns link-urile legale (terms, privacy, imprint) până creăm paginile

2. **Navigare și UX**
   - Header sticky - verificare comportament la scroll
   - Mobile menu (dacă există) - testare responsive
   - Anchor links (Features, Kits, etc.) - verificare smooth scroll

### FAZA 2: MULTILINGV (Extindere)
**Prioritate: RIDICATĂ**

3. **Switcher limbă (UI)**
   - Dropdown sau flag-uri în header
   - Stil consistent cu design-ul existent

4. **Traducere EN**
   - Traducere completă texte data-i18n
   - Creare `index-en.html` sau sistem switch

5. **Traducere DE**
   - Traducere completă în germană
   - Creare `index-de.html` sau sistem switch

### FAZA 3: PRODUSE (Conversie)
**Prioritate: RIDICATĂ**

6. **Pagini produs individuale**
   - Pagină dedicată Free Kit
   - Pagină dedicată Mini Kit  
   - Pagină dedicată Medium Kit
   - Pagină dedicată PRO Kit

7. **Redesign showcase produse**
   - Card-uri mai informative
   - Prețuri vizibile
   - Feature comparison table
   - "Best value" badge pe Medium/PRO

8. **Checkout flow**
   - Link-uri directe Gumroad verificate
   - Upsell/downsell logic (opțional)

### FAZA 4: IMPLEMENTĂRI TEHNICE (Polish)
**Prioritate: MEDIE**

9. **Performance**
    - Lazy loading imagini
    - Optimizare fonturi (subset)
    - Minificare CSS/JS

10. **Analytics și tracking**
    - Google Analytics 4 verificat
    - Facebook Pixel (dacă e cazul)
    - Event tracking butoane CTA

11. **Legal**
    - Creare pagină Terms of Service
    - Creare pagină Privacy Policy
    - Creare pagină Imprint

---

## 📋 STATUS ACTIV

**Lucrăm la:** Faza 1 - Corecții butoane CTA  
**Audit complet:** Salvat în `audit-cta-cashflowlab.md`  
**Modificări făcute:**
1. ✅ FREE Kit - buton adăugat (link către `/l/linjxk`)
2. ✅ EN/DE ascunse din header (comentate)
3. ✅ Link-uri legale ascunse în footer (comentate)

**Următoarele:**
- Verificare manuală link-uri Gumroad (deschide-le în browser)
- Verificare formular hero (unde trimite emailurile?)

---

### Note personale
Floare = Florin, prietenii îi zic așa. E în Germania, pasionat de știință și tech. Vrea ca site-ul să arate profesionist și să convertească bine.

**Stil de lucru preferat:** Pas cu pas, verificăm de două ori înainte de deploy, păstrăm backup-uri.
