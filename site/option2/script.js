document.addEventListener('DOMContentLoaded', () => {
  const toggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('.site-nav');
  const links = nav ? [...nav.querySelectorAll('a')] : [];

  if (!toggle || !nav) return;

  const closeMenu = (returnFocus = false) => {
    nav.classList.remove('open');
    toggle.setAttribute('aria-expanded', 'false');
    toggle.querySelector('.menu-label').textContent = 'Menu';
    document.body.classList.remove('menu-open');
    if (returnFocus) toggle.focus();
  };

  const openMenu = () => {
    nav.classList.add('open');
    toggle.setAttribute('aria-expanded', 'true');
    toggle.querySelector('.menu-label').textContent = 'Close';
    document.body.classList.add('menu-open');
    links[0]?.focus();
  };

  toggle.addEventListener('click', () => {
    if (nav.classList.contains('open')) closeMenu();
    else openMenu();
  });

  links.forEach(link => link.addEventListener('click', () => closeMenu()));

  document.addEventListener('keydown', event => {
    if (!nav.classList.contains('open')) return;

    if (event.key === 'Escape') {
      event.preventDefault();
      closeMenu(true);
      return;
    }

    if (event.key !== 'Tab') return;
    const focusable = [...links, toggle];
    const first = focusable[0];
    const last = focusable[focusable.length - 1];

    if (event.shiftKey && document.activeElement === first) {
      event.preventDefault();
      last.focus();
    } else if (!event.shiftKey && document.activeElement === last) {
      event.preventDefault();
      first.focus();
    }
  });
});
