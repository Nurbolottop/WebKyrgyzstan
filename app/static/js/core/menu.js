// Тень у шапки при прокрутке и мобильное меню (Esc, удержание фокуса, возврат фокуса)
export function initHeader() {
  const header = document.querySelector('[data-header]');
  if (!header) return;
  const update = () => header.classList.toggle('is-scrolled', window.scrollY > 8);
  update();
  window.addEventListener('scroll', update, { passive: true });
}

export function initMenu() {
  const menu = document.querySelector('[data-menu]');
  const openButton = document.querySelector('[data-menu-open]');
  if (!menu || !openButton) return;
  const closeButton = menu.querySelector('[data-menu-close]');

  const focusable = () => menu.querySelectorAll('a[href], button:not([disabled])');

  const onKey = (event) => {
    if (event.key === 'Escape') close();
    if (event.key !== 'Tab') return;
    const items = focusable();
    const first = items[0];
    const last = items[items.length - 1];
    if (event.shiftKey && document.activeElement === first) { event.preventDefault(); last.focus(); }
    else if (!event.shiftKey && document.activeElement === last) { event.preventDefault(); first.focus(); }
  };

  function open() {
    menu.classList.add('is-open');
    document.body.classList.add('menu-open');
    openButton.setAttribute('aria-expanded', 'true');
    document.addEventListener('keydown', onKey);
    closeButton?.focus();
  }

  function close() {
    menu.classList.remove('is-open');
    document.body.classList.remove('menu-open');
    openButton.setAttribute('aria-expanded', 'false');
    document.removeEventListener('keydown', onKey);
    openButton.focus();
  }

  openButton.addEventListener('click', open);
  closeButton?.addEventListener('click', close);
  window.matchMedia('(min-width: 1280px)').addEventListener('change', (e) => { if (e.matches) close(); });
}
