# CashFlowLab Products Documentation

## Overview

Acest director conține sistemul complet de produse digitale CashFlowLab. Toate datele produselor sunt centralizate în `products-data.json`, iar paginile HTML pentru fiecare kit sunt generate separat.

## Fișiere generate

```
workspace/
├── products-data.json          # Sursa unică de adevăr pentru toate produsele
├── mini-kit.html               # Pagina MINI Kit ($9)
├── medium-kit.html             # Pagina MEDIUM Kit ($27)
├── pro-kit.html                # Pagina PRO Kit ($97)
└── README-products.md          # Acest fișier (documentație)
```

## Structura products-data.json

### Nivelul Brand

```json
{
  "brand": {
    "name": "CashFlowLab",
    "url": "https://cashflowlabai.com",
    "tagline": "Sistemul AI care îți construiește cashflow predictibil",
    "colors": { /* culorile brandului */ }
  },
  "products": { /* produsele */ },
  "upsellPaths": { /* căi de upsell */ }
}
```

### Nivelul Produs

Fiecare produs are această structură:

```json
{
  "id": "mini-kit",
  "name": "MINI CashFlowLab Kit",
  "shortName": "MINI Kit",
  "price": 9,
  "comparePrice": 17,
  "currency": "$",
  "gumroadUrl": "https://cashflowlabai.gumroad.com/l/bpsbou",
  "badge": "MINI",
  "tagline": "Brand-ul tău financiar, pregătit în 24 de ore.",
  "description": "...",
  "promise": "...",
  "targetAudience": ["..."],
  "benefits": ["..."],
  "deliverables": [{"name": "...", "description": "..."}],
  "tools": ["..."],
  "implementationTime": "...",
  "resultsTime": "...",
  "frameworks": ["..."],
  "caseStudies": [{"name": "...", "result": "..."}],
  "bonuses": ["..."],
  "workflow": {"step1": {...}, ...},
  "seo": {"title": "...", "description": "...", "keywords": [...]}
}
```

## Cum să actualizezi produsele

### 1. Schimbare preț

Edit `products-data.json`:

```json
"mini": {
  "price": 12,        // ← preț nou
  "comparePrice": 19  // ← preț vechi pentru comparație
}
```

Apoi editează manual în pagina HTML respectivă (căută `$9` și înlocuiește cu `$12`).

### 2. Schimbare descriere

Edit `products-data.json`:

```json
"mini": {
  "description": "Descriere nouă aici..."
}
```

Pentru a actualiza și pagina HTML, caută textul vechi în fișier și înlocuiește.

### 3. Adăugare bonus nou

Edit `products-data.json`:

```json
"mini": {
  "bonuses": [
    "Bonus existent",
    "Bonus nou aici"  // ← adaugă aici
  ]
}
```

Adaugă și în HTML în secțiunea de bonusuri.

### 4. Schimbare link Gumroad

Edit `products-data.json`:

```json
"mini": {
  "gumroadUrl": "https://cashflowlabai.gumroad.com/l/NEW-LINK"
}
```

Actualizează și în HTML toate link-urile către Gumroad.

## Generare pagini noi

Dacă vrei să regenerezi complet paginile HTML:

1. Păstrează `products-data.json` ca sursă de adevăr
2. Folosește un script/template engine pentru a genera HTML din JSON
3. Alternativ, editează manual paginile existente

## Convenții de denumire

- **ID-uri produse**: `free-kit`, `mini-kit`, `medium-kit`, `pro-kit`
- **Fișiere HTML**: `{id}.html` (ex: `mini-kit.html`)
- **URL-uri**: `/{id}/` (ex: `https://cashflowlabai.com/mini-kit/`)

## SEO

Fiecare pagină are:
- Title unic
- Meta description
- Open Graph tags
- Twitter Card tags
- JSON-LD Product schema
- Canonical URL
- Hreflang pentru română

## Link-uri Gumroad

| Kit | Link |
|-----|------|
| FREE | https://cashflowlabai.gumroad.com/l/jktsac |
| MINI | https://cashflowlabai.gumroad.com/l/bpsbou |
| MEDIUM | https://cashflowlabai.gumroad.com/l/divha |
| PRO | https://cashflowlabai.gumroad.com/l/udxody |

## Prețuri curente

| Kit | Preț | Preț Comparativ |
|-----|------|-----------------|
| FREE | €0 | - |
| MINI | $9 | $17 |
| MEDIUM | $27 | $47 |
| PRO | $97 | $147 |

## Framework-uri brand

Toate kiturile folosesc aceste framework-uri originale:

1. **CashFlow Funnel Framework™** - Arhitectura de funnel
2. **Triple-Touch Automation™** - Sistemul de 3 atingeri
3. **Evergreen Conversion Architecture™** - Sistem autopilot
4. **Predictable CashFlow System™** - Cashflow stabil
5. **Zero to Launch Method™** - De la idee la live
6. **High-Ticket Conversion Framework™** - Vânzări premium

## Contact

Pentru întrebări sau actualizări: contact@cashflowlabai.com

---

*Ultima actualizare: 2025-04-07*
*Versiune: 1.0.0*