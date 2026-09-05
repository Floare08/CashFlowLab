from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def patch(path: str, replacements: list[tuple[str, str]], forbidden: list[str], required: list[str]) -> None:
    file_path = ROOT / path
    text = file_path.read_text(encoding='utf-8')
    for old, new in replacements:
        if old not in text:
            raise SystemExit(f'{path}: expected text not found: {old[:120]}')
        text = text.replace(old, new)
    for needle in forbidden:
        if needle in text:
            raise SystemExit(f'{path}: stale canonical claim remains: {needle}')
    for needle in required:
        if needle not in text:
            raise SystemExit(f'{path}: required canonical text missing: {needle}')
    file_path.write_text(text, encoding='utf-8')


RO = [
    ('<title>CashFlowLab — Sistemul AI care îți construiește cashflow predictibil</title>', '<title>CashFlowLab — Kituri și sisteme de lansare pentru produse digitale</title>'),
    ('<meta name="description" content="CashFlowLab îți oferă un sistem complet: kituri, funnel și automatizări AI pentru a lansa rapid și a scala un cashflow predictibil, fără improvizații." />', '<meta name="description" content="CashFlowLab oferă kituri de lansare verificate: checklist-uri, template-uri Notion, emailuri și un blueprint de funnel pentru produse digitale." />'),
    ('<meta property="og:title" content="CashFlowLab — Sistemul AI care îți construiește cashflow predictibil" />', '<meta property="og:title" content="CashFlowLab — Kituri și sisteme de lansare pentru produse digitale" />'),
    ('<meta property="og:description" content="Kiturile, funnelul și automatizările AI care îți scot primul cashflow și îl transformă într-un sistem predictibil." />', '<meta property="og:description" content="Checklist-uri, template-uri, emailuri și blueprint-uri de funnel bazate pe livrabilele verificate CashFlowLab." />'),
    ('<meta name="twitter:title" content="CashFlowLab — Sistemul AI care îți construiește cashflow predictibil" />', '<meta name="twitter:title" content="CashFlowLab — Kituri și sisteme de lansare pentru produse digitale" />'),
    ('<meta name="twitter:description" content="Kiturile, funnelul și automatizările AI care îți scot primul cashflow și îl transformă într-un sistem predictibil." />', '<meta name="twitter:description" content="Checklist-uri, template-uri, emailuri și blueprint-uri de funnel bazate pe livrabilele verificate CashFlowLab." />'),
    ('"description":"Funnel complet + 5 emailuri, automatizări avansate și suport."', '"description":"Blueprint de funnel + 10 emailuri template + master checklist + ghid de implementare și optimizare."'),
    ('<span class="badge" id="beta">v1 • Premium</span>', '<span class="badge" id="beta">2026 • Verificat</span>'),
    ('Lansare rapidă • Kituri + Funnel + Automatizări', 'Lansare clară • Checklist-uri + Template-uri + Funnel Blueprint'),
    ('Construiește un cashflow real cu un sistem AI, pas cu pas.', 'Lansează mai clar, cu resurse pe care le poți aplica pas cu pas.'),
    ('CashFlowLab îți dă un plan complet: <b>de la idee → la pagină → la lead → la ofertă</b>. Fără improvizații, fără "prompturi la întâmplare".', 'CashFlowLab organizează lansarea în pași practici: <b>checklist → mesaj → pagină → emailuri → ofertă</b>. Fiecare card de mai jos descrie doar livrabile verificate în repository.'),
    ('Kiturile sunt gata de folosit. Primești acces instant după înscriere / cumpărare.', 'FREE, MINI și MEDIUM au livrabile verificate. PRO este prezentat numai prin blueprint-ul și materialele confirmate în repository.'),
    ('Nu-ți vând „promisiuni". Îți dau un sistem clar: design + funnel + automate — ca să lansezi în ore, nu în săptămâni.', 'Nu-ți vindem promisiuni. Primești livrabile concrete: checklist-uri, template-uri, emailuri și un blueprint de funnel.'),
    ('Landing premium', 'Checklist-uri de lansare'),
    ('Hero strategic, secțiuni clare, SEO/OG, responsive și performanță.', 'MINI și MEDIUM includ checklist-uri PDF și pași clari pentru pre-launch și post-launch.'),
    ('Funnel + automate', 'Emailuri + funnel blueprint'),
    ('Workflow-uri preconfigurate + 5 emailuri PRO (Scale) — plug & play.', 'MINI și MEDIUM includ câte 4 emailuri, iar PRO include 10 emailuri template și arhitectura funnelului.'),
    ('Stil vizual', 'Implementare pas cu pas'),
    ('Gold + Purple + Tech Orb, cover & og-image incluse — arată scump din prima.', 'Template-urile Notion și master checklist-ul PRO te ajută să implementezi și să verifici lansarea.'),
    ('Resurse pregătite profesional pentru a construi rapid și a scală.', 'Resurse verificate în repository, organizate pe niveluri de la FREE la PRO.'),
    ('<h4 style="margin-bottom:10px">Landing Premium</h4>', '<h4 style="margin-bottom:10px">Checklist-uri & Template-uri</h4>'),
    ('Structură clară de landing page, conectată direct la Gumroad, fără fricțiune.', 'FREE oferă un template HTML, iar MINI și MEDIUM adaugă checklist-uri și template-uri Notion.'),
    ('<h4 style="margin-bottom:10px">Funnel & Automate</h4>', '<h4 style="margin-bottom:10px">Emailuri gata de adaptat</h4>'),
    ('Sistem complet: captare → nurturing → ofertă — gata de rulare.', 'MINI și MEDIUM includ câte 4 emailuri, iar PRO include o secvență de 10 emailuri template.'),
    ('<h4 style="margin-bottom:10px">Stil vizual</h4>', '<h4 style="margin-bottom:10px">Blueprint funnel & QA</h4>'),
    ('Tech orb, gold+purple, brand guidelines și cover-uri incluse.', 'PRO include arhitectura funnelului, master checklist și ghid de implementare, măsurare și optimizare.'),
    ('Începe simplu. Când vrei să construiești și să lansezi, treci pe PRO — fără să refaci totul.', 'Alege nivelul de care ai nevoie. Fiecare card listează numai livrabilele verificate în sursa canonică 2026.'),
    ('<div class="price">0€</div>', '<div class="price">$0</div>'),
    ('<li>Landing page de bază (structură clară)</li>\n              <li>Logo + cover vizual</li>\n              <li>OG image pentru share & preview</li>', '<li>Template HTML pentru landing page</li>\n              <li>Logo principal în format SVG</li>\n              <li>README cu instrucțiuni de bază</li>'),
    ('<div class="price">9$ <span class="tax">(TVA inclus)</span></div>', '<div class="price">$9</div>'),
    ('Ia MINI Kit — 9$ →', 'Ia MINI Kit — $9 →'),
    ('<div class="price">27$ <span class="tax">(TVA inclus)</span></div>', '<div class="price">$27</div>'),
    ('<li>4 emailuri + template-uri de landing/social</li>', '<li>4 emailuri + framework și verificări de lansare</li>'),
    ('Ia MEDIUM Kit — 27$ →', 'Ia MEDIUM Kit — $27 →'),
    ('<div class="price"><span class="old">97$</span>69,99$ <span class="tax">(TVA inclus)</span></div>', '<div class="price">$69.99</div>'),
    ('<li>Toolkit de implementare și template-uri de copy</li>', '<li>QA + ghid de implementare, măsurare și optimizare</li>'),
    ('Acces PRO – 69,99$', 'Acces PRO — $69.99'),
    ('Primești pagină + structură funnel + automate — ca să nu reconstruiești de la zero.', 'Primești checklist-uri, template-uri, emailuri și blueprint de funnel — fără să reconstruiești structura de la zero.'),
    ('Totul e gândit pentru "copypaste + adaptare". Începi cu Free, treci pe PRO când vrei să scalezi.', 'Materialele sunt organizate pentru adaptare rapidă. Începi cu FREE și alegi nivelul următor doar când ai nevoie de mai multă structură.'),
    ('CTA-uri, OG preview, assets și flow-uri clare — făcute să arate premium în share și ads.', 'Fiecare nivel are un scope clar, iar pagina publică descrie doar materialele pe care le putem verifica.'),
]

EN = [
    ('<title>CashFlowLab — AI Launch Systems for Predictable Cashflow</title>', '<title>CashFlowLab — Launch Kits & Systems for Digital Products</title>'),
    ('<meta name="description" content="CashFlowLab gives you a complete system: kits, funnels and AI automations to launch quickly and scale predictable cashflow, without guesswork." />', '<meta name="description" content="CashFlowLab offers verified launch kits with checklists, Notion templates, email sequences and a funnel blueprint for digital products." />'),
    ('<meta property="og:title" content="CashFlowLab — AI Launch Systems for Predictable Cashflow" />', '<meta property="og:title" content="CashFlowLab — Launch Kits & Systems for Digital Products" />'),
    ('<meta property="og:description" content="Launch faster with ready-to-use kits, funnels and AI automations built to turn traffic into a predictable sales system." />', '<meta property="og:description" content="Verified checklists, templates, email sequences and funnel blueprints for clearer digital-product launches." />'),
    ('<meta name="twitter:title" content="CashFlowLab — AI Launch Systems for Predictable Cashflow" />', '<meta name="twitter:title" content="CashFlowLab — Launch Kits & Systems for Digital Products" />'),
    ('<meta name="twitter:description" content="Launch faster with ready-to-use kits, funnels and AI automations built to turn traffic into a predictable sales system." />', '<meta name="twitter:description" content="Verified checklists, templates, email sequences and funnel blueprints for clearer digital-product launches." />'),
    ('"description":"Complete funnel + 5 emails, advanced automations and support."', '"description":"Funnel blueprint + 10 email templates + master checklist + implementation and optimization guide."'),
    ('<span class="badge" id="beta">v1 • Premium</span>', '<span class="badge" id="beta">2026 • Verified</span>'),
    ('Quick Launch • Kits + Funnel + Automations', 'Clear Launch • Checklists + Templates + Funnel Blueprint'),
    ('Build real cashflow with an AI system, step by step.', 'Launch more clearly with practical resources you can apply step by step.'),
    ('CashFlowLab gives you a complete plan: <b>from idea → to page → to lead → to offer</b>. No guesswork, no random prompts.', 'CashFlowLab organizes the launch into practical steps: <b>checklist → message → page → emails → offer</b>. Every card below lists only repository-verified deliverables.'),
    ('<h4>✅ Email confirmat!</h4>', '<h4>✅ Email confirmed!</h4>'),
    ('✔ 1 email/zi max', '✔ Up to 1 email/day'),
    ('Kits are ready to use. You get instant access after signing up / purchasing.', 'FREE, MINI and MEDIUM have verified deliverables. PRO is presented only through the blueprint and materials confirmed in the repository.'),
    ('We don\'t sell "promises". We give you a clear system: design + funnel + automations — so you launch in hours, not weeks.', 'We do not sell promises. You get concrete deliverables: checklists, templates, email sequences and a funnel blueprint.'),
    ('Premium Landing', 'Launch Checklists'),
    ('Strategic hero, clear sections, SEO/OG, responsive and performant.', 'MINI and MEDIUM include PDF checklists and clear pre-launch and post-launch steps.'),
    ('Funnel + Automations', 'Emails + Funnel Blueprint'),
    ('Workflow-uri preconfigurate + 5 emailuri PRO (Scale) — plug & play.', 'MINI and MEDIUM each include 4 emails, while PRO includes 10 email templates and the funnel architecture.'),
    ('Visual Style', 'Step-by-Step Implementation'),
    ('Gold + Purple + Tech Orb, cover & og-image included — looks premium from the start.', 'Notion templates and the PRO master checklist help you implement and verify the launch.'),
    ('Preview OG cover pentru share', 'Launch resource preview'),
    ('Identitate vizuală CashFlowLab', 'CashFlowLab implementation resource'),
    ('Professionally prepared resources to build quickly and scale.', 'Repository-verified resources organized from FREE through PRO.'),
    ('<h4 style="margin-bottom:10px">Landing Premium</h4>', '<h4 style="margin-bottom:10px">Checklists & Templates</h4>'),
    ('Clear landing page structure, connected directly to Gumroad, without friction.', 'FREE includes an HTML landing template; MINI and MEDIUM add checklists and Notion templates.'),
    ('<h4 style="margin-bottom:10px">Funnel & Automations</h4>', '<h4 style="margin-bottom:10px">Emails Ready to Adapt</h4>'),
    ('Complete system: capture → nurturing → offer — ready to run.', 'MINI and MEDIUM each include 4 emails, while PRO includes a 10-email template sequence.'),
    ('<h4 style="margin-bottom:10px">Visual Style</h4>', '<h4 style="margin-bottom:10px">Funnel Blueprint & QA</h4>'),
    ('Tech orb, gold+purple, brand guidelines and covers included.', 'PRO includes funnel architecture, a master checklist, QA and an implementation/optimization guide.'),
    ('Start simple. When you want to build and launch, upgrade to PRO — without rebuilding everything.', 'Choose the level you need. Every card lists only deliverables verified in the 2026 canonical source.'),
    ('<div class="price">0€</div>', '<div class="price">$0</div>'),
    ('<li>Basic landing page (clear structure)</li>\n              <li>Logo + visual cover</li>\n              <li>OG image for share & preview</li>', '<li>HTML landing page template</li>\n              <li>Main logo in SVG format</li>\n              <li>README with basic instructions</li>'),
    ('<div class="price">9$ <span class="tax">(TVA inclus)</span></div>', '<div class="price">$9</div>'),
    ('<li>Premium Landing (copy + improved structure)</li>\n              <li>Coherent branding, ready to use</li>\n              <li>Quick guide: from idea to online</li>', '<li>2-page Quick Launch Checklist PDF</li>\n              <li>Notion template for pre/post-launch</li>\n              <li>4 adaptable email templates</li>'),
    ('<div class="price">27$ <span class="tax">(TVA inclus)</span></div>', '<div class="price">$27</div>'),
    ('<li>Complete funnel structure (clear, logical)</li>\n              <li>Basic automations explained step by step</li>\n              <li>Templates ready for execution</li>', '<li>4-page Launch Essentials PDF + CashFlowLab framework</li>\n              <li>Notion launch-system and metrics template</li>\n              <li>4 email templates + launch checks</li>'),
    ('<div class="price"><span class="old">97$</span>69,99$ <span class="tax">(TVA inclus)</span></div>', '<div class="price">$69.99</div>'),
    ('<li>Complete system: funnel + landing + offer</li>\n              <li>5 email sequence (copy included)</li>\n              <li>Clear automations, ready to use</li>\n              <li>Launch checklist + future updates</li>', '<li>Funnel blueprint: landing → checkout → upsell</li>\n              <li>10 email templates</li>\n              <li>Master checklist: Plan → Build → Test → Launch → Scale</li>\n              <li>QA + implementation, measurement and optimization guide</li>'),
    ('You get page + funnel structure + automations — so you don\'t rebuild from zero.', 'You get checklists, templates, emails and a funnel blueprint — so you do not rebuild the structure from zero.'),
    ('Everything is designed for "copy-paste + adaptation". Start with Free, upgrade to PRO when you want to scale.', 'Materials are organized for quick adaptation. Start with FREE and move up only when you need more launch structure.'),
    ('CTAs, OG preview, assets and clear flows — made to look premium in shares and ads.', 'Each level has a clear scope, and the public page lists only materials we can verify.'),
]

DE = [
    ('<title>CashFlowLab — KI-Launch-Systeme für planbaren Cashflow</title>', '<title>CashFlowLab — Launch-Kits & Systeme für digitale Produkte</title>'),
    ('<meta name="description" content="CashFlowLab bietet ein komplettes System: Kits, Funnels und KI-Automatisierungen zum schnellen Start und Skalieren eines vorhersagbaren Cashflows, ohne Rätselraten." />', '<meta name="description" content="CashFlowLab bietet verifizierte Launch-Kits mit Checklisten, Notion-Templates, E-Mail-Sequenzen und einem Funnel-Blueprint für digitale Produkte." />'),
    ('<meta property="og:title" content="CashFlowLab — KI-Launch-Systeme für planbaren Cashflow" />', '<meta property="og:title" content="CashFlowLab — Launch-Kits & Systeme für digitale Produkte" />'),
    ('<meta property="og:description" content="Starte schneller mit einsatzbereiten Kits, Funnels und KI-Automatisierungen für ein planbares Verkaufssystem." />', '<meta property="og:description" content="Verifizierte Checklisten, Templates, E-Mail-Sequenzen und Funnel-Blueprints für klarere Launches digitaler Produkte." />'),
    ('<meta name="twitter:title" content="CashFlowLab — KI-Launch-Systeme für planbaren Cashflow" />', '<meta name="twitter:title" content="CashFlowLab — Launch-Kits & Systeme für digitale Produkte" />'),
    ('<meta name="twitter:description" content="Starte schneller mit einsatzbereiten Kits, Funnels und KI-Automatisierungen für ein planbares Verkaufssystem." />', '<meta name="twitter:description" content="Verifizierte Checklisten, Templates, E-Mail-Sequenzen und Funnel-Blueprints für klarere Launches digitaler Produkte." />'),
    ('"description":"Vollständiger Funnel + 5 E-Mails, erweiterte Automatisierungen und Support."', '"description":"Funnel-Blueprint + 10 E-Mail-Templates + Master-Checkliste + Leitfaden für Implementierung und Optimierung."'),
    ('<span class="badge" id="beta">v1 • Premium</span>', '<span class="badge" id="beta">2026 • Geprüft</span>'),
    ('Schneller Start • Kits + Funnel + Automatisierungen', 'Klarer Launch • Checklisten + Templates + Funnel-Blueprint'),
    ('Baue echten Cashflow mit einem KI-System, Schritt für Schritt.', 'Starte klarer mit praktischen Ressourcen, die du Schritt für Schritt anwenden kannst.'),
    ('CashFlowLab gibt dir einen kompletten Plan: <b>von Idee → zu Seite → zu Lead → zu Angebot</b>. Kein Rätselraten, keine zufälligen Prompts.', 'CashFlowLab ordnet den Launch in praktische Schritte: <b>Checkliste → Botschaft → Seite → E-Mails → Angebot</b>. Jede Karte unten nennt nur im Repository verifizierte Inhalte.'),
    ('<h4>✅ Email confirmat!</h4>', '<h4>✅ E-Mail bestätigt!</h4>'),
    ('✔ 1 email/zi max', '✔ Max. 1 E-Mail/Tag'),
    ('Die Kits sind einsatzbereit. Sie erhalten sofortigen Zugriff nach der Anmeldung / dem Kauf.', 'FREE, MINI und MEDIUM haben verifizierte Inhalte. PRO wird nur mit dem Blueprint und den im Repository bestätigten Materialien dargestellt.'),
    ('Wir verkaufen keine „Versprechen". Wir geben dir ein klares System: Design + Funnel + Automatisierungen — damit du in Stunden, nicht in Wochen, startest.', 'Wir verkaufen keine Versprechen. Du erhältst konkrete Inhalte: Checklisten, Templates, E-Mail-Sequenzen und einen Funnel-Blueprint.'),
    ('Premium-Landing', 'Launch-Checklisten'),
    ('Strategischer Hero, klare Abschnitte, SEO/OG, responsiv und leistungsstark.', 'MINI und MEDIUM enthalten PDF-Checklisten und klare Schritte für Pre-Launch und Post-Launch.'),
    ('Funnel + automate', 'E-Mails + Funnel-Blueprint'),
    ('Workflow-uri preconfigurate + 5 emailuri PRO (Scale) — plug & play.', 'MINI und MEDIUM enthalten jeweils 4 E-Mails; PRO enthält 10 E-Mail-Templates und die Funnel-Architektur.'),
    ('Visueller Stil', 'Schrittweise Umsetzung'),
    ('Gold + Purple + Tech Orb, cover & og-image inklusive — sieht von Anfang an premium aus.', 'Notion-Templates und die PRO-Master-Checkliste helfen bei Umsetzung und Launch-Prüfung.'),
    ('Preview OG cover pentru share', 'Vorschau einer Launch-Ressource'),
    ('Identitate vizuală CashFlowLab', 'CashFlowLab Umsetzungsressource'),
    ('Professionell vorbereitete Ressourcen zum schnellen Bauen und Skalieren.', 'Im Repository verifizierte Ressourcen, organisiert von FREE bis PRO.'),
    ('<h4 style="margin-bottom:10px">Landing Premium</h4>', '<h4 style="margin-bottom:10px">Checklisten & Templates</h4>'),
    ('Klare Landing-Page-Struktur, direkt mit Gumroad verbunden, ohne Reibung.', 'FREE enthält ein HTML-Landing-Template; MINI und MEDIUM ergänzen Checklisten und Notion-Templates.'),
    ('<h4 style="margin-bottom:10px">Funnel & Automate</h4>', '<h4 style="margin-bottom:10px">E-Mails zum Anpassen</h4>'),
    ('Komplettes System: Erfassung → Pflege → Angebot — bereit zum Start.', 'MINI und MEDIUM enthalten jeweils 4 E-Mails; PRO enthält eine Sequenz aus 10 E-Mail-Templates.'),
    ('<h4 style="margin-bottom:10px">Visueller Stil</h4>', '<h4 style="margin-bottom:10px">Funnel-Blueprint & QA</h4>'),
    ('Tech orb, gold+purple, Brand-Guidelines und Cover inklusive.', 'PRO enthält Funnel-Architektur, Master-Checkliste, QA sowie einen Leitfaden für Implementierung und Optimierung.'),
    ('Starte einfach. Wenn du bauen und starten willst, upgrade auf PRO — ohne alles neu zu machen.', 'Wähle das passende Level. Jede Karte nennt nur Inhalte, die in der kanonischen Quelle 2026 verifiziert sind.'),
    ('<div class="price">0€</div>', '<div class="price">$0</div>'),
    ('<li>Basis-Landing-Page (klare Struktur)</li>\n              <li>Logo + visuelles Cover</li>\n              <li>OG image pentru share & preview</li>', '<li>HTML-Landing-Page-Template</li>\n              <li>Hauptlogo im SVG-Format</li>\n              <li>README mit Basisanleitung</li>'),
    ('<div class="price">9$ <span class="tax">(TVA inclus)</span></div>', '<div class="price">$9</div>'),
    ('<li>Premium-Landing (copy + verbesserte Struktur)</li>\n              <li>Kohärentes Branding, sofort einsatzbereit</li>\n              <li>Schnellstart-Anleitung: von Idee zu Online</li>', '<li>2-seitige Quick-Launch-Checkliste als PDF</li>\n              <li>Notion-Template für Pre-/Post-Launch</li>\n              <li>4 anpassbare E-Mail-Templates</li>'),
    ('<div class="price">27$ <span class="tax">(TVA inclus)</span></div>', '<div class="price">$27</div>'),
    ('<li>Komplette Funnel-Struktur (klar, logisch)</li>\n              <li>Grundlegende Automatisierungen Schritt für Schritt erklärt</li>\n              <li>Vorbereitete Templates zur Ausführung</li>', '<li>4-seitiges Launch-Essentials-PDF + CashFlowLab-Framework</li>\n              <li>Notion-Template für Launch-System und Metriken</li>\n              <li>4 E-Mail-Templates + Launch-Prüfungen</li>'),
    ('<div class="price"><span class="old">97$</span>69,99$ <span class="tax">(TVA inclus)</span></div>', '<div class="price">$69.99</div>'),
    ('<li>Komplettes System: Funnel + Landing + Angebot</li>\n              <li>5-E-Mail-Sequenz (Copy inklusive)</li>\n              <li>Klare Automatisierungen, sofort einsatzbereit</li>\n              <li>Launch-Checkliste + zukünftige Updates</li>', '<li>Funnel-Blueprint: Landing → Checkout → Upsell</li>\n              <li>10 E-Mail-Templates</li>\n              <li>Master-Checkliste: Plan → Build → Test → Launch → Scale</li>\n              <li>QA + Leitfaden für Implementierung, Messung und Optimierung</li>'),
    ('PRO-Zugang – 69,99$', 'PRO-Zugang — $69.99'),
    ('Du erhältst Seite + Funnel-Struktur + Automatisierungen — damit du nicht von Null anfängst.', 'Du erhältst Checklisten, Templates, E-Mails und einen Funnel-Blueprint — damit du die Struktur nicht von Null aufbauen musst.'),
    ('Alles ist für "Copy-Paste + Anpassung" konzipiert. Starte mit Free, upgrade auf PRO, wenn du skalieren willst.', 'Die Materialien sind für schnelle Anpassung organisiert. Starte mit FREE und wechsle erst dann, wenn du mehr Launch-Struktur brauchst.'),
    ('CTAs, OG-Preview, Assets und klare Flows — gemacht, um in Shares und Ads premium auszusehen.', 'Jedes Level hat einen klaren Umfang, und die öffentliche Seite nennt nur Materialien, die wir verifizieren können.'),
]

patch(
    'index.html',
    RO,
    forbidden=['5 emailuri PRO', 'automatizări avansate', 'Logo + cover vizual', 'brand guidelines și cover-uri incluse', 'TVA inclus', '97$'],
    required=['2026 • Verificat', '$0', '$9', '$27', '$69.99', 'Secvență de 10 emailuri template', 'Logo principal în format SVG'],
)
patch(
    'en/index.html',
    EN,
    forbidden=['5 email', 'advanced automations', 'Logo + visual cover', 'brand guidelines and covers included', 'TVA inclus', '97$'],
    required=['2026 • Verified', '$0', '$9', '$27', '$69.99', '10 email templates', 'Main logo in SVG format'],
)
patch(
    'de/index.html',
    DE,
    forbidden=['5 E-Mail', 'erweiterte Automatisierungen', 'Logo + visuelles Cover', 'Brand-Guidelines und Cover inklusive', 'TVA inclus', '97$'],
    required=['2026 • Geprüft', '$0', '$9', '$27', '$69.99', '10 E-Mail-Templates', 'Hauptlogo im SVG-Format'],
)

# Extend permanent validation so stale homepage claims cannot silently return.
validator_path = ROOT / 'scripts/validate_repo.py'
validator = validator_path.read_text(encoding='utf-8')
marker = '# Homepage canonical invariants (2026).'
if marker not in validator:
    insertion = '''\n# Homepage canonical invariants (2026).\nhomepage_rules = {\n    'index.html': {\n        'required': ['2026 • Verificat', '$0', '$9', '$27', '$69.99', '10 emailuri template'],\n        'forbidden': ['5 emailuri PRO', 'automatizări avansate', 'Logo + cover vizual', 'TVA inclus', '97$'],\n    },\n    'en/index.html': {\n        'required': ['2026 • Verified', '$0', '$9', '$27', '$69.99', '10 email templates'],\n        'forbidden': ['5 email sequence', 'advanced automations', 'Logo + visual cover', 'TVA inclus', '97$'],\n    },\n    'de/index.html': {\n        'required': ['2026 • Geprüft', '$0', '$9', '$27', '$69.99', '10 E-Mail-Templates'],\n        'forbidden': ['5-E-Mail-Sequenz', 'erweiterte Automatisierungen', 'Logo + visuelles Cover', 'TVA inclus', '97$'],\n    },\n}\nfor rel, rules in homepage_rules.items():\n    text = read(rel)\n    for needle in rules['required']:\n        if needle not in text:\n            fail(f'{rel}: canonical homepage text missing: {needle}')\n    for needle in rules['forbidden']:\n        if needle in text:\n            fail(f'{rel}: stale homepage claim returned: {needle}')\n\n'''
    anchor = '# Canonical package files that must remain available.\n'
    if anchor not in validator:
        raise SystemExit('Validator anchor not found')
    validator = validator.replace(anchor, insertion + anchor, 1)
    validator_path.write_text(validator, encoding='utf-8')

print('RO/EN/DE homepages aligned to the canonical 2026 product map.')
