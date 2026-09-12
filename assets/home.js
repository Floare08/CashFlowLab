document.documentElement.classList.add('js');
const menu = document.getElementById('menu');
const navigation = document.getElementById('nav-links');
function closeMenu() {
  navigation.classList.remove('open');
  menu.setAttribute('aria-expanded', 'false');
  menu.setAttribute('aria-label', 'Open menu');
}
menu.addEventListener('click', () => {
  const open = navigation.classList.toggle('open');
  menu.setAttribute('aria-expanded', String(open));
  menu.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
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
    button.textContent = 'Sending…';
    status.textContent = 'Sending your request…';
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
      // A static preview can return the homepage for any request. That is not
      // evidence that a submission was accepted by Netlify Forms.
      const body = await response.text();
      if (body.includes('id="hero-title"')) throw new Error('Form processing unavailable');
      form.reset();
      status.textContent = form.getAttribute('name') === 'lead-review'
        ? 'Thanks — your information has been received. We’ll review the process and contact you using the email you provided.'
        : 'Thanks — your setup discussion request has been received. We’ll contact you using the email you provided to discuss the scope.';
    } catch (error) {
      status.classList.add('error');
      status.textContent = error.name === 'AbortError'
        ? 'We could not confirm your submission because the connection timed out. Your details are still here. Please check your connection before trying again, or contact contact@cashflowlabai.com.'
        : 'Your request could not be submitted. Your details are still here. Please try again, or contact contact@cashflowlabai.com.';
    } finally {
      clearTimeout(timeout);
      sending = false;
      button.disabled = false;
      button.textContent = label;
      status.focus({ preventScroll: true });
    }
  });
});
