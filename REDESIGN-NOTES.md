# Reference-aligned homepage

Branch: redesign/cinematic-homepage.

## Design and assets

Rebuilt the root homepage in English using the complete references supplied on 2026-09-12. The clean hero and continuous lower artwork are stored both as original JPGs and WebP assets. The desktop lower background is one continuous image; mobile uses scene crops at their natural proportions. All text, navigation, cards, icons, buttons, FAQ and dialogs are HTML/CSS/SVG.

The structure follows the supplied references: two-line white/gold hero, three horizontal benefits, four process steps, four reasons, three proof placeholders, compact audit CTA, €299 Beta Setup with inclusions from the reference, FAQ and footer.

## Preserved architecture

Static HTML/CSS/JavaScript; no framework or new dependencies. Existing Netlify configuration, product routes, legal pages and separate EN/DE pages are unchanged. The original Romanian root homepage remains available at /ro/. The new English homepage is at /. The Free Kit dialog retains the MailerLite endpoint and input fields. Contact actions use the real contact address already present in the imprint.

## Verification

Chrome checked at 320, 390, 768, 1024, 1280 and 1440 pixels: no horizontal overflow, missing images, invalid fragment links or JavaScript errors. Desktop and mobile full-page screenshots reviewed. Menu, FAQ, sample report and Free Kit dialogs verified; all local navigation routes return HTTP 200. No real subscriptions or purchases submitted.

## Deliberate differences and limitations

- Unsupported metrics (10x, 80%, 100%) and absolute performance promises remain neutral, following the original brief.
- Contact email uses the existing verified repository address, not the different illustrative address in the mockup. Audit and beta CTAs compose email requests; no new payment or audit backend is implied.
- The sample report is explicitly illustrative and contains no customer data.
- Current copyright year; real legal/resource links retained.
- Clean artwork and composed mockups contain different wizard positions and scene details. Exact pixel identity cannot be achieved with the supplied clean backgrounds; no text-bearing screenshots are used as backgrounds.
- English/German legacy language pages retain their existing designs and integrations.

## Release

The user authorized deployment to main before requesting the reference correction. Publishing must use the corrected, verified source.
