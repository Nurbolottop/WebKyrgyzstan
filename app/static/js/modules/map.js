// Интерактивная карта: при наведении/фокусе/касании область или достопримечательность
// подсвечивается, а подробности показываются в карточке в пустом углу карты.
import { h, readJSON } from '../core/dom.js';

// Подписи не должны перекрывать точки и друг друга: сдвигаем подпись на ближайшее свободное место
function declutter(svg) {
  const labels = [...svg.querySelectorAll('.kg-map__labels text:not(.kg-map__country)')];
  const dots = [...svg.querySelectorAll('.kg-map__pin-dot, .kg-map__city-dot')].map((c) => {
    const r = Number(c.getAttribute('r')) + 3;
    const x = Number(c.getAttribute('cx'));
    const y = Number(c.getAttribute('cy'));
    return { x: x - r, y: y - r, width: r * 2, height: r * 2 };
  });
  const hit = (a, b) => a.x < b.x + b.width && b.x < a.x + a.width && a.y < b.y + b.height && b.y < a.y + a.height;
  const placed = [];
  const offsets = [[0, 0], [0, 18], [0, -18], [0, 30], [0, -30], [22, 0], [-22, 0], [0, 42], [0, -42]];
  labels.forEach((label) => {
    const box = label.getBBox();
    if (!box.width) return;
    const shift = offsets.find(([dx, dy]) => {
      const moved = { x: box.x + dx - 2, y: box.y + dy - 1, width: box.width + 4, height: box.height + 2 };
      return !dots.some((d) => hit(moved, d)) && !placed.some((p) => hit(moved, p));
    }) || [0, 0];
    label.setAttribute('transform', `translate(${shift[0]} ${shift[1]})`);
    placed.push({ x: box.x + shift[0], y: box.y + shift[1], width: box.width, height: box.height });
  });
}

export function mount(root) {
  const svg = root.querySelector('svg');
  if (svg) {
    declutter(svg);
    // Подписи скрываются на узкой карте и появляются при расширении — пересчитываем
    new ResizeObserver(() => declutter(svg)).observe(root);
  }

  const regionTips = readJSON(root.querySelector('#map-tips')) || {};
  const placeTips = readJSON(root.querySelector('#map-pins')) || {};
  const t = readJSON(root.querySelector('#map-i18n')) || {};
  const intro = root.querySelector('.kg-map__intro');
  const card = root.querySelector('.kg-map__card');
  const regions = [...root.querySelectorAll('.kg-map__region')];
  const pins = [...root.querySelectorAll('.kg-map__pin')];
  const touch = window.matchMedia('(hover: none)').matches;

  const els = {
    media: card.querySelector('.kg-map__card-media'),
    img: card.querySelector('img'),
    kind: card.querySelector('.kg-map__card-kind'),
    title: card.querySelector('.kg-map__card-title'),
    text: card.querySelector('.kg-map__card-text'),
    stats: card.querySelector('.kg-map__card-stats'),
    link: card.querySelector('.kg-map__card-link'),
  };

  // Закреплённая карточка: выбранная касанием или текущая область на странице области
  let pinned = null;
  let hideTimer;

  function stat(label, value) {
    if (!value && value !== 0) return null;
    return h('div', {}, h('dt', { text: label }), h('dd', { text: String(value) }));
  }

  function render(data) {
    if (!data) return;
    clearTimeout(hideTimer);
    els.media.hidden = !data.image;
    if (data.image && els.img.getAttribute('src') !== data.image) {
      els.img.src = data.image;
      els.img.alt = data.title;
    }
    els.kind.textContent = data.type === 'place' ? `${data.kind} · ${data.region}` : data.kind;
    els.title.textContent = data.title;
    els.text.textContent = data.summary || '';
    els.text.hidden = !data.summary;
    const rows = data.type === 'place'
      ? [stat(data.valueLabel, data.value)]
      : [stat(t.capital, data.capital), stat(t.area, data.area && `${data.area} ${t.km2}`), stat(t.places, data.places || null)];
    els.stats.replaceChildren(...rows.filter(Boolean));
    els.link.href = data.url;
    intro.hidden = true;
    card.hidden = false;
    card.classList.remove('is-entering');
    void card.offsetWidth;
    card.classList.add('is-entering');
  }

  function highlight(el) {
    regions.forEach((r) => r.classList.toggle('is-active', r === el));
    pins.forEach((p) => p.classList.toggle('is-active', p === el));
  }

  function showFor(el) {
    const data = el.dataset.place ? placeTips[el.dataset.place] : regionTips[el.dataset.region];
    highlight(el);
    render(data);
  }

  function restore() {
    hideTimer = setTimeout(() => {
      if (pinned) { showFor(pinned); return; }
      highlight(null);
      card.hidden = true;
      intro.hidden = false;
    }, 250);
  }

  const bind = (el) => {
    el.addEventListener('mouseenter', () => showFor(el));
    el.addEventListener('mouseleave', restore);
    el.addEventListener('focus', () => showFor(el));
    el.addEventListener('blur', restore);
    if (touch) {
      // Первое касание — показать карточку, второе по тому же месту — перейти
      el.addEventListener('click', (event) => {
        if (pinned === el) return;
        event.preventDefault();
        pinned = el;
        showFor(el);
        card.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
      });
    }
  };

  regions.forEach((region) => {
    if (!regionTips[region.dataset.region]) {
      region.removeAttribute('href');
      region.setAttribute('aria-disabled', 'true');
      return;
    }
    bind(region);
  });
  pins.forEach(bind);

  // Пока курсор над карточкой — не прячем её
  card.addEventListener('mouseenter', () => clearTimeout(hideTimer));
  card.addEventListener('mouseleave', restore);

  // На странице области её карточка открыта сразу
  // ?region=naryn в адресе тоже открывает карточку (удобно делиться ссылкой)
  const active = root.closest('[data-active-region]')?.dataset.activeRegion
    || new URLSearchParams(window.location.search).get('region');
  if (active) {
    pinned = root.querySelector(`[data-region="${CSS.escape(active)}"]`);
    if (pinned) showFor(pinned);
  }

  // Подсветка области при наведении на её название в списке рядом с картой
  document.querySelectorAll('[data-region-link]').forEach((link) => {
    const region = root.querySelector(`[data-region="${link.dataset.regionLink}"]`);
    if (!region) return;
    link.addEventListener('mouseenter', () => showFor(region));
    link.addEventListener('mouseleave', restore);
    region.addEventListener('mouseenter', () => link.classList.add('is-active'));
    region.addEventListener('mouseleave', () => link.classList.remove('is-active'));
  });
}
