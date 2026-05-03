import re

# Read RO file
with open('/root/.openclaw/workspace/index.html', 'r') as f:
    ro_content = f.read()

# Start with RO content and make DE replacements
de_new = ro_content

# Meta and structural replacements
de_new = de_new.replace('lang="ro"', 'lang="de"')
de_new = de_new.replace('data-lang="ro"', 'data-lang="de"')
de_new = de_new.replace('content="ro_RO"', 'content="de_DE"')
de_new = de_new.replace('og:locale" content="ro_RO"', 'og:locale" content="de_DE"')

# Title and descriptions - using German from old DE file
de_new = de_new.replace(
    '<title>CashFlowLab — Sistemul AI care construiește cashflow predictibil</title>',
    '<title>CashFlowLab — Das AI-System, das vorhersagbaren Cashflow aufbaut</title>'
)
de_new = de_new.replace(
    'CashFlowLab îți oferă un sistem complet: kituri, funnel și automatizări AI pentru a lansa rapid și a scala un cashflow predictibil, fără improvizații.',
    'CashFlowLab bietet ein komplettes System: Kits, Funnels und KI-Automatisierungen zum schnellen Start und Skalieren eines vorhersagbaren Cashflows, ohne Rätselraten.'
)
de_new = de_new.replace(
    'Kiturile, funnelul și automatizările AI care îți generează primul cashflow și îl transformă într-un sistem predictibil.',
    'Die Kits, Funnel und KI-Automatisierungen, die deinen ersten Cashflow generieren und ihn in ein vorhersagbares System verwandeln.'
)
de_new = de_new.replace(
    '"CashFlowLab — Sistemul AI care construiește cashflow predictibil"',
    '"CashFlowLab — Das AI-System, das vorhersagbaren Cashflow aufbaut"'
)

# Canonical and links
de_new = de_new.replace('href="https://cashflowlabai.com/"', 'href="https://cashflowlabai.com/de/"')
de_new = de_new.replace('<a class="logo" href="/">', '<a class="logo" href="/de/">')

# Nav
de_new = de_new.replace('data-i18n="nav.buy">PRO Kit — 69,99 $', 'data-i18n="nav.buy">PRO Kit — 69,99 €')

# Hero section
de_new = de_new.replace('Lansare rapidă • Kituri + Funnel + Automatizări', 'Schneller Start • Kits + Funnel + Automatisierungen')
de_new = de_new.replace('Construiește un cashflow real cu un sistem AI, pas cu pas.', 'Baue echten Cashflow mit einem KI-System, Schritt für Schritt.')
de_new = de_new.replace('CashFlowLab îți dă un plan complet: ', 'CashFlowLab gibt dir einen kompletten Plan: ')
de_new = de_new.replace('de la idee → la pagină → la lead → la ofertă', 'von Idee → zu Seite → zu Lead → zu Angebot')
de_new = de_new.replace('Fără improvizații, fără "prompturi la întâmplare".', 'Kein Rätselraten, keine zufälligen Prompts.')

# Form
de_new = de_new.replace('Introdu emailul (primești Free Kit-ul imediat)', 'Email eingeben (Free Kit sofort erhalten)')
de_new = de_new.replace('Primește Free Kit-ul', 'Free Kit erhalten')
de_new = de_new.replace('🎉 Ești înscris!', '🎉 Du bist dabei!')
de_new = de_new.replace('Verifică inbox-ul. Free Kit + prima lecție AI CashFlow sunt pe drum.', 'Überprüfe deinen Posteingang. Das Free Kit + die erste KI-CashFlow-Lektion sind unterwegs.')
de_new = de_new.replace('Redirecționare către pagina de descărcare...', 'Weiterleitung zur Download-Seite...')

# Trust badges
de_new = de_new.replace('✔ Fără card', '✔ Keine Karte nötig')
de_new = de_new.replace('✔ Fără spam', '✔ Kein Spam')
de_new = de_new.replace('✔ Max. 1 email/zi', '✔ Max. 1 E-Mail/Tag')
de_new = de_new.replace('⚡ Acces instant', '⚡ Sofortiger Zugang')
de_new = de_new.replace('Înscriere confirmată', 'Anmeldung bestätigt')
de_new = de_new.replace('Prima email vine în 1–2 minute.', 'Die erste E-Mail kommt in 1–2 Minuten.')
de_new = de_new.replace('Dacă nu o vezi, verifică <i>Promoții</i>.', 'Wenn du sie nicht siehst, überprüfe <i>Werbung</i>.')
de_new = de_new.replace('Folosim emailul doar ca să-ți trimitem kitul și secvența CashFlowLab. Te poți dezabona oricând.', 'Wir nutzen deine E-Mail nur, um dir das Kit und die CashFlowLab-Sequenz zu senden. Du kannst dich jederzeit abmelden.')

# Features
de_new = de_new.replace('De ce CashFlowLab', 'Warum CashFlowLab')
de_new = de_new.replace('Nu-ți vând „promisiuni".', 'Wir verkaufen keine „Versprechen".')
de_new = de_new.replace('Îți dau un sistem clar: design + funnel + automate — ca să lansezi în ore, nu în săptămâni.', 'Wir geben dir ein klares System: Design + Funnel + Automatisierungen — damit du in Stunden, nicht in Wochen, startest.')
de_new = de_new.replace('Landing premium', 'Premium-Landing')
de_new = de_new.replace('Hero strategic, secțiuni clare, SEO/OG, responsive și optimizat performanță.', 'Strategischer Hero, klare Abschnitte, SEO/OG, responsiv und leistungsoptimiert.')
de_new = de_new.replace('Funnel + automatizări', 'Funnel + Automatisierungen')
de_new = de_new.replace('Workflowuri preconfigurate + 5 emailuri PRO — plug \u0026 play.', 'Vorkonfigurierte Workflows + 5 PRO-E-Mails — Plug \u0026 Play.')
de_new = de_new.replace('Stil vizual', 'Visueller Stil')
de_new = de_new.replace('Aur + Purpuriu + Tech Orb, cover \u0026 og-image incluse — arată premium din ziua 1.', 'Gold + Lila + Tech Orb, Cover \u0026 OG-Image inklusive — sieht ab Tag 1 premium aus.')

# Showcase
de_new = de_new.replace('Ce conțin kiturile', 'Was die Kits enthalten')
de_new = de_new.replace('Resurse profesionale pregătite pentru a construi rapid și scala.', 'Professionell vorbereitete Ressourcen zum schnellen Aufbau und Skalieren.')
de_new = de_new.replace('Landing clar', 'Klare Landing-Page')
de_new = de_new.replace('Structură landing clară, conectată direct cu Gumroad, fără fricțiune.', 'Klare Landing-Page-Struktur, direkt mit Gumroad verbunden, ohne Reibung.')
de_new = de_new.replace('Funnel \u0026 Automatizări', 'Funnel \u0026 Automatisierungen')
de_new = de_new.replace('Sistem complet: captare → nurturing → ofertă — gata de rulare.', 'Komplettes System: Erfassung → Pflege → Angebot — bereit zum Start.')
de_new = de_new.replace('Stil Visual', 'Visueller Stil')
de_new = de_new.replace('Tech Orb, Aur+Purpuriu, Brand Guidelines și Covers incluse.', 'Tech Orb, Gold+Lila, Brand Guidelines und Covers inklusive.')

# Kits
de_new = de_new.replace('Alege nivelul potrivit pentru tine', 'Wähle das richtige Level für dich')
de_new = de_new.replace('Începe simplu. Când vrei să construiești și să lansezi, treci pe PRO — fără să refaci totul.', 'Starte einfach. Wenn du bauen und starten willst, upgrade auf PRO — ohne alles neu zu machen.')
de_new = de_new.replace('Gratis', 'Kostenlos')
de_new = de_new.replace('0 RON', '0€')
de_new = de_new.replace('Structură Landing Page (clară)', 'Landing-Page-Struktur (klar)')
de_new = de_new.replace('Logo + cover vizual', 'Logo + visuelles Cover')
de_new = de_new.replace('OG-Image pentru Share \u0026 Preview', 'OG-Image für Share \u0026 Preview')
de_new = de_new.replace('👆 Introdu email-ul mai sus', '👆 Email oben eingeben')
de_new = de_new.replace('9 $ (TVA inclus)', '9 € (inkl. MwSt.)')
de_new = de_new.replace('Landing premium (copy + structură îmbunătățită)', 'Premium-Landing (Copy + verbesserte Struktur)')
de_new = de_new.replace('Branding coerent, gata de folosit', 'Kohärentes Branding, sofort einsatzbereit')
de_new = de_new.replace('Ghid rapid: de la idee la online', 'Schnellstart-Anleitung: von Idee zu Online')
de_new = de_new.replace('Ia Kitul MINI — 9 $ →', 'MINI Kit holen — 9 € →')
de_new = de_new.replace('21 $ (TVA inclus)', '21 € (inkl. MwSt.)')
de_new = de_new.replace('Structură completă de funnel (clar, logic)', 'Komplette Funnel-Struktur (klar, logisch)')
de_new = de_new.replace('Automatizări de bază explicate pas cu pas', 'Grundlegende Automatisierungen Schritt für Schritt erklärt')
de_new = de_new.replace('Template-uri pregătite pentru execuție', 'Vorbereitete Templates zur Ausführung')
de_new = de_new.replace('Ia Kitul MEDIUM — 21 $ →', 'MEDIUM Kit holen — 21 € →')
de_new = de_new.replace('69,99 $ (TVA inclus)', '69,99 € (inkl. MwSt.)')
de_new = de_new.replace('Sistem complet: funnel + landing + ofertă', 'Komplettes System: Funnel + Landing + Angebot')
de_new = de_new.replace('Secvență de 5 emailuri (copy inclus)', '5-E-Mail-Sequenz (Copy inklusive)')
de_new = de_new.replace('Automatizări clare, gata de folosit', 'Klare Automatisierungen, sofort einsatzbereit')
de_new = de_new.replace('Checklist de lansare + actualizări viitoare', 'Launch-Checkliste + zukünftige Updates')
de_new = de_new.replace('Acces PRO – 69,99$', 'PRO-Zugang – 69,99€')
de_new = de_new.replace('Află mai multe →', 'Mehr erfahren →')

# Proof section
de_new = de_new.replace('De ce funcționează', 'Warum es funktioniert')
de_new = de_new.replace('Nu promitem „bani peste noapte".', 'Wir versprechen keine „schnellen Reichtümer".')
de_new = de_new.replace('Îți dăm un sistem executabil — ca să obții rezultate prin pași clari.', 'Wir geben dir ein ausführbares System — damit du durch klare Schritte Ergebnisse erzielst.')
de_new = de_new.replace('Sistem complet, nu „prompturi"', 'Komplettes System, keine „Prompts"')
de_new = de_new.replace('Primești pagină + structură funnel + automate — ca să nu reconstruiești de la zero.', 'Du erhältst Seite + Funnel-Struktur + Automatisierungen — damit du nicht von Null anfängst.')
de_new = de_new.replace('Rapid de implementat', 'Schnell implementierbar')
de_new = de_new.replace('Totul e gândit pentru "copy-paste + adaptare".', 'Alles ist für "Copy-Paste + Anpassung" konzipiert.')
de_new = de_new.replace('Începi cu Free, treci pe PRO când vrei să scalezi.', 'Starte mit Free, upgrade auf PRO, wenn du skalieren willst.')
de_new = de_new.replace('Fără fricțiune la vânzare', 'Keine Reibung beim Verkauf')
de_new = de_new.replace('CTA-uri, OG preview, assets și flow-uri clare — făcute să arate premium în share și ads.', 'CTAs, OG-Preview, Assets und klare Flows — gemacht, um in Shares und Ads premium auszusehen.')
de_new = de_new.replace('Este pentru mine dacă…', 'Es ist für mich, wenn…')
de_new = de_new.replace('vrei să lansezi rapid un produs digital / serviciu și ai nevoie de structură + execuție fără improvizații.', 'du schnell ein digitales Produkt / Service starten willst und Struktur + Ausführung ohne Rätselraten brauchst.')
de_new = de_new.replace('Nu este pentru mine dacă…', 'Es ist NICHT für mich, wenn…')
de_new = de_new.replace('cauți "schemă de îmbogățire rapidă" sau vrei rezultate fără să aplici.', 'du nach einem „schnellen Reichtum-Schema" suchst oder Ergebnisse willst, ohne etwas zu tun.')

# Footer
de_new = de_new.replace('Resurse', 'Ressourcen')
de_new = de_new.replace('Contact', 'Kontakt')
de_new = de_new.replace('Legal', 'Rechtliches')
de_new = de_new.replace('Termeni și Condiții', 'Nutzungsbedingungen')
de_new = de_new.replace('Politica de Confidențialitate', 'Datenschutzerklärung')
de_new = de_new.replace('© 2025 CashFlowLab. Toate drepturile rezervate.', '© 2025 CashFlowLab. Alle Rechte vorbehalten.')
de_new = de_new.replace('Un sistem mic. O execuție curată. Un cashflow predictibil.', 'Ein kleines System. Saubere Ausführung. Vorhersagbarer Cashflow.')

# Cookie banner
de_new = de_new.replace('Folosim cookie-uri pentru analiză și marketing. Poți alege ce accepți.', 'Wir nutzen Cookies für Analyse und Marketing. Du kannst wählen, was du akzeptierst.')
de_new = de_new.replace('Refuză', 'Ablehnen')
de_new = de_new.replace('Acceptă analiza', 'Analyse akzeptieren')
de_new = de_new.replace('Acceptă tot', 'Alles akzeptieren')
de_new = de_new.replace('Schimbă consimțământ', 'Zustimmung ändern')
de_new = de_new.replace('Consimțământ cookie', 'Cookie-Einwilligung')

# Language switcher labels
de_new = de_new.replace('Vezi alte kituri', 'Andere Kits ansehen')

# Misc
de_new = de_new.replace('"ro"', '"de"')
de_new = de_new.replace('ro_RO', 'de_DE')

# Write the result
with open('/root/.openclaw/workspace/de/index.html', 'w') as f:
    f.write(de_new)

print(f"Done! Wrote {len(de_new)} characters to de/index.html")