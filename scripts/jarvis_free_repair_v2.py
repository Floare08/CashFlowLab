from pathlib import Path
import runpy

page = Path('free-kit/index.html')
text = page.read_text(encoding='utf-8')

replacements = {
    '<p style="color:var(--muted);margin:0;font-size:14px">Valoare reală: $27</p>': '<p style="color:var(--muted);margin:0;font-size:14px">Preț: $0</p>',
    '<span style="font-size:14px;color:var(--muted)">Logo Pack (5 variante)</span>': '<span style="font-size:14px;color:var(--muted)">Logo principal SVG</span>',
    '<span style="font-size:14px;color:var(--muted)">Social Media Covers</span>': '<span style="font-size:14px;color:var(--muted)">README de utilizare</span>',
    '<span style="font-size:14px;color:var(--muted)">Brand Guidelines</span>': '<span style="font-size:14px;color:var(--muted)">Template HTML responsive</span>',
    'Construiește-ți brandul personal cu elemente vizuale profesionale de la prima interacțiune.': 'Folosește template-ul ca punct de pornire pentru o pagină simplă de prezentare.',
    'Blogeri, YouTuberi sau influenceri din nisa financiară care vor consistență vizuală.': 'Creatori care vor un exemplu simplu de landing page pe care să-l adapteze.',
    'Ai o idee de business dar nu ai buget pentru branding? Aceasta e soluția.': 'Ai o idee și vrei să testezi rapid o pagină de prezentare fără cost pentru template.',
}

for old, new in replacements.items():
    if old not in text:
        raise SystemExit(f'Missing expected FREE v2 text: {old[:100]}')
    text = text.replace(old, new, 1)

page.write_text(text, encoding='utf-8')
runpy.run_path('scripts/jarvis_free_repair.py', run_name='__main__')
