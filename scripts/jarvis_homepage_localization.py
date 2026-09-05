from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def replace_required(path: str, pairs: list[tuple[str, str]]) -> None:
    p = ROOT / path
    text = p.read_text(encoding='utf-8')
    for old, new in pairs:
        if old not in text:
            raise SystemExit(f'{path}: expected text missing: {old}')
        text = text.replace(old, new)
    p.write_text(text, encoding='utf-8')


replace_required('index.html', [
    ('<li>HTML landing page template</li>', '<li>Template HTML pentru landing page</li>'),
    ('<li>Main logo in SVG format</li>', '<li>Logo principal în format SVG</li>'),
    ('<li>README with basic instructions</li>', '<li>README cu instrucțiuni de bază</li>'),
    ('<li>2-page Quick Launch Checklist PDF</li>', '<li>Checklist PDF Quick Launch — 2 pagini</li>'),
    ('<li>Notion template for pre/post-launch</li>', '<li>Template Notion pentru pre/post-launch</li>'),
    ('<li>4 adaptable email templates + launch checks</li>', '<li>4 emailuri template + verificări de lansare</li>'),
    ('<li>4-page Launch Essentials PDF + CashFlowLab framework</li>', '<li>PDF Launch Essentials — 4 pagini + framework CashFlowLab</li>'),
    ('<li>Notion launch-system and metrics template</li>', '<li>Template Notion pentru sistemul de lansare și metrici</li>'),
    ('<li>4 email templates + launch checks</li>', '<li>4 emailuri template + verificări de lansare</li>'),
    ('<li>Funnel blueprint: landing → checkout → upsell</li>', '<li>Blueprint funnel: landing → checkout → upsell</li>'),
    ('<li>10 email templates</li>', '<li>10 emailuri template</li>'),
    ('<li>Master checklist: Plan → Build → Test → Launch → Scale</li>', '<li>Master checklist: Plan → Build → Test → Launch → Scale</li>'),
    ('<li>QA + implementation, measurement and optimization guide</li>', '<li>QA + ghid de implementare, măsurare și optimizare</li>'),
    ('<span class="kit-badge best-value">Best Value</span>', '<span class="kit-badge best-value">Cel mai complet</span>'),
    ('alt="Launch checklist and funnel structure"', 'alt="Checklist de lansare și structură de funnel"'),
    ('alt="CashFlowLab launch resource preview"', 'alt="Preview resursă de lansare CashFlowLab"'),
    ('alt="CashFlowLab implementation resource"', 'alt="Resursă de implementare CashFlowLab"'),
])

replace_required('en/index.html', [
    ('<h4>✅ Email confirmat!</h4>', '<h4>✅ Email confirmed!</h4>'),
    ('// Ascunde formularul', '// Hide the form'),
])

replace_required('de/index.html', [
    ('<li>HTML landing page template</li>', '<li>HTML-Landing-Page-Template</li>'),
    ('<li>Main logo in SVG format</li>', '<li>Hauptlogo im SVG-Format</li>'),
    ('<li>README with basic instructions</li>', '<li>README mit Basisanleitung</li>'),
    ('<li>2-page Quick Launch Checklist PDF</li>', '<li>2-seitige Quick-Launch-Checkliste als PDF</li>'),
    ('<li>Notion template for pre/post-launch</li>', '<li>Notion-Template für Pre-/Post-Launch</li>'),
    ('<li>4 adaptable email templates + launch checks</li>', '<li>4 anpassbare E-Mail-Templates + Launch-Prüfungen</li>'),
    ('<li>4-page Launch Essentials PDF + CashFlowLab framework</li>', '<li>4-seitiges Launch-Essentials-PDF + CashFlowLab-Framework</li>'),
    ('<li>Notion launch-system and metrics template</li>', '<li>Notion-Template für Launch-System und Metriken</li>'),
    ('<li>4 email templates + launch checks</li>', '<li>4 E-Mail-Templates + Launch-Prüfungen</li>'),
    ('<li>Funnel blueprint: landing → checkout → upsell</li>', '<li>Funnel-Blueprint: Landing → Checkout → Upsell</li>'),
    ('<li>10 email templates</li>', '<li>10 E-Mail-Templates</li>'),
    ('<li>Master checklist: Plan → Build → Test → Launch → Scale</li>', '<li>Master-Checkliste: Plan → Build → Test → Launch → Scale</li>'),
    ('<li>QA + implementation, measurement and optimization guide</li>', '<li>QA + Leitfaden für Implementierung, Messung und Optimierung</li>'),
    ('<span class="kit-badge best-value">Best Value</span>', '<span class="kit-badge best-value">Komplett</span>'),
    ('alt="Launch checklist and funnel structure"', 'alt="Launch-Checkliste und Funnel-Struktur"'),
    ('alt="CashFlowLab launch resource preview"', 'alt="Vorschau einer CashFlowLab Launch-Ressource"'),
    ('alt="CashFlowLab implementation resource"', 'alt="CashFlowLab Umsetzungsressource"'),
    ('// Ascunde formularul', '// Formular ausblenden'),
])

# Add permanent language guards so mixed-language product cards cannot silently return.
vp = ROOT / 'scripts/validate_repo.py'
v = vp.read_text(encoding='utf-8')
marker = '# Homepage localization invariants (2026).'
if marker not in v:
    guard = '''\n# Homepage localization invariants (2026).\nlocalization_rules = {\n    'index.html': {\n        'required': ('Template HTML pentru landing page', '10 emailuri template', 'QA + ghid de implementare, măsurare și optimizare'),\n        'forbidden': ('Main logo in SVG format', '2-page Quick Launch Checklist PDF', 'Best Value'),\n    },\n    'en/index.html': {\n        'required': ('Email confirmed!', '10 email templates', 'QA + implementation, measurement and optimization guide'),\n        'forbidden': ('Email confirmat!', 'TVA inclus'),\n    },\n    'de/index.html': {\n        'required': ('HTML-Landing-Page-Template', '10 E-Mail-Templates', 'QA + Leitfaden für Implementierung, Messung und Optimierung'),\n        'forbidden': ('Main logo in SVG format', '2-page Quick Launch Checklist PDF', 'Email confirmat!', 'TVA inclus'),\n    },\n}\nfor rel, rules in localization_rules.items():\n    text = read(rel)\n    for needle in rules['required']:\n        if needle not in text:\n            fail(f'{rel}: localization marker missing: {needle}')\n    for needle in rules['forbidden']:\n        if needle in text:\n            fail(f'{rel}: mixed/stale localization returned: {needle}')\n\n'''
    anchor = '# Canonical package files that must remain available.\n'
    if anchor not in v:
        raise SystemExit('validator localization anchor missing')
    v = v.replace(anchor, guard + anchor, 1)
    vp.write_text(v, encoding='utf-8')

print('Final RO/EN/DE homepage localization pass completed.')
