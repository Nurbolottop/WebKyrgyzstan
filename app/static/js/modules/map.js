// Интерактивная карта: подсказка при наведении/фокусе, нижняя карточка на сенсорных экранах
import { readJSON } from '../core/dom.js';

export function mount(root) {
  const tips = readJSON(root.querySelector('#map-tips')) || {};
  const i18n = readJSON(root.querySelector('#map-i18n')) || {};
  const tip = root.querySelector('.kg-map__tip');
  const sheet = root.querySelector('.kg-map__sheet');
  const regions = root.querySelectorAll('.kg-map__region');
  const touch = window.matchMedia('(hover: none)').matches;

  const active = root.closest('[data-active-region]')?.dataset.activeRegion;
  if (active) root.querySelector(`[data-region="${active}"]`)?.classList.add('is-active');

  const describe = (data) => [
    data.capital ? `${i18n.capital}: ${data.capital}` : '',
    data.places ? `${i18n.places}: ${data.places}` : '',
  ].filter(Boolean).join(' · ');

  function showTip(region) {
    const data = tips[region.dataset.region];
    if (!data) return;
    tip.innerHTML = '';
    const title = document.createElement('strong');
    title.textContent = data.title;
    const info = document.createElement('span');
    info.textContent = describe(data);
    tip.append(title, info);
    const box = region.getBoundingClientRect();
    const host = root.getBoundingClientRect();
    tip.style.left = `${box.left - host.left + box.width / 2}px`;
    tip.style.top = `${box.top - host.top + Math.min(box.height / 2, 60)}px`;
    tip.classList.add('is-visible');
  }

  const hideTip = () => tip.classList.remove('is-visible');

  regions.forEach((region) => {
    if (!tips[region.dataset.region]) {
      // Область не опубликована — без ссылки
      region.removeAttribute('href');
      region.setAttribute('aria-disabled', 'true');
      return;
    }
    region.addEventListener('mouseenter', () => showTip(region));
    region.addEventListener('mouseleave', hideTip);
    region.addEventListener('focus', () => showTip(region));
    region.addEventListener('blur', hideTip);

    if (touch && sheet) {
      // Первое касание показывает карточку, переход — по кнопке «Открыть»
      region.addEventListener('click', (event) => {
        event.preventDefault();
        const data = tips[region.dataset.region];
        regions.forEach((r) => r.classList.toggle('is-active', r === region));
        sheet.querySelector('strong').textContent = data.title;
        sheet.querySelector('.muted').textContent = describe(data);
        sheet.querySelector('a').href = data.url;
        sheet.classList.add('is-visible');
      });
    }
  });

  // Подсветка области при наведении на её название в списке рядом с картой
  document.querySelectorAll('[data-region-link]').forEach((link) => {
    const region = root.querySelector(`[data-region="${link.dataset.regionLink}"]`);
    if (!region) return;
    link.addEventListener('mouseenter', () => region.classList.add('is-active'));
    link.addEventListener('mouseleave', () => region.classList.remove('is-active'));
    region.addEventListener('mouseenter', () => link.classList.add('is-active'));
    region.addEventListener('mouseleave', () => link.classList.remove('is-active'));
  });
}
