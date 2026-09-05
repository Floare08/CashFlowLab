from __future__ import annotations

from pathlib import Path
import json
import re
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []

ACTIVE_HTML = [
    Path('index.html'),
    Path('en/index.html'),
    Path('de/index.html'),
    Path('free-kit/index.html'),
    Path('mini-kit/index.html'),
    Path('medium-kit/index.html'),
    Path('pro-kit/index.html'),
    Path('privacy.html'),
    Path('terms.html'),
    Path('imprint.html'),
    Path('kit/index.html'),
    Path('kit/privacy.html'),
    Path('kit/terms.html'),
    Path('kit/imprint.html'),
]


def fail(message: str) -> None:
    ERRORS.append(message)


def read(rel: Path | str) -> str:
    path = ROOT / rel
    try:
        return path.read_text(encoding='utf-8')
    except Exception as exc:
        fail(f'Cannot read {rel}: {exc}')
        return ''


def resolve_local_url(url: str) -> Path | None:
    url = url.strip()
    if not url or url.startswith(('#', '//', 'http://', 'https://', 'mailto:', 'tel:', 'data:', 'javascript:')):
        return None
    # Cloudflare generates /cdn-cgi routes at runtime; they are not repository files.
    if url.startswith('/cdn-cgi/'):
        return None
    clean = url.split('#', 1)[0].split('?', 1)[0]
    if not clean:
        return None
    if clean == '/':
        return ROOT / 'index.html'
    if clean == '/favicon/favicon.png':
        # Netlify serves this via redirect to /Images/logo-mark.png.
        return ROOT / 'Images/logo-mark.png'
    rel = clean.lstrip('/')
    candidate = ROOT / rel
    if clean.endswith('/'):
        return candidate / 'index.html'
    if candidate.exists():
        return candidate
    # Extensionless static routes may map to folder/index.html.
    folder_index = candidate / 'index.html'
    if folder_index.exists():
        return folder_index
    return candidate


# Required project-level files.
for rel in [
    '.gitignore',
    'README.md',
    'netlify.toml',
    'products-data.json',
    'robots.txt',
    'sitemap.xml',
    'favicon/site.webmanifest',
    'docs/PRODUCT-CANONICAL-2026.md',
]:
    if not (ROOT / rel).exists():
        fail(f'Missing required file: {rel}')

# No obvious temporary artifacts.
if (ROOT / 'EOF').exists():
    fail('Stray EOF file exists')
for suffix in ('*.new', '*.tmp', '*.temp'):
    for path in ROOT.rglob(suffix):
        if '.git' not in path.parts:
            fail(f'Temporary file is tracked: {path.relative_to(ROOT)}')

# Every JSON file in the repo must parse.
for path in ROOT.rglob('*.json'):
    if '.git' in path.parts:
        continue
    try:
        json.loads(path.read_text(encoding='utf-8'))
    except Exception as exc:
        fail(f'Invalid JSON: {path.relative_to(ROOT)}: {exc}')

# Manifest must point at a real icon.
try:
    manifest = json.loads(read('favicon/site.webmanifest'))
    icons = manifest.get('icons', [])
    if not icons:
        fail('Manifest has no icons')
    for icon in icons:
        src = icon.get('src', '')
        target = resolve_local_url(src)
        if target is not None and not target.exists():
            fail(f'Manifest icon missing: {src}')
except Exception as exc:
    fail(f'Manifest validation failed: {exc}')

# Sitemap must be valid XML and contain the key public routes.
try:
    sitemap_root = ET.fromstring(read('sitemap.xml'))
    locs = {el.text.strip() for el in sitemap_root.iter() if el.tag.endswith('loc') and el.text}
    expected_locs = {
        'https://cashflowlabai.com/',
        'https://cashflowlabai.com/en/',
        'https://cashflowlabai.com/de/',
        'https://cashflowlabai.com/free-kit/',
        'https://cashflowlabai.com/mini-kit/',
        'https://cashflowlabai.com/medium-kit/',
        'https://cashflowlabai.com/pro-kit/',
    }
    for loc in sorted(expected_locs - locs):
        fail(f'Sitemap missing URL: {loc}')
except Exception as exc:
    fail(f'Invalid sitemap.xml: {exc}')

robots = read('robots.txt')
if 'Sitemap: https://cashflowlabai.com/sitemap.xml' not in robots:
    fail('robots.txt does not reference the canonical sitemap')

# Basic HTML and local-link/asset checks.
attr_re = re.compile(r'\b(?:src|href)=["\']([^"\']+)["\']', re.I)
og_re = re.compile(r'<meta\s+property=["\']og:image["\']\s+content=["\']https://cashflowlabai\.com/([^"\']+)["\']', re.I)

for rel in ACTIVE_HTML:
    path = ROOT / rel
    if not path.exists():
        fail(f'Missing active page: {rel}')
        continue
    text = read(rel)
    lower = text.lower()
    for marker in ('<html', '<head', '<body', '</html>'):
        if marker not in lower:
            fail(f'{rel}: missing {marker}')
    for url in attr_re.findall(text):
        target = resolve_local_url(url)
        if target is not None and not target.exists():
            fail(f'{rel}: broken local reference {url} -> {target.relative_to(ROOT)}')
    for og_path in og_re.findall(text):
        target = ROOT / og_path
        if not target.exists():
            fail(f'{rel}: missing local OG image /{og_path}')

# Product registry invariants.
try:
    registry = json.loads(read('products-data.json'))
    products = registry['products']
    expected = {
        'free_kit': 0,
        'mini_kit': 9,
        'medium_kit': 27,
        'pro_kit': 69.99,
    }
    for key, price in expected.items():
        if key not in products:
            fail(f'products-data.json missing {key}')
            continue
        if products[key].get('price') != price:
            fail(f'products-data.json unexpected {key} price: {products[key].get("price")}')
        if not products[key].get('verification_status'):
            fail(f'products-data.json missing verification_status for {key}')
except Exception as exc:
    fail(f'Product registry validation failed: {exc}')

# Guard against known stale/unverified sales claims returning to active pages.
for rel, forbidden in {
    'free-kit/index.html': [
        'og-free-kit.webp', 'PRO Kit — $39', '1,247+', '4.9★', '89%', 'Alex M.',
        'SVG, PNG, EPS', 'documentație video', 'mini-curs email',
    ],
    'mini-kit/index.html': [
        '3 Landing Variante', 'Logo Pack (5 variațiuni)', 'Garanție 14 zile', 'CashFlow Brand în 24h',
    ],
    'medium-kit/index.html': [
        '5 Pagini de Funnel', '20+ Canva Templates', 'Garanție 14 zile', 'Automatizări Gata Configurate',
    ],
    'pro-kit/index.html': [
        'Suport 1-on-1', 'Garanție 14 zile', 'Automatizări Setup', 'Brand Assets Complete',
    ],
}.items():
    text = read(rel)
    for needle in forbidden:
        if needle in text:
            fail(f'{rel}: stale/unverified claim returned: {needle}')

# Canonical package files that must remain available.
for rel in [
    'downloads/free-kit.zip',
    'downloads/free-kit/landing-template/index.html',
    'downloads/free-kit/logos/logo-main.svg',
    'products/mini-kit/pdf/mini-kit.pdf',
    'products/mini-kit/notion/mini-kit-checklist.md',
    'products/medium-kit/pdf/medium-kit.pdf',
    'products/medium-kit/notion/medium-kit-template.md',
    'pro-kit-deliverables.md',
    'downloads/pro-kit/05-Checklists/zero-to-launch-master-checklist.md',
]:
    if not (ROOT / rel).exists():
        fail(f'Missing canonical product file: {rel}')

if ERRORS:
    print('Repository validation FAILED:\n')
    for item in ERRORS:
        print(f' - {item}')
    sys.exit(1)

print('Repository validation passed.')
print(f'Checked {len(ACTIVE_HTML)} active HTML pages and all JSON files.')
