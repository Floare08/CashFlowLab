from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

LANG = {
'index.html': {
  'title':'CashFlowLab — Kituri și sisteme de lansare pentru produse digitale',
  'desc':'CashFlowLab oferă kituri de lansare verificate: checklist-uri, template-uri Notion, emailuri și un blueprint de funnel pentru produse digitale.',
  'ogdesc':'Checklist-uri, template-uri, emailuri și blueprint-uri de funnel bazate pe livrabilele verificate CashFlowLab.',
  'badge':'2026 • Verificat',
  'eyebrow':'Lansare clară • Checklist-uri + Template-uri + Funnel Blueprint',
  'h1':'Lansează mai clar, cu resurse pe care le poți aplica pas cu pas.',
  'sub':'CashFlowLab organizează lansarea în pași practici: <b>checklist → mesaj → pagină → emailuri → ofertă</b>. Fiecare ofertă de mai jos descrie doar livrabile verificate.',
  'avail':'FREE, MINI și MEDIUM au livrabile verificate. PRO este prezentat numai prin blueprint-ul și materialele confirmate în repository.',
  'features_title':'De ce CashFlowLab',
  'features_sub':'Fără promisiuni umflate: primești livrabile concrete pe care le poți adapta și implementa.',
  'f1t':'Checklist-uri de lansare','f1d':'MINI și MEDIUM includ checklist-uri PDF și pași clari pentru pre-launch și post-launch.',
  'f2t':'Emailuri + funnel blueprint','f2d':'MINI și MEDIUM includ câte 4 emailuri, iar PRO include 10 emailuri template și arhitectura funnelului.',
  'f3t':'Implementare pas cu pas','f3d':'Template-urile Notion și master checklist-ul PRO te ajută să implementezi și să verifici lansarea.',
  'show_title':'Ce primești în kituri','show_sub':'Resurse verificate în repository, organizate pe niveluri de la FREE la PRO.',
  's1t':'Checklist-uri & Template-uri','s1d':'FREE oferă un template HTML, iar MINI și MEDIUM adaugă checklist-uri și template-uri Notion.',
  's2t':'Emailuri gata de adaptat','s2d':'MINI și MEDIUM includ câte 4 emailuri, iar PRO include o secvență de 10 emailuri template.',
  's3t':'Blueprint funnel & QA','s3d':'PRO include arhitectura funnelului, master checklist, QA și ghid de implementare, măsurare și optimizare.',
  'kits_title':'Alege nivelul potrivit pentru tine','kits_sub':'Fiecare card listează numai livrabilele verificate în sursa canonică 2026.',
  'free_name':'Free Kit','free_cta':'👆 Introdu emailul mai sus',
  'mini_name':'Mini Kit','mini_cta':'Ia MINI Kit — $9 →','learn':'Află mai multe →',
  'medium_name':'Medium Kit','medium_cta':'Ia MEDIUM Kit — $27 →',
  'pro_reco':'PRO • Recomandat','pro_cta':'Acces PRO — $69.99',
  'proof_title':'De ce e mai ușor de folosit','proof_sub':'Structură clară, scope verificat și materiale pe care le poți adapta fără să reconstruiești totul.',
  'p1t':'✔ Scope clar','p1d':'Fiecare nivel spune exact ce primești, fără automatizări sau bonusuri nedocumentate.',
  'p2t':'✔ Rapid de adaptat','p2d':'Checklist-urile, template-urile și emailurile sunt organizate pentru implementare practică.',
  'p3t':'✔ Ușor de verificat','p3d':'Prețurile și livrabilele sunt aliniate la registrul canonic 2026 din repository.',
},
'en/index.html': {
  'title':'CashFlowLab — Launch Kits & Systems for Digital Products',
  'desc':'CashFlowLab offers verified launch kits with checklists, Notion templates, email sequences and a funnel blueprint for digital products.',
  'ogdesc':'Verified checklists, templates, email sequences and funnel blueprints for clearer digital-product launches.',
  'badge':'2026 • Verified',
  'eyebrow':'Clear Launch • Checklists + Templates + Funnel Blueprint',
  'h1':'Launch more clearly with practical resources you can apply step by step.',
  'sub':'CashFlowLab organizes the launch into practical steps: <b>checklist → message → page → emails → offer</b>. Every offer below lists only verified deliverables.',
  'avail':'FREE, MINI and MEDIUM have verified deliverables. PRO is presented only through the blueprint and materials confirmed in the repository.',
  'features_title':'Why CashFlowLab','features_sub':'No inflated promises: you get concrete deliverables you can adapt and implement.',
  'f1t':'Launch Checklists','f1d':'MINI and MEDIUM include PDF checklists and clear pre-launch and post-launch steps.',
  'f2t':'Emails + Funnel Blueprint','f2d':'MINI and MEDIUM each include 4 emails, while PRO includes 10 email templates and the funnel architecture.',
  'f3t':'Step-by-Step Implementation','f3d':'Notion templates and the PRO master checklist help you implement and verify the launch.',
  'show_title':'What you get in the kits','show_sub':'Repository-verified resources organized from FREE through PRO.',
  's1t':'Checklists & Templates','s1d':'FREE includes an HTML landing template; MINI and MEDIUM add checklists and Notion templates.',
  's2t':'Emails Ready to Adapt','s2d':'MINI and MEDIUM each include 4 emails, while PRO includes a 10-email template sequence.',
  's3t':'Funnel Blueprint & QA','s3d':'PRO includes funnel architecture, a master checklist, QA and an implementation, measurement and optimization guide.',
  'kits_title':'Choose the right level for you','kits_sub':'Every card lists only deliverables verified in the 2026 canonical source.',
  'free_name':'Free Kit','free_cta':'👆 Enter your email above',
  'mini_name':'Mini Kit','mini_cta':'Get MINI Kit — $9 →','learn':'Learn more →',
  'medium_name':'Medium Kit','medium_cta':'Get MEDIUM Kit — $27 →',
  'pro_reco':'PRO • Recommended','pro_cta':'PRO Access — $69.99',
  'proof_title':'Why it is easier to use','proof_sub':'Clear scope, verified materials and resources you can adapt without rebuilding everything.',
  'p1t':'✔ Clear scope','p1d':'Each level states exactly what you get, without undocumented automations or bonuses.',
  'p2t':'✔ Quick to adapt','p2d':'Checklists, templates and emails are organized for practical implementation.',
  'p3t':'✔ Easy to verify','p3d':'Prices and deliverables are aligned with the canonical 2026 repository registry.',
},
'de/index.html': {
  'title':'CashFlowLab — Launch-Kits & Systeme für digitale Produkte',
  'desc':'CashFlowLab bietet verifizierte Launch-Kits mit Checklisten, Notion-Templates, E-Mail-Sequenzen und einem Funnel-Blueprint für digitale Produkte.',
  'ogdesc':'Verifizierte Checklisten, Templates, E-Mail-Sequenzen und Funnel-Blueprints für klarere Launches digitaler Produkte.',
  'badge':'2026 • Geprüft',
  'eyebrow':'Klarer Launch • Checklisten + Templates + Funnel-Blueprint',
  'h1':'Starte klarer mit praktischen Ressourcen, die du Schritt für Schritt anwenden kannst.',
  'sub':'CashFlowLab ordnet den Launch in praktische Schritte: <b>Checkliste → Botschaft → Seite → E-Mails → Angebot</b>. Jedes Angebot unten nennt nur verifizierte Inhalte.',
  'avail':'FREE, MINI und MEDIUM haben verifizierte Inhalte. PRO wird nur mit dem Blueprint und den im Repository bestätigten Materialien dargestellt.',
  'features_title':'Warum CashFlowLab','features_sub':'Keine übertriebenen Versprechen: Du erhältst konkrete Inhalte zum Anpassen und Umsetzen.',
  'f1t':'Launch-Checklisten','f1d':'MINI und MEDIUM enthalten PDF-Checklisten und klare Schritte für Pre-Launch und Post-Launch.',
  'f2t':'E-Mails + Funnel-Blueprint','f2d':'MINI und MEDIUM enthalten jeweils 4 E-Mails; PRO enthält 10 E-Mail-Templates und die Funnel-Architektur.',
  'f3t':'Schrittweise Umsetzung','f3d':'Notion-Templates und die PRO-Master-Checkliste helfen bei Umsetzung und Launch-Prüfung.',
  'show_title':'Was du in den Kits erhältst','show_sub':'Im Repository verifizierte Ressourcen, organisiert von FREE bis PRO.',
  's1t':'Checklisten & Templates','s1d':'FREE enthält ein HTML-Landing-Template; MINI und MEDIUM ergänzen Checklisten und Notion-Templates.',
  's2t':'E-Mails zum Anpassen','s2d':'MINI und MEDIUM enthalten jeweils 4 E-Mails; PRO enthält eine Sequenz aus 10 E-Mail-Templates.',
  's3t':'Funnel-Blueprint & QA','s3d':'PRO enthält Funnel-Architektur, Master-Checkliste, QA sowie einen Leitfaden für Implementierung, Messung und Optimierung.',
  'kits_title':'Wähle das passende Level','kits_sub':'Jede Karte nennt nur Inhalte, die in der kanonischen Quelle 2026 verifiziert sind.',
  'free_name':'Free Kit','free_cta':'👆 E-Mail oben eingeben',
  'mini_name':'Mini Kit','mini_cta':'MINI Kit — $9 →','learn':'Mehr erfahren →',
  'medium_name':'Medium Kit','medium_cta':'MEDIUM Kit — $27 →',
  'pro_reco':'PRO • Empfohlen','pro_cta':'PRO-Zugang — $69.99',
  'proof_title':'Warum es leichter nutzbar ist','proof_sub':'Klarer Umfang, verifizierte Materialien und Ressourcen, die du ohne kompletten Neuaufbau anpassen kannst.',
  'p1t':'✔ Klarer Umfang','p1d':'Jedes Level sagt genau, was enthalten ist – ohne undokumentierte Automatisierungen oder Boni.',
  'p2t':'✔ Schnell anpassbar','p2d':'Checklisten, Templates und E-Mails sind für praktische Umsetzung organisiert.',
  'p3t':'✔ Leicht prüfbar','p3d':'Preise und Inhalte sind mit dem kanonischen Repository-Register 2026 abgeglichen.',
}}


def one(text, pattern, repl, label, flags=0):
    out, n = re.subn(pattern, repl, text, count=1, flags=flags)
    if n != 1:
        raise SystemExit(f'{label}: expected 1 match, got {n}')
    return out


def section_html(c):
    features=f'''<!-- Features -->
    <section id="features">
      <div class="container">
        <h2 class="section-title cfl-reveal cfl-d1" data-i18n="features.title">{c['features_title']}</h2>
        <p class="section-sub cfl-reveal cfl-d2" data-i18n="features.sub">{c['features_sub']}</p>
        <div class="features">
          <div class="feature cfl-card cfl-reveal cfl-d2"><img class="cfl-media" src="/Images/funnel-diagram.webp" alt="Launch checklist and funnel structure" loading="lazy" decoding="async" width="1200" height="750" /><h3>{c['f1t']}</h3><p>{c['f1d']}</p></div>
          <div class="feature cfl-card cfl-reveal cfl-d3"><img class="cfl-media" src="/Images/og-hero-cover.webp" alt="CashFlowLab launch resource preview" loading="lazy" decoding="async" width="1200" height="630" /><h3>{c['f2t']}</h3><p>{c['f2d']}</p></div>
          <div class="feature cfl-card cfl-reveal cfl-d4"><img class="cfl-media" src="/Images/tech-orb-alt.webp" alt="CashFlowLab implementation resource" loading="lazy" decoding="async" width="1200" height="750" /><h3>{c['f3t']}</h3><p>{c['f3d']}</p></div>
        </div>
      </div>
    </section>

    <!-- Showcase -->
    <section id="showcase" class="showcase preview-rapid">
      <div class="container">
        <h2 class="section-title cfl-reveal cfl-d1">{c['show_title']}</h2>
        <p class="section-sub cfl-reveal cfl-d2">{c['show_sub']}</p>
        <div class="gallery" style="grid-template-columns:repeat(3,1fr);gap:24px">
          <article class="shot cfl-card cfl-reveal cfl-d2" style="text-align:center;padding:32px 24px"><div style="width:64px;height:64px;margin:0 auto 20px;border-radius:16px;background:linear-gradient(135deg,var(--accent-gold),var(--accent-purple));display:flex;align-items:center;justify-content:center;font-size:32px">🚀</div><h4>{c['s1t']}</h4><p style="color:var(--muted);font-size:14px;line-height:1.6">{c['s1d']}</p></article>
          <article class="shot cfl-card cfl-reveal cfl-d3" style="text-align:center;padding:32px 24px"><div style="width:64px;height:64px;margin:0 auto 20px;border-radius:16px;background:linear-gradient(135deg,var(--accent-gold),var(--accent-purple));display:flex;align-items:center;justify-content:center;font-size:32px">✉️</div><h4>{c['s2t']}</h4><p style="color:var(--muted);font-size:14px;line-height:1.6">{c['s2d']}</p></article>
          <article class="shot cfl-card cfl-reveal cfl-d4" style="text-align:center;padding:32px 24px"><div style="width:64px;height:64px;margin:0 auto 20px;border-radius:16px;background:linear-gradient(135deg,var(--accent-gold),var(--accent-purple));display:flex;align-items:center;justify-content:center;font-size:32px">🧭</div><h4>{c['s3t']}</h4><p style="color:var(--muted);font-size:14px;line-height:1.6">{c['s3d']}</p></article>
        </div>
      </div>
    </section>

    <!-- Kits -->
    <section id="kits">
      <div class="container">
        <h2 class="section-title cfl-reveal cfl-d1">{c['kits_title']}</h2>
        <p class="section-sub cfl-reveal cfl-d2">{c['kits_sub']}</p>
        <div class="kits">
          <div class="kit cfl-card kit-free" id="free-kit"><span class="kit-badge">FREE</span><div class="kit-icon">🎁</div><h3>{c['free_name']}</h3><div class="price">$0</div><ul><li>HTML landing page template</li><li>Main logo in SVG format</li><li>README with basic instructions</li></ul><div style="padding:14px 0;background:rgba(255,209,102,.08);border-radius:999px;text-align:center;margin-top:auto"><span style="color:var(--accent-gold);font-size:14px;font-weight:600">{c['free_cta']}</span></div></div>
          <div class="kit cfl-card"><span class="kit-badge">MINI</span><div class="kit-icon">🚀</div><h3>{c['mini_name']}</h3><div class="price">$9</div><ul><li>2-page Quick Launch Checklist PDF</li><li>Notion template for pre/post-launch</li><li>4 adaptable email templates + launch checks</li></ul><a class="kit-cta kit-cta-outline gumroad-link" href="https://cashflowlabai.gumroad.com/l/bpsbou" target="_blank" rel="noopener" data-evt="mini">{c['mini_cta']}</a><a href="/mini-kit/" class="learn-more">{c['learn']}</a></div>
          <div class="kit cfl-card"><span class="kit-badge">MEDIUM</span><div class="kit-icon">⚡</div><h3>{c['medium_name']}</h3><div class="price">$27</div><ul><li>4-page Launch Essentials PDF + CashFlowLab framework</li><li>Notion launch-system and metrics template</li><li>4 email templates + launch checks</li></ul><a class="kit-cta kit-cta-outline gumroad-link" href="https://cashflowlabai.gumroad.com/l/divha" target="_blank" rel="noopener" data-evt="medium">{c['medium_cta']}</a><a href="/medium-kit/" class="learn-more">{c['learn']}</a></div>
          <div class="kit cfl-card kit-pro" id="pro-kit"><span class="kit-badge best-value">Best Value</span><span class="kit-badge pro">{c['pro_reco']}</span><div class="kit-icon">👑</div><h3>PRO Kit</h3><div class="price">$69.99</div><ul><li>Funnel blueprint: landing → checkout → upsell</li><li>10 email templates</li><li>Master checklist: Plan → Build → Test → Launch → Scale</li><li>QA + implementation, measurement and optimization guide</li></ul><a class="kit-cta kit-cta-primary gumroad-link cfl-cta-glow" href="https://cashflowlabai.gumroad.com/l/udxody" target="_blank" rel="noopener" data-evt="pro"><span class="shine"></span>{c['pro_cta']}</a><a href="/pro-kit/" class="learn-more">{c['learn']}</a></div>
        </div>
      </div>
    </section>

    <!-- Proof -->
    <section id="proof">
      <div class="container"><h2 class="section-title cfl-reveal cfl-d1">{c['proof_title']}</h2><p class="section-sub cfl-reveal cfl-d2">{c['proof_sub']}</p><div class="testimonials"><div class="quote cfl-card cfl-reveal cfl-d2"><b>{c['p1t']}</b><p class="muted" style="margin:10px 0 0;">{c['p1d']}</p></div><div class="quote cfl-card cfl-reveal cfl-d3"><b>{c['p2t']}</b><p class="muted" style="margin:10px 0 0;">{c['p2d']}</p></div><div class="quote cfl-card cfl-reveal cfl-d4"><b>{c['p3t']}</b><p class="muted" style="margin:10px 0 0;">{c['p3d']}</p></div></div></div>
    </section>'''
    return features

for rel,c in LANG.items():
    p=ROOT/rel
    text=p.read_text(encoding='utf-8')
    text=one(text,r'<title>.*?</title>',f"<title>{c['title']}</title>",rel+' title')
    text=one(text,r'<meta name="description" content="[^"]*"\s*/?>',f'<meta name="description" content="{c["desc"]}" />',rel+' description')
    text=one(text,r'<meta property="og:title" content="[^"]*"\s*/?>',f'<meta property="og:title" content="{c["title"]}" />',rel+' og title')
    text=one(text,r'<meta property="og:description" content="[^"]*"\s*/?>',f'<meta property="og:description" content="{c["ogdesc"]}" />',rel+' og desc')
    text=one(text,r'<meta name="twitter:title" content="[^"]*"\s*/?>',f'<meta name="twitter:title" content="{c["title"]}" />',rel+' twitter title')
    text=one(text,r'<meta name="twitter:description" content="[^"]*"\s*/?>',f'<meta name="twitter:description" content="{c["ogdesc"]}" />',rel+' twitter desc')
    text=one(text,r'("description":")[^"]*(","brand":)',r'\1Funnel blueprint + 10 email templates + master checklist + implementation and optimization guide.\2',rel+' product ld')
    text=one(text,r'<span class="badge" id="beta">.*?</span>',f'<span class="badge" id="beta">{c["badge"]}</span>',rel+' badge')
    text=one(text,r'(<div class="eyebrow[^>]*>).*?(</div>)',lambda m:m.group(1)+c['eyebrow']+m.group(2),rel+' eyebrow')
    text=one(text,r'(<h1 class="txt-shadow">).*?(</h1>)',lambda m:m.group(1)+c['h1']+m.group(2),rel+' h1')
    text=one(text,r'(<p class="sub">).*?(</p>)',lambda m:m.group(1)+c['sub']+m.group(2),rel+' hero sub')
    text=one(text,r'(<div class="glass hero-card.*?<p class="muted" style="margin:0;">).*?(</p>)',lambda m:m.group(1)+c['avail']+m.group(2),rel+' availability',re.S)
    if rel=='en/index.html':
        text=text.replace('✔ 1 email/zi max','✔ Up to 1 email/day').replace('Preview OG cover pentru share','Launch resource preview').replace('Identitate vizuală CashFlowLab','CashFlowLab implementation resource')
    if rel=='de/index.html':
        text=text.replace('✔ 1 email/zi max','✔ Max. 1 E-Mail/Tag').replace('Email confirmat!','E-Mail bestätigt!').replace('Preview OG cover pentru share','Vorschau einer Launch-Ressource').replace('Identitate vizuală CashFlowLab','CashFlowLab Umsetzungsressource')
    block=section_html(c)
    text=one(text,r'<!-- Features -->.*?</section>\s*<!-- Proof -->.*?</section>',block,rel+' canonical sections',re.S)
    forbidden=['TVA inclus','97$','Logo + visual cover','Logo + cover vizual','Logo + visuelles Cover','5 email sequence','5 emailuri PRO','5-E-Mail-Sequenz','advanced automations','automatizări avansate','erweiterte Automatisierungen','brand guidelines and covers included','brand guidelines și cover-uri incluse','Brand-Guidelines und Cover inklusive']
    for f in forbidden:
        if f in text: raise SystemExit(f'{rel}: stale claim remains: {f}')
    for req in [c['badge'],'$0','$9','$27','$69.99','10 email templates']:
        if req not in text: raise SystemExit(f'{rel}: canonical requirement missing: {req}')
    p.write_text(text,encoding='utf-8')

# Permanent guardrails.
vp=ROOT/'scripts/validate_repo.py'
v=vp.read_text(encoding='utf-8')
marker='# Homepage canonical invariants (2026).'
if marker not in v:
    guard='''\n# Homepage canonical invariants (2026).\nhomepage_rules = {\n    'index.html': ('2026 • Verificat',),\n    'en/index.html': ('2026 • Verified',),\n    'de/index.html': ('2026 • Geprüft',),\n}\nfor rel, markers in homepage_rules.items():\n    text = read(rel)\n    for needle in markers + ('$0', '$9', '$27', '$69.99', '10 email templates'):\n        if needle not in text:\n            fail(f'{rel}: canonical homepage marker missing: {needle}')\n    for needle in ('TVA inclus','97$','Logo + visual cover','Logo + cover vizual','Logo + visuelles Cover','5 email sequence','5 emailuri PRO','5-E-Mail-Sequenz','advanced automations','automatizări avansate','erweiterte Automatisierungen'):\n        if needle in text:\n            fail(f'{rel}: stale homepage claim returned: {needle}')\n\n'''
    anchor='# Canonical package files that must remain available.\n'
    if anchor not in v: raise SystemExit('validator anchor not found')
    v=v.replace(anchor,guard+anchor,1)
    vp.write_text(v,encoding='utf-8')
print('RO/EN/DE homepages aligned to canonical 2026 products using structural sections.')
