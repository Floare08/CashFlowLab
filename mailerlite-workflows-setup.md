# MailerLite Workflows - CashFlowLab

## Configurare Automatizări Email

---

## 🎯 Workflow 1: Welcome Sequence (FREE Kit)

**Trigger:** Cineva se înscrie pe formularul FREE Kit
**Scop:** Să livreze kitul și să înceapă nurture

### Email 1: Livrare Kit (Immediate)
- **Subiect:** "🎁 Iată CashFlowLab FREE Kit-ul tău"
- **Conținut:** 
  - Mulțumire pentru înscriere
  - Link download: `https://cashflowlabai.com/downloads/free-kit.zip`
  - Instrucțiuni rapide de utilizare
  - CTA: "Vezi și kiturile Premium →"

### Email 2: Story + Value (Ziua 2)
- **Subiect:** "Cum am construit primul meu funnel"
- **Conținut:**
  - Poveste personală (sau brand story)
  - Valoare educațională
  - Nu pitch de vânzare încă

### Email 3: Soft Pitch MINI Kit (Ziua 4)
- **Subiect:** "Ready pentru următorul pas?"
- **Conținut:**
  - Recunoaștere problemă
  - Soluția = MINI Kit
  - Link: `https://cashflowlabai.gumroad.com/l/bpsbou`

---

## 🎯 Workflow 2: Post-Purchase (MINI/MEDIUM/PRO)

**Trigger:** Cineva cumpără un kit plătit
**Scop:** Onboarding și reducere refund-uri

### Email 1: Confirmare + Access (Immediate)
- **Subiect:** "🚀 Comanda ta este confirmată!"
- **Conținut:**
  - Confirmare comandă
  - Link download kit
  - Getting started guide
  - Support contact

### Email 2: Getting Started (Ora 2)
- **Subiect:** "Cum să începi în 30 de minute"
- **Conținut:**
  - Tutorial rapid
  - Primul pas concret
  - Motivație

### Email 3: Check-in (Ziua 3)
- **Subiect:** "Ai reușit să începi?"
- **Conținut:**
  - Întrebare despre progres
  - Ofertă de ajutor
  - Link la resurse suplimentare

### Email 4: Upsell la următorul nivel (Ziua 7)
- **Subiect:** "Ești gata să scalezi?"
- **Conținut:**
  - Recunoaștere progres
  - Pitch pentru upgrade
  - Bonus/time-sensitive offer

---

## 🎯 Workflow 3: Abandoned Cart

**Trigger:** Cineva adaugă în coș dar nu finalizează (pentru Gumroad, folosim page visit + tag)
**Scop:** Recuperare vânzări pierdute

### Email 1: Reminder (Ora 1)
- **Subiect:** "Ai uitat ceva în coș?"
- **Conținut:** Friendly reminder

### Email 2: Incentive (Ziua 1)
- **Subiect:** "10% off dacă finalizezi acum"
- **Conținut:** Discount code (opțional)

---

## 🎯 Workflow 4: Re-engagement (Cold Subscribers)

**Trigger:** Nu au deschis emailuri în 30 zile
**Scop:** Curățare listă sau reactivare

### Email 1: We miss you
- **Subiect:** "Mai ești interesat de CashFlowLab?"
- **Conținut:** Întrebare directă

### Email 2: Last chance
- **Subiect:** "Ultima șansă..."
- **Conținut:** Unsubscribe sau confirmă interesul

---

## 📋 Pași de Implementare în MailerLite

### 1. Creare Automation
1. Mergi la **Automations** în MailerLite
2. Click **Create automation**
3. Alege trigger-ul potrivit

### 2. Configurare Trigger
- **Welcome:** "When subscriber joins group" → Group = FREE Kit
- **Post-Purchase:** "When subscriber is tagged" → Tag = PURCHASED
- **Abandoned:** Manual (via Zapier) sau "When subscriber visits URL"

### 3. Adăugare Emailuri
1. Click **+** pentru a adăuga email
2. Setează delay (immediate, 1 day, etc.)
3. Scrie subiectul și conținutul
4. Salvează și activează

### 4. Testing
1. Folosește funcția **Test** pentru fiecare email
2. Trimite-ți test emails
3. Verifică formatarea pe mobile
4. Testează trigger-ul

---

## 🔗 Integrare cu Gumroad

### Pentru Post-Purchase:
1. În Gumroad: **Settings → Advanced → Ping**
2. Adaugă webhook URL de la Zapier
3. Zapier: Gumroad Purchase → MailerLite Add Tag
4. Tag-ul declanșează automation

### Alternative simplă:
1. După cumpărare, Gumroad trimite email cu link
2. Adaugă în acel email: "Răspunde cu 'START' pentru bonusuri"
3. Când răspund, tag-ezi în MailerLite
4. Automation începe

---

## 📝 Template Email (HTML)

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
</head>
<body style="font-family:Inter,sans-serif;background:#0b0b10;color:#EBECF0;padding:20px;">
  <div style="max-width:600px;margin:0 auto;background:rgba(255,255,255,.05);padding:30px;border-radius:16px;">
    <!-- Logo -->
    <div style="text-align:center;margin-bottom:30px;">
      <img src="https://cashflowlabai.com/Images/logo-mark.png" width="60" alt="CashFlowLab">
    </div>
    
    <!-- Content -->
    <div style="line-height:1.6;">
      [CONTENT HERE]
    </div>
    
    <!-- CTA -->
    <div style="text-align:center;margin:30px 0;">
      <a href="[LINK]" style="display:inline-block;padding:16px 32px;background:linear-gradient(135deg,#D4AF37,#6B2D5C);color:#0b0b10;text-decoration:none;border-radius:999px;font-weight:700;">[CTA TEXT]</a>
    </div>
    
    <!-- Footer -->
    <div style="border-top:1px solid rgba(255,255,255,.1);padding-top:20px;margin-top:30px;font-size:12px;color:rgba(255,255,255,.5);text-align:center;">
      <p>© 2025 CashFlowLab. All rights reserved.</p>
      <p><a href="{unsubscribe_url}" style="color:rgba(255,255,255,.5);">Unsubscribe</a></p>
    </div>
  </div>
</body>
</html>
```

---

## ⚙️ Configurare Avansată (Zapier)

### Zap 1: Gumroad → MailerLite (New Purchase)
```
Trigger: Gumroad - New Sale
Action 1: MailerLite - Add/Update Subscriber
Action 2: MailerLite - Add Tag (e.g., "MINI_KIT_CUSTOMER")
Action 3: Slack - Send Notification (optional)
```

### Zap 2: Abandoned Cart Tracking
```
Trigger: Page visit (via Pixel/MailerLite)
Condition: No purchase in 1 hour
Action: MailerLite - Add Tag "CART_ABANDONED"
```

---

## 📊 Metrici de Urmărit

- **Open rate:** 25%+ (industry average ~21%)
- **Click rate:** 3%+ (industry average ~2.6%)
- **Unsubscribe:** Sub 0.5% per email
- **Conversion:** De la email la cumpărare

---

**Ai întrebări despre implementare?** Scrie-ne la support@cashflowlabai.com
