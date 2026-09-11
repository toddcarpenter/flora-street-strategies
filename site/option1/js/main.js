document.addEventListener('DOMContentLoaded', () => {
  const toggle = document.querySelector('.nav-toggle');
  const overlay = document.querySelector('.nav-overlay');
  const close = document.querySelector('.nav-close');

  function openMenu(moveFocus = false) {
    overlay.classList.add('open');
    document.body.classList.add('nav-open');
    toggle.setAttribute('aria-expanded', 'true');
    toggle.setAttribute('aria-label', 'Close menu');
    toggle.querySelector('.hamburger-icon').textContent = '×';
    if (close) close.setAttribute('aria-expanded', 'true');
    if (moveFocus) {
      const firstLink = overlay.querySelector('a');
      if (firstLink) firstLink.focus();
    }
  }

  function closeMenu(returnFocus = true) {
    overlay.classList.remove('open');
    document.body.classList.remove('nav-open');
    toggle.setAttribute('aria-expanded', 'false');
    toggle.setAttribute('aria-label', 'Open menu');
    toggle.querySelector('.hamburger-icon').textContent = '☰';
    if (close) close.setAttribute('aria-expanded', 'false');
    if (returnFocus) toggle.focus();
  }

  if (toggle && overlay) {
    toggle.addEventListener('click', (e) => {
      if (overlay.classList.contains('open')) closeMenu(e.detail === 0);
      else openMenu(e.detail === 0);
    });
  }

  if (close && overlay) {
    close.addEventListener('click', (e) => closeMenu(e.detail === 0));
  }

  if (overlay) {
    overlay.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => closeMenu(false));
    });

    overlay.addEventListener('click', (e) => {
      if (e.target === overlay) closeMenu(false);
    });
  }

  document.addEventListener('keydown', (e) => {
    if (!overlay.classList.contains('open')) return;

    if (e.key === 'Escape') {
      e.preventDefault();
      closeMenu(true);
      return;
    }

    if (e.key === 'Tab') {
      const focusable = [...overlay.querySelectorAll('a'), toggle];
      const first = focusable[0];
      const last = focusable[focusable.length - 1];

      if (e.shiftKey && document.activeElement === first) {
        e.preventDefault();
        last.focus();
      } else if (!e.shiftKey && document.activeElement === last) {
        e.preventDefault();
        first.focus();
      }
    }
  });
});
