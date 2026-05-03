import re

# Read RO file
with open('/root/.openclaw/workspace/index.html', 'r') as f:
    ro_content = f.read()

# Read EN file to extract EN translations
with open('/root/.openclaw/workspace/en/index.html', 'r') as f:
    en_old = f.read()

# Start with RO content and make EN replacements
en_new = ro_content

# Meta and structural replacements
en_new = en_new.replace('lang="ro"', 'lang="en"')
en_new = en_new.replace('data-lang="ro"', 'data-lang="en"')
en_new = en_new.replace('content="ro_RO"', 'content="en_US"')
en_new = en_new.replace('og:locale" content="ro_RO"', 'og:locale" content="en_US"')

# Title and descriptions
en_new = en_new.replace(
    '<title>CashFlowLab — Sistemul AI care construiește cashflow predictibil</title>',
    '<title>CashFlowLab — The AI system that builds predictable cashflow</title>'
)
en_new = en_new.replace(
    'CashFlowLab îți oferă un sistem complet: kituri, funnel și automatizări AI pentru a lansa rapid și a scala un cashflow predictibil, fără improvizații.',
    'CashFlowLab gives you a complete system: kits, funnels and AI automations to launch quickly and scale predictable cashflow, without guesswork.'
)
en_new = en_new.replace(
    'Kiturile, funnelul și automatizările AI care îți generează primul cashflow și îl transformă într-un sistem predictibil.',
    'The kits, funnel and AI automations that generate your first cashflow and turn it into a predictable system.'
)
en_new = en_new.replace(
    '"CashFlowLab — Sistemul AI care construiește cashflow predictibil"',
    '"CashFlowLab — The AI system that builds predictable cashflow"'
)

# Canonical and links
en_new = en_new.replace('href="https://cashflowlabai.com/"', 'href="https://cashflowlabai.com/en/"')
en_new = en_new.replace('href="/" hreflang="ro"', 'href="/" hreflang="ro"')
en_new = en_new.replace('href="/en/" hreflang="en"', 'href="/en/" hreflang="en"')
en_new = en_new.replace('href="/de/" hreflang="de"', 'href="/de/" hreflang="de"')
en_new = en_new.replace('<a class="logo" href="/">', '<a class="logo" href="/en/">')

# Nav
en_new = en_new.replace('data-i18n="nav.buy">PRO Kit — 69,99 $', 'data-i18n="nav.buy">PRO Kit — $69.99')

# Hero section
en_new = en_new.replace('Lansare rapidă • Kituri + Funnel + Automatizări', 'Quick Launch • Kits + Funnel + Automations')
en_new = en_new.replace('Construiește un cashflow real cu un sistem AI, pas cu pas.', 'Build real cashflow with an AI system, step by step.')
en_new = en_new.replace('CashFlowLab îți dă un plan complet: ', 'CashFlowLab gives you a complete plan: ')
en_new = en_new.replace('de la idee → la pagină → la lead → la ofertă', 'from idea → to page → to lead → to offer')
en_new = en_new.replace('Fără improvizații, fără "prompturi la întâmplare".', 'No guesswork, no random prompts.')

# Form
en_new = en_new.replace('Introdu emailul (primești Free Kit-ul imediat)', 'Enter your email (get Free Kit instantly)')
en_new = en_new.replace('Primește Free Kit-ul', 'Get Free Kit')
en_new = en_new.replace('🎉 Ești înscris!', '🎉 You\'re in!')
en_new = en_new.replace('Verifică inbox-ul. Free Kit + prima lecție AI CashFlow sunt pe drum.', 'Check your inbox. The Free Kit + the first AI CashFlow lesson are on their way.')
en_new = en_new.replace('Redirecționare către pagina de descărcare...', 'Redirecting to download page...')

# Trust badges
en_new = en_new.replace('✔ Fără card', '✔ No card required')
en_new = en_new.replace('✔ Fără spam', '✔ No spam')
en_new = en_new.replace('✔ Max. 1 email/zi', '✔ 1 email/day max')
en_new = en_new.replace('⚡ Acces instant', '⚡ Instant access')
en_new = en_new.replace('Înscriere confirmată', 'Signup confirmed')
en_new = en_new.replace('Prima email vine în 1–2 minute.', 'First email arrives in 1–2 minutes.')
en_new = en_new.replace('Dacă nu o vezi, verifică <i>Promoții</i>.', 'If you don\'t see it, check <i>Promotions</i>.')
en_new = en_new.replace('Folosim emailul doar ca să-ți trimitem kitul și secvența CashFlowLab. Te poți dezabona oricând.', 'We only use your email to send you the kit and CashFlowLab sequence. You can unsubscribe anytime.')

# Features
en_new = en_new.replace('De ce CashFlowLab', 'Why CashFlowLab')
en_new = en_new.replace('Nu-ți vând „promisiuni".', 'We don\'t sell "promises".')
en_new = en_new.replace('Îți dau un sistem clar: design + funnel + automate — ca să lansezi în ore, nu în săptămâni.', 'We give you a clear system: design + funnel + automations — so you launch in hours, not weeks.')
en_new = en_new.replace('Landing premium', 'Premium Landing')
en_new = en_new.replace('Hero strategic, secțiuni clare, SEO/OG, responsive și optimizat performanță.', 'Strategic hero, clear sections, SEO/OG, responsive and performance optimized.')
en_new = en_new.replace('Funnel + automatizări', 'Funnel + Automations')
en_new = en_new.replace('Workflowuri preconfigurate + 5 emailuri PRO — plug \u0026 play.', 'Preconfigured workflows + 5 PRO emails — plug \u0026 play.')
en_new = en_new.replace('Stil vizual', 'Visual Style')
en_new = en_new.replace('Aur + Purpuriu + Tech Orb, cover \u0026 og-image incluse — arată premium din ziua 1.', 'Gold + Purple + Tech Orb, cover \u0026 og-image included — looks premium from day one.')

# Showcase
en_new = en_new.replace('Ce conțin kiturile', 'What the kits include')
en_new = en_new.replace('Resurse profesionale pregătite pentru a construi rapid și scala.', 'Professionally prepared resources to build fast and scale.')
en_new = en_new.replace('Landing clar', 'Clear Landing')
en_new = en_new.replace('Structură landing clară, conectată direct cu Gumroad, fără fricțiune.', 'Clear landing structure, directly connected with Gumroad, no friction.')
en_new = en_new.replace('Funnel \u0026 Automatizări', 'Funnel \u0026 Automations')
en_new = en_new.replace('Sistem complet: captare → nurturing → ofertă — gata de rulare.', 'Complete system: capture → nurturing → offer — ready to run.')
en_new = en_new.replace('Stil Visual', 'Visual Style')
en_new = en_new.replace('Tech Orb, Aur+Purpuriu, Brand Guidelines și Covers incluse.', 'Tech Orb, Gold+Purple, Brand Guidelines and Covers included.')

# Kits
en_new = en_new.replace('Alege nivelul potrivit pentru tine', 'Choose the right level for you')
en_new = en_new.replace('Începe simplu. Când vrei să construiești și să lansezi, treci pe PRO — fără să refaci totul.', 'Start simple. When you want to build and launch, upgrade to PRO — without rebuilding everything.')
en_new = en_new.replace('Gratis', 'Free')
en_new = en_new.replace('0 RON', '0€')
en_new = en_new.replace('Structură Landing Page (clară)', 'Landing Page Structure (clear)')
en_new = en_new.replace('Logo + cover vizual', 'Logo + visual cover')
en_new = en_new.replace('OG-Image pentru Share \u0026 Preview', 'OG-Image for Share \u0026 Preview')
en_new = en_new.replace('👆 Introdu email-ul mai sus', '👆 Enter your email above')
en_new = en_new.replace('9 $ (TVA inclus)', '$9 (VAT incl.)')
en_new = en_new.replace('Landing premium (copy + structură îmbunătățită)', 'Premium landing (copy + improved structure)')
en_new = en_new.replace('Branding coerent, gata de folosit', 'Coherent branding, ready to use')
en_new = en_new.replace('Ghid rapid: de la idee la online', 'Quick guide: from idea to online')
en_new = en_new.replace('Ia Kitul MINI — 9 $ →', 'Get MINI Kit — $9 →')
en_new = en_new.replace('21 $ (TVA inclus)', '$21 (VAT incl.)')
en_new = en_new.replace('Structură completă de funnel (clar, logic)', 'Complete funnel structure (clear, logical)')
en_new = en_new.replace('Automatizări de bază explicate pas cu pas', 'Basic automations explained step by step')
en_new = en_new.replace('Template-uri pregătite pentru execuție', 'Templates ready for execution')
en_new = en_new.replace('Ia Kitul MEDIUM — 21 $ →', 'Get MEDIUM Kit — $21 →')
en_new = en_new.replace('69,99 $ (TVA inclus)', '$69.99 (VAT incl.)')
en_new = en_new.replace('Sistem complet: funnel + landing + ofertă', 'Complete system: funnel + landing + offer')
en_new = en_new.replace('Secvență de 5 emailuri (copy inclus)', '5 email sequence (copy included)')
en_new = en_new.replace('Automatizări clare, gata de folosit', 'Clear automations, ready to use')
en_new = en_new.replace('Checklist de lansare + actualizări viitoare', 'Launch checklist + future updates')
en_new = en_new.replace('Acces PRO – 69,99$', 'PRO Access — $69.99')
en_new = en_new.replace('Află mai multe →', 'Learn more →')

# Proof section
en_new = en_new.replace('De ce funcționează', 'Why it works')
en_new = en_new.replace('Nu promitem „bani peste noapte".', 'We don\'t promise "overnight riches".')
en_new = en_new.replace('Îți dăm un sistem executabil — ca să obții rezultate prin pași clari.', 'We give you an executable system — so you get results through clear steps.')
en_new = en_new.replace('Sistem complet, nu „prompturi"', 'Complete system, not "prompts"')
en_new = en_new.replace('Primești pagină + structură funnel + automate — ca să nu reconstruiești de la zero.', 'You get page + funnel structure + automations — so you don\'t rebuild from zero.')
en_new = en_new.replace('Rapid de implementat', 'Quick to implement')
en_new = en_new.replace('Totul e gândit pentru "copy-paste + adaptare".', 'Everything is designed for "copy-paste + adaptation".')
en_new = en_new.replace('Începi cu Free, treci pe PRO când vrei să scalezi.', 'Start with Free, upgrade to PRO when you want to scale.')
en_new = en_new.replace('Fără fricțiune la vânzare', 'No friction in sales')
en_new = en_new.replace('CTA-uri, OG preview, assets și flow-uri clare — făcute să arate premium în share și ads.', 'CTAs, OG preview, assets and clear flows — made to look premium in shares and ads.')
en_new = en_new.replace('Este pentru mine dacă…', 'It\'s for me if…')
en_new = en_new.replace('vrei să lansezi rapid un produs digital / serviciu și ai nevoie de structură + execuție fără improvizații.', 'you want to quickly launch a digital product / service and need structure + execution without guesswork.')
en_new = en_new.replace('Nu este pentru mine dacă…', 'It\'s NOT for me if…')
en_new = en_new.replace('cauți "schemă de îmbogățire rapidă" sau vrei rezultate fără să aplici.', 'you\'re looking for a "get rich quick scheme" or want results without applying.')

# Footer
en_new = en_new.replace('Resurse', 'Resources')
en_new = en_new.replace('Termeni și Condiții', 'Terms \u0026 Conditions')
en_new = en_new.replace('Politica de Confidențialitate', 'Privacy Policy')
en_new = en_new.replace('© 2025 CashFlowLab. Toate drepturile rezervate.', '© 2025 CashFlowLab. All rights reserved.')
en_new = en_new.replace('Un sistem mic. O execuție curată. Un cashflow predictibil.', 'A small system. Clean execution. Predictable cashflow.')

# Cookie banner
en_new = en_new.replace('Folosim cookie-uri pentru analiză și marketing. Poți alege ce accepți.', 'We use cookies for analytics and marketing. You can choose what to accept.')
en_new = en_new.replace('Refuză', 'Decline')
en_new = en_new.replace('Acceptă analiza', 'Accept analytics')
en_new = en_new.replace('Acceptă tot', 'Accept all')
en_new = en_new.replace('Schimbă consimțământ', 'Change consent')
en_new = en_new.replace('Consimțământ cookie', 'Cookie consent')

# Language switcher labels
en_new = en_new.replace('Vezi alte kituri', 'See other kits')

# Misc
en_new = en_new.replace('"ro"', '"en"')
en_new = en_new.replace('ro_RO', 'en_US')

# Write the result
with open('/root/.openclaw/workspace/en/index.html', 'w') as f:
    f.write(en_new)

print(f"Done! Wrote {len(en_new)} characters to en/index.html")