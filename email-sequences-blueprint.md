# CashFlowLab Email Sequences Blueprint
## Sistem Complet de Email Marketing & Automation

**Brand:** CashFlowLab (cashflowlabai.com)  
**Stil:** Premium (Gold #D4AF37, Purple #6B2D5C)  
**Ton:** Încrezător dar accesibil, practic dar inspirat  
**Audiență:** Antreprenori digitali, freelanceri, creatori de conținut financiar  
**Created:** April 2025

---

# 📊 OVERVIEW: Automation Flow Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         CASHFLOWLAB EMAIL FUNNEL                            │
└─────────────────────────────────────────────────────────────────────────────┘

[Visitor] 
    ↓
[FREE Kit Download] ───────────────────────┐
    ↓                                      │
    FREE SEQUENCE (4 emails)               │
    ├─ Email 1: Welcome + Download         │
    ├─ Email 2: Quick Start (24h)          │
    ├─ Email 3: Success Story (3z)         │
    └─ Email 4: MINI Offer (5z) ───────────┤
    ↓                                      │
[PURCHASE MINI $9?]                        │
    ├─ YES → MINI SEQUENCE                 │
    │         ├─ Email 1: Confirmare       │
    │         ├─ Email 2: 24h Guide (24h)  │
    │         ├─ Email 3: Templates (3z)   │
    │         └─ Email 4: MEDIUM Pitch (7z)│
    │                                      │
    │         ↓                            │
    │   [PURCHASE MEDIUM $21?]             │
    │       ├─ YES → MEDIUM SEQUENCE       │
    │       │         ├─ Email 1: Confirm  │
    │       │         ├─ Email 2: Setup    │
    │       │         ├─ Email 3: Auto     │
    │       │         ├─ Email 4: Biz      │
    │       │         └─ Email 5: PRO      │
    │       │                              │
    │       │         ↓                    │
    │       │   [PURCHASE PRO $39?]        │
    │       │       ├─ YES → PRO SEQUENCE  │
    │       │       │     ├─ Email 1: Conf │
    │       │       │     ├─ Email 2: Sup  │
    │       │       │     ├─ Email 3: List │
    │       │       │     ├─ Email 4: Call │
    │       │       │     └─ Email 5: Tips │
    │       │       │                      │
    │       │       └─ NO → Cart Abandon   │
    │       │                              │
    │       └─ NO → Cart Abandon           │
    │                                      │
    └─ NO → [No activity 30 days?]         │
              ↓                            │
        RE-ENGAGEMENT SEQUENCE             │
        ├─ Email 1: "We miss you" (30z)    │
        ├─ Email 2: Survey (37z)           │
        └─ Email 3: Final (45z)            │
                                           │
[CART ABANDONMENT] ←───────────────────────┘
    ├─ Email 1: Friendly (1h)
    ├─ Email 2: Bonus (24h)
    └─ Email 3: Last Chance (48h)
```

---

# 🏷️ TAGGING & SEGMENTATION STRATEGY

## Tag Structure

### Lead Source Tags
- `source:organic` - Organic traffic
- `source:paid` - Paid ads
- `source:referral` - Referral traffic
- `source:social` - Social media

### Funnel Stage Tags
- `funnel:free` - Downloaded FREE Kit
- `funnel:mini` - Purchased MINI Kit ($9)
- `funnel:medium` - Purchased MEDIUM Kit ($21)
- `funnel:pro` - Purchased PRO Kit ($39)
- `funnel:buyer` - Any purchase made

### Engagement Tags
- `engagement:high` - Open rate >50%
- `engagement:medium` - Open rate 20-50%
- `engagement:low` - Open rate <20%
- `engagement:cold` - No open in 30 days
- `engagement:inactive` - No open in 60 days

### Behavioral Tags
- `action:clicked` - Clicked email links
- `action:downloaded` - Downloaded lead magnet
- `action:purchased` - Made purchase
- `action:cart-abandoned` - Abandoned cart
- `action:upgraded` - Upgraded to higher tier

### Content Interest Tags
- `interest:landing-pages`
- `interest:automation`
- `interest:templates`
- `interest:email-marketing`
- `interest:funnel-strategy`

## Segments in MailerLite

1. **New Leads** - Tag: `funnel:free`, no purchase
2. **Active Subscribers** - Opened email in last 14 days
3. **Buyers** - Tag: `funnel:buyer`
4. **High-Value Buyers** - Tag: `funnel:medium` OR `funnel:pro`
5. **Cart Abandoners** - Tag: `action:cart-abandoned`
6. **Cold Leads** - Tag: `engagement:cold`
7. **VIP Customers** - Tag: `funnel:pro`

---

# 📧 SEQUENCE 1: FREE KIT SEQUENCE
**Trigger:** User downloads FREE Kit  
**Goal:** Nurture lead → Pitch MINI Kit  
**Duration:** 5 days  
**Tags Applied:** `funnel:free`, `source:[detected]`

---

## Email 1: Welcome + Download Link

**Timing:** Immediate (triggered by form submission)  
**Trigger:** FREE Kit form submitted  
**Tag Applied:** `funnel:free`, `action:downloaded`

### Subject Lines (A/B/C):
```
A: Welcome to CashFlowLab, {{first_name}}! 🎁
B: Your FREE CashFlowLab Kit is ready, {{first_name}}
C: {{first_name}}, download your starter kit inside
```

### Preview Text:
```
Everything you need to start building predictable cashflow...
```

### Email Body (HTML):
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome to CashFlowLab</title>
</head>
<body style="margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #0a0a0a; color: #ffffff;">
    <table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color: #0a0a0a;">
        <tr>
            <td align="center" style="padding: 40px 20px;">
                <table width="600" cellpadding="0" cellspacing="0" border="0" style="max-width: 600px; background: linear-gradient(135deg, #1a0a1a 0%, #0d0d0d 100%); border-radius: 12px; overflow: hidden; border: 1px solid #D4AF3733;">
                    <!-- Header -->
                    <tr>
                        <td style="padding: 40px 40px 20px; text-align: center; background: linear-gradient(90deg, #6B2D5C 0%, #D4AF37 100%);">
                            <h1 style="margin: 0; font-size: 28px; color: #ffffff; font-weight: 700;">CASHFLOWLAB</h1>
                            <p style="margin: 8px 0 0; font-size: 14px; color: #D4AF37; letter-spacing: 2px;">PREDICTABLE CASHFLOW SYSTEM</p>
                        </td>
                    </tr>
                    
                    <!-- Content -->
                    <tr>
                        <td style="padding: 40px;">
                            <h2 style="margin: 0 0 20px; font-size: 24px; color: #D4AF37; font-weight: 600;">Hey {{first_name}},</h2>
                            
                            <p style="margin: 0 0 20px; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                Welcome to the CashFlowLab community! 🎉
                            </p>
                            
                            <p style="margin: 0 0 20px; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                You just made a smart move. Most entrepreneurs focus on making more money — you'll be focusing on something much more powerful: <strong style="color: #D4AF37;">predictable cashflow</strong>.
                            </p>
                            
                            <p style="margin: 0 0 30px; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                Your FREE Kit is ready for download. Inside you'll find:
                            </p>
                            
                            <!-- List -->
                            <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-bottom: 30px;">
                                <tr>
                                    <td style="padding: 15px; background-color: #1a1a1a; border-left: 3px solid #D4AF37; border-radius: 0 8px 8px 0; margin-bottom: 10px;">
                                        <p style="margin: 0; font-size: 15px; color: #ffffff;">✓ High-converting landing page template</p>
                                    </td>
                                </tr>
                                <tr><td height="10"></td></tr>
                                <tr>
                                    <td style="padding: 15px; background-color: #1a1a1a; border-left: 3px solid #6B2D5C; border-radius: 0 8px 8px 0;">
                                        <p style="margin: 0; font-size: 15px; color: #ffffff;">✓ Premium logo variations + brand assets</p>
                                    </td>
                                </tr>
                                <tr><td height="10"></td></tr>
                                <tr>
                                    <td style="padding: 15px; background-color: #1a1a1a; border-left: 3px solid #D4AF37; border-radius: 0 8px 8px 0;">
                                        <p style="margin: 0; font-size: 15px; color: #ffffff;">✓ Brand guidelines starter kit</p>
                                    </td>
                                </tr>
                            </table>
                            
                            <!-- CTA Button -->
                            <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-bottom: 30px;">
                                <tr>
                                    <td align="center">
                                        <a href="{{download_link}}" style="display: inline-block; padding: 18px 40px; background: linear-gradient(90deg, #D4AF37 0%, #B8941F 100%); color: #0a0a0a; text-decoration: none; font-weight: 700; font-size: 16px; border-radius: 8px; text-transform: uppercase; letter-spacing: 1px;">Download Your FREE Kit</a>
                                    </td>
                                </tr>
                            </table>
                            
                            <p style="margin: 0 0 20px; font-size: 14px; line-height: 1.6; color: #888888; text-align: center;">
                                Or copy this link: {{download_link}}
                            </p>
                            
                            <p style="margin: 30px 0 0; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                I'll send you a quick-start guide tomorrow to help you make the most of these resources.
                            </p>
                            
                            <p style="margin: 20px 0 0; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                To your success,<br>
                                <strong style="color: #D4AF37;">The CashFlowLab Team</strong>
                            </p>
                        </td>
                    </tr>
                    
                    <!-- Footer -->
                    <tr>
                        <td style="padding: 30px 40px; background-color: #0d0d0d; border-top: 1px solid #333333; text-align: center;">
                            <p style="margin: 0 0 10px; font-size: 12px; color: #666666;">
                                © 2025 CashFlowLab. All rights reserved.
                            </p>
                            <p style="margin: 0; font-size: 12px; color: #666666;">
                                <a href="{{unsubscribe_url}}" style="color: #888888; text-decoration: underline;">Unsubscribe</a> | 
                                <a href="https://cashflowlabai.com" style="color: #888888; text-decoration: underline;">Visit Website</a>
                            </p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
```

### Plain Text Version:
```
Hey {{first_name}},

Welcome to the CashFlowLab community! 

You just made a smart move. Most entrepreneurs focus on making more money — you'll be focusing on something much more powerful: predictable cashflow.

Your FREE Kit is ready for download. Inside you'll find:
- High-converting landing page template
- Premium logo variations + brand assets  
- Brand guidelines starter kit

Download here: {{download_link}}

I'll send you a quick-start guide tomorrow to help you make the most of these resources.

To your success,
The CashFlowLab Team

---
© 2025 CashFlowLab
Unsubscribe: {{unsubscribe_url}}
```

### CTA:
**Primary:** "Download Your FREE Kit"  
**Link:** `{{download_link}}`

### Design Notes:
- Use Gold #D4AF37 accent color for headlines and CTAs
- Dark premium background (#0a0a0a to #1a0a1a gradient)
- Purple #6B2D5C as secondary accent
- Gold gradient button for main CTA
- Include brand logo at top

---

## Email 2: Quick Start Guide + Tips

**Timing:** 24 hours after Email 1  
**Trigger:** Tag `funnel:free` + 24h delay  
**Tag Applied:** `engagement:opened` (if opened)

### Subject Lines (A/B/C):
```
A: Quick-start guide for your CashFlowLab Kit 📋
B: {{first_name}}, let's put your FREE Kit to work
C: 3 ways to maximize your new templates
```

### Preview Text:
```
Most people download resources and never use them. Don't be most people...
```

### Email Body:
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quick Start Guide</title>
</head>
<body style="margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #0a0a0a; color: #ffffff;">
    <table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color: #0a0a0a;">
        <tr>
            <td align="center" style="padding: 40px 20px;">
                <table width="600" cellpadding="0" cellspacing="0" border="0" style="max-width: 600px; background: linear-gradient(135deg, #1a0a1a 0%, #0d0d0d 100%); border-radius: 12px; overflow: hidden; border: 1px solid #D4AF3733;">
                    <tr>
                        <td style="padding: 40px;">
                            <h2 style="margin: 0 0 20px; font-size: 24px; color: #D4AF37; font-weight: 600;">Hey {{first_name}},</h2>
                            
                            <p style="margin: 0 0 20px; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                Did you get a chance to download your FREE CashFlowLab Kit?
                            </p>
                            
                            <p style="margin: 0 0 20px; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                If not, <a href="{{download_link}}" style="color: #D4AF37; text-decoration: underline;">grab it here</a>.
                            </p>
                            
                            <p style="margin: 0 0 30px; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                If you did — here's how to get maximum value in the next 24 hours:
                            </p>
                            
                            <!-- Steps -->
                            <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-bottom: 30px;">
                                <tr>
                                    <td width="50" valign="top" style="padding-right: 15px;">
                                        <div style="width: 40px; height: 40px; background: linear-gradient(135deg, #D4AF37 0%, #B8941F 100%); border-radius: 50%; text-align: center; line-height: 40px; color: #0a0a0a; font-weight: 700; font-size: 18px;">1</div>
                                    </td>
                                    <td valign="top">
                                        <h3 style="margin: 0 0 8px; font-size: 18px; color: #ffffff; font-weight: 600;">Customize the landing page template</h3>
                                        <p style="margin: 0; font-size: 15px; line-height: 1.6; color: #b0b0b0;">Replace the placeholder text with your offer. Don't overthink it — done is better than perfect. The template is designed to convert, trust the structure.</p>
                                    </td>
                                </tr>
                            </table>
                            
                            <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-bottom: 25px;">
                                <tr>
                                    <td width="50" valign="top" style="padding-right: 15px;">
                                        <div style="width: 40px; height: 40px; background: linear-gradient(135deg, #6B2D5C 0%, #8B3D7C 100%); border-radius: 50%; text-align: center; line-height: 40px; color: #ffffff; font-weight: 700; font-size: 18px;">2</div>
                                    </td>
                                    <td valign="top">
                                        <h3 style="margin: 0 0 8px; font-size: 18px; color: #ffffff; font-weight: 600;">Upload your logo variations</h3>
                                        <p style="margin: 0; font-size: 15px; line-height: 1.6; color: #b0b0b0;">Use the dark and light versions we included. Consistent branding builds trust instantly. Keep them in an easy-to-access folder.</p>
                                    </td>
                                </tr>
                            </table>
                            
                            <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-bottom: 30px;">
                                <tr>
                                    <td width="50" valign="top" style="padding-right: 15px;">
                                        <div style="width: 40px; height: 40px; background: linear-gradient(135deg, #D4AF37 0%, #B8941F 100%); border-radius: 50%; text-align: center; line-height: 40px; color: #0a0a0a; font-weight: 700; font-size: 18px;">3</div>
                                    </td>
                                    <td valign="top">
                                        <h3 style="margin: 0 0 8px; font-size: 18px; color: #ffffff; font-weight: 600;">Set up your brand guidelines</h3>
                                        <p style="margin: 0; font-size: 15px; line-height: 1.6; color: #b0b0b0;">Even a simple 1-page doc with your colors, fonts, and tone will save you hours of decision fatigue. Use our starter template.</p>
                                    </td>
                                </tr>
                            </table>
                            
                            <p style="margin: 0 0 30px; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                <strong style="color: #D4AF37;">Pro tip:</strong> The entrepreneurs who succeed aren't the ones with the best templates. They're the ones who actually USE them.
                            </p>
                            
                            <p style="margin: 0; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                Keep building,<br>
                                <strong style="color: #D4AF37;">The CashFlowLab Team</strong>
                            </p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
```

### Plain Text Version:
```
Hey {{first_name}},

Did you get a chance to download your FREE CashFlowLab Kit?

If not, grab it here: {{download_link}}

If you did — here's how to get maximum value in the next 24 hours:

1. CUSTOMIZE THE LANDING PAGE TEMPLATE
Replace the placeholder text with your offer. Don't overthink it — done is better than perfect.

2. UPLOAD YOUR LOGO VARIATIONS
Use the dark and light versions we included. Consistent branding builds trust instantly.

3. SET UP YOUR BRAND GUIDELINES
Even a simple 1-page doc with your colors, fonts, and tone will save you hours.

Pro tip: The entrepreneurs who succeed aren't the ones with the best templates. They're the ones who actually USE them.

Keep building,
The CashFlowLab Team

---
Unsubscribe: {{unsubscribe_url}}
```

### CTA:
No primary CTA (value-only email)

---

## Email 3: Success Story + Soft Pitch MINI Kit

**Timing:** 3 days after Email 1  
**Trigger:** Tag `funnel:free` + 3 days delay  
**Tag Applied:** `engagement:clicked` (if clicked)

### Subject Lines (A/B/C):
```
A: How Sarah went from $0 to $3k/month in 6 weeks
B: The 24-hour shift that changed everything 💡
C: {{first_name}}, this might resonate with you...
```

### Preview Text:
```
She had the same templates you have. Here's what she did differently...
```

### Email Body:
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Success Story</title>
</head>
<body style="margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #0a0a0a; color: #ffffff;">
    <table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color: #0a0a0a;">
        <tr>
            <td align="center" style="padding: 40px 20px;">
                <table width="600" cellpadding="0" cellspacing="0" border="0" style="max-width: 600px; background: linear-gradient(135deg, #1a0a1a 0%, #0d0d0d 100%); border-radius: 12px; overflow: hidden; border: 1px solid #D4AF3733;">
                    <tr>
                        <td style="padding: 40px;">
                            <h2 style="margin: 0 0 20px; font-size: 24px; color: #D4AF37; font-weight: 600;">Hey {{first_name}},</h2>
                            
                            <p style="margin: 0 0 20px; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                I want to tell you about Sarah.
                            </p>
                            
                            <p style="margin: 0 0 20px; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                Three months ago, she was exactly where you might be right now. She had skills. She had ideas. She had the FREE CashFlowLab Kit downloaded on her desktop.
                            </p>
                            
                            <p style="margin: 0 0 20px; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                But she was stuck.
                            </p>
                            
                            <!-- Quote Box -->
                            <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin: 30px 0;">
                                <tr>
                                    <td style="padding: 25px; background: linear-gradient(135deg, #6B2D5C22 0%, #1a1a1a 100%); border-left: 4px solid #6B2D5C; border-radius: 0 8px 8px 0;">
                                        <p style="margin: 0 0 15px; font-size: 18px; line-height: 1.6; color: #ffffff; font-style: italic;">
                                            "I knew I needed a funnel, but I didn't know WHERE to start. Every tutorial I found was either too basic or way too complicated. I just wanted someone to show me exactly what to do, step by step."
                                        </p>
                                        <p style="margin: 0; font-size: 14px; color: #D4AF37; font-weight: 600;">— Sarah M., Freelance Designer</p>
                                    </td>
                                </tr>
                            </table>
                            
                            <p style="margin: 0 0 20px; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                Sound familiar?
                            </p>
                            
                            <p style="margin: 0 0 30px; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                So she grabbed the <strong style="color: #D4AF37;">MINI Kit</strong>. Within 24 hours, she had her first complete funnel live. Within 6 weeks, she had her first $3,000 month.
                            </p>
                            
                            <!-- Soft CTA -->
                            <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-bottom: 30px;">
                                <tr>
                                    <td style="padding: 25px; background-color: #1a1a1a; border-radius: 8px; text-align: center;">
                                        <p style="margin: 0 0 15px; font-size: 16px; color: #ffffff; font-weight: 600;">Ready for the next step?</p>
                                        <p style="margin: 0 0 20px; font-size: 14px; color: #b0b0b0;">The MINI Kit gives you everything Sarah had — for less than a lunch out.</p>
                                        <a href="{{mini_kit_sales_page}}" style="display: inline-block; padding: 15px 35px; background: linear-gradient(90deg, #D4AF37 0%, #B8941F 100%); color: #0a0a0a; text-decoration: none; font-weight: 700; font-size: 15px; border-radius: 8px;">See What's in the MINI Kit →</a>
                                    </td>
                                </tr>
                            </table>
                            
                            <p style="margin: 0; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                Keep building,<br>
                                <strong style="color: #D4AF37;">The CashFlowLab Team</strong>
                            </p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
```

### Plain Text Version:
```
Hey {{first_name}},

I want to tell you about Sarah.

Three months ago, she was exactly where you might be right now. She had skills, ideas, and the FREE CashFlowLab Kit.

But she was stuck.

"I knew I needed a funnel, but I didn't know WHERE to start. Every tutorial I found was either too basic or way too complicated."
— Sarah M., Freelance Designer

Sound familiar?

So she grabbed the MINI Kit. Within 24 hours, she had her first complete funnel live. Within 6 weeks, she had her first $3,000 month.

Ready for the next step?
The MINI Kit gives you everything Sarah had — for less than a lunch out.

See what's inside: {{mini_kit_sales_page}}

No pressure either way. I'm here when you're ready.

Keep building,
The CashFlowLab Team

---
Unsubscribe: {{unsubscribe_url}}
```

### CTA:
**Primary:** "See What's in the MINI Kit →"  
**Link:** `{{mini_kit_sales_page}}`  
**Style:** Soft sell, story-based

---

## Email 4: MINI Kit Offer with Urgency

**Timing:** 5 days after Email 1  
**Trigger:** Tag `funnel:free` + 5 days delay + no purchase  
**Tag Applied:** `action:pitched-mini`

### Subject Lines (A/B/C):
```
A: Last call: MINI Kit at $9 (price changes soon)
B: {{first_name}}, your templates are waiting...
C: The $9 investment that saves 10+ hours
```

### Preview Text:
```
You already have the foundation. Here's the complete system...
```

### Email Body:
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MINI Kit Offer</title>
</head>
<body style="margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #0a0a0a; color: #ffffff;">
    <table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color: #0a0a0a;">
        <tr>
            <td align="center" style="padding: 40px 20px;">
                <table width="600" cellpadding="0" cellspacing="0" border="0" style="max-width: 600px; background: linear-gradient(135deg, #1a0a1a 0%, #0d0d0d 100%); border-radius: 12px; overflow: hidden; border: 1px solid #D4AF3733;">
                    <!-- Urgency Banner -->
                    <tr>
                        <td style="padding: 15px; background: linear-gradient(90deg, #6B2D5C 0%, #D4AF37 100%); text-align: center;">
                            <p style="margin: 0; font-size: 13px; color: #ffffff; font-weight: 600; letter-spacing: 1px;">⚡ LIMITED TIME: MINI Kit at $9</p>
                        </td>
                    </tr>
                    
                    <tr>
                        <td style="padding: 40px;">
                            <h2 style="margin: 0 0 20px; font-size: 24px; color: #D4AF37; font-weight: 600;">Hey {{first_name}},</h2>
                            
                            <p style="margin: 0 0 20px; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                Quick question: How many hours have you spent searching for the "perfect" template?
                            </p>
                            
                            <p style="margin: 0 0 30px; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                What if you could stop searching and start launching?
                            </p>
                            
                            <!-- What's Included -->
                            <h3 style="margin: 0 0 20px; font-size: 20px; color: #ffffff; font-weight: 600;">The MINI Kit includes:</h3>
                            
                            <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-bottom: 30px;">
                                <tr>
                                    <td style="padding: 20px; background-color: #1a1a1a; border-radius: 8px;">
                                        <p style="margin: 0; font-size: 15px; color: #ffffff;">✓ <strong>3 Landing Page Variations</strong> — Opt-in, sales, and webinar templates</p>
                                    </td>
                                </tr>
                                <tr><td height="10"></td></tr>
                                <tr>
                                    <td style="padding: 20px; background-color: #1a1a1a; border-radius: 8px;">
                                        <p style="margin: 0; font-size: 15px; color: #ffffff;">✓ <strong>The 24-Hour Setup Guide</strong> — Exact steps to go live in one day</p>
                                    </td>
                                </tr>
                                <tr><td height="10"></td></tr>
                                <tr>
                                    <td style="padding: 20px; background-color: #1a1a1a; border-radius: 8px;">
                                        <p style="margin: 0; font-size: 15px; color: #ffffff;">✓ <strong>Premium Branding Assets</strong> — Extended logo pack, social templates</p>
                                    </td>
                                </tr>
                                <tr><td height="10"></td></tr>
                                <tr>
                                    <td style="padding: 20px; background-color: #1a1a1a; border-radius: 8px;">
                                        <p style="margin: 0; font-size: 15px; color: #ffffff;">✓ <strong>Bonus: Headline Swipe File</strong> — 50 proven headlines</p>
                                    </td>
                                </tr>
                            </table>
                            
                            <!-- Price Box -->
                            <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-bottom: 30px;">
                                <tr>
                                    <td style="padding: 30px; background: linear-gradient(135deg, #6B2D5C 0%, #4B1D3C 100%); border-radius: 12px; text-align: center; border: 2px solid #D4AF37;">
                                        <p style="margin: 0 0 10px; font-size: 14px; color: #D4AF37; text-transform: uppercase; letter-spacing: 2px;">Limited Time Offer</p>
                                        <p style="margin: 0 0 15px; font-size: 48px; color: #ffffff; font-weight: 700;">$9</p>
                                        <p style="margin: 0 0 20px; font-size: 14px; color: #b0b0b0; text-decoration: line-through;">Regular price: $27</p>
                                        <a href="{{mini_kit_checkout}}" style="display: inline-block; padding: 18px 40px; background: linear-gradient(90deg, #D4AF37 0%, #B8941F 100%); color: #0a0a0a; text-decoration: none; font-weight: 700; font-size: 16px; border-radius: 8px; text-transform: uppercase;">Get the MINI Kit →</a>
                                    </td>
                                </tr>
                            </table>
                            
                            <p style="margin: 0; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                Your move, {{first_name}}.
                            </p>
                            
                            <p style="margin: 20px 0 0; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                — The CashFlowLab Team
                            </p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
```

### Plain Text Version:
```
Hey {{first_name}},

⚡ LIMITED TIME: MINI Kit at $9

Quick question: How many hours have you spent searching for the "perfect" template?

THE MINI KIT INCLUDES:
✓ 3 Landing Page Variations — Opt-in, sales, and webinar templates
✓ The 24-Hour Setup Guide — Exact steps to go live in one day
✓ Premium Branding Assets — Extended logo pack, social templates
✓ Bonus: Headline Swipe File — 50 proven headlines

---
LIMITED TIME OFFER
$9 (Regular price: $27)
---

Get it here: {{mini_kit_checkout}}

One-time payment. Lifetime access. 30-day money-back guarantee.

Your move, {{first_name}}.

— The CashFlowLab Team

---
Unsubscribe: {{unsubscribe_url}}
```

### CTA:
**Primary:** "Get the MINI Kit →"  
**Link:** `{{mini_kit_checkout}}`

---

# 📧 SEQUENCE 2: MINI KIT PURCHASE SEQUENCE
**Trigger:** User purchases MINI Kit ($9)  
**Goal:** Deliver value → Upsell to MEDIUM Kit  
**Duration:** 7 days

---

## Email 1: Confirmare + Acces (Immediate)

**Timing:** Immediate after purchase  
**Trigger:** Purchase completed for MINI Kit  
**Tag Applied:** `funnel:mini`, `funnel:buyer`

### Subject Lines (A/B/C):
```
A: Your MINI Kit is ready, {{first_name}}! 🎉
B: Welcome to the next level — access inside
C: {{first_name}}, your purchase confirmation + download
```

### Preview Text:
```
Everything you need to launch your first funnel in 24 hours...
```

### Email Body:
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MINI Kit Access</title>
</head>
<body style="margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #0a0a0a; color: #ffffff;">
    <table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color: #0a0a0a;">
        <tr>
            <td align="center" style="padding: 40px 20px;">
                <table width="600" cellpadding="0" cellspacing="0" border="0" style="max-width: 600px; background: linear-gradient(135deg, #1a0a1a 0%, #0d0d0d 100%); border-radius: 12px; overflow: hidden; border: 1px solid #D4AF3733;">
                    <tr>
                        <td style="padding: 40px; text-align: center;">
                            <div style="width: 80px; height: 80px; background: linear-gradient(135deg, #D4AF37 0%, #B8941F 100%); border-radius: 50%; margin: 0 auto 30px; line-height: 80px; font-size: 40px;">✓</div>
                            
                            <h1 style="margin: 0 0 15px; font-size: 28px; color: #D4AF37; font-weight: 700;">Welcome to the MINI Kit!</h1>
                            
                            <p style="margin: 0 0 30px; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                Hey {{first_name}}, your purchase is confirmed and your resources are ready.
                            </p>
                        </td>
                    </tr>
                    
                    <tr>
                        <td style="padding: 0 40px 40px;">
                            <!-- Access Box -->
                            <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-bottom: 30px;">
                                <tr>
                                    <td style="padding: 30px; background: linear-gradient(135deg, #6B2D5C 0%, #4B1D3C 100%); border-radius: 12px; text-align: center;">
                                        <a href="{{mini_kit_member_area}}" style="display: inline-block; padding: 18px 40px; background: linear-gradient(90deg, #D4AF37 0%, #B8941F 100%); color: #0a0a0a; text-decoration: none; font-weight: 700; font-size: 16px; border-radius: 8px; text-transform: uppercase;">Access Your MINI Kit</a>
                                        <p style="margin: 15px 0 0; font-size: 13px; color: #D4AF37;">Save this link — lifetime access</p>
                                    </td>
                                </tr>
                            </table>
                            
                            <h3 style="margin: 0 0 20px; font-size: 18px; color: #ffffff; font-weight: 600;">What's inside:</h3>
                            
                            <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-bottom: 30px;">
                                <tr>
                                    <td style="padding: 15px; background-color: #1a1a1a; border-left: 3px solid #D4AF37; border-radius: 0 8px 8px 0; margin-bottom: 10px;">
                                        <p style="margin: 0; font-size: 15px; color: #ffffff;">✓ 3 Landing Page Templates (ZIP)</p>
                                    </td>
                                </tr>
                                <tr><td height="10"></td></tr>
                                <tr>
                                    <td style="padding: 15px; background-color: #1a1a1a; border-left: 3px solid #6B2D5C; border-radius: 0 8px 8px 0;">
                                        <p style="margin: 0; font-size: 15px; color: #ffffff;">✓ The 24-Hour Setup Guide (PDF)</p>
                                    </td>
                                </tr>
                                <tr><td height="10"></td></tr>
                                <tr>
                                    <td style="padding: 15px; background-color: #1a1a1a; border-left: 3px solid #D4AF37; border-radius: 0 8px 8px 0;">
                                        <p style="margin: 0; font-size: 15px; color: #ffffff;">✓ Branding Assets Pack (ZIP)</p>
                                    </td>
                                </tr>
                                <tr><td height="10"></td></tr>
                                <tr>
                                    <td style="padding: 15px; background-color: #1a1a1a; border-left: 3px solid #6B2D5C; border-radius: 0 8px 8px 0;">
                                        <p style="margin: 0; font-size: 15px; color: #ffffff;">✓ Headline Swipe File (PDF)</p>
                                    </td>
                                </tr>
                            </table>
                            
                            <p style="margin: 0 0 20px; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                <strong style="color: #D4AF37;">Quick tip:</strong> Start with the 24-Hour Setup Guide. It'll show you exactly which template to use for your specific situation.
                            </p>
                            
                            <p style="margin: 0; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                To your success,<br>
                                <strong style="color: #D4AF37;">The CashFlowLab Team</strong>
                            </p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
```

### Plain Text Version:
```
Hey {{first_name}},

✓ Purchase Confirmed!

Welcome to the MINI Kit!

Your purchase is confirmed and your resources are ready.

ACCESS YOUR KIT:
{{mini_kit_member_area}}

Save this link — lifetime access.

WHAT'S INSIDE:
✓ 3 Landing Page Templates (ZIP)
✓ The 24-Hour Setup Guide (PDF)
✓ Branding Assets Pack (ZIP)
✓ Headline Swipe File (PDF)

Quick tip: Start with the 24-Hour Setup Guide. It'll show you exactly which template to use.

To your success,
The CashFlowLab Team

---
Order #: {{order_number}} | Date: {{order_date}}
Unsubscribe: {{unsubscribe_url}}
```

### CTA:
**Primary:** "Access Your MINI Kit"  
**Link:** `{{mini_kit_member_area}}`

---

## Email 2: Cum să folosești ghidul 24h

**Timing:** 24 hours after purchase  
**Trigger:** Tag `funnel:mini` + 24h delay

### Subject Lines (A/B/C):
```
A: Your 24-hour funnel roadmap is here 📋
B: {{first_name}}, start here (MINI Kit walkthrough)
C: How to launch in 24 hours — step by step
```

### Preview Text:
```
The 24-hour guide only works if you use it this way...
```

### Email Body:
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>24h Guide Walkthrough</title>
</head>
<body style="margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #0a0a0a; color: #ffffff;">
    <table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color: #0a0a0a;">
        <tr>
            <td align="center" style="padding: 40px 20px;">
                <table width="600" cellpadding="0" cellspacing="0" border="0" style="max-width: 600px; background: linear-gradient(135deg, #1a0a1a 0%, #0d0d0d 100%); border-radius: 12px; overflow: hidden; border: 1px solid #D4AF3733;">
                    <tr>
                        <td style="padding: 40px;">
                            <h2 style="margin: 0 0 20px; font-size: 24px; color: #D4AF37; font-weight: 600;">Hey {{first_name}},</h2>
                            
                            <p style="margin: 0 0 30px; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                The <strong style="color: #D4AF37;">24-Hour Setup Guide</strong> is your fastest path to a working funnel. Here's the breakdown:
                            </p>
                            
                            <!-- Timeline -->
                            <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-bottom: 30px;">
                                <tr>
                                    <td style="padding: 20px; background-color: #1a1a1a; border-radius: 8px 8px 0 0; border-bottom: 1px solid #333;">
                                        <p style="margin: 0 0 8px; font-size: 14px; color: #D4AF37; font-weight: 600;">HOUR 1-2: CHOOSE YOUR TEMPLATE</p>
                                        <p style="margin: 0; font-size: 14px; color: #b0b0b0;">Pick the landing page that matches your offer type. Don't overthink it.</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td style="padding: 20px; background-color: #1a1a1a; border-bottom: 1px solid #333;">
                                        <p style="margin: 0 0 8px; font-size: 14px; color: #D4AF37; font-weight: 600;">HOUR 3-6: CUSTOMIZE THE COPY</p>
                                        <p style="margin: 0; font-size: 14px; color: #b0b0b0;">Replace placeholder text with your offer details. Use the Headline Swipe File.</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td style="padding: 20px; background-color: #1a1a1a; border-bottom: 1px solid #333;">
                                        <p style="margin: 0 0 8px; font-size: 14px; color: #D4AF37; font-weight: 600;">HOUR 7-12: ADD YOUR BRANDING</p>
                                        <p style="margin: 0; font-size: 14px; color: #b0b0b0;">Upload your logo, set your colors, apply your fonts from the Brand Assets Pack.</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td style="padding: 20px; background-color: #1a1a1a; border-bottom: 1px solid #333;">
                                        <p style="margin: 0 0 8px; font-size: 14px; color: #D4AF37; font-weight: 600;">HOUR 13-18: SET UP INTEGRATIONS</p>
                                        <p style="margin: 0; font-size: 14px; color: #b0b0b0;">Connect your email provider, payment processor, and tracking.</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td style="padding: 20px; background-color: #1a1a1a; border-radius: 0 0 8px 8px;">
                                        <p style="margin: 0 0 8px; font-size: 14px; color: #D4AF37; font-weight: 600;">HOUR 19-24: TEST & LAUNCH</p>
                                        <p style="margin: 0; font-size: 14px; color: #b0b0b0;">Test every button, form, and link. Then push it live. Done beats perfect.</p>
                                    </td>
                                </tr>
                            </table>
                            
                            <p style="margin: 0; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                <strong style="color: #D4AF37;">Remember:</strong> The goal isn't perfection. The goal is a working funnel you can improve over time.
                            </p>
                            
                            <p style="margin: 20px 0 0; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                Rooting for you,<br>
                                <strong style="color: #D4AF37;">The CashFlowLab Team</strong>
                            </p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
```

### CTA:
No primary CTA (education-focused)

---

## Email 3: Template Showcase + Tips

**Timing:** 3 days after purchase  
**Trigger:** Tag `funnel:mini` + 3 days delay

### Subject Lines (A/B/C):
```
A: Which template is right for you?
B: Pro tips for your landing pages 🎨
C: {{first_name}}, getting the most from your templates
```

### Preview Text:
```
How to choose, customize, and optimize each template...
```

### Email Body:
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Template Showcase</title>
</head>
<body style="margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #0a0a0a; color: #ffffff;">
    <table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color: #0a0a0a;">
        <tr>
            <td align="center" style="padding: 40px 20px;">
                <table width="600" cellpadding="0" cellspacing="0" border="0" style="max-width: 600px; background: linear-gradient(135deg, #1a0a1a 0%, #0d0d0d 100%); border-radius: 12px; overflow: hidden; border: 1px solid #D4AF3733;">
                    <tr>
                        <td style="padding: 40px;">
                            <h2 style="margin: 0 0 20px; font-size: 24px; color: #D4AF37; font-weight: 600;">Hey {{first_name}},</h2>
                            
                            <p style="margin: 0 0 30px; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                You have three landing page templates in your MINI Kit. Here's when to use each:
                            </p>
                            
                            <!-- Template 1 -->
                            <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-bottom: 25px;">
                                <tr>
                                    <td style="padding: 25px; background-color: #1a1a1a; border-radius: 8px; border-left: 4px solid #D4AF37;">
                                        <h3 style="margin: 0 0 8px; font-size: 18px; color: #D4AF37; font-weight: 600;">🎯 The Opt-In Template</h3>
                                        <p style="margin: 0 0 10px; font-size: 14px; color: #888888;">Best for: Lead magnets, free resources, waitlists</p>
                                        <p style="margin: 0; font-size: 15px; color: #e0e0e0;"><strong style="color: #6B9B6B;">Pro tip:</strong> Add social proof — even 2-3 testimonials can boost conversions 30%+</p>
                                    </td>
                                </tr>
                            </table>
                            
                            <!-- Template 2 -->
                            <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-bottom: 25px;">
                                <tr>
                                    <td style="padding: 25px; background-color: #1a1a1a; border-radius: 8px; border-left: 4px solid #6B2D5C;">
                                        <h3 style="margin: 0 0 8px; font-size: 18px; color: #6B2D5C; font-weight: 600;">💰 The Sales Page Template</h3>
                                        <p style="margin: 0 0 10px; font-size: 14px; color: #888888;">Best for: Courses, services, digital products</p>
                                        <p style="margin: 0; font-size: 15px; color: #e0e0e0;"><strong style="color: #6B9B6B;">Pro tip:</strong> Add 3+ CTAs throughout the page, not just at the bottom</p>
                                    </td>
                                </tr>
                            </table>
                            
                            <!-- Template 3 -->
                            <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-bottom: 30px;">
                                <tr>
                                    <td style="padding: 25px; background-color: #1a1a1a; border-radius: 8px; border-left: 4px solid #D4AF37;">
                                        <h3 style="margin: 0 0 8px; font-size: 18px; color: #D4AF37; font-weight: 600;">📅 The Webinar Template</h3>
                                        <p style="margin: 0 0 10px; font-size: 14px; color: #888888;">Best for: Live training, workshops, launches</p>
                                        <p style="margin: 0; font-size: 15px; color: #e0e0e0;"><strong style="color: #6B9B6B;">Pro tip:</strong> Include a countdown timer and clearly show date/time in their timezone</p>
                                    </td>
                                </tr>
                            </table>
                            
                            <p style="margin: 0; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                Keep building,<br>
                                <strong style="color: #D4AF37;">The CashFlowLab Team</strong>
                            </p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
```

### CTA:
No primary CTA

---

## Email 4: MEDIUM Kit Upgrade Pitch

**Timing:** 7 days after purchase  
**Trigger:** Tag `funnel:mini` + 7 days delay + no MEDIUM purchase  
**Tag Applied:** `action:pitched-medium`

### Subject Lines (A/B/C):
```
A: Ready for the complete system, {{first_name}}?
B: You've built the foundation. Here's the rest.
C: What's missing from your MINI Kit?
```

### Preview Text:
```
The difference between a landing page and a complete cashflow system...
```

### Email Body:
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MEDIUM Kit Upgrade</title>
</head>
<body style="margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #0a0a0a; color: #ffffff;">
    <table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color: #0a0a0a;">
        <tr>
            <td align="center" style="padding: 40px 20px;">
                <table width="600" cellpadding="0" cellspacing="0" border="0" style="max-width: 600px; background: linear-gradient(135deg, #1a0a1a 0%, #0d0d0d 100%); border-radius: 12px; overflow: hidden; border: 1px solid #D4AF3733;">
                    <tr>
                        <td style="padding: 40px;">
                            <h2 style="margin: 0 0 20px; font-size: 24px; color: #D4AF37; font-weight: 600;">Hey {{first_name}},</h2>
                            
                            <p style="margin: 0 0 20px; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                It's been a week since you grabbed the MINI Kit. By now, you probably have a landing page ready.
                            </p>
                            
                            <!-- Quote -->
                            <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin: 25px 0;">
                                <tr>
                                    <td style="padding: 25px; background: linear-gradient(135deg, #6B2D5C22 0%, #1a1a1a 100%); border-left: 4px solid #6B2D5C; border-radius: 0 8px 8px 0;">
                                        <p style="margin: 0; font-size: 18px; line-height: 1.6; color: #ffffff; font-style: italic;">
                                            "A landing page without a funnel is like a fishing rod without a line. It looks good, but it won't catch anything."
                                        </p>
                                    </td>
                                </tr>
                            </table>
                            
                            <p style="margin: 0 0 30px; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                The MINI Kit gave you the fishing rod. The <strong style="color: #D4AF37;">MEDIUM Kit</strong> gives you everything else:
                            </p>
                            
                            <!-- Upgrade Box -->
                            <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-bottom: 30px;">
                                <tr>
                                    <td style="padding: 30px; background: linear-gradient(135deg, #1a1a2e 0%, #0d0d1a 100%); border-radius: 12px; border: 2px solid #D4AF37;">
                                        <h3 style="margin: 0 0 20px; font-size: 20px; color: #D4AF37; text-align: center;">Upgrade to MEDIUM Kit</h3>
                                        
                                        <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-bottom: 20px;">
                                            <tr><td style="padding: 12px 0; border-bottom: 1px solid #333;"><p style="margin: 0; font-size: 14px; color: #e0e0e0;">✓ Complete funnel template (5 pages)</p></td></tr>
                                            <tr><td style="padding: 12px 0; border-bottom: 1px solid #333;"><p style="margin: 0; font-size: 14px; color: #e0e0e0;">✓ 5-email welcome sequence template</p></td></tr>
                                            <tr><td style="padding: 12px 0; border-bottom: 1px solid #333;"><p style="margin: 0; font-size: 14px; color: #e0e0e0;">✓ Automation workflow blueprints</p></td></tr>
                                            <tr><td style="padding: 12px 0; border-bottom: 1px solid #333;"><p style="margin: 0; font-size: 14px; color: #e0e0e0;">✓ Contract & proposal templates</p></td></tr>
                                            <tr><td style="padding: 12px 0;"><p style="margin: 0; font-size: 14px; color: #e0e0e0;">✓ Pricing calculator spreadsheet</p></td></tr>
                                        </table>
                                        
                                        <p style="margin: 0 0 20px; font-size: 24px; color: #ffffff; text-align: center; font-weight: 700;">$21 <span style="font-size: 14px; color: #888888; text-decoration: line-through; font-weight: 400;">$49</span></p>
                                        
                                        <table width="100%" cellpadding="0" cellspacing="0" border="0">
                                            <tr>
                                                <td align="center">
                                                    <a href="{{medium_kit_checkout}}" style="display: inline-block; padding: 18px 40px; background: linear-gradient(90deg, #D4AF37 0%, #B8941F 100%); color: #0a0a0a; text-decoration: none; font-weight: 700; font-size: 16px; border-radius: 8px; text-transform: uppercase;">Upgrade Now →</a>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
                            
                            <p style="margin: 0; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                — The CashFlowLab Team
                            </p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
```

### Plain Text Version:
```
Hey {{first_name}},

It's been a week since you grabbed the MINI Kit.

"A landing page without a funnel is like a fishing rod without a line. It looks good, but it won't catch anything."

The MINI Kit gave you the fishing rod. The MEDIUM Kit gives you:
- Complete funnel template (5 pages)
- 5-email welcome sequence template
- Automation workflow blueprints
- Contract & proposal templates
- Pricing calculator spreadsheet

---
$21 (Regular: $49)
Upgrade: {{medium_kit_checkout}}
---

— The CashFlowLab Team

---
Unsubscribe: {{unsubscribe_url}}
```

### CTA:
**Primary:** "Upgrade Now →"  
**Link:** `{{medium_kit_checkout}}`

---

# 📧 SEQUENCE 3: MEDIUM KIT PURCHASE SEQUENCE
**Trigger:** User purchases MEDIUM Kit ($21)  
**Goal:** Deep dive into features → Upsell to PRO Kit  
**Duration:** 10 days

---

## Email 1: Confirmare + Acces + Roadmap

**Timing:** Immediate after purchase  
**Trigger:** Purchase completed for MEDIUM Kit  
**Tag Applied:** `funnel:medium`, `action:purchased`

### Subject Lines (A/B/C):
```
A: Your MEDIUM Kit access is ready! 🚀
B: Welcome to the complete system, {{first_name}}
C: {{first_name}}, your MEDIUM Kit + roadmap inside
```

### Email Body:
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MEDIUM Kit Access</title>
</head>
<body style="margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #0a0a0a; color: #ffffff;">
    <table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color: #0a0a0a;">
        <tr>
            <td align="center" style="padding: 40px 20px;">
                <table width="600" cellpadding="0" cellspacing="0" border="0" style="max-width: 600px; background: linear-gradient(135deg, #1a0a1a 0%, #0d0d0d 100%); border-radius: 12px; overflow: hidden; border: 1px solid #D4AF3733;">
                    <tr>
                        <td style="padding: 40px; text-align: center;">
                            <div style="width: 80px; height: 80px; background: linear-gradient(135deg, #6B2D5C 0%, #8B3D7C 100%); border-radius: 50%; margin: 0 auto 30px; line-height: 80px; font-size: 40px;">🚀</div>
                            
                            <h1 style="margin: 0 0 15px; font-size: 28px; color: #D4AF37; font-weight: 700;">Welcome to MEDIUM Kit!</h1>
                            
                            <p style="margin: 0 0 30px; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                Hey {{first_name}}, you've just unlocked the complete CashFlowLab system.
                            </p>
                        </td>
                    </tr>
                    
                    <tr>
                        <td style="padding: 0 40px 40px;">
                            <!-- Access Box -->
                            <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-bottom: 30px;">
                                <tr>
                                    <td style="padding: 30px; background: linear-gradient(135deg, #6B2D5C 0%, #4B1D3C 100%); border-radius: 12px; text-align: center;">
                                        <a href="{{medium_kit_member_area}}" style="display: inline-block; padding: 18px 40px; background: linear-gradient(90deg, #D4AF37 0%, #B8941F 100%); color: #0a0a0a; text-decoration: none; font-weight: 700; font-size: 16px; border-radius: 8px; text-transform: uppercase;">Access Your MEDIUM Kit</a>
                                    </td>
                                </tr>
                            </table>
                            
                            <h3 style="margin: 0 0 20px; font-size: 20px; color: #ffffff; font-weight: 600;">Your Implementation Roadmap:</h3>
                            
                            <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-bottom: 30px;">
                                <tr>
                                    <td style="padding: 20px; background-color: #1a1a1a; border-radius: 8px 8px 0 0; border-bottom: 1px solid #333;">
                                        <p style="margin: 0 0 8px; font-size: 14px; color: #D4AF37; font-weight: 600;">WEEK 1: FOUNDATION</p>
                                        <p style="margin: 0; font-size: 14px; color: #b0b0b0;">Set up your complete funnel using the 5-page template</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td style="padding: 20px; background-color: #1a1a1a; border-bottom: 1px solid #333;">
                                        <p style="margin: 0 0 8px; font-size: 14px; color: #D4AF37; font-weight: 600;">WEEK 2: EMAIL SYSTEM</p>
                                        <p style="margin: 0; font-size: 14px; color: #b0b0b0;">Customize and connect the 5-email welcome sequence</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td style="padding: 20px; background-color: #1a1a1a; border-bottom: 1px solid #333;">
                                        <p style="margin: 0 0 8px; font-size: 14px; color: #D4AF37; font-weight: 600;">WEEK 3: AUTOMATION</p>
                                        <p style="margin: 0; font-size: 14px; color: #b0b0b0;">Implement the workflow blueprints for hands-off sales</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td style="padding: 20px; background-color: #1a1a1a; border-radius: 0 0 8px 8px;">
                                        <p style="margin: 0 0 8px; font-size: 14px; color: #D4AF37; font-weight: 600;">WEEK 4: OPTIMIZE</p>
                                        <p style="margin: 0; font-size: 14px; color: #b0b0b0;">Test, refine, and use business templates for operations</p>
                                    </td>
                                </tr>
                            </table>
                            
                            <p style="margin: 0; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                To your success,<br>
                                <strong style="color: #D4AF37;">The CashFlowLab Team</strong>
                            </p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
```

### CTA:
**Primary:** "Access Your MEDIUM Kit"  
**Link:** `{{medium_kit_member_area}}`

## Email 2: Funnel Setup Guide

**Timing:** 24 hours after purchase  
**Trigger:** Tag `funnel:medium` + 24h delay

### Subject Lines (A/B/C):
```
A: Your 5-page funnel blueprint 📐
B: Let's build your cashflow system, {{first_name}}
C: Step 1: The complete funnel setup
```

### Preview Text:
```
How to connect all 5 pages into a money-making machine...
```

### Email Body:
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Funnel Setup Guide</title>
</head>
<body style="margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #0a0a0a; color: #ffffff;">
    <table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color: #0a0a0a;">
        <tr>
            <td align="center" style="padding: 40px 20px;">
                <table width="600" cellpadding="0" cellspacing="0" border="0" style="max-width: 600px; background: linear-gradient(135deg, #1a0a1a 0%, #0d0d0d 100%); border-radius: 12px; overflow: hidden; border: 1px solid #D4AF3733;">
                    <tr>
                        <td style="padding: 40px;">
                            <h2 style="margin: 0 0 20px; font-size: 24px; color: #D4AF37; font-weight: 600;">Hey {{first_name}},</h2>
                            
                            <p style="margin: 0 0 30px; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                Let's dive into your 5-page funnel template. Each page has a specific job:
                            </p>
                            
                            <!-- Funnel Diagram -->
                            <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-bottom: 30px;">
                                <tr>
                                    <td style="padding: 20px; background: linear-gradient(135deg, #6B2D5C 0%, #4B1D3C 100%); border-radius: 8px; text-align: center; margin-bottom: 10px;">
                                        <p style="margin: 0; font-size: 16px; color: #ffffff; font-weight: 600;">1. OPT-IN PAGE</p>
                                        <p style="margin: 5px 0 0; font-size: 13px; color: #D4AF37;">Capture the lead →</p>
                                    </td>
                                </tr>
                                <tr><td align="center" style="padding: 10px 0; color: #D4AF37; font-size: 20px;">↓</td></tr>
                                <tr>
                                    <td style="padding: 20px; background-color: #1a1a1a; border-radius: 8px; text-align: center; border: 1px solid #333;">
                                        <p style="margin: 0; font-size: 16px; color: #ffffff; font-weight: 600;">2. TRIPWIRE OFFER</p>
                                        <p style="margin: 5px 0 0; font-size: 13px; color: #888888;">Convert to customer →</p>
                                    </td>
                                </tr>
                                <tr><td align="center" style="padding: 10px 0; color: #D4AF37; font-size: 20px;">↓</td></tr>
                                <tr>
                                    <td style="padding: 20px; background-color: #1a1a1a; border-radius: 8px; text-align: center; border: 1px solid #333;">
                                        <p style="margin: 0; font-size: 16px; color: #ffffff; font-weight: 600;">3. UPSELL PAGE</p>
                                        <p style="margin: 5px 0 0; font-size: 13px; color: #888888;">Increase order value →</p>
                                    </td>
                                </tr>
                                <tr><td align="center" style="padding: 10px 0; color: #D4AF37; font-size: 20px;">↓</td></tr>
                                <tr>
                                    <td style="padding: 20px; background-color: #1a1a1a; border-radius: 8px; text-align: center; border: 1px solid #333;">
                                        <p style="margin: 0; font-size: 16px; color: #ffffff; font-weight: 600;">4. THANK YOU PAGE</p>
                                        <p style="margin: 5px 0 0; font-size: 13px; color: #888888;">Deliver + next steps →</p>
                                    </td>
                                </tr>
                                <tr><td align="center" style="padding: 10px 0; color: #D4AF37; font-size: 20px;">↓</td></tr>
                                <tr>
                                    <td style="padding: 20px; background: linear-gradient(135deg, #D4AF37 0%, #B8941F 100%); border-radius: 8px; text-align: center;">
                                        <p style="margin: 0; font-size: 16px; color: #0a0a0a; font-weight: 600;">5. EMAIL SEQUENCE</p>
                                        <p style="margin: 5px 0 0; font-size: 13px; color: #6B2D5C;">Nurture + repeat sales ✓</p>
                                    </td>
                                </tr>
                            </table>
                            
                            <p style="margin: 0; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                <strong style="color: #D4AF37;">The key insight:</strong> Most people only build page #1 and wonder why they don't make sales. You need ALL FIVE.
                            </p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
```

### CTA:
No primary CTA (education-focused)

---

## Email 3: Automation Deep Dive

**Timing:** 3 days after purchase  
**Trigger:** Tag `funnel:medium` + 3 days delay

### Subject Lines (A/B/C):
```
A: Set up automation that runs 24/7 ⚙️
B: The "while you sleep" sales machine
C: {{first_name}}, automate your follow-up
```

### Preview Text:
```
Never miss a lead or forget a follow-up again...
```

### Email Body:
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Automation Deep Dive</title>
</head>
<body style="margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #0a0a0a; color: #ffffff;">
    <table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color: #0a0a0a;">
        <tr>
            <td align="center" style="padding: 40px 20px;">
                <table width="600" cellpadding="0" cellspacing="0" border="0" style="max-width: 600px; background: linear-gradient(135deg, #1a0a1a 0%, #0d0d0d 100%); border-radius: 12px; overflow: hidden; border: 1px solid #D4AF3733;">
                    <tr>
                        <td style="padding: 40px;">
                            <h2 style="margin: 0 0 20px; font-size: 24px; color: #D4AF37; font-weight: 600;">Hey {{first_name}},</h2>
                            
                            <p style="margin: 0 0 30px; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                Your MEDIUM Kit includes <strong style="color: #D4AF37;">automation workflow blueprints</strong>:
                            </p>
                            
                            <!-- Automation Workflows -->
                            <h3 style="margin: 0 0 20px; font-size: 18px; color: #ffffff; font-weight: 600;">3 Workflows Included:</h3>
                            
                            <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-bottom: 30px;">
                                <tr>
                                    <td style="padding: 20px; background-color: #1a1a1a; border-radius: 8px; margin-bottom: 15px;">
                                        <p style="margin: 0 0 10px; font-size: 16px; color: #D4AF37; font-weight: 600;">🔔 New Lead Welcome</p>
                                        <p style="margin: 0; font-size: 14px; color: #b0b0b0; line-height: 1.6;">Triggered: When someone opts in<br>Action: Delivers lead magnet + starts nurture sequence<br>Result: Warmed-up prospect ready to buy</p>
                                    </td>
                                </tr>
                                <tr><td height="15"></td></tr>
                                <tr>
                                    <td style="padding: 20px; background-color: #1a1a1a; border-radius: 8px;">
                                        <p style="margin: 0 0 10px; font-size: 16px; color: #D4AF37; font-weight: 600;">🛒 Cart Abandonment Recovery</p>
                                        <p style="margin: 0; font-size: 14px; color: #b0b0b0; line-height: 1.6;">Triggered: When someone adds to cart but doesn't buy<br>Action: 3-email recovery sequence<br>Result: Recovers 15-25% of lost sales</p>
                                    </td>
                                </tr>
                                <tr><td height="15"></td></tr>
                                <tr>
                                    <td style="padding: 20px; background-color: #1a1a1a; border-radius: 8px;">
                                        <p style="margin: 0 0 10px; font-size: 16px; color: #D4AF37; font-weight: 600;">📈 Post-Purchase Upsell</p>
                                        <p style="margin: 0; font-size: 14px; color: #b0b0b0; line-height: 1.6;">Triggered: After customer completes purchase<br>Action: Presents complementary offer<br>Result: 30% increase in average order value</p>
                                    </td>
                                </tr>
                            </table>
                            
                            <p style="margin: 0; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                Set these up once. They work forever.
                            </p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
```

### CTA:
No primary CTA (education-focused)

---

## Email 4: Business Templates Showcase

**Timing:** 5 days after purchase  
**Trigger:** Tag `funnel:medium` + 5 days delay

### Subject Lines (A/B/C):
```
A: Templates that save 10+ hours/month 📄
B: The business docs you didn't know you needed
C: Contracts, proposals & pricing made easy
```

### Preview Text:
```
Stop reinventing the wheel for every client interaction...
```

### Email Body:
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Business Templates</title>
</head>
<body style="margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #0a0a0a; color: #ffffff;">
    <table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color: #0a0a0a;">
        <tr>
            <td align="center" style="padding: 40px 20px;">
                <table width="600" cellpadding="0" cellspacing="0" border="0" style="max-width: 600px; background: linear-gradient(135deg, #1a0a1a 0%, #0d0d0d 100%); border-radius: 12px; overflow: hidden; border: 1px solid #D4AF3733;">
                    <tr>
                        <td style="padding: 40px;">
                            <h2 style="margin: 0 0 20px; font-size: 24px; color: #D4AF37; font-weight: 600;">Hey {{first_name}},</h2>
                            
                            <p style="margin: 0 0 30px; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                Your MEDIUM Kit includes templates for the unglamorous (but crucial) stuff:
                            </p>
                            
                            <!-- Templates Grid -->
                            <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-bottom: 30px;">
                                <tr>
                                    <td width="48%" valign="top" style="padding: 20px; background-color: #1a1a1a; border-radius: 8px;">
                                        <p style="margin: 0 0 10px; font-size: 24px;">📋</p>
                                        <h4 style="margin: 0 0 8px; font-size: 15px; color: #D4AF37;">Client Contract</h4>
                                        <p style="margin: 0; font-size: 13px; color: #b0b0b0; line-height: 1.5;">Protect your work and get paid on time. Fully customizable.</p>
                                    </td>
                                    <td width="4%"></td>
                                    <td width="48%" valign="top" style="padding: 20px; background-color: #1a1a1a; border-radius: 8px;">
                                        <p style="margin: 0 0 10px; font-size: 24px;">📊</p>
                                        <h4 style="margin: 0 0 8px; font-size: 15px; color: #D4AF37;">Project Proposal</h4>
                                        <p style="margin: 0; font-size: 13px; color: #b0b0b0; line-height: 1.5;">Win more clients with professional, persuasive proposals.</p>
                                    </td>
                                </tr>
                                <tr><td height="15" colspan="3"></td></tr>
                                <tr>
                                    <td width="48%" valign="top" style="padding: 20px; background-color: #1a1a1a; border-radius: 8px;">
                                        <p style="margin: 0 0 10px; font-size: 24px;">💰</p>
                                        <h4 style="margin: 0 0 8px; font-size: 15px; color: #D4AF37;">Pricing Calculator</h4>
                                        <p style="margin: 0; font-size: 13px; color: #b0b0b0; line-height: 1.5;">Never undercharge again. Factors in all your costs + profit.</p>
                                    </td>
                                    <td width="4%"></td>
                                    <td width="48%" valign="top" style="padding: 20px; background-color: #1a1a1a; border-radius: 8px;">
                                        <p style="margin: 0 0 10px; font-size: 24px;">📧</p>
                                        <h4 style="margin: 0 0 8px; font-size: 15px; color: #D4AF37;">Client Onboarding</h4>
                                        <p style="margin: 0; font-size: 13px; color: #b0b0b0; line-height: 1.5;">Set expectations and collect info with one smooth process.</p>
                                    </td>
                                </tr>
                            </table>
                            
                            <p style="margin: 0; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                These templates alone can save you 10+ hours every month.
                            </p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
```

### CTA:
No primary CTA (value showcase)

---

## Email 5: PRO Kit Upgrade

**Timing:** 10 days after purchase  
**Trigger:** Tag `funnel:medium` + 10 days delay + no PRO purchase  
**Tag Applied:** `action:pitched-pro`

### Subject Lines (A/B/C):
```
A: Ready for the complete CashFlowLab system?
B: The 10-email sequence that changes everything
C: {{first_name}}, your invitation to PRO
```

### Preview Text:
```
For those ready to master email marketing completely...
```

### Email Body:
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PRO Kit Upgrade</title>
</head>
<body style="margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #0a0a0a; color: #ffffff;">
    <table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color: #0a0a0a;">
        <tr>
            <td align="center" style="padding: 40px 20px;">
                <table width="600" cellpadding="0" cellspacing="0" border="0" style="max-width: 600px; background: linear-gradient(135deg, #1a0a1a 0%, #0d0d0d 100%); border-radius: 12px; overflow: hidden; border: 1px solid #D4AF3733;">
                    <tr>
                        <td style="padding: 40px;">
                            <h2 style="margin: 0 0 20px; font-size: 24px; color: #D4AF37; font-weight: 600;">Hey {{first_name}},</h2>
                            
                            <p style="margin: 0 0 30px; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                You've been working with the MEDIUM Kit for 10 days now.
                            </p>
                            
                            <!-- Quote Box -->
                            <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin: 25px 0;">
                                <tr>
                                    <td style="padding: 25px; background: linear-gradient(135deg, #6B2D5C22 0%, #1a1a1a 100%); border-left: 4px solid #D4AF37; border-radius: 0 8px 8px 0;">
                                        <p style="margin: 0; font-size: 18px; line-height: 1.6; color: #ffffff; font-style: italic;">
                                            "What if you had the EXACT email sequences, checklist, and training that the most successful CashFlowLab users rely on?"
                                        </p>
                                    </td>
                                </tr>
                            </table>
                            
                            <p style="margin: 0 0 30px; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                That's what the <strong style="color: #D4AF37;">PRO Kit</strong> delivers.
                            </p>
                            
                            <!-- PRO Features -->
                            <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-bottom: 30px;">
                                <tr>
                                    <td style="padding: 30px; background: linear-gradient(135deg, #1a1a2e 0%, #0d0d1a 100%); border-radius: 12px; border: 2px solid #D4AF37;">
                                        <h3 style="margin: 0 0 20px; font-size: 20px; color: #D4AF37; text-align: center;">🌟 PRO Kit Includes:</h3>
                                        
                                        <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-bottom: 20px;">
                                            <tr><td style="padding: 15px 0; border-bottom: 1px solid #333;"><p style="margin: 0; font-size: 15px; color: #ffffff;"><strong style="color: #D4AF37;">10 Complete Email Sequences</strong><br><span style="font-size: 13px; color: #888888;">Welcome, nurture, launch, re-engagement — all copy-paste ready</span></p></td></tr>
                                            <tr><td style="padding: 15px 0; border-bottom: 1px solid #333;"><p style="margin: 0; font-size: 15px; color: #ffffff;"><strong style="color: #D4AF37;">Master Checklist (147 Steps)</strong><br><span style="font-size: 13px; color: #888888;">The exact process for building a profitable funnel from scratch</span></p></td></tr>
                                            <tr><td style="padding: 15px 0; border-bottom: 1px solid #333;"><p style="margin: 0; font-size: 15px; color: #ffffff;"><strong style="color: #D4AF37;">Video Training Course</strong><br><span style="font-size: 13px; color: #888888;">3+ hours of advanced strategy and implementation tutorials</span></p></td></tr>
                                            <tr><td style="padding: 15px 0;"><p style="margin: 0; font-size: 15px; color: #ffffff;"><strong style="color: #D4AF37;">Advanced Automation Blueprints</strong><br><span style="font-size: 13px; color: #888888;">Segmentation, tagging, and advanced workflows</span></p></td></tr>
                                        </table>
                                        
                                        <table width="100%" cellpadding="0" cellspacing="0" border="0">
                                            <tr>
                                                <td style="padding: 20px; background: linear-gradient(135deg, #6B2D5C 0%, #4B1D3C 100%); border-radius: 8px; text-align: center;">
                                                    <p style="margin: 0 0 10px; font-size: 14px; color: #D4AF37;">MEDIUM Kit Customer Price</p>
                                                    <p style="margin: 0 0 20px; font-size: 36px; color: #ffffff; font-weight: 700;">$39</p>
                                                    <a href="{{pro_kit_checkout}}" style="display: inline-block; padding: 18px 40px; background: linear-gradient(90deg, #D4AF37 0%, #B8941F 100%); color: #0a0a0a; text-decoration: none; font-weight: 700; font-size: 16px; border-radius: 8px; text-transform: uppercase;">Upgrade to PRO →</a>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
                            
                            <p style="margin: 0; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                Think about it. No pressure.
                            </p>
                            
                            <p style="margin: 20px 0 0; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                — The CashFlowLab Team
                            </p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
```

### Plain Text Version:
```
Hey {{first_name}},

You've been working with the MEDIUM Kit for 10 days now.

"What if you had the EXACT email sequences, checklist, and training that the most successful CashFlowLab users rely on?"

That's what the PRO Kit delivers.

---
🌟 PRO KIT INCLUDES:

10 Complete Email Sequences
Welcome, nurture, launch, re-engagement — all copy-paste ready

Master Checklist (147 Steps)
The exact process for building a profitable funnel

Video Training Course
3+ hours of advanced strategy tutorials

Advanced Automation Blueprints
Segmentation, tagging, and advanced workflows

---
MEDIUM Kit Customer Price: $39

Upgrade: {{pro_kit_checkout}}
---

Think about it. No pressure.

— The CashFlowLab Team

---
Unsubscribe: {{unsubscribe_url}}
```

### CTA:
**Primary:** "Upgrade to PRO →"  
**Link:** `{{pro_kit_checkout}}`

---

# 📧 SEQUENCE 4: PRO KIT PURCHASE SEQUENCE
**Trigger:** User purchases PRO Kit ($39)  
**Goal:** VIP onboarding → Community engagement → Testimonials  
**Duration:** 14 days

---

## Email 1: Confirmare + Acces Complet

**Timing:** Immediate after purchase  
**Trigger:** Purchase completed for PRO Kit  
**Tag Applied:** `funnel:pro`, `segment:vip`, `action:purchased`

### Subject Lines (A/B/C):
```
A: 🌟 Welcome to PRO, {{first_name}}! Full access inside
B: You've unlocked everything. Here's your access.
C: PRO Kit confirmed — your complete system awaits
```

### Email Body:
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PRO Kit Access</title>
</head>
<body style="margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #0a0a0a; color: #ffffff;">
    <table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color: #0a0a0a;">
        <tr>
            <td align="center" style="padding: 40px 20px;">
                <table width="600" cellpadding="0" cellspacing="0" border="0" style="max-width: 600px; background: linear-gradient(135deg, #1a0a1a 0%, #0d0d0d 100%); border-radius: 12px; overflow: hidden; border: 2px solid #D4AF37;">
                    <tr>
                        <td style="padding: 40px; text-align: center;">
                            <div style="width: 80px; height: 80px; background: linear-gradient(135deg, #D4AF37 0%, #B8941F 100%); border-radius: 50%; margin: 0 auto 30px; line-height: 80px; font-size: 40px; color: #0a0a0a; font-weight: 700;">PRO</div>
                            
                            <h1 style="margin: 0 0 15px; font-size: 28px; color: #D4AF37; font-weight: 700;">Welcome to PRO!</h1>
                            
                            <p style="margin: 0 0 30px; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                Hey {{first_name}}, you now have access to the complete CashFlowLab system.
                            </p>
                        </td>
                    </tr>
                    
                    <tr>
                        <td style="padding: 0 40px 40px;">
                            <!-- Access Box -->
                            <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-bottom: 30px;">
                                <tr>
                                    <td style="padding: 30px; background: linear-gradient(135deg, #6B2D5C 0%, #4B1D3C 100%); border-radius: 12px; text-align: center;">
                                        <a href="{{pro_kit_member_area}}" style="display: inline-block; padding: 18px 40px; background: linear-gradient(90deg, #D4AF37 0%, #B8941F 100%); color: #0a0a0a; text-decoration: none; font-weight: 700; font-size: 16px; border-radius: 8px; text-transform: uppercase;">Access Your PRO Kit</a>
                                    </td>
                                </tr>
                            </table>
                            
                            <h3 style="margin: 0 0 20px; font-size: 20px; color: #ffffff; font-weight: 600;">Everything included:</h3>
                            
                            <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-bottom: 30px;">
                                <tr>
                                    <td style="padding: 15px; background-color: #1a1a1a; border-left: 3px solid #D4AF37; border-radius: 0 8px 8px 0; margin-bottom: 10px;">
                                        <p style="margin: 0; font-size: 15px; color: #ffffff;">✓ 10 Complete Email Sequences</p>
                                    </td>
                                </tr>
                                <tr><td height="10"></td></tr>
                                <tr>
                                    <td style="padding: 15px; background-color: #1a1a1a; border-left: 3px solid #6B2D5C; border-radius: 0 8px 8px 0;">
                                        <p style="margin: 0; font-size: 15px; color: #ffffff;">✓ Master Checklist (147 Steps)</p>
                                    </td>
                                </tr>
                                <tr><td height="10"></td></tr>
                                <tr>
                                    <td style="padding: 15px; background-color: #1a1a1a; border-left: 3px solid #D4AF37; border-radius: 0 8px 8px 0;">
                                        <p style="margin: 0; font-size: 15px; color: #ffffff;">✓ Video Training Course (3+ hours)</p>
                                    </td>
                                </tr>
                                <tr><td height="10"></td></tr>
                                <tr>
                                    <td style="padding: 15px; background-color: #1a1a1a; border-left: 3px solid #6B2D5C; border-radius: 0 8px 8px 0;">
                                        <p style="margin: 0; font-size: 15px; color: #ffffff;">✓ Advanced Automation Blueprints</p>
                                    </td>
                                </tr>
                                <tr><td height="10"></td></tr>
                                <tr>
                                    <td style="padding: 15px; background-color: #1a1a1a; border-left: 3px solid #D4AF37; border-radius: 0 8px 8px 0;">
                                        <p style="margin: 0; font-size: 15px; color: #ffffff;">✓ Priority Email Support</p>
                                    </td>
                                </tr>
                            </table>
                            
                            <p style="margin: 0; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                To your success,<br>
                                <strong style="color: #D4AF37;">The CashFlowLab Team</strong>
                            </p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
```

### CTA:
**Primary:** "Access Your PRO Kit"  
**Link:** `{{pro_kit_member_area}}`

---

## Email 2: Priority Support + Community

**Timing:** 24 hours after purchase  
**Trigger:** Tag `funnel:pro` + 24h delay

### Subject Lines (A/B/C):
```
A: Your PRO support channels are open 🎧
B: Welcome to the inner circle, {{first_name}}
C: PRO perks: Support + community access
```

### Email Body:
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PRO Support</title>
</head>
<body style="margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #0a0a0a; color: #ffffff;">
    <table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color: #0a0a0a;">
        <tr>
            <td align="center" style="padding: 40px 20px;">
                <table width="600" cellpadding="0" cellspacing="0" border="0" style="max-width: 600px; background: linear-gradient(135deg, #1a0a1a 0%, #0d0d0d 100%); border-radius: 12px; overflow: hidden; border: 1px solid #D4AF3733;">
                    <tr>
                        <td style="padding: 40px;">
                            <h2 style="margin: 0 0 20px; font-size: 24px; color: #D4AF37; font-weight: 600;">Hey {{first_name}},</h2>
                            
                            <p style="margin: 0 0 30px; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                As a PRO member, you have access to priority support.
                            </p>
                            
                            <!-- Support Options -->
                            <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-bottom: 30px;">
                                <tr>
                                    <td style="padding: 25px; background-color: #1a1a1a; border-radius: 8px; border-left: 4px solid #D4AF37;">
                                        <h3 style="margin: 0 0 10px; font-size: 18px; color: #D4AF37;">📧 Priority Email Support</h3>
                                        <p style="margin: 0; font-size: 15px; color: #b0b0b0;">Get answers within 24 hours. Reply to any email or contact support@cashflowlabai.com</p>
                                    </td>
                                </tr>
                                <tr><td height="15"></td></tr>
                                <tr>
                                    <td style="padding: 25px; background-color: #1a1a1a; border-radius: 8px; border-left: 4px solid #6B2D5C;">
                                        <h3 style="margin: 0 0 10px; font-size: 18px; color: #6B2D5C;">👥 PRO Community</h3>
                                        <p style="margin: 0; font-size: 15px; color: #b0b0b0;">Join other PRO members: {{community_link}}</p>
                                    </td>
                                </tr>
                            </table>
                            
                            <p style="margin: 0; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                We're here to help you succeed.<br>
                                <strong style="color: #D4AF37;">The CashFlowLab Team</strong>
                            </p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
```

---

## Email 3: Master Checklist Walkthrough

**Timing:** 3 days after purchase  
**Trigger:** Tag `funnel:pro` + 3 days delay

### Subject Lines (A/B/C):
```
A: How to use the 147-step master checklist ✅
B: Your complete funnel roadmap inside
C: The checklist that eliminates guesswork
```

### Email Body:
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Master Checklist</title>
</head>
<body style="margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #0a0a0a; color: #ffffff;">
    <table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color: #0a0a0a;">
        <tr>
            <td align="center" style="padding: 40px 20px;">
                <table width="600" cellpadding="0" cellspacing="0" border="0" style="max-width: 600px; background: linear-gradient(135deg, #1a0a1a 0%, #0d0d0d 100%); border-radius: 12px; overflow: hidden; border: 1px solid #D4AF3733;">
                    <tr>
                        <td style="padding: 40px;">
                            <h2 style="margin: 0 0 20px; font-size: 24px; color: #D4AF37; font-weight: 600;">Hey {{first_name}},</h2>
                            
                            <p style="margin: 0 0 30px; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                The <strong style="color: #D4AF37;">Master Checklist (147 steps)</strong> is your complete funnel-building roadmap.
                            </p>
                            
                            <!-- Checklist Breakdown -->
                            <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-bottom: 30px;">
                                <tr>
                                    <td style="padding: 20px; background: linear-gradient(135deg, #6B2D5C 0%, #4B1D3C 100%); border-radius: 8px; text-align: center;">
                                        <p style="margin: 0; font-size: 48px; color: #ffffff; font-weight: 700;">147</p>
                                        <p style="margin: 5px 0 0; font-size: 14px; color: #D4AF37;">Steps to Cashflow Success</p>
                                    </td>
                                </tr>
                            </table>
                            
                            <p style="margin: 0 0 20px; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                Organized into 7 phases:
                            </p>
                            
                            <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-bottom: 30px;">
                                <tr><td style="padding: 12px; background-color: #1a1a1a; border-radius: 8px; margin-bottom: 8px;"><p style="margin: 0; font-size: 14px; color: #ffffff;">✓ Phase 1: Foundation Setup (Steps 1-21)</p></td></tr>
                                <tr><td height="8"></td></tr>
                                <tr><td style="padding: 12px; background-color: #1a1a1a; border-radius: 8px;"><p style="margin: 0; font-size: 14px; color: #ffffff;">✓ Phase 2: Offer Creation (Steps 22-42)</p></td></tr>
                                <tr><td height="8"></td></tr>
                                <tr><td style="padding: 12px; background-color: #1a1a1a; border-radius: 8px;"><p style="margin: 0; font-size: 14px; color: #ffffff;">✓ Phase 3: Funnel Building (Steps 43-84)</p></td></tr>
                                <tr><td height="8"></td></tr>
                                <tr><td style="padding: 12px; background-color: #1a1a1a; border-radius: 8px;"><p style="margin: 0; font-size: 14px; color: #ffffff;">✓ Phase 4: Email Sequences (Steps 85-105)</p></td></tr>
                                <tr><td height="8"></td></tr>
                                <tr><td style="padding: 12px; background-color: #1a1a1a; border-radius: 8px;"><p style="margin: 0; font-size: 14px; color: #ffffff;">✓ Phase 5: Automation Setup (Steps 106-126)</p></td></tr>
                                <tr><td height="8"></td></tr>
                                <tr><td style="padding: 12px; background-color: #1a1a1a; border-radius: 8px;"><p style="margin: 0; font-size: 14px; color: #ffffff;">✓ Phase 6: Testing & Launch (Steps 127-140)</p></td></tr>
                                <tr><td height="8"></td></tr>
                                <tr><td style="padding: 12px; background-color: #1a1a1a; border-radius: 8px;"><p style="margin: 0; font-size: 14px; color: #ffffff;">✓ Phase 7: Optimization (Steps 141-147)</p></td></tr>
                            </table>
                            
                            <p style="margin: 0; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                Check off each step as you complete it. No guesswork, no overwhelm — just follow the path.
                            </p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
```

---

## Email 4: Strategy Call Booking

**Timing:** 7 days after purchase  
**Trigger:** Tag `funnel:pro` + 7 days delay

### Subject Lines (A/B/C):
```
A: Book your strategy call, {{first_name}} 📞
B: Let's talk strategy — your call link inside
C: 15 minutes that could transform your funnel
```

### Email Body:
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Strategy Call</title>
</head>
<body style="margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #0a0a0a; color: #ffffff;">
    <table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color: #0a0a0a;">
        <tr>
            <td align="center" style="padding: 40px 20px;">
                <table width="600" cellpadding="0" cellspacing="0" border="0" style="max-width: 600px; background: linear-gradient(135deg, #1a0a1a 0%, #0d0d0d 100%); border-radius: 12px; overflow: hidden; border: 1px solid #D4AF3733;">
                    <tr>
                        <td style="padding: 40px;">
                            <h2 style="margin: 0 0 20px; font-size: 24px; color: #D4AF37; font-weight: 600;">Hey {{first_name}},</h2>
                            
                            <p style="margin: 0 0 20px; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                You've had the PRO Kit for a week now. How's the implementation going?
                            </p>
                            
                            <p style="margin: 0 0 30px; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                As a PRO member, you can book a complimentary 15-minute strategy call.
                            </p>
                            
                            <!-- CTA Box -->
                            <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-bottom: 30px;">
                                <tr>
                                    <td style="padding: 30px; background: linear-gradient(135deg, #6B2D5C 0%, #4B1D3C 100%); border-radius: 12px; text-align: center;">
                                        <p style="margin: 0 0 15px; font-size: 18px; color: #ffffff; font-weight: 600;">Book Your Strategy Call</p>
                                        <p style="margin: 0 0 20px; font-size: 14px; color: #b0b0b0;">15 minutes | 1-on-1 | Custom advice for your situation</p>
                                        <a href="{{strategy_call_booking_link}}" style="display: inline-block; padding: 18px 40px; background: linear-gradient(90deg, #D4AF37 0%, #B8941F 100%); color: #0a0a0a; text-decoration: none; font-weight: 700; font-size: 16px; border-radius: 8px; text-transform: uppercase;">Book My Call →</a>
                                    </td>
                                </tr>
                            </table>
                            
                            <p style="margin: 0; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                Looking forward to talking,<br>
                                <strong style="color: #D4AF37;">The CashFlowLab Team</strong>
                            </p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
```

### CTA:
**Primary:** "Book My Call →"  
**Link:** `{{strategy_call_booking_link}}`

---

## Email 5: Advanced Tips + Testimonial Request

**Timing:** 14 days after purchase  
**Trigger:** Tag `funnel:pro` + 14 days delay

### Subject Lines (A/B/C):
```
A: Advanced tips for PRO members only 🔐
B: Your funnel 2 weeks in + one small favor
C: {{first_name}}, quick check-in + request
```

### Preview Text:
```
Plus: Would you share your experience?
```

### Email Body:
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Advanced Tips</title>
</head>
<body style="margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #0a0a0a; color: #ffffff;">
    <table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color: #0a0a0a;">
        <tr>
            <td align="center" style="padding: 40px 20px;">
                <table width="600" cellpadding="0" cellspacing="0" border="0" style="max-width: 600px; background: linear-gradient(135deg, #1a0a1a 0%, #0d0d0d 100%); border-radius: 12px; overflow: hidden; border: 1px solid #D4AF3733;">
                    <tr>
                        <td style="padding: 40px;">
                            <h2 style="margin: 0 0 20px; font-size: 24px; color: #D4AF37; font-weight: 600;">Hey {{first_name}},</h2>
                            
                            <p style="margin: 0 0 20px; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                Two weeks with the PRO Kit! Here are 3 advanced tips:
                            </p>
                            
                            <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-bottom: 30px;">
                                <tr>
                                    <td style="padding: 20px; background-color: #1a1a1a; border-radius: 8px; margin-bottom: 10px;">
                                        <p style="margin: 0 0 8px; font-size: 16px; color: #D4AF37; font-weight: 600;">1. Segment by engagement</p>
                                        <p style="margin: 0; font-size: 14px; color: #b0b0b0;">Tag subscribers based on open rates and send different content to hot vs. cold leads.</p>
                                    </td>
                                </tr>
                                <tr><td height="10"></td></tr>
                                <tr>
                                    <td style="padding: 20px; background-color: #1a1a1a; border-radius: 8px; margin-bottom: 10px;">
                                        <p style="margin: 0 0 8px; font-size: 16px; color: #D4AF37; font-weight: 600;">2. A/B test subject lines</p>
                                        <p style="margin: 0; font-size: 14px; color: #b0b0b0;">Always test 2 subject lines. Even a 5% lift compounds over time.</p>
                                    </td>
                                </tr>
                                <tr><td height="10"></td></tr>
                                <tr>
                                    <td style="padding: 20px; background-color: #1a1a1a; border-radius: 8px;">
                                        <p style="margin: 0 0 8px; font-size: 16px; color: #D4AF37; font-weight: 600;">3. Set up lead scoring</p>
                                        <p style="margin: 0; font-size: 14px; color: #b0b0b0;">Track opens, clicks, and site visits to identify your hottest prospects.</p>
                                    </td>
                                </tr>
                            </table>
                            
                            <!-- Testimonial Request -->
                            <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-bottom: 30px;">
                                <tr>
                                    <td style="padding: 25px; background: linear-gradient(135deg, #6B2D5C22 0%, #1a1a1a 100%); border-left: 4px solid #D4AF37; border-radius: 0 8px 8px 0;">
                                        <p style="margin: 0 0 15px; font-size: 16px; color: #ffffff; font-weight: 600;">One small favor...</p>
                                        <p style="margin: 0 0 20px; font-size: 14px; color: #b0b0b0; line-height: 1.6;">If you've found value in the PRO Kit, would you share a quick testimonial? It helps other entrepreneurs discover CashFlowLab.</p>
                                        <a href="{{testimonial_form_link}}" style="display: inline-block; padding: 12px 30px; background: linear-gradient(90deg, #D4AF37 0%, #B8941F 100%); color: #0a0a0a; text-decoration: none; font-weight: 600; font-size: 14px; border-radius: 6px;">Share Your Experience →</a>
                                    </td>
                                </tr>
                            </table>
                            
                            <p style="margin: 0; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                Keep building,<br>
                                <strong style="color: #D4AF37;">The CashFlowLab Team</strong>
                            </p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
```

### Plain Text Version:
```
Hey {{first_name}},

Two weeks with the PRO Kit! Here are 3 advanced tips:

1. SEGMENT BY ENGAGEMENT
Tag subscribers based on open rates and send different content to hot vs. cold leads.

2. A/B TEST SUBJECT LINES
Always test 2 subject lines. Even a 5% lift compounds over time.

3. SET UP LEAD SCORING
Track opens, clicks, and site visits to identify your hottest prospects.

---
ONE SMALL FAVOR...

If you've found value in the PRO Kit, would you share a quick testimonial?
It helps other entrepreneurs discover CashFlowLab.

Share here: {{testimonial_form_link}}

Keep building,
The CashFlowLab Team

---
Unsubscribe: {{unsubscribe_url}}
```

### CTA:
**Primary:** "Share Your Experience →"  
**Link:** `{{testimonial_form_link}}`

---

# 📧 SEQUENCE 5: ABANDONED CART SEQUENCE
**Trigger:** User adds product to cart but doesn't complete purchase  
**Goal:** Recover lost sales  
**Duration:** 48 hours

---

## Email 1: Friendly Reminder

**Timing:** 1 hour after cart abandonment  
**Trigger:** Cart abandoned + 1h delay  
**Tag Applied:** `action:cart-abandoned`

### Subject Lines (A/B/C):
```
A: Did something go wrong?
B: {{first_name}}, you left something behind...
C: Quick reminder about your cart
```

### Preview Text:
```
Your items are still waiting for you...
```

### Email Body:
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cart Reminder</title>
</head>
<body style="margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #0a0a0a; color: #ffffff;">
    <table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color: #0a0a0a;">
        <tr>
            <td align="center" style="padding: 40px 20px;">
                <table width="600" cellpadding="0" cellspacing="0" border="0" style="max-width: 600px; background: linear-gradient(135deg, #1a0a1a 0%, #0d0d0d 100%); border-radius: 12px; overflow: hidden; border: 1px solid #D4AF3733;">
                    <tr>
                        <td style="padding: 40px;">
                            <h2 style="margin: 0 0 20px; font-size: 24px; color: #D4AF37; font-weight: 600;">Hey {{first_name}},</h2>
                            
                            <p style="margin: 0 0 20px; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                I noticed you were interested in the {{cart_product_name}} but didn't complete your purchase.
                            </p>
                            
                            <p style="margin: 0 0 30px; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                Did something go wrong? Technical issue? Question I can answer?
                            </p>
                            
                            <!-- Cart Items -->
                            <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-bottom: 30px;">
                                <tr>
                                    <td style="padding: 20px; background-color: #1a1a1a; border-radius: 8px;">
                                        <p style="margin: 0 0 10px; font-size: 16px; color: #ffffff; font-weight: 600;">In your cart:</p>
                                        <p style="margin: 0 0 15px; font-size: 18px; color: #D4AF37;">{{cart_product_name}} — ${{cart_product_price}}</p>
                                        <a href="{{cart_recovery_link}}" style="display: inline-block; padding: 15px 35px; background: linear-gradient(90deg, #D4AF37 0%, #B8941F 100%); color: #0a0a0a; text-decoration: none; font-weight: 700; font-size: 15px; border-radius: 8px;">Complete My Purchase →</a>
                                    </td>
                                </tr>
                            </table>
                            
                            <p style="margin: 0; font-size: 14px; color: #888888;">
                                Your cart is saved for 48 hours.
                            </p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
```

### CTA:
**Primary:** "Complete My Purchase →"  
**Link:** `{{cart_recovery_link}}`

---

## Email 2: Bonus Offer / Objection Handler

**Timing:** 24 hours after abandonment  
**Trigger:** Tag `action:cart-abandoned` + 24h delay + no purchase

### Subject Lines (A/B/C):
```
A: Still thinking it over? Here's a little nudge...
B: One question about your cart
C: {{first_name}}, quick question...
```

### Preview Text:
```
What's holding you back? (Seriously, I'd love to know)
```

### Email Body:
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cart Recovery - Bonus</title>
</head>
<body style="margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #0a0a0a; color: #ffffff;">
    <table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color: #0a0a0a;">
        <tr>
            <td align="center" style="padding: 40px 20px;">
                <table width="600" cellpadding="0" cellspacing="0" border="0" style="max-width: 600px; background: linear-gradient(135deg, #1a0a1a 0%, #0d0d0d 100%); border-radius: 12px; overflow: hidden; border: 1px solid #D4AF3733;">
                    <tr>
                        <td style="padding: 40px;">
                            <h2 style="margin: 0 0 20px; font-size: 24px; color: #D4AF37; font-weight: 600;">Hey {{first_name}},</h2>
                            
                            <p style="margin: 0 0 20px; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                Quick question: What's holding you back from grabbing the {{cart_product_name}}?
                            </p>
                            
                            <p style="margin: 0 0 20px; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                Is it:
                            </p>
                            
                            <ul style="margin: 0 0 25px; padding-left: 25px; color: #e0e0e0;">
                                <li style="margin-bottom: 10px; font-size: 15px;">The price?</li>
                                <li style="margin-bottom: 10px; font-size: 15px;">Not sure if it's right for you?</li>
                                <li style="margin-bottom: 10px; font-size: 15px;">Technical concerns?</li>
                                <li style="font-size: 15px;">Something else entirely?</li>
                            </ul>
                            
                            <p style="margin: 0 0 30px; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                Hit reply and let me know. I read every response and I'm happy to help.
                            </p>
                            
                            <!-- Recovery CTA -->
                            <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-bottom: 30px;">
                                <tr>
                                    <td style="padding: 25px; background-color: #1a1a1a; border-radius: 8px; text-align: center;">
                                        <p style="margin: 0 0 15px; font-size: 16px; color: #ffffff; font-weight: 600;">Still interested?</p>
                                        <a href="{{cart_recovery_link}}" style="display: inline-block; padding: 15px 35px; background: linear-gradient(90deg, #D4AF37 0%, #B8941F 100%); color: #0a0a0a; text-decoration: none; font-weight: 700; font-size: 15px; border-radius: 8px;">Complete My Purchase →</a>
                                    </td>
                                </tr>
                            </table>
                            
                            <p style="margin: 0; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                — The CashFlowLab Team
                            </p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
```

### CTA:
**Primary:** "Complete My Purchase →"  
**Link:** `{{cart_recovery_link}}`

---

## Email 3: Last Chance

**Timing:** 48 hours after abandonment  
**Trigger:** Tag `action:cart-abandoned` + 48h delay + no purchase

### Subject Lines (A/B/C):
```
A: Final reminder: Your cart expires soon
B: Last call, {{first_name}} ⏰
C: About your cart...
```

### Preview Text:
```
Your items will be released in a few hours...
```

### Email Body:
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cart Expiring</title>
</head>
<body style="margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #0a0a0a; color: #ffffff;">
    <table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color: #0a0a0a;">
        <tr>
            <td align="center" style="padding: 40px 20px;">
                <table width="600" cellpadding="0" cellspacing="0" border="0" style="max-width: 600px; background: linear-gradient(135deg, #1a0a1a 0%, #0d0d0d 100%); border-radius: 12px; overflow: hidden; border: 1px solid #D4AF3733;">
                    <tr>
                        <td style="padding: 40px;">
                            <h2 style="margin: 0 0 20px; font-size: 24px; color: #D4AF37; font-weight: 600;">Hey {{first_name}},</h2>
                            
                            <p style="margin: 0 0 20px; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                This is my final email about your cart.
                            </p>
                            
                            <p style="margin: 0 0 30px; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                The {{cart_product_name}} will be released soon, and I don't want you to miss out if you're still interested.
                            </p>
                            
                            <!-- Final CTA -->
                            <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-bottom: 30px;">
                                <tr>
                                    <td style="padding: 30px; background: linear-gradient(135deg, #6B2D5C 0%, #4B1D3C 100%); border-radius: 12px; text-align: center; border: 2px solid #D4AF37;">
                                        <p style="margin: 0 0 15px; font-size: 18px; color: #ffffff; font-weight: 600;">Last Chance</p>
                                        <p style="margin: 0 0 20px; font-size: 14px; color: #b0b0b0;">{{cart_product_name}} — ${{cart_product_price}}</p>
                                        <a href="{{cart_recovery_link}}" style="display: inline-block; padding: 18px 40px; background: linear-gradient(90deg, #D4AF37 0%, #B8941F 100%); color: #0a0a0a; text-decoration: none; font-weight: 700; font-size: 16px; border-radius: 8px; text-transform: uppercase;">Complete Purchase Now →</a>
                                    </td>
                                </tr>
                            </table>
                            
                            <p style="margin: 0; font-size: 14px; color: #888888; text-align: center;">
                                If you're not interested, no worries. I won't email you about this again.
                            </p>
                            
                            <p style="margin: 20px 0 0; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                — The CashFlowLab Team
                            </p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
```

### CTA:
**Primary:** "Complete Purchase Now →"  
**Link:** `{{cart_recovery_link}}`

---

# 📧 SEQUENCE 6: RE-ENGAGEMENT SEQUENCE
**Trigger:** User hasn't opened emails in 30 days  
**Goal:** Win back cold subscribers or clean list  
**Duration:** 15 days (emails at day 30, 37, 45)

---

## Email 1: "We Miss You" + Value

**Timing:** 30 days after last open/click  
**Trigger:** Tag `engagement:cold` (no open in 30 days)

### Subject Lines (A/B/C):
```
A: We miss you, {{first_name}} 💔
B: Is this goodbye?
C: One last try...
```

### Preview Text:
```
We haven't heard from you in a while...
```

### Email Body:
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>We Miss You</title>
</head>
<body style="margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #0a0a0a; color: #ffffff;">
    <table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color: #0a0a0a;">
        <tr>
            <td align="center" style="padding: 40px 20px;">
                <table width="600" cellpadding="0" cellspacing="0" border="0" style="max-width: 600px; background: linear-gradient(135deg, #1a0a1a 0%, #0d0d0d 100%); border-radius: 12px; overflow: hidden; border: 1px solid #D4AF3733;">
                    <tr>
                        <td style="padding: 40px; text-align: center;">
                            <p style="margin: 0 0 20px; font-size: 48px;">💔</p>
                            
                            <h2 style="margin: 0 0 20px; font-size: 24px; color: #D4AF37; font-weight: 600;">We miss you, {{first_name}}</h2>
                            
                            <p style="margin: 0 0 20px; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                We noticed you haven't opened our emails in a while.
                            </p>
                            
                            <p style="margin: 0 0 30px; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                Maybe you're busy. Maybe our content isn't hitting the mark. Either way, we want to make sure you're getting value.
                            </p>
                            
                            <p style="margin: 0 0 30px; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                Here's a fresh resource — our most popular guide on building a cashflow system:
                            </p>
                            
                            <a href="{{reengagement_gift_link}}" style="display: inline-block; padding: 15px 35px; background: linear-gradient(90deg, #D4AF37 0%, #B8941F 100%); color: #0a0a0a; text-decoration: none; font-weight: 700; font-size: 15px; border-radius: 8px;">Get the Free Guide →</a>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
```

### CTA:
**Primary:** "Get the Free Guide →"  
**Link:** `{{reengagement_gift_link}}`

---

## Email 2: Survey + Special Offer

**Timing:** 37 days after last open/click  
**Trigger:** Tag `engagement:cold` + 7 days from Email 1 + no engagement

### Subject Lines (A/B/C):
```
A: 30 seconds + a special offer inside 🎁
B: Help us improve (and get something special)
C: {{first_name}}, your opinion matters
```

### Preview Text:
```
Quick survey + exclusive offer for returning subscribers...
```

### Email Body:
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quick Survey</title>
</head>
<body style="margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #0a0a0a; color: #ffffff;">
    <table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color: #0a0a0a;">
        <tr>
            <td align="center" style="padding: 40px 20px;">
                <table width="600" cellpadding="0" cellspacing="0" border="0" style="max-width: 600px; background: linear-gradient(135deg, #1a0a1a 0%, #0d0d0d 100%); border-radius: 12px; overflow: hidden; border: 1px solid #D4AF3733;">
                    <tr>
                        <td style="padding: 40px;">
                            <h2 style="margin: 0 0 20px; font-size: 24px; color: #D4AF37; font-weight: 600;">Quick question, {{first_name}}...</h2>
                            
                            <p style="margin: 0 0 30px; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                What would make our emails worth opening again?
                            </p>
                            
                            <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-bottom: 30px;">
                                <tr><td style="padding: 12px; background-color: #1a1a1a; border-radius: 8px; margin-bottom: 8px;"><p style="margin: 0; font-size: 14px; color: #ffffff;">📝 <a href="{{survey_link}}?answer=templates" style="color: #D4AF37; text-decoration: none;">More templates and resources</a></p></td></tr>
                                <tr><td height="8"></td></tr>
                                <tr><td style="padding: 12px; background-color: #1a1a1a; border-radius: 8px; margin-bottom: 8px;"><p style="margin: 0; font-size: 14px; color: #ffffff;">📝 <a href="{{survey_link}}?answer=case_studies" style="color: #D4AF37; text-decoration: none;">More case studies and examples</a></p></td></tr>
                                <tr><td height="8"></td></tr>
                                <tr><td style="padding: 12px; background-color: #1a1a1a; border-radius: 8px; margin-bottom: 8px;"><p style="margin: 0; font-size: 14px; color: #ffffff;">📝 <a href="{{survey_link}}?answer=less_emails" style="color: #D4AF37; text-decoration: none;">Fewer emails, less often</a></p></td></tr>
                                <tr><td height="8"></td></tr>
                                <tr><td style="padding: 12px; background-color: #1a1a1a; border-radius: 8px;"><p style="margin: 0; font-size: 14px; color: #ffffff;">📝 <a href="{{survey_link}}?answer=other" style="color: #D4AF37; text-decoration: none;">Something else (hit reply and tell us!)</a></p></td></tr>
                            </table>
                            
                            <p style="margin: 0; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                As a thank you, here's a special discount: <strong style="color: #D4AF37;">{{discount_code}} for 20% off any kit</strong>.
                            </p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
```

### CTA:
**Primary:** Survey options (click-based)  
**Link:** `{{survey_link}}`

---

## Email 3: Final Attempt + Unsubscribe Option

**Timing:** 45 days after last open/click  
**Trigger:** Tag `engagement:cold` + 8 days from Email 2 + no engagement

### Subject Lines (A/B/C):
```
A: Should we keep you on the list?
B: Final email: Unsubscribe link inside
C: One click to stay or go...
```

### Preview Text:
```
We don't want to clutter your inbox if you're not interested...
```

### Email Body:
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Final Email</title>
</head>
<body style="margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #0a0a0a; color: #ffffff;">
    <table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color: #0a0a0a;">
        <tr>
            <td align="center" style="padding: 40px 20px;">
                <table width="600" cellpadding="0" cellspacing="0" border="0" style="max-width: 600px; background: linear-gradient(135deg, #1a0a1a 0%, #0d0d0d 100%); border-radius: 12px; overflow: hidden; border: 1px solid #D4AF3733;">
                    <tr>
                        <td style="padding: 40px; text-align: center;">
                            <h2 style="margin: 0 0 20px; font-size: 24px; color: #D4AF37; font-weight: 600;">This is it, {{first_name}}</h2>
                            
                            <p style="margin: 0 0 20px; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                We haven't heard from you in over 45 days.
                            </p>
                            
                            <p style="margin: 0 0 30px; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                We don't want to clutter your inbox if our content isn't valuable to you anymore.
                            </p>
                            
                            <p style="margin: 0 0 30px; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                So here's the deal:
                            </p>
                            
                            <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-bottom: 30px;">
                                <tr>
                                    <td width="48%" style="padding: 20px; background: linear-gradient(135deg, #6B2D5C 0%, #4B1D3C 100%); border-radius: 8px; text-align: center;">
                                        <p style="margin: 0 0 15px; font-size: 16px; color: #ffffff; font-weight: 600;">Want to stay?</p>
                                        <a href="{{resubscribe_link}}" style="display: inline-block; padding: 12px 25px; background: linear-gradient(90deg, #D4AF37 0%, #B8941F 100%); color: #0a0a0a; text-decoration: none; font-weight: 600; font-size: 14px; border-radius: 6px;">Keep Me Subscribed</a>
                                    </td>
                                    <td width="4%"></td>
                                    <td width="48%" style="padding: 20px; background-color: #1a1a1a; border-radius: 8px; text-align: center; border: 1px solid #333;">
                                        <p style="margin: 0 0 15px; font-size: 16px; color: #888888;">Time to part ways?</p>
                                        <a href="{{unsubscribe_url}}" style="display: inline-block; padding: 12px 25px; background-color: #333; color: #ffffff; text-decoration: none; font-weight: 600; font-size: 14px; border-radius: 6px;">Unsubscribe</a>
                                    </td>
                                </tr>
                            </table>
                            
                            <p style="margin: 0; font-size: 14px; color: #888888;">
                                If you don't click either link, we'll automatically remove you from the list in a few days.
                            </p>
                            
                            <p style="margin: 20px 0 0; font-size: 16px; line-height: 1.7; color: #e0e0e0;">
                                No hard feelings either way.<br>
                                <strong style="color: #D4AF37;">The CashFlowLab Team</strong>
                            </p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
```

### CTA:
**Primary:** "Keep Me Subscribed" / "Unsubscribe"  
**Links:** `{{resubscribe_link}}` / `{{unsubscribe_url}}`

---

# 🛠️ MAILERLITE SETUP INSTRUCTIONS

## Step 1: Create Custom Fields

Go to **Subscribers → Fields** and create:

| Field Name | Type | Purpose |
|------------|------|---------|
| `first_name` | Text | Personalization |
| `funnel_stage` | Text | Tag for funnel position |
| `lead_source` | Text | Attribution tracking |
| `last_engagement` | Date | Re-engagement trigger |

## Step 2: Create Groups (Segments)

Go to **Subscribers → Groups** and create:

1. **FREE Kit Downloaded** - Tag: `funnel:free`
2. **MINI Kit Buyers** - Tag: `funnel:mini`
3. **MEDIUM Kit Buyers** - Tag: `funnel:medium`
4. **PRO Kit Buyers** - Tag: `funnel:pro`
5. **All Buyers** - Tag: `funnel:buyer`
6. **Cart Abandoners** - Tag: `action:cart-abandoned`
7. **Cold Leads** - Tag: `engagement:cold`
8. **VIP Customers** - Tag: `funnel:pro`

## Step 3: Create Automation Workflows

### Workflow 1: FREE Kit Sequence
```
Trigger: Form submitted (FREE Kit download form)
↓
Action: Add tag "funnel:free"
↓
Email 1: Welcome + Download Link (immediate)
↓
Wait 24 hours
↓
Email 2: Quick Start Guide
↓
Wait 2 days
↓
Email 3: Success Story + Soft Pitch
↓
Wait 2 days
↓
Condition: Has NOT purchased MINI Kit
↓
Email 4: MINI Kit Offer with Urgency
```

### Workflow 2: MINI Kit Purchase
```
Trigger: Purchase completed (MINI Kit)
↓
Action: Add tags "funnel:mini", "funnel:buyer"
↓
Action: Remove from "FREE Kit" workflow
↓
Email 1: Confirmation + Access (immediate)
↓
Wait 24 hours
↓
Email 2: 24h Guide Walkthrough
↓
Wait 2 days
↓
Email 3: Template Showcase
↓
Wait 4 days
↓
Condition: Has NOT purchased MEDIUM Kit
↓
Email 4: MEDIUM Kit Upgrade Pitch
```

### Workflow 3: MEDIUM Kit Purchase
```
Trigger: Purchase completed (MEDIUM Kit)
↓
Action: Add tags "funnel:medium", "funnel:buyer"
↓
Email 1: Confirmation + Roadmap (immediate)
↓
Wait 24 hours
↓
Email 2: Funnel Setup Guide
↓
Wait 2 days
↓
Email 3: Automation Deep Dive
↓
Wait 2 days
↓
Email 4: Business Templates
↓
Wait 5 days
↓
Condition: Has NOT purchased PRO Kit
↓
Email 5: PRO Kit Upgrade
```

### Workflow 4: PRO Kit Purchase
```
Trigger: Purchase completed (PRO Kit)
↓
Action: Add tags "funnel:pro", "funnel:buyer", "segment:vip"
↓
Email 1: Confirmation + Access (immediate)
↓
Wait 24 hours
↓
Email 2: Priority Support + Community
↓
Wait 2 days
↓
Email 3: Master Checklist Walkthrough
↓
Wait 4 days
↓
Email 4: Strategy Call Booking
↓
Wait 7 days
↓
Email 5: Advanced Tips + Testimonial Request
```

### Workflow 5: Cart Abandonment
```
Trigger: Product added to cart
↓
Wait 1 hour
↓
Condition: Has NOT completed purchase
↓
Email 1: Friendly Reminder
↓
Wait 23 hours
↓
Condition: Has NOT completed purchase
↓
Email 2: Bonus Offer / Objection Handler
↓
Wait 24 hours
↓
Condition: Has NOT completed purchase
↓
Email 3: Last Chance
```

### Workflow 6: Re-engagement
```
Trigger: No email opened in 30 days
↓
Action: Add tag "engagement:cold"
↓
Email 1: "We Miss You" + Value
↓
Wait 7 days
↓
Condition: Has NOT opened email
↓
Email 2: Survey + Special Offer
↓
Wait 8 days
↓
Condition: Has NOT opened email
↓
Email 3: Final Attempt + Unsubscribe Option
↓
Condition: Has NOT clicked "Keep Me Subscribed"
↓
Action: Unsubscribe contact
```

## Step 4: A/B Testing Setup

### Subject Line Testing
1. Create email with 3 subject line variants
2. Set test split: 33% / 33% / 34%
3. Run test for 4 hours
4. Winner sends to remaining subscribers

### Recommended Tests:

| Email | Test A | Test B | Test C |
|-------|--------|--------|--------|
| FREE-1 | Welcome to CashFlowLab! | Your FREE Kit is ready | Download your starter kit |
| FREE-4 | Last call: MINI Kit at $9 | Your templates are waiting | The $9 investment... |
| MINI-1 | Your MINI Kit is ready! | Welcome to the next level | Purchase confirmation |
| CART-1 | Did something go wrong? | You left something behind | Quick reminder |

## Step 5: Integration Checklist

- [ ] Connect your store (WooCommerce/Shopify/ThriveCart)
- [ ] Set up webhook for purchase events
- [ ] Connect lead capture forms
- [ ] Verify tracking pixels
- [ ] Test unsubscribe links
- [ ] Set up SPF/DKIM for deliverability
- [ ] Create backup of all sequences

---

# 📊 A/B TESTING SUGGESTIONS

## Priority 1 Tests (High Impact)

### 1. Subject Line Length
- **Hypothesis:** Shorter subject lines get higher open rates
- **Test:** 
  - A: "Your FREE Kit is ready" (24 chars)
  - B: "{{first_name}}, your CashFlowLab starter kit is ready for download" (62 chars)
- **Metric:** Open rate
- **Duration:** 4 hours or 100 opens

### 2. Personalization vs. Generic
- **Hypothesis:** First name personalization increases opens
- **Test:**
  - A: "Welcome to CashFlowLab!"
  - B: "Welcome to CashFlowLab, {{first_name}}!"
- **Metric:** Open rate
- **Duration:** 4 hours

### 3. Emoji Usage
- **Hypothesis:** Emojis increase visibility in crowded inboxes
- **Test:**
  - A: "Your MINI Kit is ready!"
  - B: "Your MINI Kit is ready! 🎉"
- **Metric:** Open rate
- **Note:** Test with your audience — emojis can increase OR decrease opens depending on market

## Priority 2 Tests (Medium Impact)

### 4. CTA Button Color
- **Hypothesis:** Gold CTA outperforms purple
- **Test:**
  - A: Gold gradient (#D4AF37)
  - B: Purple gradient (#6B2D5C)
- **Metric:** Click-through rate
- **Location:** Email 4 in FREE sequence

### 5. Social Proof Placement
- **Hypothesis:** Testimonials above the fold increase conversions
- **Test:**
  - A: Testimonial at top of email
  - B: Testimonial below main copy
- **Metric:** Click-through rate
- **Location:** MINI Kit sales email

### 6. Urgency Elements
- **Hypothesis:** Time-sensitive language increases action
- **Test:**
  - A: "Limited time offer"
  - B: "Price goes up tomorrow"
- **Metric:** Conversion rate
- **Location:** Cart abandonment sequence

## Priority 3 Tests (Low Impact, Easy Wins)

### 7. Send Time
- **Hypothesis:** Morning sends outperform afternoon
- **Test:**
  - A: 9:00 AM
  - B: 3:00 PM
- **Metric:** Open rate
- **Duration:** 1 week

### 8. Preview Text
- **Hypothesis:** Curiosity-driven preview text wins
- **Test:**
  - A: "Everything you need to start building..."
  - B: "Inside: 3 templates that changed Sarah's business..."
- **Metric:** Open rate

### 9. Email Length
- **Hypothesis:** Shorter emails get more clicks
- **Test:**
  - A: Full detailed email (current)
  - B: Short version with "Read more" link
- **Metric:** Click-through rate

## Testing Framework

### How to Run Tests:

1. **Hypothesis First** — Always start with a prediction
2. **Test One Variable** — Subject line OR CTA, not both
3. **Statistical Significance** — Wait for at least 100 conversions
4. **Document Results** — Keep a testing log
5. **Implement Winners** — Update templates with winning variants

### Testing Calendar:

| Week | Test Focus | Emails |
|------|------------|--------|
| 1 | Subject lines | FREE-1, MINI-1 |
| 2 | Send times | All sequences |
| 3 | CTA buttons | FREE-4, MEDIUM-5 |
| 4 | Preview text | FREE-1, CART-1 |

---

# ✅ PRE-LAUNCH CHECKLIST

## Technical Setup
- [ ] All merge tags tested ({{first_name}}, {{download_link}}, etc.)
- [ ] Unsubscribe links working
- [ ] Plain text versions created
- [ ] Mobile responsiveness verified
- [ ] Spam score checked (use Mail-Tester.com)
- [ ] Links tested and working
- [ ] Images optimized and hosted

## Automation Setup
- [ ] All workflows created
- [ ] Triggers configured correctly
- [ ] Tagging logic tested
- [ ] Exit conditions set (don't email if purchased)
- [ ] Delays configured correctly

## Legal Compliance
- [ ] Physical address in footer
- [ ] Unsubscribe link in every email
- [ ] Privacy policy linked
- [ ] GDPR compliance (if applicable)
- [ ] CAN-SPAM compliance (US)

## Testing
- [ ] Test send to yourself
- [ ] Test on Gmail, Outlook, Apple Mail
- [ ] Test on mobile devices
- [ ] Test automation triggers
- [ ] Test purchase flow end-to-end

---

**Document Version:** 1.0  
**Last Updated:** April 2025  
**Brand:** CashFlowLab (cashflowlabai.com)  
**Platform:** MailerLite (ready for import)

---

*Acest blueprint conține tot ce ai nevoie pentru a implementa funnel-ul complet de email marketing pentru CashFlowLab. Toate emailurile sunt gata de copy-paste în MailerLite. Succes! 🚀*