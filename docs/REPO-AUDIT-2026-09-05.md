# CashFlowLab Repository Audit — 2026-09-05

## Rezumat

Audit efectuat pe branch-ul `jarvis/repo-cleanup-2026-09-05` pornind din `main`.

Repo-ul este funcțional, dar amestecă în același nivel:

- pagini live;
- materiale de produs;
- arhive;
- audituri vechi;
- documentație internă;
- scripturi de mentenanță;
- fișiere temporare generate accidental.

## Probleme corectate

### 1. `products-data.json` nu era JSON valid

Fișierul începea cu comentarii `#`, sintaxă invalidă pentru JSON. A fost convertit în JSON valid.

### 2. URL-urile Gumroad din datele de produs nu foloseau aceeași formă ca paginile live

URL-urile au fost aliniate la domeniul folosit de site: `https://cashflowlabai.gumroad.com/l/...`.

### 3. Notă de preț PRO inconsistentă

Datele produsului aveau prețul PRO `$69.99`, dar nota meta spunea `$65`. Nota a fost corectată.

### 4. Fișiere temporare în repository

Au fost eliminate:

- `EOF`
- `en/index.html.new`
- `de/index.html.new`

`.gitignore` a fost extins pentru a preveni revenirea fișierelor `*.new`, `EOF`, `*.bak` și `*.backup`.

### 5. Repository fără hartă clară

A fost adăugat `README.md` cu separarea dintre paginile active, produse, downloads, archive și documentația internă.

## Probleme găsite, dar lăsate pentru o modificare separată

### EN / DE SEO localization

În `en/index.html` și `de/index.html`:

- `<title>` este încă în română;
- `og:title` este în română;
- `og:description` este în română;
- `twitter:title` este în română;
- `twitter:description` este în română;
- `og:url` indică `https://cashflowlabai.com/` în loc de URL-ul localizat.

Acestea trebuie corectate fără a altera restul paginilor mari.

### Favicon declarat, dar lipsă

Paginile fac referire la:

- `/favicon/favicon.png`
- `/favicon/site.webmanifest`

Folderul `favicon/` nu există în repository. Trebuie fie adăugate asset-urile reale, fie eliminate/reconfigurate referințele.

### Garanții / mesaje comerciale inconsistente

Auditul vechi `AUDIT-COMPLET-CashFlowLab.md` afirmă că toate garanțiile au fost eliminate, însă `medium-kit/index.html` conține în prezent `Garanție 14 zile`.

Decizia comercială trebuie stabilită într-o singură sursă și apoi sincronizată în toate paginile și materialele.

### `products-data.json` nu este o sursă runtime

Deși documentația veche îl descria drept „sursa unică de adevăr”, paginile HTML sunt statice și conțin prețuri/linkuri hardcodate. Am marcat explicit acest lucru în `meta.runtime_source=false`.

### Audituri vechi

Mai multe fișiere de audit și planuri din root descriu stări mai vechi ale site-ului. Nu trebuie folosite ca adevăr curent fără verificarea fișierelor live.

## Structură recomandată pe termen mediu

```text
/
├── index.html
├── en/
├── de/
├── free-kit/
├── mini-kit/
├── medium-kit/
├── pro-kit/
├── Images/
├── products/
├── downloads/
├── docs/
│   ├── audits/
│   ├── product-plans/
│   └── operations/
├── scripts/
├── archive/
├── netlify.toml
├── products-data.json
└── README.md
```

Mutarea masivă a documentelor nu a fost făcută în acest PR deoarece poate rupe referințe interne și merită făcută separat, după verificarea dependențelor.

## Concluzie

Curățenia actuală este conservatoare: repară erori certe și elimină gunoi evident, fără să mute sau să șteargă materiale care pot fi încă necesare pentru produs ori deploy.
