// YouTube загружается только после нажатия — страница быстрее, без трекинга до клика
function videoId(url) {
  const match = url.match(/(?:youtu\.be\/|v=|embed\/|shorts\/)([\w-]{11})/);
  return match ? match[1] : null;
}

export function mount(root) {
  const id = videoId(root.dataset.url);
  if (!id) { root.remove(); return; }
  const preview = document.createElement('img');
  preview.src = `https://i.ytimg.com/vi/${id}/hqdefault.jpg`;
  preview.alt = '';
  preview.loading = 'lazy';
  root.prepend(preview);
  root.querySelector('.video__play').addEventListener('click', () => {
    const frame = document.createElement('iframe');
    frame.src = `https://www.youtube-nocookie.com/embed/${id}?autoplay=1&rel=0`;
    frame.allow = 'autoplay; encrypted-media; picture-in-picture';
    frame.allowFullscreen = true;
    frame.title = 'YouTube';
    root.replaceChildren(frame);
  }, { once: true });
}
