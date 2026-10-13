// Пошаговая сборка (юрта): на каждом шаге выбрать нужную деталь среди лишних
import { h, readJSON, shuffle } from '../core/dom.js';
import { t } from '../core/i18n.js';

export function mount(root) {
  const data = readJSON(root.dataset.payload);
  if (!data?.steps?.length) return;
  root.innerHTML = '';
  const built = h('ol', { class: 'steps', style: 'margin-top:24px' });
  const stage = h('div');
  root.append(stage, built);
  let index = 0;

  function render() {
    const step = data.steps[index];
    const options = shuffle([step, ...shuffle(data.distractors).slice(0, 2), ...data.steps.slice(index + 1, index + 2)]);
    const list = h('ul', { class: 'answers' });
    const feedback = h('div', { class: 'feedback', role: 'status' });
    options.forEach((option) => {
      const button = h('button', { class: 'answer', type: 'button' },
        option.image ? h('img', { src: option.image, alt: '', width: 56, height: 56, style: 'border-radius:10px;object-fit:cover' }) : null,
        h('span', { text: option.title }));
      button.addEventListener('click', () => {
        if (option !== step) {
          button.classList.remove('is-wrong'); void button.offsetWidth; button.classList.add('is-wrong');
          feedback.className = 'feedback is-visible is-wrong';
          feedback.replaceChildren(h('strong', { text: t.wrong }), option.explanation ? h('p', { text: option.explanation }) : '');
          return;
        }
        built.append(h('li', { class: 'step' }, h('h3', { text: step.title }), step.text ? h('p', { text: step.text }) : ''));
        index += 1;
        if (index < data.steps.length) render();
        else stage.replaceChildren(h('div', { class: 'feedback is-visible is-correct' }, h('strong', { text: root.dataset.success || t.done })));
      });
      list.append(h('li', {}, button));
    });
    stage.replaceChildren(
      h('p', { class: 'muted', text: `${t.step} ${index + 1} / ${data.steps.length}` }),
      h('h3', { class: 'quiz__question', text: t.choose }),
      list, feedback,
    );
  }
  render();
}
