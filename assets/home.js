document.documentElement.classList.add('js');
const language = document.documentElement.lang;
const messages = {
 en: { open: 'Open menu', close: 'Close menu', sending: 'Sending…', pending: 'Sending your request…',
  review: 'Thanks — your information has been received. We’ll review the process and contact you using the email you provided.',
  beta: 'Thanks — your setup discussion request has been received. We’ll contact you using the email you provided to discuss the scope.',
  timeout: 'We could not confirm your submission because the connection timed out. Your details are still here. Please check your connection before trying again, or contact contact@cashflowlabai.com.',
  error: 'Your request could not be submitted. Your details are still here. Please try again, or contact contact@cashflowlabai.com.' },
 de: { open: 'Menü öffnen', close: 'Menü schließen', sending: 'Wird gesendet…', pending: 'Deine Anfrage wird gesendet…',
  review: 'Danke — deine Angaben sind eingegangen. Wir prüfen den Prozess und melden uns über die angegebene E-Mail-Adresse bei dir.',
  beta: 'Danke — deine Anfrage zum Einrichtungsgespräch ist eingegangen. Wir melden uns über die angegebene E-Mail-Adresse, um den Umfang zu besprechen.',
  timeout: 'Wegen einer Zeitüberschreitung konnten wir den Eingang nicht bestätigen. Deine Angaben sind noch vorhanden. Prüfe vor einem neuen Versuch deine Verbindung oder kontaktiere contact@cashflowlabai.com.',
  error: 'Deine Anfrage konnte nicht gesendet werden. Deine Angaben sind noch vorhanden. Versuche es erneut oder kontaktiere contact@cashflowlabai.com.' },
 ro: { open: 'Deschide meniul', close: 'Închide meniul', sending: 'Se trimite…', pending: 'Solicitarea ta se trimite…',
  review: 'Mulțumim — am primit informațiile tale. Vom analiza procesul și te vom contacta la adresa de email indicată.',
  beta: 'Mulțumim — am primit solicitarea de discuție despre configurare. Te vom contacta la adresa de email indicată pentru a stabili detaliile.',
  timeout: 'Nu am putut confirma trimiterea deoarece conexiunea a expirat. Datele tale sunt încă aici. Verifică conexiunea înainte de a reîncerca sau contactează contact@cashflowlabai.com.',
  error: 'Solicitarea nu a putut fi trimisă. Datele tale sunt încă aici. Încearcă din nou sau contactează contact@cashflowlabai.com.' }
}[language] || null;
const ui = messages || {open:'Open menu',close:'Close menu'};
const menu = document.getElementById('menu');
const navigation = document.getElementById('nav-links');
function closeMenu() {
  navigation.classList.remove('open');
  menu.setAttribute('aria-expanded', 'false');
  menu.setAttribute('aria-label', ui.open);
}
menu.addEventListener('click', () => {
  const open = navigation.classList.toggle('open');
  menu.setAttribute('aria-expanded', String(open));
  menu.setAttribute('aria-label', open ? ui.close : ui.open);
});
navigation.querySelectorAll('a').forEach(link => link.addEventListener('click', closeMenu));
document.addEventListener('keydown', event => { if (event.key === 'Escape') closeMenu(); });
document.querySelectorAll('[data-dialog]').forEach(button => button.addEventListener('click', () => {
  document.getElementById(button.dataset.dialog).showModal();
}));
document.querySelectorAll('dialog .close').forEach(button => button.addEventListener('click', () => button.closest('dialog').close()));
document.querySelectorAll('dialog a[href^="#"]').forEach(link => link.addEventListener('click', () => {
  link.closest('dialog').close();
  const heading = document.querySelector(link.getAttribute('href') + ' h2');
  if (heading) heading.focus({ preventScroll: true });
}));

// Netlify detects these static forms at deploy time. Never report a local or
// failed POST as a successful submission, and retain entered values on errors.
document.querySelectorAll('[data-request-form]').forEach(form => {
  let sending = false;
  form.addEventListener('submit', async event => {
    event.preventDefault();
    if (sending || !form.reportValidity()) return;
    const status = form.querySelector('.form-status');
    const button = form.querySelector('[type="submit"]');
    const label = button.textContent;
    sending = true;
    button.disabled = true;
    button.textContent = ui.sending;
    status.textContent = ui.pending;
    status.classList.remove('error');
    const controller = new AbortController();
    const timeout = setTimeout(() => controller.abort(), 20000);
    try {
      const data = new URLSearchParams(new FormData(form));
      data.set('form-name', form.getAttribute('name'));
      const response = await fetch(form.action, {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: data.toString(),
        signal: controller.signal
      });
      if (!response.ok) throw new Error('Submission rejected');
      // Netlify returns 2xx after accepting the URL-encoded submission. Its
      // response may contain the homepage HTML, so do not reject that content.
      form.reset();
      status.textContent = form.getAttribute('name') === 'lead-review'
        ? ui.review : ui.beta;
    } catch (error) {
      status.classList.add('error');
      status.textContent = error.name === 'AbortError'
        ? ui.timeout : ui.error;
    } finally {
      clearTimeout(timeout);
      sending = false;
      button.disabled = false;
      button.textContent = label;
      status.focus({ preventScroll: true });
    }
  });
});
