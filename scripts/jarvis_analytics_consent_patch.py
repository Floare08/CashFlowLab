from pathlib import Path
import re

pages = [Path('index.html'), Path('en/index.html'), Path('de/index.html')]
pattern = re.compile(
    r'\s*<!-- Google Analytics 4.*?-->\s*'
    r'<script async src="https://www\.googletagmanager\.com/gtag/js\?id=G-WL5X8JNFFL"></script>\s*'
    r'<script>.*?</script>',
    re.S,
)
replacement = '\n\n  <!-- Analytics loads only after explicit consent -->\n  <script src="/analytics-consent.js" defer></script>'

for page in pages:
    text = page.read_text(encoding='utf-8')
    text, count = pattern.subn(replacement, text, count=1)
    if count != 1:
        raise SystemExit(f'{page}: expected one legacy GA block, found {count}')
    if 'https://www.googletagmanager.com/gtag/js?id=G-WL5X8JNFFL' in text:
        raise SystemExit(f'{page}: direct GA loader still present')
    if '/analytics-consent.js' not in text:
        raise SystemExit(f'{page}: consent loader missing')
    page.write_text(text, encoding='utf-8')

print('Direct GA loaders replaced with consent-gated analytics on RO/EN/DE pages.')
