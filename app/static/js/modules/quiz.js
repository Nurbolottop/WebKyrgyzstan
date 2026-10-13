// Викторина: вопрос → ответ → обратная связь → следующий → итог. Ничего не отправляется на сервер.
import { h, readJSON } from '../core/dom.js';

const LETTERS = ['A', 'B', 'C', 'D', 'E', 'F'];

export function mount(root) {
  const data = readJSON(root.dataset.payload);
  const t = readJSON(root.querySelector('.quiz__i18n')) || {};
  if (!data?.questions?.length) return;

  const mini = root.hasAttribute('data-mini');
  const questions = data.questions;
  const storageKey = data.id ? `webkg:quiz:${data.id}` : null;
  let index = 0;
  let score = 0;

  root.querySelector('.quiz__static')?.remove();
  const stage = h('div', { class: 'quiz__stage' });
  root.prepend(stage);

  function renderQuestion() {
    const q = questions[index];
    stage.innerHTML = '';

    if (!mini) {
      const progress = h('div', { class: 'quiz__progress', 'aria-hidden': 'true' }, h('span'));
      progress.firstChild.style.width = `${(index / questions.length) * 100}%`;
      stage.append(h('div', { class: 'quiz__top' },
        h('span', { text: `${t.question} ${index + 1} ${t.of} ${questions.length}` }), progress));
    }

    const heading = h('h3', { class: 'quiz__question', tabindex: '-1', text: q.text });
    stage.append(heading);
    if (q.image) stage.append(h('img', { class: 'quiz__image', src: q.image, alt: q.imageAlt || '', loading: 'lazy' }));

    const list = h('ul', { class: 'answers' });
    const feedback = h('div', { class: 'feedback', role: 'status', 'aria-live': 'polite' });
    q.answers.forEach((answer, i) => {
      const button = h('button', { class: 'answer', type: 'button' },
        h('span', { class: 'answer__letter', 'aria-hidden': 'true', text: LETTERS[i] }),
        h('span', { text: answer.text }));
      button.addEventListener('click', () => choose(button, answer, list, feedback, q));
      list.append(h('li', {}, button));
    });
    stage.append(list, feedback);
    if (index > 0) heading.focus();
  }

  function choose(button, answer, list, feedback, q) {
    const buttons = [...list.querySelectorAll('.answer')];
    buttons.forEach((b) => { b.disabled = true; });
    const correctIndex = q.answers.findIndex((a) => a.correct);
    buttons[correctIndex]?.classList.add('is-correct');
    if (answer.correct) score += 1;
    else button.classList.add('is-wrong');

    feedback.className = `feedback is-visible ${answer.correct ? 'is-correct' : 'is-wrong'}`;
    feedback.innerHTML = '';
    feedback.append(h('strong', { text: answer.correct ? t.correct : t.wrong }));
    if (!answer.correct) feedback.append(h('p', { text: `${t.rightAnswer}: ${q.answers[correctIndex].text}` }));
    if (q.explanation) feedback.append(h('p', { text: q.explanation }));

    if (mini) return;
    const last = index === questions.length - 1;
    const next = h('button', { class: 'btn btn--section quiz__next', type: 'button', text: last ? t.finish : t.next });
    next.addEventListener('click', () => {
      index += 1;
      if (last) renderResult(); else renderQuestion();
    });
    stage.append(next);
    next.focus();
  }

  function renderResult() {
    const percent = Math.round((score / questions.length) * 100);
    let best = percent;
    try {
      best = Math.max(percent, Number(localStorage.getItem(storageKey)) || 0);
      if (storageKey) localStorage.setItem(storageKey, String(best));
    } catch { /* приватный режим — без лучшего результата */ }

    const message = percent >= 80 ? t.great : percent >= 50 ? t.good : t.try;
    const ring = h('div', { class: 'quiz__score' }, h('span', { text: `${score}/${questions.length}` }));
    ring.style.setProperty('--score', percent);
    const again = h('button', { class: 'btn btn--section', type: 'button', text: t.again });
    again.addEventListener('click', () => { index = 0; score = 0; renderQuestion(); });

    stage.innerHTML = '';
    const heading = h('h3', { tabindex: '-1', text: t.result });
    stage.append(h('div', { class: 'quiz__result' }, heading, ring, h('p', { class: 'lead', text: message }), again));
    heading.focus();
  }

  renderQuestion();
}
