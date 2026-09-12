# High-detail, art-directed website backgrounds

Generated with the built-in ImageGen tool on 2026-09-12, using the supplied clean artwork as reference. These are faithful re-creations, not lossless restoration of missing source pixels. No local enlargement is used; export variants only downsample the generated masters.

## Delivered assets

- `scene-1-desktop.webp` through `scene-6-desktop.webp`: **2172 × 724** pixels each, generated as six independent 3:1 panoramas.
- `scene-1-compact.webp` through `scene-6-compact.webp`: 1100 × 367, for smaller desktop/tablet viewports.
- `scene-1-mobile.webp` through `scene-6-mobile.webp`: 724 × 720 phone compositions. Rendered at viewport width without enlarging them to fill tall sections; dark gradients blend the remaining space.
- `hero-desktop.webp`: 1672 × 941; compact version 840 × 473.
- `hero-mobile.webp`: 1254 × 1254; compact version 640 × 640. A deliberately recomposed square that keeps the wizard, orb, volcano and city visible.
- `manifest.json`: exact encoded dimensions and byte sizes.

The original lower JPG was 720 pixels wide for the entire six-section page. Every new desktop scene now has about three times that width and roughly ten times the pixels of an old section crop. These are not 4K files; the generator returned the native dimensions listed above despite larger size requests.

`picture`/`source`/`srcset` select the appropriate composition and resolution. Below-the-fold section images use native lazy loading. WebP exports use quality 91; no synthetic upscaling, sharpen filter or extra grain was applied. Old source artwork remains available for rollback.

## Final prompt set

Common desktop prompt:

> Edit target: supplied single panoramic fantasy scene. Generate ONE faithful rebuilt high-detail panorama, aspect ratio EXACTLY 3:1 ultra-wide landscape (not portrait, not atlas), largest available native resolution. Requested 3072 x 1024. [Scene specification below.] Preserve original layout, camera and midnight navy-purple-black palette with natural warm gold lights. Fine photorealistic cinematic fantasy matte-painting detail: individual masonry joints, tiny castle windows, fine waterfall streams, rocks, foliage and embroidery where present. Keep middle 55% spacious, very dark and low contrast for real HTML text. No new elements, no words, letters, logos, UI, watermarks, panel dividers, blur, grain or sharpening halos. Reconstruct true crisp detail rather than magnifying the small source. One standalone panoramic scene only.

Scene specifications:

1. Ancient torch-lit broken stone arch on the FAR LEFT, almost black purple valley in center, golden city and volcano far RIGHT.
2. Ancient tree and hanging amber lantern FAR LEFT; broad dark center; golden Gothic castle, stone bridge and waterfalls at FAR RIGHT.
3. Distant golden castle and waterfalls FAR LEFT, dark mountain valley and broad lake center, embroidered gold banner and fire FAR RIGHT.
4. Same elderly hooded white-bearded wizard and gold orb staff on LEFT edge, preserve identity and pose; dark center; distant golden castle and waterfalls FAR RIGHT.
5. Candlelit ancient stone ruin arch FAR LEFT, dark lake and purple mountain valley center, golden castle on cliffs and winding illuminated path FAR RIGHT.
6. Detailed ruined arch and candles FAR LEFT, dark misty mountains center, ruined arch with hanging golden lantern FAR RIGHT.

Mobile prompt specifications: regenerate the same scenes as two atlases of exactly three square compositions, in original order, without text/UI/gutters. Recompose naturally for a phone rather than stretching a landscape: keep identifiable landmarks toward the sides within the central 70% of the image and a dark center for text. Use detailed realistic stonework, water, cloth and natural warm gold lighting against midnight purple/black. Separate each atlas into three square files and trim two-pixel seams.

Hero desktop prompt specification: faithful 16:9 reconstruction preserving dark left 42%, wizard on right, volcano upper center-right, golden city, waterfalls, river and rocky foreground; same elderly wizard, white beard, gold-embroidered black cloak and orb staff. Rebuild fine hair, embroidery, stonework and water; no text/UI/extra objects or sharpening halos.

Hero mobile prompt specification: square adaptation shown below the phone's copy/CTAs. Preserve wizard identity on right, visible face and staff orb, volcano high center-left, golden city center-left, waterfalls and river below. Include all key subjects without cropping their defining features; dark corners blend into the page. Same realistic cinematic black/purple/gold rendering with no text or UI.

## Verification and limits

Reviewed in the browser at 390 and 1440/1920 pixels; checked 320 and 768 breakpoints. Responsive source selection, loaded assets and absence of horizontal overflow verified. The page copy, forms, prices and routing are unchanged by this image-quality update.

No finite image can remain equally sharp at arbitrary zoom or on every very large high-density display. The new desktop sources cover normal Full HD display widths without the former 720-pixel enlargement; mobile avoids aggressive panoramic crops.
