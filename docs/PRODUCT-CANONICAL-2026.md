# CashFlowLab — Canonical Product Map 2026

**Data:** 2026-09-05  
**Scop:** să existe o singură regulă clară pentru ce fișiere reprezintă fiecare produs și ce poate fi promis public.

## Regula principală

Pagina de vânzare trebuie să descrie numai livrabile care există efectiv în sursa canonică de mai jos. Fișierele vechi din root, `archive/` sau folderele legacy pot fi utile ca referință, dar nu sunt automat parte din produsul curent.

## FREE Kit

**Sursă canonică:** `downloads/free-kit/`  
**Arhivă publică:** `downloads/free-kit.zip`

Livrabile verificate:
- `landing-template/index.html`
- `logos/logo-main.svg`
- `README.md`

Nu sunt verificate ca parte a pachetului curent: social covers, PNG/EPS, brand guidelines, curs video sau licențe speciale.

## MINI Kit

**Sursă canonică:** `products/mini-kit/`  
**Generație verificată:** 2026-06-17

Livrabile verificate:
- PDF Quick Launch Checklist — 2 pagini
- template Notion
- 4 emailuri
- README actualizat

Folderele `downloads/mini-kit/` și arhivele vechi trebuie tratate ca legacy/reference până când sunt comparate și regenerate din sursa canonică.

## MEDIUM Kit

**Sursă canonică:** `products/medium-kit/`  
**Generație verificată:** 2026-06-17

Livrabile verificate:
- PDF Launch Essentials — 4 pagini
- template Notion
- 4 emailuri
- README actualizat

Folderele `downloads/medium-kit/` și documentele vechi care promit 20+ template-uri, pagini de funnel gata construite sau automatizări preconfigurate sunt legacy/reference, nu livrabile canonice.

## PRO Kit

**Status:** blueprint verificat, packaging review necesar.

Surse verificate:
- `pro-kit-deliverables.md`
- `downloads/pro-kit/05-Checklists/zero-to-launch-master-checklist.md`
- `products/pro-kit/README.md` — documentația actuală de scope

Putem afirma:
- arhitectură de funnel;
- 10 emailuri template;
- master checklist Plan → Build → Test → Launch → Scale;
- QA și ghid de implementare/optimizare.

Nu afirmăm până nu sunt create și împachetate efectiv:
- 1-on-1;
- comunitate privată;
- curs video;
- automatizări Zapier/Make/ActiveCampaign gata configurate;
- brand assets complete;
- dashboard-uri/calculatoare lipsă;
- suport 24h neconfirmat.

## Fișiere legacy

Următoarele categorii nu se șterg automat, deoarece pot avea valoare istorică sau pot fi legate din livrări vechi:
- `archive/`
- `downloads/mini-kit/`
- `downloads/medium-kit/`
- `downloads/pro-kit/` în afara surselor PRO explicit verificate
- documentele vechi din root despre design, Notion, kit structure și audituri

La refresh-ul 2026 le putem muta într-o structură `legacy/` numai după verificarea linkurilor publice și a checkout-urilor existente.

## Prețuri de referință în branch-ul de cleanup

- FREE: $0
- MINI: $9
- MEDIUM: $27
- PRO: $69.99

Acestea sunt valori din repository. **Prețul și setările reale din Gumroad trebuie verificate separat înainte de deploy-ul 2026.**

## Sursa de date

`products-data.json` este registrul de referință actualizat. În prezent nu controlează automat paginile HTML; acestea sunt statice și au copy/prețuri hardcodate. La refresh-ul 2026 merită să eliminăm această duplicare și să generăm cardurile/paginile dintr-o singură sursă.
