export default async (request: Request) => {
  const url = new URL(request.url);
  const origin = `${url.protocol}//${url.host}`;

  // Listează rutele reale ale site-ului tău
  const paths = ["/", "/en/"];

  const body =
    `<?xml version="1.0" encoding="UTF-8"?>` +
    `<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">` +
    paths.map(p => `
  <url>
    <loc>${origin}${p}</loc>
    <changefreq>weekly</changefreq>
    <priority>${p === "/" ? "1.0" : "0.8"}</priority>
  </url>`).join("") +
    `
</urlset>`;

  return new Response(body, {
    headers: {
      "content-type": "application/xml; charset=utf-8",
      "cache-control": "public, max-age=86400"
    }
  });
};
