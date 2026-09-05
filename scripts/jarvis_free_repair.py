from pathlib import Path
import re

PAGE = Path('free-kit/index.html')
text = PAGE.read_text(encoding='utf-8')


def replace_all(old: str, new: str, label: str) -> None:
    global text
    if old not in text:
        raise SystemExit(f'Missing expected FREE text for {label}: {old[:100]}')
    text = text.replace(old, new)


def replace_once(old: str, new: str, label: str) -> None:
    global text
    if old not in text:
        raise SystemExit(f'Missing expected FREE text for {label}: {old[:100]}')
    text = text.replace(old, new, 1)


# Metadata: only advertise assets that actually exist in downloads/free-kit.
replace_once(
    '<title>FREE CashFlowLab Starter Kit — Instrumente gratuite pentru cashflow predictibil</title>',
    '<title>FREE CashFlowLab Starter Kit — Landing Page Template + Logo SVG</title>',
    'title',
)
replace_once(
    '<meta name="description" content="Primește GRATUIT structura completă de landing page, logo-uri profesionale și brand guidelines. Primul pas către independența financiară.">',
    '<meta name="description" content="Descarcă gratuit un template de landing page responsive și logo-ul principal CashFlowLab în format SVG.">',
    'description',
)
replace_once(
    '<link rel="canonical" href="https://cashflowlabai.com/free-kit/">',
    '<link rel="canonical" href="https://cashflowlabai.com/free-kit/">\n  <link rel="icon" href="/favicon/favicon.png">',
    'favicon',
)
replace_once(
    '<meta property="og:title" content="FREE CashFlowLab Starter Kit — Instrumente gratuite pentru cashflow predictibil">',
    '<meta property="og:title" content="FREE CashFlowLab Starter Kit — Landing Page Template + Logo SVG">',
    'og title',
)
replace_once(
    '<meta property="og:description" content="Landing page template + Logo-uri + Brand guidelines. Gratis.">',
    '<meta property="og:description" content="Template HTML responsive + logo SVG. Gratuit.">',
    'og description',
)
replace_once(
    '<meta property="og:image" content="https://cashflowlabai.com/Images/og-free-kit.webp">',
    '<meta property="og:image" content="https://cashflowlabai.com/Images/og-hero-cover.webp">',
    'og image',
)

# Hero and preview cards.
replace_once(
    'Începe călătoria către independența financiară cu kitul nostru gratuit. Primești structura completă de landing page, logo-uri profesionale și elementele vizuale esențiale pentru a construi o prezență online premium.',
    'Primești gratuit un template de landing page responsive și logo-ul principal CashFlowLab în SVG — un punct de pornire simplu pe care îl poți edita pentru proiectul tău.',
    'hero copy',
)
replace_once('Logo CashFlowLab', 'Logo principal SVG', 'preview logo title')
replace_once('SVG, PNG, EPS în multiple formate', 'Fișier vectorial SVG, scalabil', 'preview logo formats')
replace_once('Social Media Covers', 'README de utilizare', 'preview social title')
replace_once('Instagram, Facebook, LinkedIn', 'Instrucțiuni pentru template și logo', 'preview social copy')
replace_once('Brand Guidelines', 'Structură editabilă', 'preview guidelines title')
replace_once('Paletă culori și tipografie', 'HTML simplu, ușor de personalizat', 'preview guidelines copy')

# What's inside: keep the real landing template and one SVG logo only.
replace_once(
    'Logo în Multiple Formate',
    'Logo principal în SVG',
    'inside logo title',
)
replace_once(
    'Varianta principală, icon-only, white version și monocrom. Toate în SVG, PNG și EPS pentru orice utilizare.',
    'Fișierul <code>logo-main.svg</code>, vectorial și scalabil, inclus în folderul <code>logos/</code>.',
    'inside logo copy',
)
replace_once(
    'Cover-uri Social Media',
    'README cu pașii de utilizare',
    'inside social title',
)
replace_once(
    'Dimensiuni optimizate pentru Instagram (1080×1080), Facebook (1200×630) și LinkedIn (1584×396).',
    'Instrucțiuni scurte pentru personalizarea template-ului și folosirea logo-ului.',
    'inside social copy',
)
replace_once(
    'OG Images',
    'Template responsive',
    'inside og title',
)
replace_once(
    'Imagini optimizate pentru sharing pe social media, cu dimensiunile corecte (1200×630).',
    'Landing page-ul este responsive și include structură de hero, beneficii, CTA și footer.',
    'inside og copy',
)
replace_once(
    'Brand Guidelines Basic',
    'Fișiere simple, fără dependențe',
    'inside guidelines title',
)
replace_once(
    'Paletă de culori exactă (HEX, RGB, CMYK), tipografie recomandată și reguli de utilizare logo.',
    'Template-ul poate fi deschis într-un editor și adaptat fără framework sau build system.',
    'inside guidelines copy',
)

# Remove invented social proof. We cannot substantiate these numbers/testimonial from the repo.
pattern = re.compile(r'\n<!-- Social Proof -->.*?\n<!-- FAQ -->', re.S)
text, count = pattern.subn('\n<!-- FAQ -->', text, count=1)
if count != 1:
    raise SystemExit(f'Expected one social-proof section, found {count}')

# Replace FAQ with verified, conservative answers.
faq = '''<!-- FAQ -->
<section style="padding:80px 0">
  <div class="container" style="max-width:800px">
    <div class="section-header">
      <h2>Întrebări frecvente</h2>
      <p>Ce conține versiunea verificată a FREE Kit-ului</p>
    </div>
    <div style="display:flex;flex-direction:column;gap:16px">
      <details style="border:1px solid rgba(255,255,255,.08);border-radius:16px;padding:20px;background:rgba(15,15,20,.6)">
        <summary style="font-weight:600;font-size:16px;cursor:pointer;list-style:none;display:flex;justify-content:space-between;align-items:center">Ce format au fișierele? <span style="font-size:20px">+</span></summary>
        <p style="color:var(--muted);margin:16px 0 0;font-size:15px;line-height:1.6">Pachetul verificat conține un template HTML și logo-ul principal în format SVG, plus README-ul cu instrucțiuni.</p>
      </details>
      <details style="border:1px solid rgba(255,255,255,.08);border-radius:16px;padding:20px;background:rgba(15,15,20,.6)">
        <summary style="font-weight:600;font-size:16px;cursor:pointer;list-style:none;display:flex;justify-content:space-between;align-items:center">Trebuie să știu programare? <span style="font-size:20px">+</span></summary>
        <p style="color:var(--muted);margin:16px 0 0;font-size:15px;line-height:1.6">Pentru modificări de text și linkuri ai nevoie doar de un editor de text. Pentru schimbări mai avansate de design ajută cunoștințe de HTML/CSS.</p>
      </details>
      <details style="border:1px solid rgba(255,255,255,.08);border-radius:16px;padding:20px;background:rgba(15,15,20,.6)">
        <summary style="font-weight:600;font-size:16px;cursor:pointer;list-style:none;display:flex;justify-content:space-between;align-items:center">Cum primesc fișierele? <span style="font-size:20px">+</span></summary>
        <p style="color:var(--muted);margin:16px 0 0;font-size:15px;line-height:1.6">Butonul de download de pe această pagină descarcă arhiva FREE Kit din site.</p>
      </details>
      <details style="border:1px solid rgba(255,255,255,.08);border-radius:16px;padding:20px;background:rgba(15,15,20,.6)">
        <summary style="font-weight:600;font-size:16px;cursor:pointer;list-style:none;display:flex;justify-content:space-between;align-items:center">Include cover-uri social, PNG/EPS sau brand guidelines? <span style="font-size:20px">+</span></summary>
        <p style="color:var(--muted);margin:16px 0 0;font-size:15px;line-height:1.6">Nu în versiunea curentă verificată. Pagina a fost corectată ca să descrie doar fișierele care există efectiv în pachet.</p>
      </details>
    </div>
  </div>
</section>

<!-- Final CTA -->'''
pattern = re.compile(r'<!-- FAQ -->.*?<!-- Final CTA -->', re.S)
text, count = pattern.subn(faq, text, count=1)
if count != 1:
    raise SystemExit(f'Expected one FAQ section, found {count}')

# Remove unverifiable value/marketing claims and align upsell cards everywhere.
replace_all('Valoare reală: $27 • Tu plătești: $0', 'Preț: $0', 'free value claim')
replace_all('După ce descarci, verifică și emailul pentru confirmare și next steps.', 'Arhiva se descarcă direct din această pagină.', 'email follow-up claim')
replace_all('3 landing variante + ghid 24h + branding complet', 'Checklist PDF + Notion + 4 emailuri', 'MINI upsell')
replace_all('PRO Kit — $39', 'PRO Kit — $69.99', 'PRO old price')
replace_all('Sistem complet cu funnel, 10 emailuri, automatizări și suport', 'Blueprint funnel + 10 emailuri + master checklist', 'PRO upsell scope')
replace_all('Alătură-te celor 1,200+ de creatori care și-au construit fundația brandului cu FREE Kit.', 'Descarcă template-ul și adaptează-l la proiectul tău.', 'final social proof')
replace_all('© 2025 CashFlowLab. Toate drepturile rezervate.', '© 2026 CashFlowLab. Toate drepturile rezervate.', 'copyright')

# Fix footer links: legal pages exist as root .html files on the static site.
replace_all('href="/terms/"', 'href="/terms.html"', 'terms link')
replace_all('href="/privacy/"', 'href="/privacy.html"', 'privacy link')

# Conservative trust copy: local file download is enough; no invented licensing/update promise.
replace_all('✓ Fără card de credit ✓ Instant download ✓ Folosește pentru totdeauna', '✓ Fără card ✓ Download direct ✓ Fișiere editabile', 'hero trust')
replace_all('♾️ Lifetime Use', '📦 Fișiere locale', 'trust lifetime')
replace_all('♾️ Lifetime', '📦 Fișiere locale', 'final trust lifetime')

# Sanity checks for claims that must no longer exist.
forbidden = [
    'og-free-kit.webp',
    'Social Media Covers',
    'Brand Guidelines Basic',
    'SVG, PNG, EPS',
    '1,247+',
    '4.9★',
    '89%',
    'Alex M.',
    'PRO Kit — $39',
    'documentație video',
    'mini-curs email',
    'update-uri gratuite',
    'licență completă pentru uz personal și comercial',
]
for needle in forbidden:
    if needle in text:
        raise SystemExit(f'Stale/unverified FREE claim remains: {needle}')

if '<html' not in text or '<body' not in text or '</html>' not in text:
    raise SystemExit('FREE HTML sanity check failed')
if not Path('downloads/free-kit/landing-template/index.html').exists():
    raise SystemExit('Missing FREE landing template')
if not Path('downloads/free-kit/logos/logo-main.svg').exists():
    raise SystemExit('Missing FREE SVG logo')
if not Path('downloads/free-kit.zip').exists():
    raise SystemExit('Missing FREE zip')
if not Path('Images/og-hero-cover.webp').exists():
    raise SystemExit('Missing shared OG image')

PAGE.write_text(text, encoding='utf-8')
print('FREE kit sales page aligned with verified package contents.')
