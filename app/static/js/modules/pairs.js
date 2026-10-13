// «Соедини пары» (match) и «Найди пару» (memory)
import { h, readJSON, shuffle } from '../core/dom.js';
import { t } from '../core/i18n.js';

export function mount(root) {
  const data = readJSON(root.dataset.payload);
  if (!data?.pairs?.length) return;
  root.innerHTML = '';
  (data.engine === 'memory' ? memory : match)(root, data.pairs.slice(0, 8));
}

function finish(root, restart) {
  const again = h('button', { class: 'btn btn--section', type: 'button', text: t.again, onclick: restart });
  root.append(h('div', { class: 'feedback is-visible is-correct', role: 'status' },
    h('strong', { text: root.dataset.success || t.done })), h('p', { style: 'margin-top:16px' }, again));
}

function match(root, pairs) {
  let selected = null;
  let solved = 0;
  const left = h('ul', { class: 'answers', style: 'grid-template-columns:1fr' });
  const right = h('ul', { class: 'answers', style: 'grid-template-columns:1fr' });

  const make = (text, id, side, image) => {
    const button = h('button', { class: 'answer', type: 'button', 'data-id': id, 'data-side': side },
      image ? h('img', { src: image, alt: '', width: 48, height: 48, style: 'border-radius:10px;object-fit:cover' }) : null,
      h('span', { text }));
    button.addEventListener('click', () => pick(button));
    return h('li', {}, button);
  };

  function pick(button) {
    if (button.disabled) return;
    if (!selected || selected.dataset.side === button.dataset.side) {
      selected?.classList.remove('is-correct');
      selected = button;
      button.style.borderColor = 'var(--ink)';
      return;
    }
    const ok = selected.dataset.id === button.dataset.id;
    [selected, button].forEach((b) => {
      b.style.borderColor = '';
      b.classList.remove('is-wrong');
      void b.offsetWidth;
      b.classList.add(ok ? 'is-correct' : 'is-wrong');
      if (ok) b.disabled = true;
    });
    if (!ok) { const pair = [selected, button]; setTimeout(() => pair.forEach((b) => b.classList.remove('is-wrong')), 500); }
    selected = null;
    if (ok && (solved += 1) === pairs.length) finish(root, () => { root.innerHTML = ''; match(root, pairs); });
  }

  shuffle(pairs.map((p, i) => [p, i])).forEach(([p, i]) => left.append(make(p.a, i, 'a', p.image)));
  shuffle(pairs.map((p, i) => [p, i])).forEach(([p, i]) => right.append(make(p.b, i, 'b')));
  root.append(h('div', { style: 'display:grid;gap:16px;grid-template-columns:1fr 1fr' }, left, right));
}

function memory(root, pairs) {
  const cards = shuffle(pairs.flatMap((p, i) => [{ id: i, text: p.a, image: p.image }, { id: i, text: p.b }]));
  let open = [];
  let solved = 0;
  let moves = 0;
  const counter = h('p', { class: 'muted', text: `${t.score}: 0` });
  const grid = h('ul', { class: 'flashcards', style: '--min:140px' });

  cards.forEach((card) => {
    const button = h('button', { type: 'button', 'aria-pressed': 'false' },
      h('span', { class: 'flashcard__face' }, h('span', { class: 'flashcard__word', text: '?' })),
      h('span', { class: 'flashcard__face flashcard__face--back' },
        card.image ? h('img', { src: card.image, alt: '' }) : null,
        h('span', { class: 'flashcard__word', style: 'font-size:1.2rem', text: card.text })));
    const item = h('li', { class: 'flashcard' }, button);
    button.addEventListener('click', () => {
      if (item.classList.contains('is-flipped') || open.length === 2) return;
      item.classList.add('is-flipped');
      button.setAttribute('aria-pressed', 'true');
      open.push({ item, button, card });
      if (open.length < 2) return;
      moves += 1;
      counter.textContent = `${t.score}: ${moves}`;
      const [a, b] = open;
      if (a.card.id === b.card.id) {
        open = [];
        if ((solved += 1) === pairs.length) finish(root, () => { root.innerHTML = ''; memory(root, pairs); });
      } else {
        setTimeout(() => {
          [a, b].forEach((x) => { x.item.classList.remove('is-flipped'); x.button.setAttribute('aria-pressed', 'false'); });
          open = [];
        }, 900);
      }
    });
    grid.append(item);
  });
  root.append(counter, grid);
}
