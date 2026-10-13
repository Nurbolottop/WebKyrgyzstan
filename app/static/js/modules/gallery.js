// Лайтбокс галереи на <dialog>: Esc и клик по фону закрывают
export function mount(root) {
  const dialog = root.querySelector('.lightbox');
  if (!dialog?.showModal) return;
  const img = dialog.querySelector('img');
  const caption = dialog.querySelector('p');
  root.querySelectorAll('[data-full]').forEach((button) => {
    button.addEventListener('click', () => {
      img.src = button.dataset.full;
      img.alt = button.querySelector('img')?.alt || '';
      caption.textContent = button.dataset.caption;
      dialog.showModal();
    });
  });
  dialog.querySelector('.lightbox__close').addEventListener('click', () => dialog.close());
  dialog.addEventListener('click', (event) => { if (event.target === dialog) dialog.close(); });
}
