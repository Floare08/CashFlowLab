# MEMORY.md - CashFlowLab Project

## Proiect: CashFlowLab AI Website
**URL:** https://cashflowlabai.com  
**Ultima activitate:** Iunie 2025  
**Status:** Reactivat - în lucru activ

### Ce avem până acum
- Landing page principal în română (`cashflowlab_index_FIXED.html`)
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

1. **CTA-uri și butoane** ✅ *În lucru - vezi `audit-cta-cashflowlab.md`*
   - [x] FREE Kit - adăugat buton funcțional către Gumroad
   - [ ] Verificare backend formular hero (unde merg emailurile?)
   - [x] Ascuns link-urile EN/DE până avem pagini traduse
   - [x] Ascuns link-urile legale (terms, privacy, imprint) până creăm paginile
   - [ ] Verificare link-uri Gumroad funcționale (testare manuală)

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
