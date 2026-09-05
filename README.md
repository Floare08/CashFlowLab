# CashFlowLab

Repository-ul principal pentru site-ul CashFlowLab și materialele produselor digitale.

## Ce este activ în producție

- `index.html` — pagina principală în română
- `en/index.html` — versiunea în engleză
- `de/index.html` — versiunea în germană
- `free-kit/index.html` — FREE Kit
- `mini-kit/index.html` — MINI Kit
- `medium-kit/index.html` — MEDIUM Kit
- `pro-kit/index.html` — PRO Kit
- `Images/` — asset-uri vizuale folosite de site
- `netlify.toml` — configurare Netlify și security headers
- `privacy.html`, `terms.html`, `imprint.html` — pagini legale

## Produse și livrabile

- `products/` — livrabilele structurate ale produselor
- `downloads/` — fișiere pregătite pentru download / bundle-uri
- `products-data.json` — date de referință pentru produse

> Important: site-ul este static și, în prezent, prețurile, textele și URL-urile produselor sunt încă hardcodate în paginile HTML. `products-data.json` nu actualizează automat site-ul.

## Materiale interne

Fișierele `.md` din root sunt în mare parte documentație, audituri, planuri, blueprint-uri și materiale de lucru. `archive/` conține versiuni HTML vechi care nu trebuie confundate cu paginile active.

## Reguli de lucru

1. Modificările site-ului live se fac în paginile active, nu în `archive/`.
2. Nu se păstrează fișiere temporare `*.new`, `*.tmp`, `*.temp` sau fișiere goale `EOF`.
3. Prețurile și linkurile trebuie verificate în toate paginile de limbă și kit înainte de deploy.
4. Schimbările mari se fac pe branch separat și se verifică înainte de merge în `main`.
5. Nu se șterg fișiere din `archive/`, `products/` sau `downloads/` fără verificarea dependențelor.

## Probleme cunoscute la auditul din 2026-09-05

- Meta title / Open Graph pentru paginile EN și DE conțin încă text în română.
- `og:url` pentru EN și DE indică pagina principală, nu URL-ul localizat.
- Paginile declară `/favicon/favicon.png` și `/favicon/site.webmanifest`, dar folderul `favicon/` nu există în repository.
- `products-data.json` a fost corectat pentru a fi JSON valid și pentru a reflecta clar că este doar date de referință.
- Unele documente vechi de audit nu mai reflectă starea actuală a site-ului și trebuie tratate ca istoric.

## Branch de curățenie

Auditul și curățenia Jarvis din 2026-09-05 sunt făcute pe:

`jarvis/repo-cleanup-2026-09-05`
