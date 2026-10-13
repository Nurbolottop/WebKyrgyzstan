// «Угадай область»: показываем название — ребёнок нажимает область на карте
import { h, readJSON } from '../core/dom.js';
import { t } from '../core/i18n.js';

export function mount(root) {
  const data = readJSON(root.dataset.payload);
  const svg = root.querySelector('svg');
  if (!data?.targets?.length || !svg) return;
  root.querySelector('.kg-map__pins')?.remove();
  svg.querySelectorAll('a').forEach((a) => { a.removeAttribute('href'); a.setAttribute('role', 'button'); a.setAttribute('tabindex', '0'); });

  const prompt = h('h3', { class: 'quiz__question', 'aria-live': 'polite' });
  const feedback = h('div', { class: 'feedback', role: 'status' });
  const scoreLine = h('p', { class: 'muted' });
  root.prepend(scoreLine, prompt);
  root.append(feedback);
  const wrap = h('div', { class: 'kg-map' });
  svg.replaceWith(wrap);
  wrap.append(svg);

  let index = 0;
  let score = 0;
  let locked = false;

  function render() {
    const target = data.targets[index];
    prompt.textContent = `${t.where} ${target.title}`;
    scoreLine.textContent = `${t.score}: ${score} / ${data.targets.length}`;
    feedback.className = 'feedback';
    svg.querySelectorAll('.kg-map__region').forEach((r) => r.classList.remove('is-active'));
    locked = false;
  }

  function answer(region) {
    if (locked) return;
    locked = true;
    const target = data.targets[index];
    const ok = region.dataset.region === target.id;
    if (ok) score += 1;
    svg.querySelector(`[data-region="${target.id}"]`)?.classList.add('is-active');
    feedback.className = `feedback is-visible ${ok ? 'is-correct' : 'is-wrong'}`;
    feedback.replaceChildren(h('strong', { text: ok ? t.correct : t.wrong }));
    setTimeout(() => {
      index += 1;
      if (index < data.targets.length) { render(); return; }
      prompt.textContent = root.dataset.success || t.done;
      scoreLine.textContent = `${t.score}: ${score} / ${data.targets.length}`;
      feedback.replaceChildren(h('button', {
        class: 'btn btn--section', type: 'button', text: t.again,
        onclick: () => { index = 0; score = 0; render(); },
      }));
      feedback.className = 'feedback is-visible';
    }, 1200);
  }

  svg.querySelectorAll('.kg-map__region').forEach((region) => {
    region.addEventListener('click', () => answer(region));
    region.addEventListener('keydown', (e) => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); answer(region); } });
  });
  render();
}
